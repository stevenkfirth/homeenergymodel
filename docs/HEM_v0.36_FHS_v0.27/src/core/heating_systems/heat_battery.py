#!/usr/bin/env python3

"""
This module provides object(s) to model the behaviour of heat batteries.
"""

# Third-party imports
import sys
from enum import Enum, auto
import numpy as np
#import types

# Local imports
import core.units as units
from core.simulation_time import SimulationTime
from core.controls.time_control import ChargeControl
from core.units import Celcius2Kelvin, Kelvin2Celcius
from core.material_properties import WATER

class ServiceType(Enum):
    WATER_REGULAR = auto()
    SPACE = auto()

class OperationMode(Enum):
    NORMAL = auto()
    ONLY_CHARGING = auto()
    LOSSES = auto()

class HeatBatteryService:
    """ A base class for objects representing services (e.g. water heating) provided by a heat battery.

    This object encapsulates the name of the service, meaning that the system
    consuming the energy does not have to specify this on every call, and
    helping to enforce that each service has a unique name.

    Separate subclasses need to be implemented for different types of service
    (e.g. HW and space heating). These should implement the following functions:
    - demand_energy(self, energy_demand)
    """

    def __init__(self, heat_battery, service_name, control=None):
        """ Construct a HeatBatteryService object

        Arguments:
        heat_battery -- reference to the Heat Battery object providing the service
        service_name -- name of the service demanding energy from the heat battery
        control -- reference to a control object which must implement is_on() func
        """
        self._heat_battery = heat_battery
        self._service_name = service_name
        self.__control = control

    def is_on(self):
        if self.__control is not None:
            service_on = self.__control.is_on()
        else:
            service_on = True
        return service_on

class HeatBatteryServiceWaterRegular(HeatBatteryService):
    """ An object to represent a water heating service provided by a regular heat battery.

    This object contains the parts of the heat battery calculation that are
    specific to providing hot water.
    """

    def __init__(self,
                 heat_battery,
                 heat_battery_data,
                 service_name,
                 cold_feed,
                 simulation_time,
                 controlmin,
                 controlmax
                ):
        """ Construct a HeatBatteryServiceWaterRegular object

        Arguments:
        heat_battery       -- reference to the Heat Battery object providing the service
        heat_battery_data  -- regular heat battery heating properties
        service_name       -- name of the service demanding energy from the heat_battery_data
        cold_feed          -- reference to ColdWaterSource object
        simulation_time    -- reference to SimulationTime object
        controlmin            -- reference to a control object which must select current
                                the minimum timestep temperature
        controlmax            -- reference to a control object which must select current
                                the maximum timestep temperature
        """
        super().__init__(heat_battery, service_name, controlmin)

        self.__cold_feed = cold_feed
        self.__service_name = service_name
        self.__simulation_time = simulation_time
        self.__controlmin = controlmin
        self.__controlmax = controlmax

    def setpnt(self):
        """ Return setpoint (not necessarily temperature) """
        return self.__controlmin.setpnt(), self.__controlmax.setpnt()

    def get_cold_water_source(self):
        return self.__cold_feed

    def get_temp_hot_water(self):
        volume = 20 # Nominal volumen to calculate water temperature from battery
        inlet_temp = self.__cold_feed.temperature()

        return self._heat_battery._HeatBattery__get_temp_hot_water(
                            inlet_temp,
                            volume)

    def demand_hot_water(self, usage_events):
        """ Demand volume from boiler. Currently combi only """
        timestep = self.__simulation_time.timestep()

        energy_demand = 0.0
        self.__temp_hot_water = 0.0

        if usage_events is not None:
            # Filtering out IES events that don't get added a 'warm_volume' when processing 
            # the dhw_demand calculation
            filtered_events = filter(lambda e: 'warm_volume' in e, usage_events)
            for event in filtered_events:
                warm_temp = event['temperature']
                warm_volume = event['warm_volume']

                if warm_temp > self.__temp_hot_water:
                    self.__temp_hot_water = warm_temp
                    
                energy_content_kWh_per_litre = WATER.volumetric_energy_content_kWh_per_litre(
                    warm_temp,
                    self.__cold_feed.temperature()
                    )
                energy_demand += warm_volume * energy_content_kWh_per_litre

        service_on = self.is_on()
        if not service_on:
            energy_demand = 0.0
            
        return self._heat_battery._HeatBattery__demand_energy(
            self.__service_name,
            ServiceType.WATER_REGULAR,
            energy_demand,
            self.__cold_feed.temperature(),
            self.__temp_hot_water,
            service_on,
            update_heat_source_state = True
            )

    def demand_energy(self, energy_demand, temp_return, time_start=0.0, update_heat_source_state=True):
        """ Demand energy (in kWh) from the heat_battery """
        service_on = self.is_on()
        if not service_on:
            energy_demand = 0.0

        return self._heat_battery._HeatBattery__demand_energy(
            self.__service_name,
            ServiceType.WATER_REGULAR,
            energy_demand,
            temp_return,
            self.__controlmax.setpnt(),
            service_on,
            update_heat_source_state = update_heat_source_state
            )

    def energy_output_max(self, temp_flow, temp_return):
        """ Calculate the maximum energy output of the heat_battery"""
        service_on = self.is_on()
        if not service_on:
            return 0.0

        return self._heat_battery._HeatBattery__energy_output_max(temp_flow)

class HeatBatteryServiceSpace(HeatBatteryService):
    """ An object to represent a space heating service provided by a heat_battery to e.g. radiators.

    This object contains the parts of the heat battery calculation that are
    specific to providing space heating.
    """
    
    def __init__(self, heat_battery, service_name, control):
        """ Construct a HeatBatteryServiceSpace object

        Arguments:
        heat_battery -- reference to the Heat Battery object providing the service
        service_name -- name of the service demanding energy from the heat battery
        control      -- reference to a control object which must implement is_on() and setpnt() funcs
        """
        super().__init__(heat_battery, service_name, control)
        self.__service_name = service_name
        self.__control = control

    def temp_setpnt(self):
        return self.__control.setpnt()

    def in_required_period(self):
        return self.__control.in_required_period()

    def demand_energy(self, energy_demand, temp_flow, temp_return, time_start=0.0, update_heat_source_state=True):
        """ Demand energy (in kWh) from the heat battery """
        service_on = self.is_on()
        if not service_on:
            energy_demand = 0.0

        return self._heat_battery._HeatBattery__demand_energy(
            self.__service_name,
            ServiceType.SPACE,
            energy_demand,
            temp_return,
            temp_flow,
            service_on,
            update_heat_source_state = update_heat_source_state,
            )

    def energy_output_max(self, temp_output, temp_return_feed, time_start=0.0):
        """ Calculate the maximum energy output of the heat battery"""
        if not self.is_on():
            return 0.0

        return self._heat_battery._HeatBattery__energy_output_max(temp_output, time_start)

class HeatBattery:
    """ Class to represent hydronic Heat Batteries that are electrically charged """
    
    """ This class has been introduced as a replacement for heat sources like boilers. 
        It models a type of heat battery, primarily PCM that can be charged by different
        heat sources (heat pumps, solar thermal, etc.) in addition to electricity.
        
        Currently electric charging is implemented and the function to charge the battery
        hydraulic (with Heat Pump or solar thermal) is ready but not connected to the
        rest of the HEM code. 
    """

    def __init__(self,
                heat_battery_dict,
                charge_control,
                energy_supply,
                energy_supply_conn,
                simulation_time,
                ext_cond,
                n_zones=8,
                hb_time_step=20,
                minimum_time_required_to_run = 120,
                initial_inlet_temp = 10,
                estimated_outlet_temp = 53,
                output_detailed_results=False,
                ):

        """Construct a HeatBattery object

        Arguments:
        n_units               -- number of units installed in zone

        rated_charge_power    -- in kW (Charging)
        heat_storage_capacity -- in kWh
        max_rated_heat_output -- in kW (Output to hot water and space heat services)
        max_rated_losses      -- in kW (Losses to internal or external)

        energy_supply         -- reference to EnergySupplyConnection object
        simulation_time       -- reference to SimulationTime object
        control               -- reference to a control object which must implement is_on() and setpnt() funcs
        
        Other variables:
        energy_supply_connections
                              -- dictionary with service name strings as keys and corresponding
                                 EnergySupplyConnection objects as values
        output_detailed_results -- flag to create detailed emitter output results
                                 
        """
        self.__hb_time_step = hb_time_step # 20secs is the current preferred timestep to run the heat battery iterative calculations
        self.__minimum_time_required_to_run = minimum_time_required_to_run # 120secs minimum time required for battery to deliver energy to services.
        # Number of zones in heat battery
        self.__n_zones = n_zones
        self.__initial_inlet_temp = initial_inlet_temp #initial inlet temperature to calculate first Reynolds in HeatBattery module
        self.__estimated_outlet_temp = estimated_outlet_temp #estimated outlet temperature to calculate first Reynolds in HeatBattery module

        self.__energy_supply = energy_supply
        self.__energy_supply_conn = energy_supply_conn
        self.__simulation_time: SimulationTime = simulation_time
        self.__external_conditions = ext_cond
        self.__energy_supply_connections = {}

        self.__pwr_in: float = heat_battery_dict["rated_charge_power"]
        self.__max_rated_losses: float = heat_battery_dict["max_rated_losses"]

        self.__power_circ_pump = heat_battery_dict["electricity_circ_pump"]
        self.__power_standby = heat_battery_dict["electricity_standby"]

        self.__n_units: int = heat_battery_dict["number_of_units"]
        self.__charge_control: ChargeControl = charge_control

        self.__time_unit: float = units.seconds_per_hour
        self.__total_time_running_current_timestep = 0.0
        self.__flag_first_call = True
        # Set the initial charge level of the heat battery to zero.
        self.__charge_level: float = 0.0
        self.__energy_charged = 0.0

        # Simultaneous charging allows while discharging
        self.__simultaneous_charging_and_discharging =heat_battery_dict['simultaneous_charging_and_discharging']
        # Max temperature allowed, [temp of charge]
        self.__max_temp_of_charge = heat_battery_dict['max_temperature']
        # Zone temperatures
        self.__zone_temp_C_dist_initial = self.__n_zones * [self.__max_temp_of_charge]
        # heat capacity zone material in kJ per K above Phase transition
        self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition = heat_battery_dict[
            'heat_storage_zone_material_kJ_per_K_above_Phase_transition']
        # heat capacity zone material in kJ per K below Phase transition
        self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition = heat_battery_dict[
            'heat_storage_zone_material_kJ_per_K_below_Phase_transition']
        # heat capacity zone material in kJ per K during Phase transition
        self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition = heat_battery_dict[
            'heat_storage_zone_material_kJ_per_K_during_Phase_transition']
        # phase transition temperature upper
        self.__phase_transition_temperature_upper = heat_battery_dict['phase_transition_temperature_upper']
        # phase transition temperature lower
        self.__phase_transition_temperature_lower = heat_battery_dict['phase_transition_temperature_lower']
        # velocity in HEX tube at 1 l per min in m per s
        self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s = heat_battery_dict['velocity_in_HEX_tube_at_1_l_per_min_m_per_s']
        self.__capillary_diameter_m = heat_battery_dict['capillary_diameter_m']
        # Heat Battery heat exchanger performance characterisation equation parameters A and B from test data:
        # UA = A * Ln(Re) + B
        # Where UA = Overall heat transfer coefficient of the heat exchanger in Heat Battery, [W/K]
        # charge heat transfer factor A
        self.__A = heat_battery_dict['A']
        # charge heat transfer factor B
        self.__B = heat_battery_dict['B']
        self.__heat_exchanger_surface_area_m2 = heat_battery_dict['heat_exchanger_surface_area_m2']
        self.__flow_rate_l_per_min = heat_battery_dict['flow_rate_l_per_min']

        self.__pipe_energy = {}

        self.__service_results = []
        self.__output_detailed_results = output_detailed_results
        # If detailed results are to be output, initialise list
        if output_detailed_results:
            self.__detailed_results = []
        else:
            self.__detailed_results = None

        self.__flag_1_warning = [ True, True ]

    def __create_service_connection(self, service_name):
        #Create an EnergySupplyConnection for the service name given 
        # Check that service_name is not already registered
        if service_name in self.__energy_supply_connections.keys():
            sys.exit("Error: Service name already used: "+service_name)
            # TODO Exit just the current case instead of whole program entirely?

        # Set up EnergySupplyConnection for this service
        self.__energy_supply_connections[service_name] = \
            self.__energy_supply.connection(service_name)

        # Set up PipeEnergy for this service to store extra
        # energy pushed into the pipe to run the battery and temperature
        self.__pipe_energy[service_name] = { 'energy': 0.0, 'temperature': 0.0 }

    def create_service_hot_water_regular(
            self,
            heat_battery_data,
            service_name,
            cold_feed,
            controlmin,
            controlmax,
            ):
            """ Return a HeatBatteryServiceWaterRegular object and create an EnergySupplyConnection for it

            Arguments:
            service_name     -- name of the service demanding energy from the heat battery
            temp_limit_upper -- upper operating limit for temperature, in deg C
            cold_feed        -- reference to ColdWaterSource object
            controlmin       -- reference to a control object which must select current
                                the minimum timestep temperature
            controlmax       -- reference to a control object which must select current
                                the maximum timestep temperature
            """

            self.__create_service_connection(service_name)
            return HeatBatteryServiceWaterRegular(
                self,
                heat_battery_data,
                service_name,
                cold_feed,
                self.__simulation_time,
                controlmin,
                controlmax,
                )

    def create_service_space_heating(
            self,
            service_name,
            control,
            ):
        """ Return a HeatBatteryServiceSpace object and create an EnergySupplyConnection for it

        Arguments:
        service_name -- name of the service demanding energy from the heat battery
        control -- reference to a control object which must implement is_on() and setpnt() funcs
        """
        self.__create_service_connection(service_name)
        return HeatBatteryServiceSpace(
            self,
            service_name,
            control,
            )

    def __electric_charge(self) -> float:
        """ Calculates power required for unit
        
        Arguments
        time    -- current time period that we are looking at

        returns -- Power required in watts
        """
        if self.__charge_control.is_on(): 
            return self.__pwr_in
        else:
            return 0.0

    def __time_available(self, time_start, timestep):
        """ Calculate time available for the current service """
        # Assumes that time spent on other services is evenly spread throughout
        # the timestep so the adjustment for start time below is a proportional
        # reduction of the overall time available, not simply a subtraction
        time_available \
            = (timestep - self.__total_time_running_current_timestep) \
            * (1.0 - time_start / timestep)
        return time_available

    def __calculate_heat_transfer_coeff(self,
                                         A, 
                                         B, 
                                         flow_rate_l_per_min,
                                         reynold_number_at_1_l_per_min):

        # Equations parameters A and B are based on test data.
        # Consider adding further documentation and evidence for this in future updates.
        return A * np.log(reynold_number_at_1_l_per_min * flow_rate_l_per_min) + B

    def __calculate_heat_transfer_kW_per_K(self,
                                           heat_transfer_coeff,
                                           surface_area_m2):

        return (heat_transfer_coeff * surface_area_m2) / units.W_per_kW

    def __calculate_outlet_temp_C(self, 
                                  heat_transfer_kW_per_K,
                                  zone_temp_C, inlet_temp_C,
                                  flow_rate_kg_per_s):
        """
        Heat transfer from heat battery zone to water flowing through it.
            UAZ(n) = UA1Z(n) ------- (a) When the heat battery is discharging e.g. hot water heating mode.
            UAZ(n) = UA2Z(n) ------- (b) When the heat battery is charging via external heat source
            
            Q3Z(n) = mWCW(twoZ(n) – twiZ(n) )= UAZ(n)(TZ(n) – (twiZ(n) + twoZ(n) )/2) ----- (1)
            
            Q3Z(n) = Heat transfer rate between PCM and the water flowing through it, (W)
            mW = water mass flow rate, (kg/s)
            CW = Specific heat of water, (J/(kg.K)
            twoZ(n) = Water outlet temperature from zone, n, (oC)
            twiZ(n) = Water inlet temperature from zone, n, (oC)
            UAZ(n) = Overall heat transfer coefficient of heat exchanger in zone, n, (W/k)
            TZ(n) = Heat battery zone temperature, (oC)
        
        Outlet temperature twoZ is calculated by resolving the equation (1) 
        """
        return ((2 * heat_transfer_kW_per_K * zone_temp_C - heat_transfer_kW_per_K * inlet_temp_C
              + 2 * flow_rate_kg_per_s * WATER.specific_heat_capacity_kWh() * units.kJ_per_kWh * inlet_temp_C)
             / (2 * flow_rate_kg_per_s * WATER.specific_heat_capacity_kWh() * units.kJ_per_kWh + heat_transfer_kW_per_K))

    def __calculate_water_kinematic_viscosity_m2_per_s(self,
                                                       inlet_temp_C,
                                                       outlet_temp_C):
        """
        Calculate the kinematic viscosity of water (m²/s) based on average circuit temperature.
    
        This method uses a quadratic approximation to estimate the kinematic viscosity
        of water as a function of the average temperature of the secondary circuit.
    
        The equation used is:
            ν = a * T_avg² + b * T_avg + c
        where:
            - ν is the kinematic viscosity in m²/s
            - T_avg is the average of the inlet and outlet temperatures in °C
            - a, b, c are experimentally determined coefficients:
                a = 0.000000000145238
                b = -0.0000000248238
                c = 0.000001432
    
        These coefficients are likely derived from experimental test data or
        thermodynamic property tables for water within a specific temperature range
        relevant to secondary circuit operation.
    
        Parameters:
            inlet_temp_C (float): The inlet temperature of the circuit in °C.
            outlet_temp_C (float): The outlet temperature of the circuit in °C.
    
        Returns:
            float: The kinematic viscosity of water in m²/s.
    
        Notes:
            - This approximation is valid for the expected operating range of secondary
              circuits (e.g., HVAC or hydronic systems) and may lose accuracy outside
              typical temperature ranges (e.g., 0–100 °C).
            - The coefficients are fixed constants based on empirical data and are not
              variables in this implementation.
        """ 
        average_temp = (inlet_temp_C + outlet_temp_C) / 2
        return 0.000000000145238 * average_temp**2 - 0.0000000248238 * average_temp + 0.000001432

    def __calculate_reynold_number_at_1_l_per_min(self,
                                                  water_kinematic_viscosity_m2_per_s, 
                                                  velocity_in_HEX_tube_at_1_l_per_min_m_per_s,
                                                  diameter_m):

        return (
               (velocity_in_HEX_tube_at_1_l_per_min_m_per_s * diameter_m)
               / water_kinematic_viscosity_m2_per_s
               )

    def __get_zone_properties(self, 
                              index, 
                              mode, 
                              zone_temp_C_dist, 
                              inlet_temp_C, 
                              inlet_temp_C_Zone, 
                              Q_max_kJ, 
                              reynold_number_at_1_l_per_min, 
                              flow_rate_kg_per_s, 
                              time_step_s):
        outlet_temp_C = 0
        if mode == OperationMode.ONLY_CHARGING:
            zone_index = len(zone_temp_C_dist) - index - 1
            energy_transf = 0
            zone_temp_C_start = zone_temp_C_dist[zone_index]
        elif mode == OperationMode.LOSSES:
            zone_index = index
            zone_temp_C_start = zone_temp_C_dist[zone_index]
            if zone_temp_C_start > inlet_temp_C:
                energy_transf = Q_max_kJ / len(zone_temp_C_dist)
            else:
                energy_transf = 0
        elif mode == OperationMode.NORMAL: # NORMAL mode include battery primarily hydraulic charging or discharing with or without simultaneous electric charging.
            zone_index = index
            zone_temp_C_start = zone_temp_C_dist[zone_index]
            heat_transfer_coeff = self.__calculate_heat_transfer_coeff(self.__A, self.__B, self.__flow_rate_l_per_min, reynold_number_at_1_l_per_min)
            heat_transfer_kW_per_K = self.__calculate_heat_transfer_kW_per_K(heat_transfer_coeff, self.__heat_exchanger_surface_area_m2) 

            # Calculate outlet temperature and heat exchange for this zone
            outlet_temp_C = self.__calculate_outlet_temp_C(heat_transfer_kW_per_K, zone_temp_C_start, inlet_temp_C_Zone, flow_rate_kg_per_s)
            energy_transf = (WATER.specific_heat_capacity_kWh() * units.kJ_per_kWh * flow_rate_kg_per_s * (outlet_temp_C - inlet_temp_C_Zone) * time_step_s)
        else:
            sys.exit("Battery operation mode error.")

        return energy_transf, zone_index, zone_temp_C_start, outlet_temp_C

    def __calculate_zone_energy_required(self, zone_temp_C_start, target_temp):
        Q_required = 0
        if zone_temp_C_start >= self.__phase_transition_temperature_upper:
            Q_required = self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition * (zone_temp_C_start - target_temp )
        elif zone_temp_C_start >= self.__phase_transition_temperature_lower:
            if target_temp > self.__phase_transition_temperature_upper:
                Q_required = self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition * (self.__phase_transition_temperature_upper - target_temp) + \
                            self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition * (zone_temp_C_start - self.__phase_transition_temperature_upper)
            else:
                Q_required = self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition * (zone_temp_C_start - target_temp)
        else:
            if target_temp > self.__phase_transition_temperature_upper:
                Q_required = self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition * (self.__phase_transition_temperature_upper - target_temp) + \
                                self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition * (self.__phase_transition_temperature_lower - self.__phase_transition_temperature_upper) + \
                                self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition * (zone_temp_C_start - self.__phase_transition_temperature_lower )
            elif target_temp > self.__phase_transition_temperature_lower:
                Q_required = self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition * (self.__phase_transition_temperature_lower - target_temp) + \
                                self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition * (zone_temp_C_start - self.__phase_transition_temperature_lower )
            else:
                Q_required = self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition * (zone_temp_C_start - target_temp )

        return Q_required

    def __process_zone_simultaneous_charging(self, zone_temp_C_start, target_temp, Q_max_kJ, energy_transf, energy_charged):
        Q_required = 0

        if zone_temp_C_start < target_temp: # zone initially below full charge
            Q_required = self.__calculate_zone_energy_required(zone_temp_C_start, target_temp)

            if energy_transf >= 0: # inlet water withdraws energy from battery
                if -Q_max_kJ >= energy_transf: # Charging is enough to recover energy withdrawn and possibly more
                    Q_max_kJ += energy_transf
                    energy_charged += ( energy_transf / units.kJ_per_kWh )
                    energy_transf = 0

                    if Q_max_kJ > Q_required: # Charging is not enough to push zone temperature to target
                        Q_required = Q_max_kJ
                        energy_charged += ( -Q_max_kJ / units.kJ_per_kWh )
                        Q_max_kJ = 0.0
                    else: # Charging is enough to push zone temperature to target temperature
                        Q_max_kJ -= Q_required
                        energy_charged += ( -Q_required / units.kJ_per_kWh)
                    # Update zone temperature with energy from charging
                    energy_transf += Q_required
                else: # Charging can only recover partially the energy withdrawn
                    energy_transf += Q_max_kJ
                    energy_charged += ( -Q_max_kJ / units.kJ_per_kWh )
                    Q_max_kJ = 0
            else: # inlet water adds energy to battery
                if Q_max_kJ + energy_transf > Q_required: # inlet water + charging is not enough to push zone temperature to target
                    Q_required = Q_max_kJ + energy_transf
                    energy_charged += ( -Q_max_kJ / units.kJ_per_kWh )
                    Q_max_kJ = 0.0

                    energy_transf = Q_required
                else: # inlet temperature + charging can take zone temperature to target temp
                    if energy_transf < Q_required: # inlet temperature would take zone temperature over target temperature!
                        if self.__flag_1_warning[0]:
                            print(f"\nWarning: Inlet temperature pushing over battery max temp! {energy_transf}")
                            self.__flag_1_warning[0] = False
                    else:
                        if Q_max_kJ > Q_required - energy_transf: # Charging cannot take zone temperature to target after zone warmed by inlet water...
                            Q_required = Q_max_kJ + energy_transf
                            energy_charged += ( -Q_max_kJ / units.kJ_per_kWh )
                            Q_max_kJ = 0.0

                            energy_transf += Q_required
                        else: # There is plenty of charging after taking zone temperature to target
                            Q_max_kJ -= (Q_required - energy_transf)
                            energy_charged += ( -(Q_required - energy_transf) / units.kJ_per_kWh )

                            energy_transf = Q_required
        else: # zone initially fully charged
            if energy_transf >= 0: # inlet water withdraws energy from battery 
                if -Q_max_kJ > energy_transf: # Charging is enough to recover energy withdrawn
                    Q_max_kJ += energy_transf
                    energy_charged += ( energy_transf / units.kJ_per_kWh )
                    energy_transf = 0
                else: # Charging can only recover partially the energy withdrawn
                    energy_transf += Q_max_kJ
                    energy_charged += ( -Q_max_kJ / units.kJ_per_kWh )
                    Q_max_kJ = 0
            else:
                if self.__flag_1_warning[1]:
                    print(f"\nWarning: Inlet temperature pushing over battery max temp! {energy_transf}")
                    self.__flag_1_warning[1] = False

        return Q_max_kJ, energy_charged, energy_transf

    def __calculate_new_zone_temperature(self, zone_temp_C_start, energy_transf):
        """
        ranges _1, _2, and _3 refer to:
        _1: temperature of PCM above transition phase
        _2: temperature of PCM within transition phase
        _3: temperature of PCM below transition phase
        
        """
        delta_temp_1 = 0
        delta_temp_2 = 0
        delta_temp_3 = 0
        if energy_transf > 0: # zone delivering energy to water
            if zone_temp_C_start >= self.__phase_transition_temperature_upper:
                heat_range_1 = ((zone_temp_C_start - self.__phase_transition_temperature_upper)
                                 * self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition)
                heat_range_2 = ((self.__phase_transition_temperature_upper - self.__phase_transition_temperature_lower)
                                 * self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition)

                if energy_transf <= heat_range_1:
                    delta_temp_1 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition
                else:
                    delta_temp_1 = zone_temp_C_start - self.__phase_transition_temperature_upper 

                    energy_transf -= heat_range_1
                    if energy_transf <= heat_range_2:
                        delta_temp_2 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition
                    else:
                        delta_temp_2 = self.__phase_transition_temperature_upper - self.__phase_transition_temperature_lower
                        energy_transf -= heat_range_2
                        delta_temp_3 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition

            elif self.__phase_transition_temperature_lower <= zone_temp_C_start < self.__phase_transition_temperature_upper:
                heat_range_2 = ((zone_temp_C_start - self.__phase_transition_temperature_lower)
                                 * self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition)

                if energy_transf <= heat_range_2:
                    delta_temp_2 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition
                else:
                    delta_temp_2 = zone_temp_C_start - self.__phase_transition_temperature_lower
                    energy_transf -= heat_range_2
                    delta_temp_3 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition

            else:
                delta_temp_3 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition

        elif energy_transf < 0: # zone retriving energy from water
            if zone_temp_C_start <= self.__phase_transition_temperature_lower:
                heat_range_3 = ((zone_temp_C_start - self.__phase_transition_temperature_lower)
                             * self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition)
                heat_range_2 = ((self.__phase_transition_temperature_lower - self.__phase_transition_temperature_upper)
                              * self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition)

                if energy_transf >= heat_range_3:
                    delta_temp_3 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_below_Phase_transition
                else:
                    delta_temp_3 = zone_temp_C_start - self.__phase_transition_temperature_lower

                    energy_transf -= heat_range_3
                    if energy_transf >= heat_range_2:
                        delta_temp_2 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition
                    else:
                        delta_temp_2 = self.__phase_transition_temperature_lower - self.__phase_transition_temperature_upper

                        energy_transf -= heat_range_2
                        delta_temp_1 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition

            elif  self.__phase_transition_temperature_lower < zone_temp_C_start <= self.__phase_transition_temperature_upper:
                heat_range_2 = ((zone_temp_C_start - self.__phase_transition_temperature_upper)
                              * self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition)

                if energy_transf >= heat_range_2:
                    delta_temp_2 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_during_Phase_transition
                else:
                    delta_temp_2 = zone_temp_C_start - self.__phase_transition_temperature_upper
                    energy_transf -= heat_range_2
                    delta_temp_1 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition

            else:
                delta_temp_1 = energy_transf / self.__heat_storage_zone_material_kJ_per_K_above_Phase_transition

        return zone_temp_C_start - (delta_temp_1 + delta_temp_2 + delta_temp_3)


    def __process_heat_battery_zones(self, 
                                   inlet_temp_C, 
                                   zone_temp_C_dist, 
                                   flow_rate_kg_per_s, 
                                   time_step_s, 
                                   reynold_number_at_1_l_per_min,
                                   pwr_in=0,
                                   mode = OperationMode.NORMAL):

        target_temp = self.__max_temp_of_charge * self.__charge_control.target_charge()
        energy_transf_delivered = self.__n_zones * [0]
        energy_charged = 0

        Q_max_kJ = -pwr_in * time_step_s / units.seconds_per_hour * units.kJ_per_kWh

        inlet_temp_C_Zone = inlet_temp_C
        for j in range(len(zone_temp_C_dist)):
            # Get zone index, starting temperature, outlet temperature and energy_transfer based on operation mode
            energy_transf, zone_index, zone_temp_C_start, outlet_temp_C = self.__get_zone_properties(j,
                                                                                      mode, 
                                                                                      zone_temp_C_dist, 
                                                                                      inlet_temp_C,
                                                                                      inlet_temp_C_Zone, 
                                                                                      Q_max_kJ, 
                                                                                      reynold_number_at_1_l_per_min, 
                                                                                      flow_rate_kg_per_s, 
                                                                                      time_step_s)

            energy_transf_delivered[zone_index] += energy_transf

            # Process energy transfer in zone with simultaneous charging.
            if Q_max_kJ < 0:
                Q_max_kJ, energy_charged, energy_transf = self.__process_zone_simultaneous_charging(zone_temp_C_start, 
                                                                                                    target_temp, 
                                                                                                    Q_max_kJ, 
                                                                                                    energy_transf,
                                                                                                    energy_charged)

            # Recalculate zone temperatures after energy transfer
            zone_temp_C_dist[zone_index] = self.__calculate_new_zone_temperature(zone_temp_C_start,
                                                                                 energy_transf,
                                                                                 )

            # Update values for the next iteration
            inlet_temp_C_Zone = outlet_temp_C

        return outlet_temp_C, zone_temp_C_dist, energy_transf_delivered, energy_charged

    def __charge_battery_hydraulic(self,
                      inlet_temp_C,
                      ):
    # Charge the battery (update the zones temperature).
    # It follows the same methodology as energy_demand function.

        total_time_s = self.__simulation_time.timestep() * units.seconds_per_hour
        time_step_s = self.__hb_time_step
        # Initial Reynold number
        water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(self.__initial_inlet_temp, self.__estimated_outlet_temp)
        reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

        flow_rate_kg_per_s = (self.__flow_rate_l_per_min / units.seconds_per_minute) * WATER.density()
        n_time_steps = int(total_time_s / time_step_s)

        zone_temp_C_dist = self.__zone_temp_C_dist_initial.copy()

        energy_transf_charged = self.__n_zones*[0]

        #iterating through time steps.
        total_charge = 0
        for j in range(n_time_steps):
            # Processing HB zones
            outlet_temp_C, zone_temp_C_dist, energy_transf_charged, __ = self.__process_heat_battery_zones(
                inlet_temp_C=inlet_temp_C,
                zone_temp_C_dist=zone_temp_C_dist,
                flow_rate_kg_per_s=flow_rate_kg_per_s,
                time_step_s=time_step_s,
                reynold_number_at_1_l_per_min=reynold_number_at_1_l_per_min,
                pwr_in=0)

            # RN for next time step.
            water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(inlet_temp_C, outlet_temp_C)
            reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

            energy_charged_during_battery_time_step = sum(energy_transf_charged)
            if outlet_temp_C < inlet_temp_C:
                total_charge += energy_charged_during_battery_time_step
            else:
                break

        self.__zone_temp_C_dist_initial = zone_temp_C_dist

        return total_charge

    def __charge_battery(self):
    # Charge the battery (update the zones temperature).
    # It follows the same methodology as energy_demand function.
        timestep: float = self.__simulation_time.timestep()
        time_available = self.__time_available(0.0, timestep)

        pwr_in = self.__electric_charge()
    
        time_step_s = time_available * units.seconds_per_hour

        zone_temp_C_dist = self.__zone_temp_C_dist_initial.copy()

        # Processing HB zones
        __, zone_temp_C_dist, __ , energy_charged_during_battery_time_step = self.__process_heat_battery_zones(
            inlet_temp_C=0,
            zone_temp_C_dist=zone_temp_C_dist,
            flow_rate_kg_per_s=0,
            time_step_s=time_step_s,
            reynold_number_at_1_l_per_min=0,
            pwr_in=pwr_in,
            mode=OperationMode.ONLY_CHARGING)

        self.__energy_charged += energy_charged_during_battery_time_step
        energy_charged = energy_charged_during_battery_time_step

        self.__zone_temp_C_dist_initial = zone_temp_C_dist

        return energy_charged, zone_temp_C_dist

    def __battery_heat_loss(self):
        # Battery losses
        timestep: float = self.__simulation_time.timestep()
        time_step_s = timestep * units.seconds_per_hour #time_available * units.seconds_per_hour

        zone_temp_C_dist = self.__zone_temp_C_dist_initial.copy()

        # Processing HB zones
        __, zone_temp_C_dist, energy_loss , __ = self.__process_heat_battery_zones(
            inlet_temp_C=22, # Replace with room temperature
            zone_temp_C_dist=zone_temp_C_dist,
            flow_rate_kg_per_s=0,
            time_step_s=time_step_s,
            reynold_number_at_1_l_per_min=0,
            pwr_in=-self.__max_rated_losses,
            mode=OperationMode.LOSSES)

        self.__zone_temp_C_dist_initial = zone_temp_C_dist

        return sum(energy_loss) / units.kJ_per_kWh, zone_temp_C_dist

    def __get_temp_hot_water(self, inlet_temp: float, volume: float) -> float:

        total_time_s = volume / self.__flow_rate_l_per_min * units.seconds_per_minute

        time_step_s = min(self.__hb_time_step * 5, 100)

        pwr_in = self.__electric_charge()

        # Initial Reynold number
        water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(self.__initial_inlet_temp, self.__estimated_outlet_temp)
        reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

        flow_rate_kg_per_s = (self.__flow_rate_l_per_min / units.seconds_per_minute) * WATER.density()

        zone_temp_C_dist = self.__zone_temp_C_dist_initial.copy()
        inlet_temp_C = inlet_temp

        if total_time_s > time_step_s:
            n_time_steps = int(total_time_s / time_step_s)
        else:
            n_time_steps = 1

        #iterating through time steps.
        for j in range(n_time_steps):
            # Processing HB zones
            outlet_temp_C, zone_temp_C_dist, __, __ = self.__process_heat_battery_zones(
                inlet_temp_C=inlet_temp_C,
                zone_temp_C_dist=zone_temp_C_dist,
                flow_rate_kg_per_s=flow_rate_kg_per_s,
                time_step_s=time_step_s,
                reynold_number_at_1_l_per_min=reynold_number_at_1_l_per_min,
                pwr_in=pwr_in)

            # RN for next time step.
            water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(inlet_temp_C, outlet_temp_C)
            reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

            inlet_temp_C = outlet_temp_C

        return outlet_temp_C

    def __energy_output_max(self,
                            temp_output,
                            time_start=0.0):

        # Return the energy the battery can provide assuming the HB temperature inlet
        # is constant during HEM time step equal to the required emitter temperature (temp_output)
        # Maximun energy for a given HB zones temperature distribution and inlet temperature.
        # The calculation methodology is the same as described in the demand_energy function.
        
        total_time_s = self.__simulation_time.timestep() * units.seconds_per_hour
        # time_step_s for HB calculation is a sensitive inputs for the process as, the longer it is, the 
        # lower the accuracy due to maintaining Reynolds number working in intervals where the properties
        # of the fluid have changed sufficiently to degrade the accuracy of the calculation.
        # This is critical for the demand_energy function but less so for the energy_output_max as this
        # only provides an estimation of the heat capacity of the battery and can be slightly overestitmated
        # with a longer time step that reduces the calculation time, which is a critical factor for HEM.
        # However, from current testing, time_step_s longer than 100 might cause instabilities in the calculation
        # leading to failure to complete. Thus, we are capping the max timestep to 100 seconds.
        time_step_s = min(self.__hb_time_step * 5, 100)

        pwr_in = self.__electric_charge()

        # Initial Reynold number
        water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(self.__initial_inlet_temp, self.__estimated_outlet_temp)
        reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

        flow_rate_kg_per_s = (self.__flow_rate_l_per_min / units.seconds_per_minute) * WATER.density()

        zone_temp_C_dist = self.__zone_temp_C_dist_initial.copy()
        energy_delivered_HB = 0
        inlet_temp_C = temp_output
        n_time_steps = int(total_time_s / time_step_s)

        #iterating through time steps.
        for j in range(n_time_steps):
            # Processing HB zones
            outlet_temp_C, zone_temp_C_dist, energy_transf_delivered, __ = self.__process_heat_battery_zones(
                inlet_temp_C=inlet_temp_C,
                zone_temp_C_dist=zone_temp_C_dist,
                flow_rate_kg_per_s=flow_rate_kg_per_s,
                time_step_s=time_step_s,
                reynold_number_at_1_l_per_min=reynold_number_at_1_l_per_min,
                pwr_in=pwr_in)

            # RN for next time step.
            water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(inlet_temp_C, outlet_temp_C)
            reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

            energy_delivered_ts = sum(energy_transf_delivered)
            if outlet_temp_C > temp_output:
                # In this new method, adjust total energy to make more real with the 6 ts we have configured
                energy_delivered_HB += energy_delivered_ts
            else:
                break

            inlet_temp_C = temp_output

        if energy_delivered_HB < 0:
            energy_delivered_HB = 0

        return energy_delivered_HB * self.__n_units

    def __first_call(self):
        timestep: float = self.__simulation_time.timestep()
        current_hour: int = self.__simulation_time.current_hour()
        time_range = (current_hour)*self.__time_unit

        self.__flag_first_call = False

    def __demand_energy(self,
                        service_name,
                        service_type,
                        energy_output_required,
                        temp_return_feed,
                        temp_output,
                        service_on,
                        time_start=0.0,
                        update_heat_source_state=True
                  ):
        # Return the energy provided by the HB during a HEM time step (assuming
        # an inlet temperature constant) and update the HB state (zones distribution temperatures) 
        # The HEM time step is divided into sub-timesteps. For each sub-timestep the zones temperature are
        # calculated (loop through zones). 

        timestep: float = self.__simulation_time.timestep()
        time_available = self.__time_available(time_start, timestep)
        # __demand_energy is called for each service in each timestep
        # Some calculations are only required once per timestep
        # Perform these calculations here
        if self.__flag_first_call:
            self.__first_call()

        pwr_in = 0.0
        if self.__simultaneous_charging_and_discharging:
            pwr_in = self.__electric_charge()

        if temp_output is None or temp_output <= self.__pipe_energy[service_name]['temperature']:
            if energy_output_required > self.__pipe_energy[service_name]['energy']:
                energy_output_required -= self.__pipe_energy[service_name]['energy']
                self.__pipe_energy[service_name]['energy'] = 0.0
                self.__pipe_energy[service_name]['temperature'] = 0.0
            else:
                self.__pipe_energy[service_name]['energy'] -= energy_output_required
                energy_output_required = 0

        # Distributing energy demand through all units
        energy_demand: float = energy_output_required / self.__n_units

        # Initial Reynold number
        water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(self.__initial_inlet_temp, self.__estimated_outlet_temp)
        reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

        flow_rate_kg_per_s = (self.__flow_rate_l_per_min / units.seconds_per_minute) * WATER.density()

        energy_delivered_HB = 0
        total_energy_low_temp = 0
        inlet_temp_C = temp_return_feed
        zone_temp_C_dist = self.__zone_temp_C_dist_initial.copy()

        if energy_output_required <= 0:
            if update_heat_source_state:
                self.__service_results.append({
                    'service_name': service_name,
                    'service_type': service_type,
                    'service_on': service_on,
                    'energy_output_required': energy_output_required,
                    'temp_output': temp_output,
                    'temp_inlet': temp_return_feed,
                    'time_running': 0,
                    'energy_left_in_pipe': self.__pipe_energy[service_name]['energy'],
                    'temperature_left_in_pipe': self.__pipe_energy[service_name]['temperature'],
                    'energy_delivered_HB': 0.0,
                    'energy_delivered_backup': 0.0,
                    'energy_delivered_total': 0.0,
                    'energy_delivered_low_temp': 0.0,
                    'energy_charged_during_service': 0.0,
                    'hb_zone_temperatures': zone_temp_C_dist,
                    'current_hb_power': "",
                    })
            return energy_delivered_HB

        time_step_s = 1
        time_running_current_service = 0

        flag_minimum_run = False # False: supply energy to emitter; True: running water to complete loop 
        energy_charged = 0

        while time_step_s > 0:
            # Processing HB zones
            outlet_temp_C, zone_temp_C_dist, energy_transf_delivered, energy_charged_during_battery_time_step = self.__process_heat_battery_zones(
                inlet_temp_C=inlet_temp_C,
                zone_temp_C_dist=zone_temp_C_dist,
                flow_rate_kg_per_s=flow_rate_kg_per_s,
                time_step_s=time_step_s,
                reynold_number_at_1_l_per_min=reynold_number_at_1_l_per_min,
                pwr_in=pwr_in)

            if update_heat_source_state:
                self.__energy_charged += energy_charged_during_battery_time_step
            energy_charged += energy_charged_during_battery_time_step

            time_running_current_service += time_step_s
            # RN for next time step.
            water_kinematic_viscosity_m2_per_s = self.__calculate_water_kinematic_viscosity_m2_per_s(temp_return_feed, outlet_temp_C)
            reynold_number_at_1_l_per_min = self.__calculate_reynold_number_at_1_l_per_min(water_kinematic_viscosity_m2_per_s, self.__velocity_in_HEX_tube_at_1_l_per_min_m_per_s, self.__capillary_diameter_m)

            energy_delivered_ts = sum(energy_transf_delivered) / units.kJ_per_kWh
            if temp_output is None or outlet_temp_C > temp_output:
                if not flag_minimum_run:
                    energy_delivered_HB += energy_delivered_ts #demand_per_time_step_kwh
                    #balance = total_energy - energy_charged
                    max_instant_power = energy_delivered_ts / time_step_s
                    if max_instant_power > 0:
                        time_step_s = (energy_demand - energy_delivered_HB) / max_instant_power
                else:
                    if energy_delivered_ts != 0:
                        current_energy = self.__pipe_energy[service_name]['energy']
                        current_temperature = self.__pipe_energy[service_name]['temperature']
                        new_temperature = ((current_temperature * current_energy) + (outlet_temp_C * energy_delivered_ts)) / (current_energy + energy_delivered_ts)
                        
                        self.__pipe_energy[service_name]['energy'] += energy_delivered_ts
                        self.__pipe_energy[service_name]['temperature'] = new_temperature

                if time_step_s > self.__hb_time_step:
                    time_step_s = self.__hb_time_step

                if (energy_demand - energy_delivered_HB) < 0.0001:
                    #Energy supplied, run to complete water loop
                    if time_running_current_service > self.__minimum_time_required_to_run:
                        break

                    if not flag_minimum_run:
                        time_extra = self.__minimum_time_required_to_run - time_running_current_service
                        flag_minimum_run = True
                    else:
                        time_extra -= time_step_s

                    if time_extra > self.__hb_time_step:
                        time_step_s = self.__hb_time_step
                    else:
                        time_step_s = time_extra

                if time_running_current_service + time_step_s >  time_available * units.seconds_per_hour:
                    time_step_s = time_available * units.seconds_per_hour - time_running_current_service

            else: # outlet_temp_C is below required temperature
                total_energy_low_temp += energy_delivered_ts
                if energy_delivered_HB > 0:
                    if time_running_current_service > self.__minimum_time_required_to_run:
                        break

                    if not flag_minimum_run:
                        time_extra = self.__minimum_time_required_to_run - time_running_current_service
                        flag_minimum_run = True
                    else:
                        time_extra -= time_step_s

                    if time_extra > self.__hb_time_step:
                        time_step_s = self.__hb_time_step
                    else:
                        time_step_s = time_extra
                else:
                    break

        if update_heat_source_state:
            self.__zone_temp_C_dist_initial = zone_temp_C_dist

            self.__total_time_running_current_timestep += time_running_current_service / units.seconds_per_hour

            if time_running_current_service >0:
                current_hb_power = energy_delivered_HB * units.seconds_per_hour / time_running_current_service
            else:
                current_hb_power = ""
            # TODO: Clarify whether Heat Batteries can have direct electric backup if depleted
            self.__service_results.append({
                'service_name': service_name,
                'service_type': service_type,
                'service_on': service_on,
                'energy_output_required': energy_output_required,
                'temp_output': temp_output,
                'temp_inlet': temp_return_feed,
                'time_running': time_running_current_service,
                'energy_left_in_pipe': self.__pipe_energy[service_name]['energy'],
                'temperature_left_in_pipe': self.__pipe_energy[service_name]['temperature'],
                'energy_delivered_HB': energy_delivered_HB * self.__n_units,
                'energy_delivered_backup': 0.0,
                'energy_delivered_total': energy_delivered_HB * self.__n_units + 0.0,
                'energy_delivered_low_temp': total_energy_low_temp * self.__n_units,
                'energy_charged_during_service': energy_charged * self.__n_units,
                'hb_zone_temperatures': zone_temp_C_dist,
                'current_hb_power': current_hb_power,
                })

        return energy_delivered_HB * self.__n_units

    def __calc_auxiliary_energy(self, timestep, time_remaining_current_timestep):
        """Calculation of heat battery auxilary energy consumption"""

        #Energy used by circulation pump
        energy_aux = self.__total_time_running_current_timestep \
            * self.__power_circ_pump

        #Energy used in standby mode
        energy_aux += self.__power_standby * time_remaining_current_timestep

        self.__energy_supply_conn.demand_energy(energy_aux)
        
        return energy_aux

    def timestep_end(self):
        """" Calculations to be done at the end of each timestep"""
        timestep: float = self.__simulation_time.timestep()
        time_remaining_current_timestep = timestep - self.__total_time_running_current_timestep

        if self.__flag_first_call:
            self.__first_call()
        self.__flag_first_call = True

        # Calculatin auxiliary energy to provide services during timestep
        energy_aux = self.__calc_auxiliary_energy(timestep, time_remaining_current_timestep)

        # Calculating heat battery losses in timestep to correct charge level
        # Currently assumed all losses are to the exterior independently of the 
        # heat battery location
        # TODO: Assign thermal losses to relevant zone if heat battery is not outdoors.
        battery_losses, zone_temp_C_after_losses = self.__battery_heat_loss()

        # Charging battery for the remaining of the timestep. 
        end_of_ts_charge = 0.0
        zone_temp_C_after_charging = self.__zone_temp_C_dist_initial
        if self.__charge_control.is_on(): 
            end_of_ts_charge, zone_temp_C_after_charging = self.__charge_battery()

        # TODO: Area for improvement when we confirm if the battery can be charged by hidraulic
        # methods in addition to electrically.
        #if self.__charge_control.is_on(): 
        #    self.__energy_charged = self.__charge_battery_hydraulic(self.__max_temp_of_charge)

        self.__energy_supply_conn.demand_energy(self.__energy_charged * self.__n_units)

        # If detailed results are to be output, save the results from the current timestep

        if self.__detailed_results is not None:
            self.__service_results.append({
                'energy_aux': energy_aux * self.__n_units,
                'battery_losses': battery_losses * self.__n_units,
                'Temps_after_losses': zone_temp_C_after_losses,
                'total_charge': self.__energy_charged * self.__n_units,
                'end_of_timestep_charge': end_of_ts_charge * self.__n_units,
                'hb_after_only_charge_zone_temp': zone_temp_C_after_charging,
                })
            self.__detailed_results.append(self.__service_results)

        # Variables below need to be reset at the end of each timestep.
        self.__total_time_running_current_timestep = 0.0
        self.__service_results = []
        self.__energy_charged = 0.0

    def output_detailed_results(self, hot_water_energy_output):
        """ Output detailed results of heat battery calculation """

        # Define parameters to output
        # Second element of each tuple controls whether item is summed for annual total

        output_parameters = [
            ('service_name', None, False),
            ('service_type', None, False),
            ('service_on', None, False),
            ('energy_output_required', 'kWh', True),
            ('temp_output', 'degC', False),
            ('temp_inlet', 'degC', False),
            ('time_running', 'secs', True),
            ('energy_left_in_pipe', 'kWh', True),
            ('temperature_left_in_pipe', 'degC', False),
            ('energy_delivered_HB', 'kWh', True),
            ('energy_delivered_backup', 'kWh', True),
            ('energy_delivered_total', 'kWh', True),
            ('energy_delivered_low_temp', 'kWh', True),
            ('energy_charged_during_service', 'kWh', True),
            ('hb_zone_temperatures','degC', False),
            ('current_hb_power','kW', False)
            ]
        aux_parameters = [
            ('energy_aux', 'kWh', True),
            ('battery_losses', 'kWh', True),
            ('Temps_after_losses','degC', False),
            ('total_charge', 'kWh', True),
            ('end_of_timestep_charge', 'kWh', True),
            ('hb_after_only_charge_zone_temp','degC', False),
            ]

        results_per_timestep = {'auxiliary': {}}
        # Report auxiliary parameters (not specific to a service)
        for parameter, param_unit, _ in aux_parameters:
            # Check if the parameter is a list to handle individual elements
            if parameter in ['Temps_after_losses', 'hb_after_only_charge_zone_temp']:
                # Create labels for each element in the list
                labels = None
                for t_idx, service_results in enumerate(self.__detailed_results):
                    # Determine the number of elements in the list for this parameter
                    if labels is None:
                        labels = [f"{parameter}{i}" for i in range(len(service_results[-1][parameter]))]
                        for label in labels:
                            results_per_timestep['auxiliary'][(label, param_unit)] = []
                    # Append each element of the list to the respective label
                    for label, result in zip(labels, service_results[-1][parameter]):
                        results_per_timestep['auxiliary'][(label, param_unit)].append(result)
            else:
                # Default behaviour for scalar parameters
                results_per_timestep['auxiliary'][(parameter, param_unit)] = []
                for t_idx, service_results in enumerate(self.__detailed_results):
                    result = service_results[-1][parameter]
                    results_per_timestep['auxiliary'][(parameter, param_unit)].append(result)

        # For each service, report required output parameters
        for service_idx, service_name in enumerate(self.__energy_supply_connections.keys()):
            results_per_timestep[service_name] = {}
            # Look up each required parameter
            for parameter, param_unit, _ in output_parameters:
                if parameter == "hb_zone_temperatures":
                    labels = [f"{parameter}{i}" for i in range(len(service_results[service_idx][parameter]))]
                    for label, result in zip(labels, service_results[service_idx][parameter]):
                        results_per_timestep[service_name][(label, param_unit)] = []
                else:
                    results_per_timestep[service_name][(parameter, param_unit)] = []
                # Look up value of required parameter in each timestep
                for t_idx, service_results in enumerate(self.__detailed_results):
                    if parameter == "hb_zone_temperatures":
                        labels = [f"{parameter}{i}" for i in range(len(service_results[service_idx][parameter]))]
                        for label, result in zip(labels, service_results[service_idx][parameter]):
                            results_per_timestep[service_name][(label, param_unit)].append(result)

                    else:
                        result = service_results[service_idx][parameter]
                        results_per_timestep[service_name][(parameter, param_unit)].append(result)
            # For water heating service, record hot water energy delivered from tank
            if self.__detailed_results[0][service_idx]['service_type'] == ServiceType.WATER_REGULAR :
                # For DHW, need to include storage and primary circuit losses.
                # Can do this by replacing H4 numerator with total energy
                # draw-off from hot water cylinder.
                # TODO Note that the below assumes that there is only one water
                #      heating service and therefore that all hot water energy
                #      output is assigned to that service. If the model changes in
                #      future to allow more than one hot water system, this code may
                #      need to be revised to handle that scenario.
                results_per_timestep[service_name][('energy_delivered_H4', 'kWh')] \
                    = hot_water_energy_output
            else:
                # TODO Note that the below assumes there is no buffer tank for
                #      space heating, which is not currently included in the
                #      model. If this is included in future, this code will need
                #      to be revised.
                results_per_timestep[service_name][('energy_delivered_H4', 'kWh')] \
                    = results_per_timestep[service_name][('energy_delivered_total', 'kWh')]

        results_annual = {
            'Overall': {
                (parameter, param_units): 0.0
                for parameter, param_units, incl_in_annual in output_parameters
                if incl_in_annual
                },
            'auxiliary': {},
            }
        results_annual['Overall'][('energy_delivered_H4', 'kWh')] = 0.0
        # Report auxiliary parameters (not specific to a service)
        for parameter, param_unit, incl_in_annual in aux_parameters:
            if incl_in_annual:
                results_annual['auxiliary'][(parameter, param_unit)] \
                    = sum(results_per_timestep['auxiliary'][(parameter, param_unit)])
        # For each service, report required output parameters
        for service_idx, service_name in enumerate(self.__energy_supply_connections.keys()):
            results_annual[service_name] = {}
            for parameter, param_unit, incl_in_annual in output_parameters:
                if incl_in_annual:
                    parameter_annual_total \
                        = sum(results_per_timestep[service_name][(parameter, param_unit)])
                    results_annual[service_name][(parameter, param_unit)] = parameter_annual_total
                    results_annual['Overall'][(parameter, param_unit)] += parameter_annual_total
            results_annual[service_name][('energy_delivered_H4', 'kWh')] \
                = sum(results_per_timestep[service_name][('energy_delivered_H4', 'kWh')])
            results_annual['Overall'][('energy_delivered_H4', 'kWh')] \
                += results_annual[service_name][('energy_delivered_H4', 'kWh')]

        return results_per_timestep, results_annual
