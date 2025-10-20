#!/usr/bin/env python3

"""
This module contains objects that represent electric battery systems.
"""

import sys

class ElectricBattery:
    """ An object to represent an electric battery system """

    def __init__(self, capacity, charge_discharge_efficiency, battery_age,
                 minimum_charge_rate, maximum_charge_rate, maximum_discharge_rate, battery_location,
                 grid_charging_possible, simulation_time, external_conditions):
        """ Construct an ElectricBattery object

        Arguments:
        capacity                    -- the maximum capacity of the battery (kWh)
        charge_discharge_efficiency -- charge/discharge round trip efficiency of battery
                                       system (between 0 & 1)
        battery_age                 -- the starting age of the battery in (years)
        minimum_charge_rate         -- the minimum charge rate one way trip the battery allows (kW)
        maximum_charge_rate         -- the maximum charge rate one way trip the battery allows (kW)
        maximum_discharge_rate      -- the maximum discharge rate one way trip the battery allows (kW)
        battery_location            -- Location of battery (outside or inside)
        grid_charging_possible      -- Is charging from the grid possible?
        simulation_time             -- reference to SimulationTime object
        external_conditions         -- reference to ExternalConditions object

        Other variables:
        current_energy_stored -- the current energy stored in the battery at the
                                 end of hour (kWh)
        """
        self.__capacity = capacity
        self.__charge_discharge_efficiency = charge_discharge_efficiency
        self.__battery_age = battery_age
        self.__minimum_charge_rate = minimum_charge_rate
        self.__maximum_charge_rate = maximum_charge_rate
        self.__maximum_discharge_rate = maximum_discharge_rate
        self.__battery_location = battery_location
        self.__grid_charging_possible = grid_charging_possible
        self.__simulation_time = simulation_time
        self.__external_conditions = external_conditions
        self.__current_energy_stored = 0
        self.__total_time_charging_current_timestep = 0.0

        # Calculate state of health of battery. 
        self.__state_of_health = max(self.__state_of_health_equ(self.__battery_age), 0)    
        
        # Calculate max capacity based on battery original capacity * state of health
        self.__max_capacity = self.__capacity * self.__state_of_health
        
        self.__one_way_battery_efficiency = self.__charge_discharge_efficiency ** 0.5
        self.__reverse_one_way_battery_efficiency = 1/ self.__one_way_battery_efficiency
    
    # Equation for charge rate as function of state of charge (used for calculating the maximum charge rate)
    # We included this as a function in anticipation to the dependency between the charge/discharge rate with the
    # state of charge. Having considered the evidence available, we don't think we have solid enough basis to 
    # propose an equation to model this dependency yet.
    # TODO Revisit available research to improve charge/discharge rate dependency with state of charge
    #      Consider paper "Joint State of Charge (SOC) and State of Health (SOH) Estimation for Lithium-Ion Batteries
    #      Packs of Electric Vehicles. Principal Author: Panpan Hu  
    def __charge_rate_soc_equ(self, x): 
        return 1

    # Equation for discharge rate as function of state of charge (used for calculating the maximum discharge rate)
    # We included this as a function in anticipation to the dependency between the charge/discharge rate with the
    # state of charge. Having considered the evidence available, we don't think we have solid enough basis to 
    # propose an equation to model this dependency yet.
    # TODO Revisit available research to improve charge/discharge rate dependency with state of charge
    #      Consider paper "Joint State of Charge (SOC) and State of Health (SOH) Estimation for Lithium-Ion Batteries
    #      Packs of Electric Vehicles. Principal Author: Panpan Hu  
    def __discharge_rate_soc_equ(self, x): 
        return 1

    # Equation for battery capacity as function of external air temperature (only used if battery is outside)
    # Based on manufacturer data (graph): https://www.bonnenbatteries.com/the-effect-of-low-temperature-on-lithium-batteries/
    # TODO Revisit available research to improve capacity temperature dependency 
    def __capacity_temp_equ(self, x): 
        if x > 20:
            y = 1
        else:
            y = 0.8496 + 0.01208 * x - 0.000228 * x ** 2
        return y
    
    # Equation for battery state of health as function of battery age
    # Based on manufacturer guarantee of 60% remaining capacity after 10 years - i.e. 4% drop per year. 
    # Guaranteed performance is probably quite conservative. Seek to refine this in future. 
    # TODO Seek less conservative source
    def __state_of_health_equ(self, x):
        return -0.04 * x + 1
    
    def get_charge_efficiency(self):
        air_temp_capacity_factor = self.__limit_capacity_due_to_temp()
        return self.__one_way_battery_efficiency * self.__state_of_health * air_temp_capacity_factor
    
    def get_discharge_efficiency(self):
        air_temp_capacity_factor = self.__limit_capacity_due_to_temp()
        return self.__reverse_one_way_battery_efficiency * self.__state_of_health * air_temp_capacity_factor

    def is_grid_charging_possible(self):
        return(self.__grid_charging_possible)
    
    def get_state_of_charge(self):
        return self.__current_energy_stored / self.__max_capacity
    
    def get_max_capacity(self):
        return self.__max_capacity

    def charge_discharge_battery(self, elec_demand, charging_from_grid=False):
        """
        Arguments:
        elec_demand -- the supply (-ve) or demand (+ve) to/on the electric battery (kWh)
        charging_from_grid        -- Charging from charging_from_grid, not PV.

        Other variables:
        energy_available_to_charge_battery -- the total energy that could charge/discharge the battery
                                              including losses from charging efficiency (kWh)
        current_energy_stored_unconstrained -- current energy stored in battery + the total energy that
                                               would charge/discharge the battery without minimum/maximum
                                               constraints of the battery (kWh)
        energy_accepted_by_battery -- the total energy the battery is able to supply or charge (kWh)
        """
        timestep = self.__simulation_time.timestep()

        if timestep <= self.__total_time_charging_current_timestep and elec_demand < 0:
            # No more scope for charging
            return 0.0
        
        max_charge_rate = None
        
        # Calculate State of Charge (SoC)
        state_of_charge = self.get_state_of_charge()

        # Calculate the impact on the battery capacity of air temperature
        air_temp_capacity_factor = self.__limit_capacity_due_to_temp()
        
        # Ensure state_of_charge is between 0 and 1
        state_of_charge = min(state_of_charge, 1)
        state_of_charge = max(state_of_charge, 0)
        
        # Convert elec_demand (in kWh) to a power (in kW) by dividing energy by timestep (in hours)
        elec_demand_power = elec_demand / self.__simulation_time.timestep()
        if elec_demand < 0:  # Charging battery
            # Convert elec_demand (in kWh) to a power (in kW) by dividing energy by ime available for charging (in hours)
            elec_demand_power = elec_demand / ( timestep - self.__total_time_charging_current_timestep )
            # If supply is less than minimum charge rate, do not add charge to the battery
            if not charging_from_grid and -elec_demand_power < self.__minimum_charge_rate:
                energy_available_to_charge_battery = 0
            else:
                max_charge, max_charge_rate = self.__calculate_max_charge(state_of_charge)
                energy_available_to_charge_battery = \
                    min(-elec_demand * self.__one_way_battery_efficiency \
                    * self.__state_of_health * air_temp_capacity_factor, max_charge)

        else:  # Discharging battery
            if charging_from_grid:
                max_discharge = 0
            else:
                max_discharge = self.calculate_max_discharge(state_of_charge) # max charge energy the battery can supply in the timestep
            energy_available_to_charge_battery = \
                max(-elec_demand, max_discharge) / self.__one_way_battery_efficiency \
                * self.__state_of_health * air_temp_capacity_factor # reductions due to state of health (i.e age) and cold temperature applied here
        
        # Charge/discharge the battery by the amount available
        current_energy_stored_unconstrained = self.__current_energy_stored + energy_available_to_charge_battery

        prev_energy_stored = self.__current_energy_stored
        # Energy stored cannot be > battery capacity or < 0
        self.__current_energy_stored = min(self.__max_capacity, max(0, current_energy_stored_unconstrained))
        energy_accepted_by_battery = self.__current_energy_stored - prev_energy_stored
        # Return the supply/demand energy the battery can accept (including charging/discharging losses)
        if elec_demand < 0:  # Charging battery
            # Calculate charging time of battery
            if max_charge_rate is not None and max_charge_rate >= 0.0:
                time_charging_current_load = min(
                    energy_accepted_by_battery / max_charge_rate / self.__one_way_battery_efficiency \
                    / self.__state_of_health / air_temp_capacity_factor,
                    timestep - self.__total_time_charging_current_timestep
                    )
                # TODO some of these adjustment factors are probably adjusting the energy_accepted_by_battery while others are adjusting max_charge_rate, 
                #      and I think it would clearer to calculate adjusted versions of those two variables separately.
            else:
                time_charging_current_load = 0.0
            self.__total_time_charging_current_timestep += time_charging_current_load
            
            return -energy_accepted_by_battery/self.__one_way_battery_efficiency
        else:  # Discharging battery
            return -energy_accepted_by_battery*self.__one_way_battery_efficiency

    def __limit_capacity_due_to_temp(self):
        if self.__battery_location == "outside":
            air_temp = self.__external_conditions.air_temp()          
        elif self.__battery_location == "inside": 
            air_temp = 20 # Fixed for now, but if we add zone location of battery (if inside) as an input, we could look this up in future.
        else:
            sys.exit('Invalid battery location.')
            
        capacity_reduction_due_to_temp = max(0, min(1, self.__capacity_temp_equ(air_temp) ) )        

        return capacity_reduction_due_to_temp
    

    def __calculate_max_charge(self, state_of_charge):
        """ Calculate the maximum rate of charge rate based on the current state of charge of the battery
        Arguments:
        state_of_charge -- the current state of charge (0 - 1) of the battery
        """
        charge_factor_for_soc = self.__charge_rate_soc_equ(state_of_charge)
        
        max_charge_rate = self.__maximum_charge_rate * charge_factor_for_soc
        
        max_charge = self.__maximum_charge_rate * charge_factor_for_soc * self.__simulation_time.timestep()

        return max_charge, max_charge_rate

    def calculate_max_discharge(self, state_of_charge):
        """ Calculate the maximum amount of discharge possible based on the current state of charge of the battery
        Arguments:
        state_of_charge -- the current state of charge (0 - 1) of the battery
        """

        discharge_factor_for_soc = self.__discharge_rate_soc_equ(state_of_charge)

        max_discharge = \
            (self.__maximum_discharge_rate * discharge_factor_for_soc * self.__simulation_time.timestep()) * -1

        return max_discharge

    def timestep_end(self):
        """" Calculations to be done at the end of each timestep"""
        
        #Variabales below need to be reset at the end of each timestep
        self.__total_time_charging_current_timestep = 0.0
        
    def get_charge_discharge_efficiency(self):
        return self.__charge_discharge_efficiency
