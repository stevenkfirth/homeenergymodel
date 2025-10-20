#!/usr/bin/env python3

"""
This module provides objects to model heat storage vessels e.g. hot water
cylinder with immersion heater.
Also incudes solar thermal behaviours.
Energy calculation (storage modelled with multiple volumes) - Method A from BS EN 15316-5:2017
"""

# Standard library imports
import sys
from copy import deepcopy

# Third-party imports
import numpy as np

# Local imports
import core.units as units
from core.material_properties import WATER
from core.pipework import Location, Pipework
from core.water_heat_demand.misc import frac_hot_water


class StorageTank:
    """ An object to represent a hot water storage tank/cylinder

    Models the case where hot water is drawn off and replaced by fresh cold
    water which is then heated in the tank by a heat source. Assumes the water
    is stratified by temperature.

    Implements function demand_hot_water(volume_demanded) which all hot water
    source objects must implement.
    """
    #BS EN 15316-5:2017 Appendix B default input data
    #Model Information
    #Product Description Data
    #factors for energy recovery Table B.3
    #part of the auxiliary energy transmitted to the medium
    __f_rvd_aux = 0.25
    #part of the thermal losses transmitted to the room. Note same approach in BufferTank if this is
    #modified in future
    __f_sto_m = 0.75
    #standby losses adaptation
    __f_sto_bac_acc = 1
    #ambient temperature - degress
    #TODO - link to zone temp at timestep possibly and location of tank (in or out of heated space)
    _temp_amb = 16

    # Primary pipework gains for the timestep
    __primary_gains = 0

    # Time of finalisation of the previous hot water event
    __time_end_previous_event = 0.0

    def __init__(
            self,
            volume,
            losses,
            init_temp,
            cold_feed,
            simulation_time,
            heat_source_dict,
            project,
            external_conditions,
            detailed_output=False,
            nb_vol=4,
            primary_pipework_lst=None,
            energy_supply_conn_unmet_demand=None,
            contents=WATER,
    ):
        """ Construct a StorageTank object

        Arguments:
        volume               -- total volume of the tank, in litres
        losses               -- measured standby losses due to cylinder insulation
                                at standardised conditions, in kWh/24h
        init_temp             -- initial temperature required for DHW
        cold_feed            -- reference to ColdWaterSource object
        simulation_time      -- reference to SimulationTime object
        heat_source_dict     -- dict where keys are heat source objects and
                                values are tuples of heater and thermostat
                                position
        nb_vol               --  
                               #number of volumes the storage is modelled with
                               #see App.C (C.1.2 selection of the number of volumes to model the storage unit)
                               #for more details if this wants to be changed.
        energy_supply_conn_unmet_demand 
            -- reference to EnergySupplyConnection object to be used to record unmet energy demand
        contents             -- reference to MaterialProperties object

        Other variables:
        heat_source_data     -- list of heat sources, sorted by heater position
        """
        self.__init_temp      = init_temp
        self.__Q_std_ls_ref   = losses
        self._cold_feed      = cold_feed
        self.__contents       = contents
        self.__energy_supply_conn_unmet_demand = energy_supply_conn_unmet_demand
        self._simulation_time = simulation_time
        self.__project = project
        self.__external_conditions = external_conditions
        self._detailed_output = detailed_output
        self._NB_VOL         = nb_vol
        self._detailed_results = []
        self.__temp_flow_prev = None

        #total volume in litres
        self._V_total = volume
        #list of volume of layers in litres
        self._Vol_n = [self._V_total / self._NB_VOL] * self._NB_VOL
        #water specific heat in kWh/kg.K
        self._Cp = contents.specific_heat_capacity_kWh()
        #volumic mass in kg/litre
        self._rho = contents.density()

        #6.4.3.2 STEP 0 Initialization
        self._temp_n = [init_temp] * self._NB_VOL
        self.__energy_demand_test = 0
        
        # __primary_pipework_losses_kWh added for reporting
        self.__primary_pipework_losses_kWh = 0
        self.__storage_losses_kWh = 0
        
        # Set initial values
        self.__input_energy_adj_prev_timestep = 0

        self.__primary_pipework_lst = []
        if primary_pipework_lst:
            for pipework_data in primary_pipework_lst:
                new_pipework = Pipework(
                    Location.from_string(pipework_data["location"]),
                    pipework_data["internal_diameter"],
                    pipework_data["external_diameter"],
                    pipework_data["length"],
                    pipework_data["insulation_thermal_conductivity"],
                    pipework_data["insulation_thickness"],
                    pipework_data["surface_reflectivity"],
                    pipework_data["pipe_contents"]
                )
                self.__primary_pipework_lst.append(new_pipework)

        # With pre-heatd storage tanks, there could be the situation of tanks without heat sources
        # They could just get warmed up with WWHRS water. 
        if heat_source_dict is not None:
            # sort heat source data in order from the bottom of the tank based on heater position
            self.__heat_source_data = sorted(heat_source_dict.items(), key=lambda x:x[1])
    
            self._heating_active = {}
            for heat_source_data in self.__heat_source_data:
                # heating on or off
                self._heating_active[heat_source_data[0]] = False
        else:
            self.__heat_source_data = None

    def demand_hot_water(self, usage_events):
        """ Draw off hot water from the tank
        Energy calculation as per BS EN 15316-5:2017 Method A sections 6.4.3, 6.4.6, 6.4.7
        Modification of calculation based on volumes and actual temperatures for each layer of water in the tank
        instead of the energy stored in the layer and a generic temperature (self.__temp_out_W_min) = min_temp
        to decide if the tank can satisfy the demand (this was producing unnecesary unmet demand for strict high
        __temp_out_W_min values 

        Arguments:
        usage_events -- All draw off events for the timestep
        """
    
        Q_use_W = 0.0
        Q_unmet_W = 0.0
        volume_demanded = 0.0
        temp_ini_n = deepcopy(self._temp_n)
        temp_s3_n = deepcopy(self._temp_n)
        
        self.__temp_final_drawoff = self.get_temp_hot_water()
        self.__temp_average_drawoff_volweighted = 0.0
        self.__total_volume_drawoff = 0.0
        self.__temp_average_drawoff = self.get_temp_hot_water()
        
        if usage_events is not None:
            # Filtering out IES events that don't get added a 'warm_volume' when processing 
            # the dhw_demand calculation
            filtered_events = filter(lambda e: 'warm_volume' in e, usage_events)

            for event in filtered_events:
                # Check if 'pipework_volume' key exists in the event dictionary
                if 'pipework_volume' not in event:
                    # If 'pipework_volume' is not found, add it with a default value of 0.0
                    event['pipework_volume'] = 0.0
                # Decision no to include yet the overlapping of events for pipework losses
                # even if applying pipework losses to all events might be overstimating
                # the following overlapping processing could be understimating for multiple
                # branches of the pipework system
                # TODO  Improve approach for avoiding double counting of genuine overlapping
                #       events
                # Avoid double counting pipework loses when events overlap
                #time_start_current_event = event['start']
                #if self.__time_end_previous_event >= time_start_current_event:
                #    event['pipework_volume'] = 0.0
                # 0.0 can be modified for additional minutes when pipework could be considered still warm/hot
                #self.__time_end_previous_event = deepcopy(time_start_current_event + (event['duration'] + 0.0) / 60.0)
                volume_used, energy_withdrawn, energy_unmet, remaining_vols = self.extract_hot_water(event)
                
                # Determine the new temperature distribution after displacement
                # Now that pre-heated sources can be the 'cold' feed, rearrangement of temperaturs, that used to
                # only happen before after the input from heat sources, could be required after the displacement
                # of water bringing new water from the 'cold' feed that could be warmer than the existing one. 
                # flag is calculated for that purpose. 
                temp_s3_n, rearrange = self.calc_temps_after_extraction(remaining_vols)
                if rearrange:
                    #Re-arrange the temperatures in the storage after energy input from pre-heated tank
                    _ , temp_s3_n = self.rearrange_temperatures(temp_s3_n)
                
                self._temp_n = deepcopy(temp_s3_n)
                
                volume_demanded += volume_used
                Q_unmet_W += energy_unmet
                Q_use_W += energy_withdrawn
        
        # if tank cannot provide enough hot water report unmet demand
        if self.__energy_supply_conn_unmet_demand is not None:
            self.__energy_supply_conn_unmet_demand.demand_energy(Q_unmet_W)

        
        if self.__total_volume_drawoff != 0.0:
            self.__temp_average_drawoff = self.__temp_average_drawoff_volweighted / self.__total_volume_drawoff
        else: 
            self.__temp_average_drawoff = temp_s3_n[-1]


        #TODO 6.4.3.6 STEP 4 Volume to be withdrawn from the storage (for Heating)
        #TODO - 6.4.3.7 STEP 5 Temperature of the storage after volume withdrawn (for Heating)

        # Run over multiple heat sources
        temp_after_prev_heat_source = temp_s3_n
        Q_ls = 0.0
        self.__Q_ls_n_prev_heat_source = [0.0] * self._NB_VOL
        # With the possibility of not having heat sources now, some parameters might not be defined now 
        # in the for loop before and wouldn't be available for the testoutput unless initialised here. 
        Q_x_in_n = [0.0] * self._NB_VOL
        Q_s6 = 0
        Q_in_H_W = 0
        temp_s6_n = temp_s3_n
        temp_s7_n = temp_s3_n
        temp_s8_n = temp_s3_n
        Q_ls_this_heat_source = 0
        for heat_source,  heat_source_data in self.__heat_source_data:
            heater_layer = int(heat_source_data[0] *self._NB_VOL)
            thermostat_layer = int(heat_source_data[1] *self._NB_VOL) if heat_source_data[1] is not None else None

            temp_s8_n, Q_x_in_n, Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, \
                Q_ls_this_heat_source, Q_ls_n_this_heat_source \
                = self.run_heat_sources(
                    temp_after_prev_heat_source,
                    heat_source,
                    heater_layer,
                    thermostat_layer,
                    self.__Q_ls_n_prev_heat_source,
                    )

            temp_after_prev_heat_source = temp_s8_n
            Q_ls += Q_ls_this_heat_source
            for i, Q_ls_n in enumerate(Q_ls_n_this_heat_source):
                self.__Q_ls_n_prev_heat_source[i] += Q_ls_n

            #Trigger heating to stop
            self._determine_heat_source_switch_off(temp_s8_n, heat_source, heater_layer, thermostat_layer)

        #print interim steps to output file for investigation
        self.testoutput(
            usage_events, volume_demanded, Q_use_W, Q_unmet_W,
            temp_ini_n, temp_s3_n, Q_x_in_n, Q_s6, temp_s6_n,
            temp_s7_n, Q_in_H_W, Q_ls_this_heat_source, temp_s8_n,
            self.__temp_final_drawoff, self.__temp_average_drawoff
            )

        #Additional calculations
        #6.4.6 Calculation of the auxiliary energy
        #accounted for elsewhere so not included here
        W_sto_aux = 0

        #6.4.7 Recoverable, recovered thermal losses
        #recovered auxiliary energy to the heating medium - kWh
        Q_sto_h_aux_rvd = W_sto_aux * self.__f_rvd_aux
        #recoverable auxiliary energy transmitted to the heated space - kWh
        Q_sto_h_rbl_aux = W_sto_aux * self.__f_sto_m * (1 - self.__f_rvd_aux)
        #recoverable heat losses (storage) - kWh
        Q_sto_h_rbl_env = Q_ls * self.__f_sto_m
        #total recoverable heat losses  for heating - kWh
        self.__Q_sto_h_ls_rbl = Q_sto_h_rbl_env + Q_sto_h_rbl_aux
        #set temperatures calculated to be initial temperatures of volumes for the next timestep
        self._temp_n = deepcopy(temp_s8_n)

        #TODOrecoverable heat losses for heating should impact heating

        # Return total energy of hot water supplied and unmet
        return Q_use_W, Q_unmet_W, self.__temp_final_drawoff, self.__temp_average_drawoff, self.__total_volume_drawoff
        # Sending temp_final_drawoff, temp_average_drawoff
        # for pipework loss and internal gains calculations

    def extract_hot_water(self, event):
        #"""
        #Allocate hot water layers to meet a single temperature demand.
        #
        #Arguments:
        #event -- Dictionary containing information about the draw-off event
        #         (e.g. {'start': 18, 'duration': 1, 'temperature': 41.0, 'type': 'Other', 'name': 'other', 'warm_volume': 8.0})
        #"""
        # Make a copy of the volume list to keep track of remaining volumes

        # Remaining volume of water in storage tank layers
        remaining_vols = deepcopy(self._Vol_n)

        # Extract the temperature and required warm volume from the event
        warm_temp = event['temperature']
        warm_volume = event['warm_volume']
        # Remaining volume of warm water to be satisfied for current event
        remaining_demanded_warm_volume = warm_volume
    
        # Initialize the unmet and met energies
        energy_unmet = 0.0
        energy_withdrawn = 0.0
        pipework_temp = self._cold_feed.temperature() # This value set to initialise, but is never used - overwritten later.
    
        if event['pipework_volume'] <= 0.0:
            pipework_considered = True
        else:
            pipework_considered = False
            
        # Loop through storage layers (starting from the top)
        for layer_index in reversed(range(len(self._temp_n))):
            layer_temp = self._temp_n[layer_index]
            layer_vol = remaining_vols[layer_index]
    
            if remaining_demanded_warm_volume <= 0:
                if pipework_considered:
                    # Event inclusive of pipework is completed at this layer temp
                    self.__temp_final_drawoff = pipework_temp
                    break
                else:
                    remaining_demanded_warm_volume = event['pipework_volume']
                    warm_temp = layer_temp
                    pipework_considered = True
                    #continue
                
            # If event is finished and we are serving the pipework, this is the temperature
            # of the water stranded    
            pipework_temp = layer_temp
    
            # Skip this layer if its remaining volume is already zero
            if remaining_vols[layer_index] <= 0.0:
                continue
    
            # Skip this layer if its temperature is lower than the target temperature
            if layer_temp < warm_temp:
                break
    
            # Calculate the fraction of hot water required
            fraction = frac_hot_water(warm_temp, layer_temp, self._cold_feed.temperature())
    
            # Volume of hot water required at this layer
            if layer_vol <= remaining_demanded_warm_volume * fraction:
                # This is the case where layer cannot meet all remaining demand for this event
                required_vol = layer_vol
                warm_vol_removed = layer_vol / fraction
                # Deduct the required volume from the remaining demand and update the layer's volume
                remaining_vols[layer_index] -= layer_vol
                remaining_demanded_warm_volume -= warm_vol_removed
            else:
                # This is the case where layer can meet all remaining demand for this event
                required_vol = remaining_demanded_warm_volume * fraction
                warm_vol_removed = remaining_demanded_warm_volume
                # Deduct the required volume from the remaining demand and update the layer's volume
                remaining_vols[layer_index] -= required_vol
                remaining_demanded_warm_volume = 0.0
            
            self.__temp_average_drawoff_volweighted += required_vol * layer_temp
            self.__total_volume_drawoff += required_vol
            
            # Record the met volume demand for the current temperature target
            # warm_vol_removed is the volume of warm water that has been satisfied from hot water in this layer
            energy_withdrawn += (
                # Calculation with event water parameters
                #self._rho * self._Cp * warm_vol_removed * (warm_temp - self._cold_feed.temperature())
                # Calculation with layer water parameters
                self._rho * self._Cp * required_vol * (layer_temp - self._cold_feed.temperature())
            )


        # When the event has not been fully met or has been exactly met with the last of the hot water
        # in the tank, there's only cold water from the feed left to fill the pipework after the event.    
        if not pipework_considered:
            self.__temp_final_drawoff = self._temp_n[layer_index]

        # Record the unmet energy for the current event
        energy_unmet += (
            self._rho * self._Cp * remaining_demanded_warm_volume * (warm_temp - self._cold_feed.temperature())
        )
    
        # Calculate the remaining total volume
        remaining_total_volume = sum(remaining_vols)
    
        # Calculate the total volume used
        volume_used = self._V_total - remaining_total_volume
        
        # Return the remaining storage volumes, volume used, new temperature distribution, the met/unmet targets, and flag to rearrange layers
        return volume_used,energy_withdrawn, energy_unmet, remaining_vols

    def calc_temps_after_extraction(self, remaining_vols):
        """Calculate the new temperature distribution after displacement.
    
        Arguments:
        remaining_vols -- List of remaining volumes for each storage layer after draw-off
        temp_cold     -- Temperature of the cold water being added
        """
        new_temps = deepcopy(self._temp_n)
        # If the 'cold' feed water is hotter than the existing water in the tank, rearrange will be needed.
        # as if it was a heat source coming from the cold feed. 
        flag_rearrange_layers = False
        # Iterate from the top layer downwards
        for i in reversed(range(len(self._Vol_n))):
            # Determine how much volume needs to be added to this layer
            needed_volume = self._Vol_n[i] - remaining_vols[i]
            # If this layer is already full, continue to the next
            if needed_volume <= 0:
                break
    
            # Initialize the variables for mixing temperatures
            total_volume = remaining_vols[i]
            volume_weighted_temperature = remaining_vols[i] * self._temp_n[i]

            # Initialisation of min temperature of tank layers to compare eventually against
            # the 'cold' feed temperature to check if rearrangement is needed.                 
            temp_layer_min = self._temp_n[i]    
            # Add water from the layers below to this layer
            for j in range(i - 1, -1, -1):
                available_volume = remaining_vols[j]
                if available_volume > 0:
                    # Determine the volume to move up from this layer
                    move_volume = min(needed_volume, available_volume)
                    remaining_vols[j] -= move_volume
    
                    # Adjust the temperature by mixing in the moved volume
                    total_volume += move_volume
                    volume_weighted_temperature += move_volume * self._temp_n[j]
                    # Update min temperature of the tank so far. 
                    if self._temp_n[j] < temp_layer_min:
                        temp_layer_min = self._temp_n[j]
                        
                    # Decrease the amount of volume needed for the current layer
                    needed_volume -= move_volume
                    if needed_volume <= 0:
                        break
    
            # If not enough water is available from the lower layers, use the cold supply
            if needed_volume > 0:
                total_volume += needed_volume
                # This is when the tank gets refilled with 'cold' water from the 'cold' feed.
                # Amount/Volume wasn't important before as it was assume an infinite amount at
                # the cold feed was available.
                # The pre-heated tank is limited in the amount of water that can be provided at
                # a given temperature, eventually resourting to its own cold feed. So cold feed
                # temperature for the tank depends on the volume required.
                temp_cold_feed = self._cold_feed.temperature(needed_volume)
                volume_weighted_temperature += needed_volume * temp_cold_feed
                if temp_cold_feed > temp_layer_min:
                    flag_rearrange_layers = True
    
            # Calculate the new temperature for the current layer
            # Round to 2 decimals to match instrumentation limits and significant figures,
            # ensuring practical accuracy, computational efficiency, and avoiding minute e-18 differences.
            new_temps[i] = round(volume_weighted_temperature / total_volume,2)
            remaining_vols[i] = total_volume
    
        return new_temps, flag_rearrange_layers

    def rearrange_temperatures(self, temp_s6_n):
        """When the temperature of the volume i is higher than the one of the upper volume,
        then the 2 volumes are melded. This iterative process is maintained until the temperature
        of the volume i is lower or equal to the temperature of the volume i+1."""
        temp_s7_n = deepcopy(temp_s6_n)
        while(True):
            # Flag for which layers need mixing
            mix_layer_n = [0] * self._NB_VOL
            #for loop :-1 is important here!
            #loop through layers from bottom to top, without including top layer.
            #this is because the top layer has no upper layer to compare too
            for i, vol_i in list(enumerate(self._Vol_n[:-1])):
                if temp_s7_n[i] >= temp_s7_n[i+1]:
                    # '>=' With the potential of a few layers being replaced at the bottom with pre-heated water,
                    # there are more than one layer that would need to be mixed up.
                    # Previous implementation worked with '>' as aonly one layer would receive the heat source input. 
                    #set layers to mix
                    mix_layer_n[i] = 1
                    mix_layer_n[i+1] = 1
                    #mix temeratures of all applicable layers
                    #note error in formula 12 in standard as adding temperature to volume
                    #this is what I think they intended from the description
                    temp_mix = sum( self._Vol_n[k] * temp_s7_n[k] * mix_layer_n[k] \
                                    for k in range(len(self._Vol_n)) \
                                  ) \
                                / ( sum(self._Vol_n[l] * mix_layer_n[l] \
                                        for l in range(len(self._Vol_n)) \
                                       ) \
                                  )
                    #set same temperature for all applicable layers
                    for j, temp_j in list(enumerate(temp_s7_n[:i+2])):
                        if mix_layer_n[j] == 1:
                            temp_s7_n[j] = temp_mix
                else:
                    #reset mixing as lower levels now stabalised
                    mix_layer_n = [0] * self._NB_VOL
            if sorted(temp_s7_n) == temp_s7_n:
                break

        Q_h_sto_end \
            = [ self._rho * self._Cp \
              * self._Vol_n[i] * temp_s7_n[i]
              for i in range(len(self._Vol_n))
              ]

        return Q_h_sto_end, temp_s7_n

    def run_heat_sources(self, temp_s3_n, heat_source, heater_layer, thermostat_layer, Q_ls_prev_heat_source):
        #6.4.3.8 STEP 6 Energy input into the storage
        #input energy delivered to the storage in kWh - timestep dependent
        Q_x_in_n = self.potential_energy_input(temp_s3_n, heat_source, heater_layer, thermostat_layer)

        # Calculate final temperatures
        temp_s8_n, Q_x_in_n, Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, Q_ls, Q_ls_n = self.calc_final_temps(
            temp_s3_n,
            heat_source,
            Q_x_in_n,
            heater_layer,
            Q_ls_prev_heat_source,
            )

        return temp_s8_n, Q_x_in_n, Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, Q_ls, Q_ls_n

    # Heat source. Addition of temp_s3_n as an argument
    def potential_energy_input(self, temp_s3_n, heat_source, heater_layer, thermostat_layer):
        """Energy input for the storage from the generation system
        (expressed per energy carrier X)
        Heat Source = energy carrier"""
        #initialise list of potential energy input for each layer
        Q_x_in_n = [0] * self._NB_VOL

        if isinstance(heat_source, SolarThermalSystem):
            # We are passing the storage tank object to the SolarThermal as this needs to call
            # back the storage tank....
            energy_potential = heat_source.energy_output_max(self, temp_s3_n)
        else:

            self._determine_heat_source_switch_on(temp_s3_n, heat_source, heater_layer, thermostat_layer)
            if self._heating_active[heat_source]:
                if isinstance(heat_source, ImmersionHeater):
                    energy_potential = heat_source.energy_output_max()
                else:
                    # TODO Use different temperatures for flow and return in the call to
                    #      heat_source.energy_output_max below
                    temp_flow = self._temp_flow(heat_source)
                    energy_potential = heat_source.energy_output_max(temp_flow, temp_flow)

                    # TODO Consolidate checks for systems with/without primary pipework
                    primary_pipework_losses_kWh, _ \
                        = self.__primary_pipework_losses(energy_potential, temp_flow)
                    energy_potential -= primary_pipework_losses_kWh

            else:
                energy_potential = 0.0

        Q_x_in_n[heater_layer] += energy_potential
        return Q_x_in_n

    def calc_final_temps(
            self,
            temp_s3_n,
            heat_source,
            Q_x_in_n,
            heater_layer,
            Q_ls_n_prev_heat_source,
            controlmax_diverter = None,
            ):

        if controlmax_diverter is not None:
            setpntmax = controlmax_diverter.setpnt()
        else:
            _, setpntmax = self._retrieve_setpnt(heat_source)

        Q_s6, temp_s6_n = self.calc_temps_with_energy_input(temp_s3_n, Q_x_in_n)

        #6.4.3.9 STEP 7 Re-arrange the temperatures in the storage after energy input
        Q_h_sto_s7, temp_s7_n = self.rearrange_temperatures(temp_s6_n)

        #STEP 8 Thermal losses and final temperature
        Q_in_H_W, Q_ls, temp_s8_n, Q_ls_n = self.calc_temps_after_thermal_losses(
            temp_s7_n,
            Q_x_in_n,
            Q_h_sto_s7,
            heater_layer,
            Q_ls_n_prev_heat_source,
            setpntmax,
            )

        #TODO 6.4.3.11 Heat exchanger

        #demand adjusted energy from heat source (before was just using potential without taking it)
        input_energy_adj = deepcopy(Q_in_H_W)

        #energy demand saved for unittest
        self.__energy_demand_test = deepcopy(input_energy_adj)

        heat_source_output = self.heat_source_output(heat_source, input_energy_adj)
        input_energy_adj = input_energy_adj - heat_source_output

        return temp_s8_n, Q_x_in_n, Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, Q_ls, Q_ls_n

    def calc_temps_with_energy_input(self, temp_s3_n, Q_x_in_n):
        """The input of energy(s) is (are) allocated to the specific location(s)
        of the input of energy.
        Note: for energy withdrawn froma heat exchanger, the energy is accounted negatively.

        For step 6, the addition of the temperature of volume 'i' and theoretical variation of
        temperature calculated according to formula (10) can exceed the set temperature defined
        by the control system of the storage unit."""
        #initialise list of theoretical variation of temperature of layers in degrees
        delta_temp_n = [0] * self._NB_VOL
        #initialise list of theoretical temperature of layers after input in degrees
        temp_s6_n = [0] * self._NB_VOL
        #output energy delivered by the storage in kWh - timestep dependent
        Q_sto_h_out_n = [0] * self._NB_VOL

        for i, vol_i in list(enumerate(self._Vol_n)):
            delta_temp_n[i] = (Q_x_in_n[i] + Q_sto_h_out_n[i]) \
                              / (self._rho * self._Cp * self._Vol_n[i])
            temp_s6_n[i] = temp_s3_n[i] + delta_temp_n[i]

        Q_s6 = self._rho * self._Cp * sum(self._Vol_n[i] \
                * temp_s6_n[i] for i in range(len(self._Vol_n)))

        return Q_s6, temp_s6_n

    def calc_temps_after_thermal_losses(self,
                       temp_s7_n,
                       Q_x_in_n,
                       Q_h_sto_s7,
                       heater_layer,
                       Q_ls_n_prev_heat_source,
                       temp_setpntmax,
                       ):
        """Thermal losses are calculated with respect to the impact of the temperature set point"""
        Q_x_in_adj = sum(Q_x_in_n)

        #standby losses coefficient - W/K
        H_sto_ls = self.stand_by_losses_coefficient()

        #standby losses correction factor - dimensionless
        #do not think these are applicable so used: f_sto_dis_ls = 1, f_sto_bac_acc = 1

        #initialise list of thermal losses in kWh
        Q_ls_n = [0] * self._NB_VOL
        #initialise list of final temperature of layers after thermal losses in degrees
        temp_s8_n = [0] * self._NB_VOL

        # Thermal losses
        # Note: Eqn 13 from BS EN 15316-5:2017 does not explicitly multiply by
        # timestep (it seems to assume a 1 hour timestep implicitly), but it is
        # necessary to convert the rate of heat loss to a total heat loss over
        # the time period
        for i, vol_i in list(enumerate(self._Vol_n)):
            temp_before_losses = min(temp_s7_n[i], temp_setpntmax) if temp_setpntmax is not None else temp_s7_n[i]
            Q_ls_n[i] = (H_sto_ls * self._rho * self._Cp) \
                        * (self._Vol_n[i] / self._V_total) \
                        * (temp_before_losses - self._temp_amb) \
                        * self._simulation_time.timestep()
            # Prevent double-counting of losses with multiple heat sources
            Q_ls_n[i] = max(0.0, Q_ls_n[i] - Q_ls_n_prev_heat_source[i])

        #total thermal losses kWh
        Q_ls = sum(Q_ls_n)
        self.__storage_losses_kWh = Q_ls
        
        #the final value of the temperature is reduced due to the effect of the thermal losses.
        #check temperature compared to set point
        #the temperature for each volume are limited to the set point for any volume controlled
        for i, vol_i in list(enumerate(self._Vol_n)):
            # Need to check for heating input below, otherwise temperature will be wrongly
            # capped at temp_setpntmax in cases where tank temperature already exceeded temp_setpntmax
            # without any contribution from the heat source. This could happen if the temp_setpntmax
            # setting is lower in the current timestep than the previous timestep, or if
            # another heat source has a higher temp_setpntmax (and therefore heated the tank to a
            # higher temperature) than the heat source currently being considered
            if Q_x_in_adj > 0.0 and temp_setpntmax is not None and temp_s7_n[i] > temp_setpntmax:
                #Case 2 - Temperature exceeding the set point
                temp_s8_n[i] = temp_setpntmax
            else:
                #Case 1 - Temperature below the set point
                #TODO - spreadsheet accounts for total thermal losses not just layer
                """temp_s8_n[i] \
                    = temp_s7_n[i] - (Q_ls / (self._rho * self._Cp * self._V_total))"""

                #the final value of the temperature
                #is reduced due to the effect of the thermal losses
                #Formula (14) in the standard appears to have error as addition not multiply
                #and P instead of rho
                temp_s8_n[i] \
                    = temp_s7_n[i] - (Q_ls_n[i] / (self._rho * self._Cp * self._Vol_n[i]))

        if Q_x_in_adj > 0.0:
            #excess energy / energy surplus
            """excess energy is calculated as the difference from the energy stored, Qsto,step7, and
               energy stored once the set temperature is obtained, Qsto,step8, with addition of the
               thermal losses."""
            # Note: The surplus must be calculated only for those layers that the
            #       heat source currently being considered is capable of heating,
            #       i.e. excluding those below the heater position.
            energy_surplus = 0.0
            if temp_setpntmax is not None and temp_s7_n[heater_layer] > temp_setpntmax:
                for i in range(heater_layer, self._NB_VOL):
                    energy_surplus \
                        += Q_h_sto_s7[i] - Q_ls_n[i] \
                         - (self._rho * self._Cp * self._Vol_n[i] * temp_setpntmax)

            #the thermal energy provided to the system (from heat sources) shall be limited
            #adjustment of the energy delivered to the storage according with the set temperature
            #potential input from generation
            #TODO - find in standard - availability of back-up - where is this from?
            #also refered to as electrical power on
            STO_BU_ON = 1
            Q_in_H_W = min((Q_x_in_adj - energy_surplus), Q_x_in_adj * STO_BU_ON)
        else:
            Q_in_H_W = 0.0

        return Q_in_H_W, Q_ls, temp_s8_n, Q_ls_n

    def heat_source_output(self, heat_source, input_energy_adj):
        # function that also calculates pipework loss before sending on the demand energy 
        # if immersion heater, no pipework losses
        temp_flow = self._temp_flow(heat_source)
        # Input energy rounded so that almost zero negative numbers (caused by 
        # floating point error) do not cause errors in subsequent code
        input_energy_adj = round(input_energy_adj, 10)
        if isinstance(heat_source, ImmersionHeater):
            return(heat_source.demand_energy(input_energy_adj))
        elif isinstance(heat_source, SolarThermalSystem):
            return(heat_source.demand_energy(input_energy_adj))
        else:
            primary_pipework_losses_kWh, primary_gains \
                = self.__primary_pipework_losses(input_energy_adj, temp_flow)
            input_energy_adj += primary_pipework_losses_kWh
            # TODO Use different temperatures for flow and return in the call to
            #      heat_source.demand_energy below
            heat_source_output \
                = heat_source.demand_energy(input_energy_adj, temp_flow, temp_flow) \
                - primary_pipework_losses_kWh
            # Save input energy for next timestep
            self.__input_energy_adj_prev_timestep = input_energy_adj
            # Save primary gains for internal gains calculation
            self.__primary_gains = primary_gains

            # TODO - how are these gains reflected in the calculations? allocation by zone?
            return(heat_source_output)

    def _retrieve_setpnt(self, heat_source):
        #No demand from heat source if the temperature of the tank at the 
        #thermostat position is below the set point
        #Trigger heating to start when temperature falls below the minimum
        setpntmin, setpntmax = heat_source.setpnt()
        # Ensure that if setpntmax is None then setpntmin must be None too
        if setpntmax is None and setpntmin is not None:
            raise ValueError("setpntmin must be None if setpntmax is None")
        if setpntmin is not None and setpntmax is not None and setpntmin > setpntmax:
            raise ValueError(f"setpntmin: {setpntmin} must not be greater than setpntmax: {setpntmax}")

        return setpntmin, setpntmax
    
    def _determine_heat_source_switch_on(self, temp_s3_n, heat_source, heater_layer, thermostat_layer):
        setpntmin, setpntmax = self._retrieve_setpnt(heat_source)
        if setpntmin is not None and temp_s3_n[thermostat_layer] <= setpntmin:
            self._heating_active[heat_source] = True
    
    def _determine_heat_source_switch_off(self, temp_s8_n, heat_source, heater_layer, thermostat_layer):
        _, setpntmax = self._retrieve_setpnt(heat_source)
        if setpntmax is None or temp_s8_n[thermostat_layer] >= setpntmax:
            self._heating_active[heat_source] = False
   
    def _temp_flow(self, heat_source):
        _, setpntmax = self._retrieve_setpnt(heat_source)
        if setpntmax is None:
            setpntmax = self.__temp_flow_prev
        self.__temp_flow_prev = setpntmax
        return setpntmax

    def temp_surrounding_primary_pipework(self, pipework_data):
        location = pipework_data.get_location()
        if location == Location.EXTERNAL:
            return self.__external_conditions.air_temp()
        elif location == Location.INTERNAL:
            return self.__project.temp_internal_air_prev_timestep()
        else: 
            #if the location is neither external nor internal, raise an AssertionError
            assert False, f"Unexpected location value: {location}"

    def get_cold_water_source(self):
        return self._cold_feed

    def get_temp_hot_water(self):
        # This is only used to calculate the equivalent volume of water for IES showers
        # in order to get the energy content for the internal gains. 
        # Therefore the actual value used is not critical.
        # It has been suggested/considered the use of the top layer of the storage tank
        # but this could be similar to the cold feed temperature after big draw-offs
        # To avoid any issues in those situations we use the setpoing temperature of the
        # tank.
        return self.__init_temp # Use intial temperature of tank as reference value.

    def stand_by_losses_coefficient(self):
        """Appendix B B.2.8 Stand-by losses are usually determined in terms of energy losses during
        a 24h period. Formula (B.2) allows the calculation of _sto_stbl_ls_tot based on a reference
        value of the daily thermal energy losses.

        H_sto_ls is the stand-by losses, in W/K 

        TODO there are alternative methods listed in App B (B.2.8) which are not included here."""
        #BS EN 12897:2016 appendix B B.2.2
        #temperature of the water in the storage for the standardized conditions - degrees
        #these are reference (ref) temperatures from the standard test conditions for cylinder loss.
        temp_set_ref = 65
        temp_amb_ref = 20
    
        H_sto_ls = (1000 * self.__Q_std_ls_ref) / (24 * (temp_set_ref - temp_amb_ref))

        return H_sto_ls

    # Function added into Storage tank to be called by the Solar Thermal object.
    # Calculates the impact on storage tank temperature due to the proposed energy input
    def storage_tank_potential_effect(self, energy_proposed, temp_s3_n):
        """ Assuming initially no water draw-off """

        #initialise list of potential energy input for each layer
        Q_x_in_n = [0] * self._NB_VOL
        
        # TODO - Ensure we are feeding in the right volumen
        Q_x_in_n[0] = energy_proposed

        Q_s6, temp_s6_n = self.calc_temps_with_energy_input(temp_s3_n, Q_x_in_n)

        #6.4.3.9 STEP 7 Re-arrange the temperatures in the storage after energy input
        Q_h_sto_s7, temp_s7_n = self.rearrange_temperatures(temp_s6_n)                
        
        # TODO - Check [0] is bottom layer temp and that solart thermal inlet is top layer _NB_VOL-1
        return temp_s7_n[0], temp_s7_n[self._NB_VOL-1]
  

    def toreport(self):
        """ Send more intermediate output parameters to report """
        return self.__primary_pipework_losses_kWh, self.__storage_losses_kWh

    def testoutput(self, usage_events, volume_extracted, Q_use_W, Q_unmet_W,
                   temp_ini_n,temp_s3_n, Q_x_in_n,
                   Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, Q_ls,
                   temp_s8_n, temp_final, temp_average,
                   ):
        """ print output to a file for analysis """
        if self._detailed_output:
            demand = summarise_events(usage_events)
            if self._simulation_time.index() == 0:
                def header_dup(header: str, n: int, with_index=True):
                    for i in range(n):
                        yield header + (f" {i+1}" if with_index else "")

                # Include headers first
                self._detailed_results.append(
                    [
                        "time",
                        "volume total",
                        "specific heat",
                        "density",
                        "cold water",
                        "events",
                        "volume extracted",
                        *header_dup("initial temp.", len(temp_ini_n)),
                        "energy withdrawn",
                        "energy unmet",
                        *header_dup("temp. after volume withdrawn", len(temp_s3_n)),
                        *header_dup("potential energy input", len(Q_x_in_n)),
                        "theoretical energy stored after energy input",
                        *header_dup("theoretical temp. after energy input", len(temp_s6_n)),
                        *header_dup("temp. after volume mixing", len(temp_s7_n)),
                        "energy input (adjusted)",
                        "thermal losses",
                        *header_dup("temp. after thermal losses", len(temp_s8_n)),
                        "temp_final_drawoff",
                        "temp_average_drawoff",
                    ])
                self._detailed_results.append(
                    [
                        "h",
                        "litres",
                        "kWh/kgK",
                        "kg/l",
                        "oC",
                        "T(l@oC)",
                        "litres",
                        *header_dup("oC",len(temp_ini_n),False),
                        "kWh",
                        "kWh",
                        *header_dup("oC", len(temp_s3_n), False),
                        *header_dup("kWh", len(Q_x_in_n), False),
                        "kWh",
                        *header_dup("oC", len(temp_s6_n), False),
                        *header_dup("oC", len(temp_s7_n), False),
                        "kWh",
                        "kWh",
                        *header_dup("oC", len(temp_s8_n), False),
                        "oC",
                        "oC"
                    ])

            self._detailed_results.append(
                [
                    str(self._simulation_time.hour_of_day()),
                    str(self._V_total),
                    str(self._Cp),
                    str(self._rho),
                    str(self._cold_feed.temperature()),
                    demand,
                    str(volume_extracted),
                    *temp_ini_n,
                    str(Q_use_W),
                    str(Q_unmet_W),
                    *temp_s3_n,
                    *Q_x_in_n,
                    str(Q_s6),
                    *temp_s6_n,
                    *temp_s7_n,
                    str(Q_in_H_W),
                    str(Q_ls),
                    *temp_s8_n,
                    str(temp_final),
                    str(temp_average),
                ]
            )

            # Do we need these output too?
            #o.write(str(Q_out_W_n)[1:-1])
            #o.write(str(volume_demanded))
            #o.write(str(Q_out_W_dis_req))
            #o.write(str(Vol_use_W_n)[1:-1])

    def draw_off_hot_water(self, volume):
        """
        draw off hot water layers until required volume is provided.
        
        Arguments:
        volume    -- volume of water required
        """
        # Remaining volume of water in storage tank layers
        remaining_vols = deepcopy(self._Vol_n)

        remaining_demanded_volume = volume
        
        # Initialize the unmet and met energies
        energy_withdrawn = 0.0
        self.__temp_average_drawoff_volweighted = 0.0
        self.__total_volume_drawoff = 0.0
        self.__temp_average_drawoff = self._cold_feed.temperature()
        self.__temp_final_drawoff = self._cold_feed.temperature()       
        temp_ini_n = deepcopy(self._temp_n)
        temp_s3_n = deepcopy(self._temp_n)
    
        # Loop through storage layers (starting from the top)
        for layer_index in reversed(range(len(self._temp_n))):
            layer_temp = self._temp_n[layer_index]
            layer_vol = remaining_vols[layer_index]
    
            # This cannot happen in the preheated tank. Check!
            # Skip this layer if its remaining volume is already zero
            #if remaining_vols[layer_index] <= 0.0:
            #    continue
    
            # Volume of water required at this layer
            if layer_vol <= remaining_demanded_volume:
                # This is the case where layer cannot meet all remaining demanded volume
                required_vol = layer_vol
                remaining_vols[layer_index] -= layer_vol
                remaining_demanded_volume -= layer_vol
            else:
                # This is the case where layer can meet all remaining demanded volume
                required_vol = remaining_demanded_volume
                # Deduct the required volume from the remaining demand and update the layer's volume
                remaining_vols[layer_index] -= required_vol
                remaining_demanded_volume = 0.0
            
            self.__temp_average_drawoff_volweighted += required_vol * layer_temp
            self.__total_volume_drawoff += required_vol
            
            # Record the met volume demand for the current temperature target
            # warm_vol_removed is the volume of warm water that has been satisfied from hot water in this layer
            energy_withdrawn += (
                # Calculation with event water parameters
                #self._rho * self._Cp * warm_vol_removed * (warm_temp - self._cold_feed.temperature())
                # Calculation with layer water parameters
                self._rho * self._Cp * required_vol * (layer_temp - self._cold_feed.temperature())
            )
            
            if remaining_demanded_volume <= 0:
                break

        if remaining_demanded_volume > 0:
            self.__temp_average_drawoff_volweighted += remaining_demanded_volume * self._cold_feed.temperature(remaining_demanded_volume)
            self.__total_volume_drawoff += remaining_demanded_volume
            
        if self.__total_volume_drawoff != 0.0:
            self.__temp_average_drawoff = self.__temp_average_drawoff_volweighted / self.__total_volume_drawoff
        else: 
            self.__temp_average_drawoff = temp_s3_n[-1]
        
        # Determine the new temperature distribution after displacement
        new_temp_distribution, flag_rearrange_layers = self.calc_temps_after_extraction(remaining_vols)
        
        if flag_rearrange_layers:
            #Re-arrange the temperatures in the storage after energy input from pre-heated tank
            _ , new_temp_distribution = self.rearrange_temperatures(new_temp_distribution)
    
        self._temp_n = deepcopy(new_temp_distribution)

        # Return the remaining storage volumes, volume used, new temperature distribution, and the met/unmet targets
        return self.__temp_average_drawoff

    def additional_energy_input(self, heat_source, energy_input, controlmax_diverter):
        if energy_input == 0.0:
            return 0.0
        for heat_source_ref, heat_source_data in self.__heat_source_data:
            if heat_source is heat_source_ref:
                # Break out of loop, preserving current value of heat_source_data
                break

        heater_layer = int(heat_source_data[0] *self._NB_VOL)

        Q_x_in_n = [0] * self._NB_VOL
        Q_x_in_n[heater_layer] = energy_input
        temp_s8_n, _, _, _, _, Q_in_H_W, _, Q_ls_n_this_heat_source = self.calc_final_temps(
                self._temp_n,
                heat_source,
                Q_x_in_n,
                heater_layer,
                self.__Q_ls_n_prev_heat_source,
                controlmax_diverter,
                )
        for i, Q_ls_n in enumerate(Q_ls_n_this_heat_source):
            self.__Q_ls_n_prev_heat_source[i] += Q_ls_n

        #set temperatures calculated to be initial temperatures of volumes for the next timestep
        self._temp_n = deepcopy(temp_s8_n)

        # Return energy accepted
        return Q_in_H_W


    def test_energy_demand(self):
        return(self.__energy_demand_test)

    def internal_gains(self):
        """ Return the DHW recoverable heat losses as internal gain for the current timestep in W"""
        primary_gains_timestep = self.__primary_gains
        self.__primary_gains = 0
        return self.__Q_sto_h_ls_rbl * units.W_per_kW / self._simulation_time.timestep() \
        + primary_gains_timestep

    def __primary_pipework_losses(self, input_energy_adj, temp_flow):
        primary_pipework_losses_kWh = 0.0
        primary_gains_W = 0.0
        #TODO multiple heat source for primary pipework

        # Start of heating event
        if input_energy_adj > 0.0 and self.__input_energy_adj_prev_timestep == 0.0:
            for pipework_data in self.__primary_pipework_lst:
                primary_pipework_losses_kWh \
                    += pipework_data.cool_down_loss(temp_flow, self.temp_surrounding_primary_pipework(pipework_data))

        # During heating event
        if input_energy_adj > 0.0:
            for pipework_data in self.__primary_pipework_lst:
                # Primary losses for the timestep calculated from temperature difference
                primary_pipework_losses_W \
                    = pipework_data.heat_loss(temp_flow, self.temp_surrounding_primary_pipework(pipework_data))
                # Check if pipework location is internal
                location = pipework_data.get_location()
                if location == Location.INTERNAL:
                    primary_gains_W += primary_pipework_losses_W
                primary_pipework_losses_kWh \
                    += primary_pipework_losses_W * self._simulation_time.timestep() / units.W_per_kW

        # End of heating event
        if input_energy_adj == 0.0 and self.__input_energy_adj_prev_timestep > 0.0:
            for pipework_data in self.__primary_pipework_lst:
                location = pipework_data.get_location()
                if location == Location.INTERNAL:
                    primary_gains_W \
                        += pipework_data.cool_down_loss(temp_flow, self.temp_surrounding_primary_pipework(pipework_data)) \
                            * units.W_per_kW / self._simulation_time.timestep()

        #keeping primary_pipework_losses_kWh for reporting as part of investigation of issue #31225: FDEV A082
        self.__primary_pipework_losses_kWh = deepcopy(primary_pipework_losses_kWh)
        
        return primary_pipework_losses_kWh, primary_gains_W

    def temperature(self, volume_needed = 0.0):
        """ Return the pre-heated water temperature for the current timestep """
        # This is only relevant when the storage tank is working as a pre-heated source.
        # If the volume required is 0.0 or not provided, the calculation assumes the requirement is
        # for the actual cold feed temperature of the pre-heated tank (eventually the real cold-feed)
        # Otherwise, it calculates the average water the tank can provided for the required volume.
        if volume_needed == 0.0:
            return self._cold_feed.temperature()
        else:
            average_temperature_draw_off = self.draw_off_hot_water(volume_needed)
            return average_temperature_draw_off

    def output_results(self):
        """Return the data dictionary containing detailed storage tank results"""
        return self._detailed_results

class SmartHotWaterTank(StorageTank):
    """
    An object to represent a smart hot water storage tank/cylinder

    """
    def __init__(
            self,
            volume,
            losses,
            init_temp,
            power_pump_kW,
            max_flow_rate_pump_l_per_min,
            temp_usable,
            temp_setpnt_max,
            cold_feed,
            simulation_time,
            heat_source_dict,
            project,
            external_conditions,
            detailed_output=False,
            nb_vol=100,
            primary_pipework_lst=None,
            energy_supply_conn_unmet_demand=None,
            energy_supply_conn_pump=None,
            contents=WATER,
            ):
        """
        Construct a SmartHotWaterTank object
        
        Arguments:
        volume               -- total volume of the tank, in litres
        losses               -- measured standby losses due to cylinder insulation
                                at standardised conditions, in kWh/24h
        init_temp             -- initial temperature required for DHW
        power_pump_kW            -- power of pump used to pump water from the bottom
                                 to the top of the tank in kW
        max_flow_rate_pump_l_per_min     -- maximum flow rate that pump can provide in l/min
        temp_usable           -- lowest water temperature that the water can be useable
        temp_setpnt_max          -- maximum set point temperature
        cold_feed            -- reference to ColdWaterSource object
        simulation_time      -- reference to SimulationTime object
        heat_source_dict     -- dict where keys are heat source objects and
                                values are tuples of heater and thermostat
                                position
        nb_vol               --  
                               #number of volumes the storage is modelled with
                               #see App.C (C.1.2 selection of the number of volumes to model the storage unit)
                               #for more details if this wants to be changed.
        energy_supply_conn_unmet_demand 
            -- reference to EnergySupplyConnection object to be used to record unmet energy demand
        energy_supply_conn_pump
        contents             -- reference to MaterialProperties object

        """
        # initialise StorageTank class
        super().__init__(
            volume,
            losses,
            init_temp,
            cold_feed,
            simulation_time,
            heat_source_dict,
            project,
            external_conditions,
            detailed_output,
            nb_vol,
            primary_pipework_lst=None,
            energy_supply_conn_unmet_demand=None,
            contents=WATER,
            )

        # Initialise smart hot water tank specific parameters
        self.__power_pump_kW = power_pump_kW
        self.__max_flow_rate_pump_l_per_min = max_flow_rate_pump_l_per_min
        self.__temp_usable = temp_usable
        self.__temp_setpnt_max = temp_setpnt_max
        self.__energy_supply_connection_pump = energy_supply_conn_pump

    def _retrieve_setpnt(self, heat_source):
        setpntmin, setpntmax = super()._retrieve_setpnt(heat_source)

        if setpntmin is not None:
            if not 0 <= setpntmin <= 1:
                raise ValueError(f"setpntmin for {heat_source} must be between 0 and 1, value is {setpntmin}")

        if setpntmax is not None:
            if not 0 <= setpntmax <= 1:
                raise ValueError(f"setpntmax for {heat_source} must be between 0 and 1, value is {setpntmax}")

        return setpntmin, setpntmax

    def _determine_heat_source_switch_on(self, temp_s3_n, heat_source, heater_layer, thermostat_layer=None):
        setpntmin, _ = self._retrieve_setpnt(heat_source)

        # Calculates state of charge
        state_of_charge = self.calc_state_of_charge(temp_s3_n)

        # Turn heater on if state of charge is less than minimum state of charge
        if setpntmin is not None and state_of_charge <= setpntmin:
            self._heating_active[heat_source] = True


    def _determine_heat_source_switch_off(self, temp_s8_n, heat_source, heater_layer, thermostat_layer=None):
        _, setpntmax = self._retrieve_setpnt(heat_source)

        # Calculates state of charge
        state_of_charge = self.calc_state_of_charge(temp_s8_n)

        # Turn heater off if max temp is None or state of charge has reached maximum state of charge
        if setpntmax is None or state_of_charge >= setpntmax:
            self._heating_active[heat_source] = False

    def _temp_flow(self, heat_source):
        return self.__temp_setpnt_max.setpnt()

    def calc_state_of_charge(self, T_h):
        """Calculate state of charge"""

        # Thermocline sensors calculate temperatures at all layers in the tank
        number_of_layers = len(T_h)
        height_of_layer = 1.0 / number_of_layers
    
        # Usable temperature
        T_u = self.__temp_usable

        # Cold inlet temperature
        T_c = self._cold_feed.temperature()

        # Max set point temperature
        T_sp = self.__temp_setpnt_max.setpnt()
    
        # Calculate state of charge
        soc_numerator_total = 0.0
        for T_h_i in T_h:
            if T_h_i >= T_u:
                soc_numerator_total += (1 + (T_h_i - T_u) / (T_u - T_c)) * height_of_layer
        soc_denominator = 1 + (T_sp - T_u) / (T_u - T_c)

        # Rounding to avoid floating point errors
        soc =  round(soc_numerator_total / soc_denominator, 5)

        # Raise error if below 0
        # TODO add an error message if state of charge above 1 when function called.
        # The error should be raised when appropriate as there are instances when 
        # the SOC can be above 1 which may not be invalid such as when temp_setpnt_max
        # is decreased from one timestep to another. To determine whether when it's 
        # apprpropriate to call an error the soc from the pre timestep is needed 
        # which is currently not recorded. 
        if soc < 0:
            raise ValueError(f"State of charge should not be below 0, instead SOC is {soc}")

        return soc

    def energy_req_target_temp(
            self,
            initial_temps,
            energy_available,
            heater_layer,
            Q_ls_n_prev_heat_source,
            temp_setpntmax
        ):
        """Calculate energy required to hit target temperature"""
        # Calculate temps with energy_available
        _, temp_after_input = self.calc_temps_with_energy_input(initial_temps, energy_available)

        # Rearrange tank temperatures
        stored_heat, rearranged_temps = self.rearrange_temperatures(temp_after_input)

        # Calculate final temperatures after thermal losses
        energy_input, Q_ls, final_temps, Q_ls_n = self.calc_temps_after_thermal_losses(
            rearranged_temps,
            energy_available,
            stored_heat,
            heater_layer,
            Q_ls_n_prev_heat_source,
            temp_setpntmax,
        )

        return energy_input, final_temps, Q_ls_n

    def calculate_energy_for_state_of_charge(
            self,
            heat_source,
            initial_temps,
            Q_x_in_n,
            heater_layer,
            Q_ls_n_prev_heat_source,
            controlmax_diverter = None,
        ):
        """Calculate energy required for state of charge"""
        if controlmax_diverter is not None:
            soc_max = controlmax_diverter.setpnt()
        else:
            _, soc_max = self._retrieve_setpnt(heat_source)
        temp_layers = deepcopy(initial_temps)
        energy_available = deepcopy(Q_x_in_n)
        Q_in_H_W = [0] * len(self._Vol_n)
        Q_ls_n_already_considered = Q_ls_n_prev_heat_source

        for i in range(len(self._Vol_n)):
            if sum(energy_available) <= 0:
                break

            # Calculate energy required for usable and max temperatures
            energy_req_usable, temp_simulation_usable, Q_ls_n_usable = self.energy_req_target_temp(temp_layers, energy_available, heater_layer, Q_ls_n_already_considered, self.__temp_usable)
            energy_req_max, temp_simulation_max, Q_ls_n_max = self.energy_req_target_temp(temp_layers, energy_available, heater_layer, Q_ls_n_already_considered, self.__temp_setpnt_max.setpnt())

            # Ensure energy required for usable and max temperatures are not negative
            energy_req_usable = max(energy_req_usable, 0)
            energy_req_max = max(energy_req_max, 0)

            # Calculate state of charge for usable and max temperatures
            soc_temp_usable = self.calc_state_of_charge(temp_simulation_usable)
            soc_temp_max = self.calc_state_of_charge(temp_simulation_max)

            if soc_temp_usable >= soc_max:
                Q_in_H_W[heater_layer] += energy_req_usable
                break
            elif soc_temp_max > soc_max:
                Q_in_H_W[heater_layer] += np.interp(soc_max, (soc_temp_usable, soc_temp_max), (energy_req_usable, energy_req_max))
                break
            Q_ls_n_already_considered = [sum(x) for x in zip(Q_ls_n_max, Q_ls_n_already_considered)]
            Q_in_H_W[heater_layer] += energy_req_max
            energy_available[heater_layer] -= energy_req_max
            temp_layers = temp_simulation_max

            energy_req_bottom_layer_to_setpnt = self._rho * self._Cp * self._Vol_n[0] * temp_layers[0]
            if sum(energy_available) <= energy_req_bottom_layer_to_setpnt:
                # Pump partial layer to the top
                fraction_to_pump = sum(energy_available) / energy_req_bottom_layer_to_setpnt
                volume_to_pump = fraction_to_pump * self._Vol_n[0]
                remaining_vols = deepcopy(self._Vol_n)
                temp_layers = self.temps_after_pumping(volume_to_pump, remaining_vols, temp_layers)
            else:
                # Pump one layer to the top
                temp_pumped_layer = temp_layers.pop(0)
                temp_layers.append(temp_pumped_layer)
                Q_ls_layer = Q_ls_n_already_considered.pop(0)
                Q_ls_n_already_considered.append(Q_ls_layer)

        # Calculate total energy required to meet max state of charge
        energy_req_for_soc = sum(Q_in_H_W)

        # Calculate energy in layers
        Q_layers \
            = self._rho * self._Cp \
            * sum(
                self._Vol_n[i] * temp_layers[i]
                for i in range(len(self._Vol_n))
            )

        return energy_req_for_soc, Q_in_H_W

    def calc_final_temps(
            self,
            temp_s3_n,
            heat_source,
            Q_x_in_n,
            heater_layer,
            Q_ls_n_prev_heat_source,
            controlmax_diverter = None,
        ):
        temp_setpntmax = self.__temp_setpnt_max.setpnt()

        # Tank with energy required for state of charge
        energy_req_for_soc, Q_in_H_W_n = self.calculate_energy_for_state_of_charge(heat_source, temp_s3_n, Q_x_in_n, heater_layer, Q_ls_n_prev_heat_source, controlmax_diverter)

        # Calculate temperatures after energy required to hit state of charge input
        Q_s6, temp_s6_n = self.calc_temps_with_energy_input(temp_s3_n, Q_in_H_W_n)

        # Rearrange tank
        Q_h_sto_s7, temp_s7_n = self.rearrange_temperatures(temp_s6_n)

        # Calculate new temperatures after operation of top up pump
        temp_s7_n = self.calc_temps_after_top_up_pump(temp_s7_n, energy_req_for_soc, heater_layer)

        # Rearrange tank
        Q_h_sto_s7, temp_s7_n = self.rearrange_temperatures(temp_s7_n)

        # STEP 8 Thermal losses and final temperature
        Q_in_H_W, Q_ls, temp_s8_n, Q_ls_n = self.calc_temps_after_thermal_losses(
            temp_s7_n,
            Q_in_H_W_n,
            Q_h_sto_s7,
            heater_layer,
            Q_ls_n_prev_heat_source,
            temp_setpntmax,
        )

        # Adjust energy input based on actual usage
        input_energy_adj = deepcopy(Q_in_H_W)
        self.__energy_demand_test = deepcopy(input_energy_adj)

        # Actual heat source output
        heat_source_output = self.heat_source_output(heat_source, input_energy_adj)

        # calculate volume pumped using actual heat source output
        volumes = deepcopy(self._Vol_n)
        volume_pumped = self.bottom_to_top_pump_volume(temp_s3_n, heat_source_output, heater_layer, volumes)

        # Calculate pump energy consumption
        energy_per_litre = self.__power_pump_kW / (self.__max_flow_rate_pump_l_per_min  * units.minutes_per_hour)
        pump_energy_kWh = energy_per_litre * volume_pumped

        # Record pump energy consumption
        self.__energy_supply_connection_pump.demand_energy(pump_energy_kWh)

        return temp_s8_n, Q_x_in_n, Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, Q_ls, Q_ls_n

    def calc_temps_after_top_up_pump(self, temp_s7_n, Q_x_in_n, heater_layer):
        """Calculate new temperatures after top up pump of Smart hot water tank """

        # Init for remaining volume of water in storage layers
        remaining_vols = deepcopy(self._Vol_n)
        # Temperature of water in storage tank layers
        temp_tank = deepcopy(temp_s7_n)

        # Volume pumped using top up pump
        volume_pumped = self.bottom_to_top_pump_volume(temp_tank, Q_x_in_n, heater_layer, remaining_vols)

        return self.temps_after_pumping(volume_pumped, remaining_vols, temp_tank)

    def temps_after_pumping(self, volume_pumped, remaining_vols, temp_tank):
        """Calculate the temperatures of the tank after volume is pumped"""
        if volume_pumped > 0:
            # Calculate water removed
            # --------------- 
            # If there is water to be pumped, remove water from bottom layers 
            # starting from bottom layer. This will keep removing until there 
            # is no more water to be removed. 
            volume_pumped_remaining = volume_pumped
            for i in range(len(remaining_vols)):
                if volume_pumped_remaining <= 0:
                    break
                volume_removed = min(volume_pumped_remaining, remaining_vols[i])
                remaining_vols[i] -= volume_removed
                volume_pumped_remaining -= volume_removed

            # Carry out water redistribution
            # --------------- 
            # Iterate from the bottom layer upwards. Calculate the amount of 
            # water needed to refill each layer
            for i in range(len(self._Vol_n)):
                # Determine how much volume needs to be added to this layer
                needed_volume = self._Vol_n[i] - remaining_vols[i]

                # If this layer is already full, continue to the next
                if needed_volume <= 0:
                    continue

                # Initialise the variables for mixing temperatures
                volume_weighted_temperature = remaining_vols[i] * temp_tank[i]

                # Filling layer
                # --------------- 
                # For each layer that needs water, it looks at layer above
                # it to find available water. As it finds available water, it 
                # moves it to the current layer and mixes the temperature.
                # Code allows circular movement of water where if it reaches the 
                # top layer and still requires more water, it will circle back to 
                # the bottom layer and check again.
                for j in range(i + 1, i + len(self._Vol_n)):
                    if j >= len(self._Vol_n):
                        j -= len(self._Vol_n)
                    # remaining_vols list is the volume of water available to replenish layer i
                    if remaining_vols[j] > 0:
                        # Determine the volume to move down from this layer
                        move_volume = min(needed_volume, remaining_vols[j])
                        remaining_vols[j] = remaining_vols[j] - move_volume
                        remaining_vols[i] += move_volume

                        # Adjust the temperature by mixing in the moved volume
                        volume_weighted_temperature += move_volume * temp_tank[j]

                        # Decrease the amount of volume needed for the current layer
                        needed_volume -= move_volume
                        if needed_volume <= 0:
                            break

                assert remaining_vols[i] == self._Vol_n[i], "Volume mismatch in layer " +str(i)


                # Temperatures after moving
                # ----------------
                # After moving water to a layer, calculate the new temperature
                # for the current layer based on vol and temperature.
                temp_tank[i] = volume_weighted_temperature / remaining_vols[i]

        return temp_tank

    def bottom_to_top_pump_volume(self, temp_s7_n, Qin, heater_layer, volumes):
        """Calculate the volume of water pumped from bottom to top of the tank"""

        # Initialise list of thermal losses in kWh
        Q_ls_n =  [0] * self._NB_VOL

        # Standby losses coefficient - W/K
        H_sto_ls = self.stand_by_losses_coefficient()

        # Calculate heat losses difference for all layers 
        for i, vol_i in list(enumerate(self._Vol_n)):
            Q_ls_n[i] = (H_sto_ls * self._rho * self._Cp) \
                      * (self._Vol_n[i] / self._V_total) \
                      * (self.__temp_setpnt_max.setpnt() - self._temp_amb) \
                      * self._simulation_time.timestep()
        # The heat losses list is used to calculate the temperature difference 
        # required for the top layer.
        temp_diff_losses = Q_ls_n[-1] / (self._rho * self._Cp * self._Vol_n[-1])

        # Top layer temperature
        top_layer_temp = temp_s7_n[-1]

        # Target temperature is increased to account for thermal losses.
        temp_target = self.__temp_setpnt_max.setpnt() + temp_diff_losses

        if top_layer_temp <= temp_target or Qin <= 0:
            # No pumping needed if top layer is below setpoint or no energy available
            return 0

        # Split volumes into below the heater layer
        bottom_volumes = volumes[:heater_layer]

        # Initialize fractions
        # 0 for layers below heater layer, 1 for heater layer and above
        temp_factors = [0] * heater_layer + [1] * (len(volumes) - heater_layer)

        # Iterates through the tank up to heater layer to determine how much each layer needs to be pumped
        for current_layer in range(heater_layer):
            # Calcualte the fraction of the current layer that needs to be pumped to maintain the overall temperature
            # Note: strictly speaking, the sums in the formula below should
            # exclude the current layer, but as the initial value of the temperature
            # factor is zero, this makes no difference in practice
 
            numerator = sum(t * f for t, f in zip(temp_s7_n, temp_factors)) - temp_target * sum(f for f in temp_factors)
            denominator = temp_target - temp_s7_n[current_layer]
            if denominator <= 0:
                # If the currrent layer is at or above target temperature, pump all of it
                temp_factors[current_layer] = 1.0
            else:
                # Calculate the fraction of the current layer to be pumped
                temp_factors[current_layer] = numerator / denominator

            if temp_factors[current_layer] < 1.0:
                # If we don't need to pump the entire layer, stop iteration
                break
            else:
                # If entire layer needs to be pumped, set factor to 1 
                # and continue to next layer
                temp_factors[current_layer] = 1.0

        # Calculate volume to be pumped (only from layers below heater_layer)
        volume_pumped = sum(v * f for v, f in zip(bottom_volumes, temp_factors[:heater_layer]))

        # Check that the volume pumped doesn't exceed the volume of water up to the heater layer
        assert volume_pumped <= sum(bottom_volumes)

        # Cap volume pumped based on pump max flow rate in timestep
        max_volume_pumped = self.__max_flow_rate_pump_l_per_min * self._simulation_time.timestep() * units.minutes_per_hour
        volume_pumped = min(volume_pumped, max_volume_pumped)

        return volume_pumped

    def testoutput(self, usage_events, volume_extracted, Q_use_W, Q_unmet_W,
                   temp_ini_n,temp_s3_n, Q_x_in_n,
                   Q_s6, temp_s6_n, temp_s7_n, Q_in_H_W, Q_ls,
                   temp_s8_n, temp_final, temp_average,
                   ):
        """ print output to a file for analysis """
        if self._detailed_output:
            demand = summarise_events(usage_events)
            # Calculates state of charge
            state_of_charge_draw_off = round(self.calc_state_of_charge(temp_s3_n), 6)
            state_of_charge_final = round(self.calc_state_of_charge(temp_s8_n), 6)

            if self._simulation_time.index() == 0:
                def header_dup(header: str, n: int, with_index=True):
                    for i in range(n):
                        yield header + (f" {i+1}" if with_index else "")

                # Include headers first
                self._detailed_results.append(
                    [
                        "time",
                        "volume total",
                        "specific heat",
                        "density",
                        "cold water",
                        "events",
                        "volume extracted",
                        *header_dup("initial temp.", len(temp_ini_n)),
                        "energy withdrawn",
                        "energy unmet",
                        *header_dup("temp. after volume withdrawn", len(temp_s3_n)),
                        "state of charge after volume withdrawn",
                        *header_dup("potential energy input", len(Q_x_in_n)),
                        "theoretical energy stored after energy input",
                        *header_dup("theoretical temp. after energy input", len(temp_s6_n)),
                        *header_dup("temp. after volume mixing", len(temp_s7_n)),
                        "energy input (adjusted)",
                        "thermal losses",
                        *header_dup("temp. after thermal losses", len(temp_s8_n)),
                        "temp_final_drawoff",
                        "temp_average_drawoff",
                        "state of charge final"
                    ])
                self._detailed_results.append(
                    [
                        "h",
                        "litres",
                        "kWh/kgK",
                        "kg/l",
                        "oC",
                        "T(l@oC)",
                        "litres",
                        *header_dup("oC",len(temp_ini_n),False),
                        "kWh",
                        "kWh",
                        *header_dup("oC", len(temp_s3_n), False),
                        "fraction",
                        *header_dup("kWh", len(Q_x_in_n), False),
                        "kWh",
                        *header_dup("oC", len(temp_s6_n), False),
                        *header_dup("oC", len(temp_s7_n), False),
                        "kWh",
                        "kWh",
                        *header_dup("oC", len(temp_s8_n), False),
                        "oC",
                        "oC",
                        "fraction",
                    ])

            self._detailed_results.append(
                [
                    str(self._simulation_time.hour_of_day()),
                    str(self._V_total),
                    str(self._Cp),
                    str(self._rho),
                    str(self._cold_feed.temperature()),
                    demand,
                    str(volume_extracted),
                    *temp_ini_n,
                    str(Q_use_W),
                    str(Q_unmet_W),
                    *temp_s3_n,
                    str(state_of_charge_draw_off),
                    *Q_x_in_n,
                    str(Q_s6),
                    *temp_s6_n,
                    *temp_s7_n,
                    str(Q_in_H_W),
                    str(Q_ls),
                    *temp_s8_n,
                    str(temp_final),
                    str(temp_average),
                    str(state_of_charge_final),
                ]
            )

class ImmersionHeater:
    """ An object to represent an immersion heater """

    def __init__(self, rated_power, energy_supply_conn, simulation_time, controlmin=None, controlmax=None):
        """ Construct an ImmersionHeater object

        Arguments:
        rated_power        -- in kW
        energy_supply_conn -- reference to EnergySupplyConnection object
        simulation_time    -- reference to SimulationTime object
        controlmin            -- reference to a control object which must select current
                                the minimum timestep temperature
        controlmax            -- reference to a control object which must select current
                                the maximum timestep temperature
        diverter           -- reference to a PV diverter object
        """
        self.__pwr                = rated_power
        self.__energy_supply_conn = energy_supply_conn
        self.__simulation_time    = simulation_time
        self.__controlmin         = controlmin
        self.__controlmax         = controlmax
        self.__diverter = None

    def setpnt(self):
        """ Return setpoint (not necessarily temperature) """
        return self.__controlmin.setpnt(), self.__controlmax.setpnt()

    def connect_diverter(self, diverter):
        if self.__diverter is not None:
            sys.exit('Diverter already connected.')
        self.__diverter = diverter

    def demand_energy(self, energy_demand):
        """ Demand energy (in kWh) from the heater """
        if energy_demand < 0.0:
            raise ValueError("Negative energy demand on ImmersionHeater: " + str(energy_demand))

        # Account for time control where present. If no control present, assume
        # system is always active (except for basic thermostatic control, which
        # is implicit in demand calculation).
        if self.__controlmin is None or self.__controlmin.is_on():
            # Energy that heater is able to supply is limited by power rating
            energy_supplied = min(energy_demand, self.__pwr * self.__simulation_time.timestep())
        else:
            energy_supplied = 0.0

        # If there is a diverter to this immersion heater, then any heating
        # capacity already in use is not available to the diverter.
        if self.__diverter is not None:
            self.__diverter.capacity_already_in_use(energy_supplied)

        self.__energy_supply_conn.demand_energy(energy_supplied)
        return energy_supplied

    def energy_output_max(self, ignore_standard_ctrl=False):
        """ Calculate the maximum energy output (in kWh) from the heater """

        # Account for time control where present. If no control present, assume
        # system is always active (except for basic thermostatic control, which
        # is implicit in demand calculation).
        if self.__controlmin is None or self.__controlmin.is_on() or ignore_standard_ctrl:
            # Energy that heater is able to supply is limited by power rating
            power_max = self.__pwr * self.__simulation_time.timestep()
        else:
            power_max = 0.0

        return power_max


class PVDiverter:
    """ An object to represent a PV diverter """

    def __init__(self, storage_tank, immersion_heater, controlmax):
        """ Construct a PVDiverter object
        
        Arguments:
        storage_tank -- reference to the StorageTank or SmartHotWaterTank object fed by the diverter
        immersion_heater -- reference to the ImmersionHeater object fed by the diverter
        controlmax -- reference to a control object which must select current
                                the maximum timestep temperature for the diverter

        Other variables:
        capacity_already_in_use -- variable to track heater output that would
                                   happen anyway, to avoid double-counting
        """
        self.__storage_tank = storage_tank
        self.__immersion_heater = immersion_heater
        self.__controlmax = controlmax
        self.__capacity_already_in_use = 0.0

        self.__immersion_heater.connect_diverter(self)

    def capacity_already_in_use(self, energy_supplied):
        """ Record heater output that would happen anyway, to avoid double-counting """
        self.__capacity_already_in_use += energy_supplied

    def divert_surplus(self, supply_surplus):
        """ Divert as much surplus as possible to the heater

        Arguments:
        supply_surplus -- surplus energy, in kWh, available to be diverted (negative by convention)
        """
        # Check how much spare capacity the immersion heater has
        imm_heater_max_capacity_spare \
            = self.__immersion_heater.energy_output_max(ignore_standard_ctrl=True) \
            - self.__capacity_already_in_use

        # Calculate the maximum energy that could be diverted
        # Note: supply_surplus argument is negative by convention, so negate it here
        energy_diverted_max = min(imm_heater_max_capacity_spare, - supply_surplus)

        # Add additional energy to storage tank and calculate how much energy was accepted
        energy_diverted = self.__storage_tank.additional_energy_input(
            self.__immersion_heater,
            energy_diverted_max,
            self.__controlmax,
            )

        return energy_diverted

    def timestep_end(self):
        """ Reset variable at end of timestep """
        self.__capacity_already_in_use = 0.0


""" The following code contains objects that represent solar thermal systems.
Method 3 in BS EN 15316-4-3:2017.
"""

class SolarThermalSystem:
    """ An object to represent a solar thermal system """

    def __init__(self, 
                 sol_loc,
                 area_module,
                 modules,
                 peak_collector_efficiency,
                 incidence_angle_modifier,
                 first_order_hlc,
                 second_order_hlc,
                 collector_mass_flow_rate,
                 power_pump,
                 power_pump_control,
                 energy_supply_conn,
                 tilt,
                 orientation,
                 solar_loop_piping_hlc,
                 ext_cond, 
                 simulation_time,
                 project,
                 controlmax,
                 contents=WATER,
                 energy_supply_from_environment_conn = None
                 ):
        """ Construct a SolarThermalSystem object

        Arguments:
        sol_loc         -- Location of the main part of the collector loop piping
        area_module     -- Collector module reference area 
        modules         -- Number of collector modules installed
        peak_collector_efficiency 
                        -- Peak collector efficiency
        incidence_angle_modifier 
                        -- Hemispherical incidence angle modifier
        first_order_hlc -- First order heat loss coefficient
        second_order_hlc 
                        -- Second order heat loss coefficient
        collector_mass_flow_rate 
                        -- Mass flow rate solar loop
        power_pump      -- Power of collector pump
        power_pump_control
                        -- Power of collector pump controller
        energy_supply_conn    
                        -- reference to EnergySupplyConnection object
        tilt            -- is the tilt angle (inclination) of the PV panel from horizontal,
                            measured upwards facing, 0 to 90, in degrees.
                            0=horizontal surface, 90=vertical surface.
                            Needed to calculate solar irradiation at the panel surface.
        orientation     -- is the orientation angle of the inclined surface, expressed as the
                            geographical azimuth angle of the horizontal projection of the inclined
                            surface normal, -180 to 180, in degrees;
                            Assumed N 180 or -180, E 90, S 0, W -90
                            TODO - PV standard refers to angle as between 0 to 360?
                            Needed to calculate solar irradiation at the panel surface.
        solar_loop_piping_hlc 
                        -- Heat loss coefficient of the collector loop piping                   
        ext_cond        -- reference to ExternalConditions object
        simulation_time -- reference to SimulationTime object
        contents        -- reference to MaterialProperties object

        overshading     -- TODO could add at a later date. Feed into solar module
        controlmax      -- reference to a control object which must select current
                        the maximum timestep temperature
        """
        self.__sol_loc = sol_loc
        self.__area = area_module * modules
        self.__peak_collector_efficiency = peak_collector_efficiency
        self.__incidence_angle_modifier = incidence_angle_modifier
        self.__first_order_hlc = first_order_hlc
        self.__second_order_hlc = second_order_hlc
        self.__collector_mass_flow_rate = collector_mass_flow_rate
        self.__power_pump = power_pump
        self.__power_pump_control = power_pump_control
        self.__energy_supply_conn = energy_supply_conn
        self.__tilt = tilt
        self.__orientation = orientation
        self.__solar_loop_piping_hlc = solar_loop_piping_hlc
        self.__external_conditions = ext_cond
        self.__simulation_time = simulation_time
        self.__heat_output_collector_loop = 0
        self.__energy_supplied = 0
        self.__project = project
        self.__controlmax = controlmax
        self.__energy_supply_from_environment_conn = energy_supply_from_environment_conn

        # Water specific heat in J/kg.K
        # (defined under eqn 51 on page 40 of BS EN ISO 15316-4-3:2017)
        self.__Cp = contents.specific_heat_capacity()

    def setpnt(self):
        """ Return setpoint (not necessarily temperature) """
        return self.__controlmax.setpnt(), self.__controlmax.setpnt()

    def energy_output_max(self, storage_tank, temp_storage_tank_s3_n):
        """ Calculate collector loop heat output
            eq 49 to 58 of STANDARD """

        #Air temperature in a heated space in the building
        air_temp_heated_room = self.__project.temp_internal_air_prev_timestep()

        # Eq 49        
        if self.__sol_loc == 'HS':
            self.__air_temp_coll_loop = air_temp_heated_room
        elif self.__sol_loc == 'NHS':
            self.__air_temp_coll_loop \
                = (air_temp_heated_room
                + self.__external_conditions.air_temp()
                ) / 2
        elif self.__sol_loc == 'OUT':
            self.__air_temp_coll_loop = self.__external_conditions.air_temp()
        else:
            sys.exit('SolarThermalSystem: Collector loop location not valid.')
            
        #First estimation of average collector water temperature. Eq 51
        #initialise temperature
        # If first time step, pick bottom of the tank temperature as inlet_temp_s1
        if (self.__simulation_time.index() == 0):
            inlet_temp_s1 = temp_storage_tank_s3_n[0]
            self.__inlet_temp = deepcopy(inlet_temp_s1)
        else:
            inlet_temp_s1 = deepcopy(self.__inlet_temp)

        #solar_irradiance in W/m2
        solar_irradiance = self.__external_conditions.calculated_total_solar_irradiance( \
            self.__tilt,
            self.__orientation
            )
        if (solar_irradiance == 0):
            # TODO Consider the case of energy left from previous step not totally dissipated
            # TODO Solar irradiance can be negative due to negative diffuse radiation values.
            # TODO Should negative values be set to zero? Why is diffuse irradiation calc producing neg values?
            self.__heat_output_collector_loop = 0
            return 0
            
        avg_collector_water_temp \
            = inlet_temp_s1 \
            + ( 0.4 * solar_irradiance * self.__area ) \
            / ( self.__collector_mass_flow_rate * self.__Cp * 2 )
            
        #Calculation of collector efficiency
        for _ in range(4):
            # Eq 53
            Th = (avg_collector_water_temp - self.__external_conditions.air_temp()) / (solar_irradiance )
            
            # Eq 52
            collector_efficiency \
                = self.__peak_collector_efficiency \
                * self.__incidence_angle_modifier \
                - self.__first_order_hlc * Th \
                - self.__second_order_hlc * Th**2 * solar_irradiance 

            # Eq 54
            collector_absorber_heat_input = self.__peak_collector_efficiency * solar_irradiance * \
            self.__area * self.__simulation_time.timestep() / units.W_per_kW

            # Eq 55
            collector_output_heat = collector_efficiency * solar_irradiance * \
            self.__area * self.__simulation_time.timestep() / units.W_per_kW

            # Eq 56
            heat_loss_collector_loop_piping \
                 = self.__solar_loop_piping_hlc \
                 * ( avg_collector_water_temp 
                   - self.__air_temp_coll_loop 
                   ) \
                 * self.__simulation_time.timestep() / units.W_per_kW

            # Eq 57
            self.__heat_output_collector_loop = collector_output_heat - heat_loss_collector_loop_piping
            if self.__heat_output_collector_loop < self.__power_pump * self.__simulation_time.timestep() * 3 / units.W_per_kW:
                self.__heat_output_collector_loop = 0
            
            #Call to the storage tank
            temp_layer_0, inlet_temp2 = \
                storage_tank.storage_tank_potential_effect(self.__heat_output_collector_loop, temp_storage_tank_s3_n)
            
            # Eq 58
            avg_collector_water_temp \
                = ( self.__inlet_temp + inlet_temp2 ) / 2 \
                + self.__heat_output_collector_loop \
                / (self.__collector_mass_flow_rate 
                  * self.__Cp 
                  * 2
                  )
                                                
        # Copy the finishing value of inlet temp ready for start of next timestep
        self.__inlet_temp = deepcopy(inlet_temp2)

        return self.__heat_output_collector_loop
    
    def demand_energy(self, energy_demand):
        """ Demand energy (in kWh) from the solar thermal"""

        self.__energy_supplied = min(energy_demand, self.__heat_output_collector_loop )

        # Eq 59 and 60 to calculate auxiliary energy - note that the if condition
        # is the wrong way round in BS EN 15316-4-3:2017
        if self.__energy_supplied == 0: 
            auxilliary_energy_consumption = self.__power_pump_control * self.__simulation_time.timestep()
        else:
            auxilliary_energy_consumption = ( self.__power_pump_control + self.__power_pump ) \
            * self.__simulation_time.timestep()
            
        self.__energy_supply_conn.demand_energy(auxilliary_energy_consumption)
        
        if self.__energy_supply_from_environment_conn:
            self.__energy_supply_from_environment_conn.demand_energy(self.__energy_supplied)
        
        return self.__energy_supplied

    # methods to facilitate unit testing
    def test_energy_potential(self):
        return(self.__heat_output_collector_loop)

    def test_energy_supplied(self):
        return(self.__energy_supplied)

def summarise_events(events):
    # Exclude 'IES' events
    if events is None:
        return ''
    filtered_events = [e for e in events if e['name'] != 'IES']
    
    # Map event types to abbreviations
    abbreviations = {'Shower': 'S', 'Bath': 'B', 'Other': 'O'}
    
    # Generate the summary in the desired format
    def format_event(e):
        # Retrieve warm_volume if it exists, or use a placeholder if missing
        warm_volume = e.get('warm_volume', '?')
        temperature = e['temperature']
        abbrev = abbreviations[e['type']]
        return f"{abbrev}({warm_volume}@{temperature})"
    
    condensed = '|'.join([format_event(e) for e in filtered_events if e['type'] in abbreviations])
    
    return condensed
