#!/usr/bin/env python3

"""
This module provides objects to represent the internal gains.
"""
# Standard library imports
from math import ceil, floor

# Local imports
import core.units as units
from core.schedule import expand_schedule, expand_events


class InternalGains:
    """ An object to represent internal gains """

    def __init__(self, total_internal_gains, simulation_time, start_day, time_series_step):
        """ Construct a InternalGains object

        Arguments:
        total_internal_gains -- list of internal gains, in W/m2 (one entry per hour)
        simulation_time      -- reference to SimulationTime object
        start_day            -- first day of the time series, day of the year, 0 to 365 (single value)
        time_series_step     -- timestep of the time series data, in hours
        """
        self.__total_internal_gains = total_internal_gains
        self.__simulation_time  = simulation_time
        self.__start_day = start_day
        self.__time_series_step = time_series_step

    def total_internal_gain(self, zone_area):
        """ Return the total internal gain for the current timestep in W"""
        return self.__total_internal_gains[self.__simulation_time.time_series_idx(self.__start_day, self.__time_series_step)] * zone_area


class ApplianceGains:
    """ An object to represent internal gains and energy consumption from appliances"""

    def __init__(self, total_energy_supply, energy_supply_conn, gains_fraction, simulation_time, start_day, time_series_step):
        """ Construct a InternalGains object

        Arguments:
        total_energy_supply      -- list of energy supply from appliances, in W / m2 (one entry per hour)
        energy_supply_connection -- reference to EnergySupplyConnection object representing
                                    the electricity supply attached to the appliance
        gains_fraction           -- fraction of energy supply which is counted as an internal gain
        simulation_time          -- reference to SimulationTime object
        start_day                -- first day of the time series, day of the year, 0 to 365 (single value)
        time_series_step         -- timestep of the time series data, in hours
        """
        self.__total_energy_supply = total_energy_supply
        self.__energy_supply_conn = energy_supply_conn
        self.__gains_fraction = gains_fraction
        self.__simulation_time  = simulation_time
        self.__start_day = start_day
        self.__time_series_step = time_series_step

    def total_internal_gain(self, zone_area):
        """ Return the total internal gain for the current timestep, in W """
        # Forward elctricity demand (in kWh) to relevant EnergySupply object
        total_energy_supplied = self.__total_energy_supply[self.__simulation_time.time_series_idx(self.__start_day, self.__time_series_step)] 
        total_energy_supplied_W = total_energy_supplied * zone_area # convert to W
        total_energy_supplied_kWh = total_energy_supplied_W / units.W_per_kW * self.__simulation_time.timestep() # convert to kWh

        self.__energy_supply_conn.demand_energy(total_energy_supplied_kWh)

        return total_energy_supplied_W * self.__gains_fraction


class EventApplianceGains:
    """ An object to represent internal gains and energy consumption from appliances"""

    def __init__(self, energy_supply_conn, simulation_time, appliance_data, TFA, smartcontrol=None):
        """ Construct a InternalGains object

        Arguments:
        energy_supply_connection -- reference to EnergySupplyConnection object representing
                                    the electricity supply attached to the appliance
        simulation_time          -- reference to SimulationTime object
        appliance_data           -- dictionary of appliance gains data from project dict, including:
                                    gains_fraction    -- proportion of appliance demand turned into heat gains
                                    start_day         -- first day of the time series, day of the year, 0 to 365 (single value)
                                    time_series_step  -- timestep of the time series data, in hours
                                    Standby           -- appliance power consumption when not in use in Watts
                                    Events            -- list of appliance usage events, which are dictionaries,
                                                         containing demand_W, start and duration, 
                                                         with start and duration in hours
                                    loadshifting      -- (optional) dictionary defining loadshifting parameters
                                                         max_shift_hrs         - the maximum time, in hours, that an event 
                                                                                 may be shifted away from when it was originally
                                                                                 intended to occur. This may be up to 24 hours. 
                                                         weight_timeseries     - this may be, for example, the hourly cost per 
                                                                                 kWh of a 7hr tariff, but could be any time series. 
                                                                                 The sum of the other demand and the demand of the 
                                                                                 appliance in question at any given time is multiplied 
                                                                                 by the value of this timeseries to obtain a figure 
                                                                                 that is used to determine whether to shift an event,
                                                                                 and when would be the most appropriate time to shift 
                                                                                 the event to.
                                                         demand_limit_weighted - value above which the sum demand multiplied by the 
                                                                                 weight should not exceed. If a 7hr tariff were used for 
                                                                                 the weight timeseries, then this would be a cost. If this value
                                                                                 is 0, then all events will be shifted to the optimal time
                                                                                 within the window, otherwise they will be shifted to the earliest
                                                                                 time at which the weighted demand goes below the limit.
                                                                                 (if there is no time in the window when the weighted demand is below
                                                                                 the limit, then the optimum is chosen.)
        TFA                      -- total floor area of dwelling
        smartcontrol             -- reference to SmartApplianceControl object (required for loadshifting, otherwise not needed)
        """
        self.__energy_supply_conn = energy_supply_conn
        self.__energy_supply_name = appliance_data['EnergySupply']
        self.__gains_fraction = appliance_data["gains_fraction"]
        
        self.__simulation_time  = simulation_time
        self.__start_day = appliance_data["start_day"]

        self.__timeseries_step = appliance_data["time_series_step"]
        self.__series_length = ceil(self.__simulation_time.total_steps() * self.__simulation_time.timestep()
                                     / self.__timeseries_step)
        
        self.__total_floor_area = TFA
        self.__standby_power = appliance_data["Standby"]
        self.__usage_events = appliance_data["Events"]
        
        
        if "loadshifting" in appliance_data:
            self.__max_shift = appliance_data["loadshifting"]["max_shift_hrs"] / self.__simulation_time.timestep()
            self.__demand_limit = appliance_data["loadshifting"]["demand_limit_weighted"]
            self.__weight_timeseries = appliance_data["loadshifting"]["weight_timeseries"]
            self.__smartcontrol = smartcontrol
        else:
            self.__max_shift = -1
            self.__demand_limit = None
        
        #initialize list with standby power on all timesteps
        self.__total_power_supply = [self.__standby_power for x in range(
            self.__simulation_time.total_steps()
            )
        ]

    def __process_events(self):
        #adds demand from events up to and including the current timestep 
        #to the total annual demand. If there is loadshifting the demand of the event
        #may occur in the future rather than at the time specified
        for event_idx in range(len(self.__usage_events)):
            if floor(self.__usage_events[0]["start"]) <= self.__simulation_time.current_hour():
                eventdict = self.__usage_events.pop(0)
            else:
                #no events to process yet
                break
            start_idx, power_timesteps = self.__process_event(eventdict)
            for i, power in enumerate(power_timesteps):
                #any demand that is expected to run off past the end of the simulation is put at the last step
                t_idx = min((start_idx + i), self.__simulation_time.total_steps() - 1)
                self.__total_power_supply[t_idx] += power
                if self.__max_shift >= 0:
                    self.__smartcontrol.add_appliance_demand(t_idx, power / units.W_per_kW * self.__simulation_time.timestep(), self.__energy_supply_name)

    def __process_event(self, eventdict):
        start_idx, power_list_over_timesteps = self.__event_to_schedule(eventdict)
        if self.__max_shift >= 0:
            start_shift = self.__shift_iterative(start_idx, power_list_over_timesteps, eventdict)
            return start_idx + start_shift, power_list_over_timesteps
        return start_idx, power_list_over_timesteps
    
    def __shift_iterative(self, start_idx, power_list_over_timesteps, eventdict):
        """ 
        shifts an event forward in time one timestep at a time,
        until either the total weighted demand on that timestep is below demandlimit
        or the event has been shifted beyond the maximum allowed number of timesteps
        away from its original position. In the latter case, move the event to the
        most favourable time within the allowed window
        """
        #pos list will store the total weighted demand (including from the rest of the dwelling)
        #for the usage event happening at the intended time, or 1 timestep into the future, or 2, up to
        #the max shift time.
        #the lowest value in this list will represent the time at which the usage event would result in the
        #lowest demand.
        pos_list = [0 for x in range(ceil(self.__max_shift))]
        for start_shift in range(len(pos_list)):
            for i, power in enumerate(power_list_over_timesteps):
                t_idx = min(start_idx + i + start_shift, self.__simulation_time.total_steps() - 1)
                series_idx = floor(t_idx * self.__simulation_time.timestep() / self.__timeseries_step)
                
                if self.__total_power_supply[t_idx] >= eventdict["demand_W"]:
                    #the appliance is already turned on for the entire timestep
                    #cannot put an event here
                    #put arbitrarily high demand at this position so it is not picked
                    pos_list[start_shift] += 10000 * self.__weight_timeseries[series_idx]
                    break
                otherdemand = self.__smartcontrol.get_demand(t_idx,self.__energy_supply_name)
                newdemand = power / units.W_per_kW * self.__simulation_time.timestep()#
                pos_list[start_shift] += (newdemand + otherdemand) * self.__weight_timeseries[series_idx]
            if self.__demand_limit > 0 and pos_list[start_shift] < self.__demand_limit:
                #demand is below the limit, good enough, no need to look further into the future
                return start_shift
        
        start_shift = pos_list.index(min(pos_list))
        return start_shift
    
    def __event_to_schedule(self, eventdict):
        demand_W_event = eventdict["demand_W"]
        start = eventdict["start"]
        duration = eventdict["duration"]
        
        startoffset = start % self.__simulation_time.timestep()
        start_idx = floor(start / self.__simulation_time.timestep())
        
        #if the event overruns the end of the timestep it starts in,
        #power needs to be allocated to two (or more) timesteps
        #according to the length of time within each timestep the appliance is being used for
        integralx = 0.0
        power_timesteps = [0 for x in range(ceil(duration / self.__simulation_time.timestep()))]
        while integralx < duration:
            segment = min(self.__simulation_time.timestep() - startoffset, duration - integralx)
            idx = floor((integralx) / self.__simulation_time.timestep())
            #subtract standby power from the added event power
            #as it is already accounted for when the list is initialised
            power_timesteps[idx] += (demand_W_event - self.__standby_power) * segment
            integralx += segment
        return start_idx, power_timesteps

    def total_internal_gain(self, zone_area):
        """ Return the total internal gain for the current timestep, in W """
        #first process any usage events expected to occur within this timestep
        self.__process_events()
        # Forward electricity demand (in kWh) to relevant EnergySupply object
        total_power_supplied = self.__total_power_supply[self.__simulation_time.index()] 
        total_power_supplied_zone = total_power_supplied * zone_area / self.__total_floor_area 
        total_energy_supplied_kWh = total_power_supplied_zone / units.W_per_kW * self.__simulation_time.timestep() # convert to kWh

        self.__energy_supply_conn.demand_energy(total_energy_supplied_kWh)

        return total_power_supplied_zone * self.__gains_fraction
