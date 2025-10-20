#!/usr/bin/env python3

"""
This module provides objects to represent Infiltration and Ventilation.
The calculations are based on Method 1 of BS EN 16798-7.
"""

# Standard library imports
import sys
import warnings

# Third-party imports
import numpy as np
from scipy.optimize import fsolve, root_scalar, minimize_scalar

# Local imports
from core.units import seconds_per_hour, Celcius2Kelvin, litres_per_cubic_metre, W_per_kW, mm_per_m
from core.simulation_time import SimulationTime
from core.material_properties import AIR
from core.space_heat_demand.building_element import BuildingElement, HeatFlowDirection

# Local imports
from core.ductwork import Ductwork

# Define constants
p_a_ref = AIR.density_kg_per_m3()
c_a = AIR.specific_heat_capacity_kWh()

# (Default values from BS EN 16798-7, Table 11)
# Coefficient to take into account stack effect in airing calculation in (m/s)/(m*K)
C_stack = 0.0035
# Coefficient to take into account wind speed in airing calculation in 1/(m/s)
C_wnd = 0.001
# Gravitational constant in m/s2
g = 9.81
#Room temperature in degrees K
T_e_ref = 293.15
#Absolute zero in degrees K
T_0_abs = 273.15


def calculate_pressure_difference_at_an_airflow_path(
        h_path,
        C_p_path,
        u_site,
        T_e,
        T_z,
        p_z_ref
        ):
    """Calculate pressure difference between the exterior and the interior of the dwelling
    for a flow path (at it's elevavation above the vent zone floor)

    Arguments:
    h_path -- height of air flow path (m)
    C_p_path -- wind pressure coefficient
    u_site -- wind velocity at zone level (m/s)
    T_e -- external air temperature (K)
    T_z -- thermal zone air temperature (K)
    p_z_ref -- internal reference pressure (Pa)
    """
    p_e_path = p_a_ref * T_e_ref/T_e * (0.5 * C_p_path * u_site**2 - h_path * g) #(5)
    p_z_path = p_z_ref - p_a_ref * h_path * g * T_e_ref/T_z #(6)
    delta_p_path = p_e_path - p_z_path #(4)
    return delta_p_path

def air_change_rate_to_flow_rate(air_change_rate, zone_volume):
    """ Convert infiltration rate from ach to m^3/s """
    return air_change_rate * zone_volume / seconds_per_hour

def get_fuel_flow_factor(fuel_type, appliance_type):
    """ Table B.3 fuel flow factors

    Arguments:
    fuel_type -- options are 'wood', 'gas', 'oil' or 'coal'.
    appliance_type -- options are 'open_fireplace', 'closed_with_fan',
        open_gas_flue_balancer', 'open_gas_kitchen_stove', 'open_gas_fire' or 'closed_fire'
    """
    if fuel_type == 'wood':
        if appliance_type == 'open_fireplace':
            f_ff = 2.8
        else:
            sys.exit("appliance_type: "+ str(appliance_type) +" not applicable for the fuel_type: "+ str(fuel_type) +" selected.")
    elif fuel_type == 'gas':
        if appliance_type == 'closed_with_fan':
            f_ff = 0.38
        elif appliance_type == 'open_gas_flue_balancer':
            f_ff = 0.78
        elif appliance_type == 'open_gas_kitchen_stove':
            f_ff = 3.35
        elif appliance_type == 'open_gas_fire':
            f_ff = 3.35
        else:
            sys.exit("appliance_type: "+ str(appliance_type) +" not applicable for the fuel_type: "+ str(fuel_type) +" selected.")
    elif fuel_type == 'oil':
        if appliance_type == 'closed_fire':
            f_ff = 0.32
        else:
            sys.exit("appliance_type: "+ str(appliance_type) +" not applicable for the fuel_type: "+ str(fuel_type) +" selected.")
    elif fuel_type == 'coal':
        if appliance_type == 'closed_fire':
            f_ff = 0.52
        else:
            sys.exit("appliance_type: "+ str(appliance_type) +" not applicable for the fuel_type: "+ str(fuel_type) +" selected.")
    else:
        sys.exit(" fuel_type: "+ str(fuel_type) +" not found.")
    return f_ff

def get_appliance_system_factor(supply_situation, exhaust_situation):
    """Interpreted from Table B.2 from BS EN 16798-7, get the appliance system factor
    for a combustion appliance.

    Arguments:
    supply_situation -- Combustion air supply situation: 'room_air' or 'outside'
    exhaust_situation -- flue gas exhaust situation: 'into_room', 'into_separate_duct' or 'into_mech_vent'
    """
    if supply_situation == "outside":
        f_as = 0
    elif supply_situation == "room_air":
        if exhaust_situation == "into_room":
            f_as = 0
        elif exhaust_situation == "into_separate_duct":
            f_as = 1
        elif exhaust_situation == "into_mech_vent":
            sys.exit("Cannot currently handle 'exhaust_situation': "+ str(exhaust_situation) +" for combustion appliance.")
        else:
            sys.exit("'exhaust_situation': "+ str(exhaust_situation) +" not recognised for combustion appliance")
    else:
        sys.exit("'supply_situation': "+ str(supply_situation) +" not recognised for combustion appliance")
    return f_as

def adjust_air_density_for_altitude(h_alt):
    """Adjust air density for altitude above sea level.

    Arguments:
    h_alt -- altitude above sea level (m)
    """
    p_a_alt = p_a_ref * (1 - ((0.00651 * h_alt) / 293))** 4.255
    return p_a_alt

def air_density_at_temp(temperature, air_density_adjusted_for_alt):
    """Recalculate air density based on the current temperature

    Arguments:
    temperature -- temperature to adjust (K)
    air_density_adjusted_for_alt - The air density after adjusting for altitude (Kg/m3)
    """
    return T_e_ref / temperature * air_density_adjusted_for_alt

def convert_to_mass_air_flow_rate(qv_in, qv_out, T_e, T_z, p_a_alt):
    """Converts volume air flow rate (qv) to mass air flow rate (qm).
    (Equations 65 & 66 from BS EN 16798-7)

    Arguments:
    qv_in -- volume flow rate of air entering the dwelling
    qv_out -- volume flow rate of air leaving the dwelling
    T_e -- External air temperature (K)
    T_e -- Thermal zone air temperature (K)
    p_a_alt -- The air density after adjusting for altitude (Kg/m3)
    """
    qm_in = convert_volume_flow_rate_to_mass_flow_rate(qv_in, T_e, p_a_alt)
    qm_out = convert_volume_flow_rate_to_mass_flow_rate(qv_out, T_z, p_a_alt)
    return qm_in, qm_out

def convert_volume_flow_rate_to_mass_flow_rate(qv, temperature, p_a_alt):
    """ Convert volume flow rate in m3/hr to mass flow rate in kg/hr, at temperature in Kelvin 

    Arguments:
    qv -- volume flow rate (m3/h)
    temperature -- air temperature (K)
    p_a_alt -- The air density after adjusting for altitude (Kg/m3)
    """
    return qv * air_density_at_temp(temperature, p_a_alt)

def convert_mass_flow_rate_to_volume_flow_rate(qm, temperature, p_a_alt):
    """ Convert mass flow rate in kg/hr to volume flow rate in m3/hr, at temperature in Kelvin

    Arguments:
    qm -- mass flow rate (Kg/h)
    temperature -- air temperature (K)
    p_a_alt -- The air density after adjusting for altitude (Kg/m3)
    """
    return qm / air_density_at_temp(temperature, p_a_alt)

def ter_class_to_roughness_coeff(terrain_class, z):
    """
    Retrieves the roughness parameters and calculates the roughness coefficient (CR)
    based on the terrain type and height of airflow path.

    Args:
        terrain_class (str): The terrain type ('OpenWater', 'OpenField', 'Suburban', 'Urban').
        z (float): Height of airflow path relative to the ground (m).

    Returns:
        float: Calculated roughness coefficient CR.

    Raises:
        ValueError: If an invalid terrain type is provided.
    """
    # Mapping of terrain types to their roughness parameters (KR, z0, zmin)
    terrain_data = {
        'OpenWater': (0.17, 0.01, 2),  # Rough open sea, lake shore
        'OpenField': (0.19, 0.05, 4),  # Farm land, small structures
        'Suburban': (0.22, 0.3, 8),    # Suburban or industrial areas
        'Urban': (0.24, 1.0, 16),      # Urban areas with tall buildings
    }

    if terrain_class not in terrain_data:
        raise ValueError(f"Unknown terrain type: {terrain_class}")

    # Retrieve the terrain parameters
    KR, z0, zmin = terrain_data[terrain_class]
    
    # Ensure z is at least zmin
    z = max(z, zmin)

    # Calculate the roughness coefficient
    CR = KR * np.log(z / z0)

    return CR


def wind_speed_at_zone_level(C_rgh_site, u_10, C_top_site=1, C_rgh_met=1, C_top_met=1):
    """Meteorological wind speed at 10 m corrected to reference wind speed at zone level of the dwelling

    Arguments:
    C_rgh_site -- roughness coefficient at building site
    u_10 -- wind velocity at 10m (m/s)
    C_top_site -- topography coefficient at building site
    C_rgh_met -- roughness coefficient at 10m depending on meteorological station
    C_top_met -- topography coefficient at building height depending on meteorological station
    """
    u_site = ((C_rgh_site * C_top_site) / (C_rgh_met * C_top_met)) * u_10
    return u_site

#Not needed as using internal pressure for windows, not cross ventilation
# def wind_speed_at_10m_height(C_rgh_10_site, u_10, C_top_10_site=1, C_rgh_met=1, C_top_met=1):
#     """The meteorological wind speed at 10 m is corrected as follows to obtain the reference wind speed at
#     site at 10m height:
#     """
#     u_10_site = ((C_rgh_10_site * C_top_10_site) / (C_rgh_met * C_top_met)) * u_10
#     return u_10_site

def orientation_difference(orientation1, orientation2):
    """ Determine difference between two bearings, taking shortest route around circle """
    if not 0 <= orientation1 <= 360 or not 0 <= orientation2 <= 360:
        raise ValueError("Orientations must be in the range 0-360")
    op_rel_orientation = abs(orientation1 - orientation2)
    if op_rel_orientation > 180:
        op_rel_orientation = 360 - op_rel_orientation
    return op_rel_orientation

def get_facade_direction(f_cross, orientation, pitch, wind_direction):
    """Gets direction of the facade from pitch and orientation

    Arguments:
    f_cross -- boolean, dependant on if cross ventilation is possible or not
    orientation -- orientation of the facade (degrees)
    pitch -- pitch of the facade (degrees)
    wind_direction -- direction the wind is blowing (degrees)
    """
    if f_cross == True:
        if pitch < 10:
            facade_direction = "Roof10"
        elif pitch <= 30:
            facade_direction = "Roof10_30"
        elif pitch < 60:
            facade_direction = "Roof30"
        else:
            orientation_diff = orientation_difference(orientation, wind_direction)
            if orientation_diff <= 60:
                facade_direction = "Windward"
            elif orientation_diff < 120:
                facade_direction = "Neither"
            else:
                facade_direction = "Leeward"
    elif f_cross == False:
        if pitch < 60:
            facade_direction = "Roof"
        else:
            orientation_diff = orientation_difference(orientation, wind_direction)
            if orientation_diff <= 60:
                facade_direction = "Windward"
            elif orientation_diff < 120:
                facade_direction = "Neither"
            else:
                facade_direction = "Leeward"
    else:
        sys.exit('f_cross should be set to True or False')
    return facade_direction

def get_C_p_path(f_cross,
                 shield_class,
                 z,
                 wind_direction,
                 orientation=None,
                 pitch=None,
                 facade_direction=None,
                 ):
    """Interpreted from Table B.7 for determining dimensionless wind pressure coefficients

    Arguments:
    f_cross -- boolean, dependant on if cross ventilation is possible or not
    shield_class -- indicates exposure to wind
    z -- height of air flow path relative to ground (m)
    wind_direction -- direction the wind is blowing (degrees)
    orientation -- orientation of the facade (degrees)
    pitch -- pitch of the facade (degrees)
    facade_direction -- direction of the facade (from get_facade_direction or manual entry)
    """
    if facade_direction == None:
        if orientation is None or pitch is None:
            sys.exit('You have not entered a pitch or orientation for an opaque building element.')
        else:
            facade_direction = get_facade_direction(f_cross, orientation, pitch, wind_direction)
    if f_cross == True:
        if z < 15:
            if shield_class == "Open":
                C_p = {"Windward": 0.50, "Leeward": -0.70, "Neither": 0.0, "Roof10": -0.70, "Roof10_30": -0.60, "Roof30": -0.20}
            elif shield_class == "Normal":
                C_p = {"Windward": 0.25, "Leeward": -0.50, "Neither": 0.0, "Roof10": -0.60, "Roof10_30": -0.50, "Roof30": -0.20}
            elif shield_class == "Shielded":
                C_p = {"Windward": 0.05, "Leeward": -0.30, "Neither": 0.0, "Roof10": -0.50, "Roof10_30": -0.40, "Roof30": -0.20}
        elif 15 <= z < 50:
            if shield_class == "Open":
                C_p = {"Windward": 0.65, "Leeward": -0.70, "Neither": 0.0, "Roof10": -0.70, "Roof10_30": -0.60, "Roof30": -0.20}
            elif shield_class == "Normal":
                C_p = {"Windward": 0.45, "Leeward": -0.50, "Neither": 0.0, "Roof10": -0.60, "Roof10_30": -0.50, "Roof30": -0.20}
            elif shield_class == "Shielded":
                C_p = {"Windward": 0.25, "Leeward": -0.30, "Neither": 0.0, "Roof10": -0.50, "Roof10_30": -0.40, "Roof30": -0.20}
        elif z >= 50:
            if shield_class == "Open":
                C_p = {"Windward": 0.80, "Leeward": -0.70, "Neither": 0.0, "Roof10": -0.70, "Roof10_30": -0.60, "Roof30": -0.20}
    elif f_cross == False:
        C_p = {"Windward": 0.05, "Leeward": -0.05, "Neither": 0.0, "Roof": 0}
    else:
        sys.exit('f_cross should be set to True or False')
    return C_p[facade_direction]


class Window:
    """ An object to represent Windows """
    def __init__(
            self,
            h_w_fa,
            h_w_path,
            A_w_max,
            window_part_list,
            orientation,
            pitch,
            altitude,
            on_off_ctrl_obj,
            ventilation_zone_base_height,
            ):
        """Construct a Window object

        Arguments:
            extcond -- The external conditions.
            h_w_fa -- The free area height of the window
            h_w_path -- The midheight of the window.
            A_w_max -- The maximum window opening area.
            window_part_list -- The list of window parts.
            orientation -- The orientation of the window.
            pitch -- The pitch of the window.
            altitude -- altitude of dwelling above sea level (m)
            on_off_ctrl_obj - 

        Method
            - Based on Section 6.4.3.5 Airflow due to windows opening section.
        """
        self.__h_w_fa = h_w_fa
        self.__h_w_path = h_w_path
        self.__A_w_max = A_w_max
        self.__C_D_w = 0.67 # Discharge coefficient for windows based on Section B.3.2.1 of BS EN 16798-7:2017
        self.__n_w = 0.5 # Flow exponent of window based on Section B.3.2.2 of BS EN 16798-7:2017
        self.__orientation = orientation 
        self.__pitch = pitch
        self.__N_w_div = max(len(window_part_list) - 1 , 0) 
        self.__on_off_ctrl_obj = on_off_ctrl_obj
        self.__altitude = altitude
        self.__p_a_alt = adjust_air_density_for_altitude(altitude)
        self.__z = self.__h_w_path + ventilation_zone_base_height

        self.__window_parts = []
        for window_part_number, window_part in enumerate(window_part_list):
            self.__window_parts.append(
                WindowPart(
                    window_part["mid_height_air_flow_path"], #h_w_path
                    self.__h_w_fa,
                    self.__N_w_div,
                    window_part_number + 1,
                    ventilation_zone_base_height,
                    )
                )

    def calculate_window_opening_free_area(self, R_w_arg):
        """The window opening free area A_w for a window 
        Equation 40 in BS EN 16798-7.
        Arguments:
        R_w_arg -- ratio of window opening (0-1)
        """
        # Assume windows are shut if the control object is empty      
        if self.__on_off_ctrl_obj is None:
            R_w_arg = 0
        if self.__on_off_ctrl_obj is not None and self.__on_off_ctrl_obj.is_on() == False:
            R_w_arg = 0        
        return R_w_arg * self.__A_w_max #self.__A_w

    def calculate_flow_coeff_for_window(self, R_w_arg):
        """The C_w_path flow coefficient for a window
        Equation 54 from BS EN 16798-7
        Arguments:
        R_w_arg -- ratio of window opening (0-1)
        """
        # Assume windows are shut if the control object is empty      
        if self.__on_off_ctrl_obj is None:
            R_w_arg = 0
        if self.__on_off_ctrl_obj is not None and self.__on_off_ctrl_obj.is_on() == False:
            R_w_arg = 0
        A_w = self.calculate_window_opening_free_area(R_w_arg)
        return (3600 * self.__C_D_w * A_w * (2/p_a_ref)** self.__n_w)

    def calculate_flow_from_internal_p(self, wind_direction, u_site, T_e, T_z, p_z_ref, f_cross, shield_class, R_w_arg = None):
        """Calculate the airflow through window opening based on the how open the window is and internal pressure

        Arguments:
        wind_direction -- direction wind is blowing from, in clockwise degrees from North
        u_site -- wind velocity at zone level (m/s)
        T_e -- external air temperature (K)
        T_z -- thermal zone air temperature (K)
        p_z_ref -- internal reference pressure (Pa)
        f_cross -- boolean, dependant on if cross ventilation is possible or not
        shield_class -- indicates exposure to wind
        R_w_arg -- ratio of window opening (0-1)
        """
        # Assume windows are shut if the control object is empty      
        if self.__on_off_ctrl_obj is None:
            R_w_arg = 0
        if self.__on_off_ctrl_obj is not None and self.__on_off_ctrl_obj.is_on() == False:
            R_w_arg = 0

        # Wind pressure coefficient for the window
        C_p_path = get_C_p_path(
            f_cross,
            shield_class,
            self.__z,
            wind_direction,
            self.__orientation,
            self.__pitch,
            )

        # Airflow coefficient of the window
        C_w_path = self.calculate_flow_coeff_for_window(R_w_arg)

        # Sum airflow through each window part entering and leaving - based on Equation 56 and 57
        qv_in_through_window_opening = 0
        qv_out_through_window_opening = 0
        for window_part in self.__window_parts:
            air_flow = window_part.calculate_ventilation_through_windows_using_internal_p(
                u_site,
                T_e,
                T_z,
                C_w_path,
                p_z_ref,
                C_p_path,
                )
            if air_flow >= 0:
                qv_in_through_window_opening += air_flow
            else:
                qv_out_through_window_opening += air_flow
        
        # Convert volume air flow rate to mass air flow rate
        qm_in_through_window_opening, qm_out_through_window_opening = convert_to_mass_air_flow_rate(
            qv_in_through_window_opening,
            qv_out_through_window_opening,
            T_e,
            T_z,
            self.__p_a_alt
        )
        return qm_in_through_window_opening, qm_out_through_window_opening


class WindowPart:
    def __init__(
            self,
            h_w_path,
            h_w_fa,
            N_w_div,
            window_part_number,
            ventilation_zone_base_height,
            ):
        """
        Construct a WindowPart object

        Argument:
            h_w_path -- Mid-height of the window
            h_w_fa -- free area height of the window
            N_w_div -- number of window divisions
            window_part_number -- The identifying number of the window part
        """
        self.__h_w_path = h_w_path #Find from inp file - Midheight of window part
        self.__h_w_fa = h_w_fa #Find from inp file
        self.__N_w_div = N_w_div
        self.__h_w_div_path = self.calculate_height_for_delta_p_w_div_path(window_part_number)
        self.__n_w = 0.5 # Flow exponent of window
        self.__z = self.__h_w_path + ventilation_zone_base_height

    def calculate_ventilation_through_windows_using_internal_p(
            self,
            u_site,
            T_e,
            T_z,
            C_w_path,
            p_z_ref,
            C_p_path,
            ):
        """Calculate the airflow through window parts from internal pressure

        Arguments:
        u_site -- wind velocity at zone level (m/s)
        T_e -- external air temperature (K)    
        T_z -- thermal zone air temperature (K)
        C_w_path -- wind pressure coefficient at height of the window
        p_z_ref -- internal reference pressure (Pa)
        C_p_path -- wind pressure coefficient at the height of the window part
        """
        delta_p_path = calculate_pressure_difference_at_an_airflow_path(
            self.__h_w_div_path,
            C_p_path,
            u_site,
            T_e,
            T_z,
            p_z_ref
        )
        # Based on Equation 53
        qv_w_div_path = C_w_path / (self.__N_w_div + 1) \
                      * np.sign(delta_p_path) \
                      * abs(delta_p_path) ** self.__n_w
        return qv_w_div_path

    def calculate_height_for_delta_p_w_div_path(self, j):
        """ The height to be considered for delta_p_w_div_path
        Equation 55 from BS EN 16798-7"""
        h_w_div_path = self.__h_w_path - self.__h_w_fa/2 + self.__h_w_fa/(2 * (self.__N_w_div + 1)) +\
                      (self.__h_w_fa/(self.__N_w_div + 1)) * (j-1)
        return h_w_div_path


class Vent:
    """ An object to represent Vents """
    def __init__(
            self,
            h_path,
            A_vent,
            delta_p_vent_ref,
            orientation,
            pitch,
            altitude,
            ventilation_zone_base_height, 
            ):
        """ Construct a Vent object

        Arguments:
            h_path -- mid height of air flow path relative to ventilation zone (m)
            A_vent - Equivalent area of a vent (m2)
            delta_p_vent_ref -- reference pressure difference for vent (Pa)
            orientation -- The orientation of the vent (degrees)
            pitch -- The pitch of the vent (degrees)
            altitude -- altitude of dwelling above sea level (m)
        
        Method:
            - Based on Section 6.4.3.6 Airflow through vents from BS EN 16798-7
        """
        self.__h_path = h_path
        self.__A_vent = A_vent 
        self.__delta_p_vent_ref = delta_p_vent_ref
        self.__orientation = orientation
        self.__pitch = pitch
        self.__altitude = altitude
        self.__n_vent = 0.5 # Flow exponent for vents based on Section B.3.2.2 from BS EN 16798-7
        self.__C_D_vent = 0.6 # Discharge coefficient of vents based on B.3.2.1 from BS EN 16798-7
        self.__p_a_alt = adjust_air_density_for_altitude(altitude)
        self.__z = self.__h_path + ventilation_zone_base_height

    def calculate_vent_opening_free_area(self, R_v_arg):
        """The vent opening free area A_vent for a vent 
        Arguments:
        R_v_arg -- ratio of vent opening (0-1)
        """
        return R_v_arg * self.__A_vent

    def calculate_flow_coeff_for_vent(self, R_v_arg):
        """The airflow coefficient of the vent calculated from equivalent area A_vent
        according to EN 13141-1 and EN 13141-2. 
        Based on Equation 59 from BS EN 16798-7.
        """
        #NOTE: The standard does not define what the below 3600 and 10000 are.
        A_vent = self.calculate_vent_opening_free_area(R_v_arg)
        C_vent_path = (3600/10000) \
                    * self.__C_D_vent * A_vent \
                    * (2/p_a_ref)**0.5 * (1/self.__delta_p_vent_ref)**(self.__n_vent - 0.5)
        return C_vent_path

    def calculate_ventilation_through_vents_using_internal_p(
            self,
            u_site,
            T_e,
            T_z,
            C_vent_path,
            C_p_path,
            p_z_ref,
            ):
        """Calculate the airflow through vents from internal pressure

        Arguments:
        u_site -- wind velocity at zone level (m/s)
        T_e -- external air temperature (K)
        T_z -- thermal zone air temperature (K)
        C_vent_path -- wind pressure coefficient at height of the vent
        C_p_path -- wind pressure coefficient at the height of the window part
        p_z_ref -- internal reference pressure (Pa)
        """
        # Pressure_difference at the vent level
        delta_p_path = calculate_pressure_difference_at_an_airflow_path(
            self.__h_path,
            C_p_path,
            u_site,
            T_e,
            T_z,
            p_z_ref
        )

        # Air flow rate for each couple of height and wind pressure coeficient associated with vents.
        # Based on Equation 58
        qv_vent_path = C_vent_path * np.sign(delta_p_path) \
                     * abs(delta_p_path) \
                     ** self.__n_vent
        return qv_vent_path

    def calculate_flow_from_internal_p(self, wind_direction, u_site, T_e, T_z, p_z_ref, f_cross, shield_class, R_v_arg):
        """Calculate the airflow through vents from internal pressure

        Arguments:
        wind_direction -- direction wind is blowing from, in clockwise degrees from North
        u_site -- wind velocity at zone level (m/s)
        T_e -- external air temperature (K)
        T_z -- thermal zone air temperature (K)
        p_z_ref -- internal reference pressure (Pa)
        f_cross -- boolean, dependant on if cross ventilation is possible or not
        shield_class -- indicates exposure to wind
        """

        # Wind pressure coefficient for the air flow path
        C_p_path = get_C_p_path(
            f_cross,
            shield_class,
            self.__z,
            wind_direction,
            self.__orientation,
            self.__pitch,
            )
        C_vent_path = self.calculate_flow_coeff_for_vent(R_v_arg)
        # Calculate airflow through each vent
        air_flow = self.calculate_ventilation_through_vents_using_internal_p(
            u_site,
            T_e,
            T_z,
            C_vent_path,
            C_p_path,
            p_z_ref,
            )

        # Sum airflows entering and leaving - based on Equation 60 and 61
        qv_in_through_vent = 0
        qv_out_through_vent = 0
        if air_flow >= 0:
            qv_in_through_vent += air_flow
        else:
            qv_out_through_vent += air_flow

        # Convert volume air flow rate to mass air flow rate
        qm_in_through_vent, qm_out_through_vent = convert_to_mass_air_flow_rate(
            qv_in_through_vent,
            qv_out_through_vent,
            T_e,
            T_z,
            self.__p_a_alt
        )
        return qm_in_through_vent, qm_out_through_vent


class Leaks:
    """ An object to represent Leaks """
    def __init__(
            self,
            h_path,
            delta_p_leak_ref,
            qv_delta_p_leak_ref,
            facade_direction,
            A_roof,
            A_facades,
            A_leak,
            altitude,
            ventilation_zone_base_height,
            ):
        """ Construct a Leaks object

        Arguments:
            extcond -- reference to ExternalConditions object
            h_path -- mid height of the air flow path relative to ventlation zone floor level
            delta_p_leak_ref -- Reference pressure difference (From pressure test e.g blower door = 50Pa)
            C_leak_path -- Coefficient of leakage in the external envelope
            qv_delta_p_leak_ref -- flow rate through
            facade_direction -- The direction of the facade the leak is on.
            A_roof -- Surface area of the roof of the ventilation zone (m2)
            A_facades -- Surface area of facades (m2)
            A_leak - Reference area of the envelope airtightness index qv_delta_p_leak_ref (depends on national context)
            altitude -- altitude of dwelling above sea level (m)
            ventilation_zone_base_height -- Base height of the ventilation zone relative to ground (m)

        Method:
            - - Based on Section 6.4.3.6 Airflow through leaks from BS EN 16798-7.
        
        """
        self.__h_path = h_path
        self.__delta_p_leak_ref = delta_p_leak_ref
        self.__A_roof = A_roof
        self.__A_facades = A_facades
        self.__A_leak = A_leak
        self.__qv_delta_p_leak_ref = qv_delta_p_leak_ref
        self.__facade_direction = facade_direction
        self.__altitude = altitude
        self.__n_leak = 0.667 # Flow exponent through leaks based on value in B.3.3.14
        self.__C_leak_path = self.calculate_flow_coeff_for_leak()
        self.__p_a_alt = adjust_air_density_for_altitude(altitude)
        self.__z = self.__h_path + ventilation_zone_base_height

    def calculate_flow_coeff_for_leak(self):
        """The airflow coefficient of the leak """
        # C_leak - Leakage coefficient of ventilation zone
        C_leak = self.__qv_delta_p_leak_ref * self.__A_leak / (self.__delta_p_leak_ref) ** self.__n_leak

        # Leakage coefficient of roof, estimated to be proportional to ratio 
        # of surface area of the facades to that of the facades plus the roof.
        if self.__facade_direction != 'Windward' and self.__facade_direction != 'Leeward': #leak in roof
            C_leak_roof = C_leak * self.__A_roof / (self.__A_facades + self.__A_roof)
            C_leak_path = C_leak_roof #Table B.12
        # Leakage coefficient of facades, estimated to be proportional to ratio 
        # of surface area of the roof to that of the facades plus the roof.
        else: #leak in facades
            C_leak_facades = C_leak * self.__A_facades / (self.__A_facades + self.__A_roof)
            C_leak_path = 0.25 * C_leak_facades #Table B.12
        return C_leak_path

    def calculate_ventilation_through_leaks_using_internal_p(
            self,
            u_site,
            T_e,
            T_z,
            C_p_path,
            p_z_ref,
            ):
        """Calculate the airflow through leaks from internal pressure

        Arguments:
        u_site -- wind velocity at zone level (m/s)
        T_e -- external air temperature (K)
        T_z -- thermal zone air temperature (K)
        C_p_path -- wind pressure coefficient at the height of the window part
        p_z_ref -- internal reference pressure (Pa)
        """
        # For each couple of height and wind pressure coeficient associated with vents,
        # the air flow rate.
        delta_p_path = calculate_pressure_difference_at_an_airflow_path(
            self.__h_path,
            C_p_path,
            u_site,
            T_e,
            T_z,
            p_z_ref,
            )

        # Airflow through leaks based on Equation 62
        qv_leak_path = self.__C_leak_path * np.sign(delta_p_path) \
                     * abs(delta_p_path) \
                     ** self.__n_leak

        return qv_leak_path

    def calculate_flow_from_internal_p(self, wind_direction, u_site, T_e, T_z, p_z_ref, f_cross, shield_class):
        # Wind pressure coefficient for the air flow path
        C_p_path = get_C_p_path(f_cross,
                                shield_class,
                                self.__z,
                                wind_direction,
                                None,
                                None,
                                self.__facade_direction,
                                ) #TABLE from annex B
        # Calculate airflow through each leak
        qv_in_through_leak = 0
        qv_out_through_leak = 0
        air_flow = self.calculate_ventilation_through_leaks_using_internal_p(
            u_site,
            T_e,
            T_z,
            C_p_path,
            p_z_ref,
            )

        # Add airflow entering and leaving through leak
        if air_flow >= 0:
            qv_in_through_leak += air_flow
        else:
            qv_out_through_leak += air_flow

        # Convert volume air flow rate to mass air flow rate
        qm_in_through_leak, qm_out_through_leak = convert_to_mass_air_flow_rate(
            qv_in_through_leak,
            qv_out_through_leak,
            T_e,
            T_z,
            self.__p_a_alt
        )
        return qm_in_through_leak, qm_out_through_leak


class AirTerminalDevices:
    """An object to represent AirTerminalDevices"""
    def __init__(
            self,
            A_ATD,
            delta_p_ATD_ref,
            ):
        """
        Construct a AirTerminalDevices object

        Arguments:
            A_ATD -- equivalent area of the air terminal device (m2)
            delta_p_ATD_ref -- Reference pressure difference for an air terminal device (Pa)
        
        Method:
            Based on Section 6.4.3.2.2 from BS EN 16798-7
        """
        self.__C_D_ATD = 0.6 # Discharge coefficient for air terminal devices based on B.3.2.1
        self.__n_ATD = 0.5 # Flow exponent of air terminal devices based on B.3.2.2
        self.__A_ATD = A_ATD 
        self.__delta_p_ATD_ref = delta_p_ATD_ref
        self.__C_ATD_path = self.calculate_flow_coeff_for_ATD()

    def calculate_flow_coeff_for_ATD(self):
        """The airflow coefficient of the ATD is calculated 
        from the equivalent area A_vent value, according to
        EN 13141-1 and EN 13141-2.
        Equation 26 from BS EN 16798-7."""
        #NOTE: The standard does not define what the below 3600 and 10000 are.
        C_ATD_path = (3600/10000) * self.__C_D_ATD \
                                  * self.__A_ATD \
                                  * (2 / p_a_ref)**0.5 \
                                  * (1 / self.__delta_p_ATD_ref) \
                                  **(self.__n_ATD - 0.5)
        return C_ATD_path

    def calculate_pressure_difference_atd(self, qv_pdu):
        """The pressure loss at internal air terminal devices is calculated from
        the total air flow rate passing through the device.
        Equation 25 from BS EN 16798-7.
        Solving for qv_pdu.

        Arguments:
        qv_pdu - volume flow rate through passive and hybrid ducts.
        """
        delta_p_ATD = -(np.sign(qv_pdu)) \
                    * (abs(qv_pdu)/self.__C_ATD_path) \
                    ** (1/self.__n_ATD)
        return delta_p_ATD

class Cowls:
    """An object to represent Cowls"""
    def __init__(self,
                 height,
                 ):
        """
        Construct a Cowls object

        Arguments:
        height - height Between the top of the roof and the roof outlet in m (m)
        """
        self.__C_p_cowl_roof = 0 #Default B.3.3.5
        self.__delta_cowl_height = self.get_delta_cowl_height(height)

    def get_delta_cowl_height(self, height):
        """Interpreted Table B.9 from BS EN 16798-7
        Get values for delta_C_cowl_height.

        Arguments:
        height - height Between the top of the roof and the roof outlet in m (m)
        """
        if height < 0.5:
            delta_p_cowl_height = -0.0
        elif height >= 0.5 and height <= 1.0:
            delta_p_cowl_height = -0.1
        else:
            delta_p_cowl_height = -0.2
        return delta_p_cowl_height

class CombustionAppliances:
    """ An object to represent CombustionAppliances """
    def __init__(self,
                 supply_situation,
                 exhaust_situation,
                 fuel_type,
                 appliance_type,
                 ):
        """Construct a CombustionAppliances object
        
        Arguments:
        f_op_comp -- Operation requirement signal (combustion appliance) (0 =  OFF ; 1 = ON)
        supply_situation - Combustion air supply situation: 'room_air' or 'outside'
        exhaust_situation - flue gas exhaust situation: 'into_room', 'into_separate_duct' or 'into_mech_vent'
        f_ff -- combustion air flow factor
        P_h_fi - Combustion appliance heating fuel input power (kW)
        """
        self.__f_as = get_appliance_system_factor(supply_situation, exhaust_situation) #Combustion appliance system factor (0 or 1)
        self.__f_ff = get_fuel_flow_factor(fuel_type, appliance_type) #Fuel flow factor (0-5)

    def calculate_air_flow_req_for_comb_appliance(self, f_op_comp, P_h_fi):
        """Calculate additional air flow rate required for the operation of
        combustion appliance q_v_comb.

        Arguments:
        f_op_comp --  Operation requirement signal (combustion appliance) (0 =  OFF ; 1 = ON)
        P_h_fi -- Combustion appliance heating fuel input power (kW)
        """
        if f_op_comp == 1:
            q_v_comb = 3.6 * f_op_comp * self.__f_as * self.__f_ff * P_h_fi #(35)
            q_v_in_through_comb = 0 #(37)
            q_v_out_through_comb = -q_v_comb # (38)
            #temp associated with q_v_out_through_comb is ventilation zone temperature Tz
        else:
            q_v_in_through_comb = 0
            q_v_out_through_comb = 0
            #TODO flue is considered as vertical passive duct, standard formulas in CIBSE guide.
        return q_v_in_through_comb, q_v_out_through_comb
    


class MechanicalVentilation:
    """ An object to represent Mechanical Ventilation """
    def __init__(
            self,
            sup_air_flw_ctrl,
            sup_air_temp_ctrl,
            Q_H_des,
            Q_C_des,
            vent_type,
            specific_fan_power,
            design_outdoor_air_flow_rate,
            simulation_time,
            energy_supply_conn,
            total_volume,
            altitude,
            ctrl_intermittent_MEV = None,
            mvhr_eff = 0.0,
            theta_ctrl_sys = None, #Only required if sup_air_temp_ctrl = LOAD_COM
            ):
        """Construct a Mechanical Ventilation object
        
        Arguments:
            sup_air_flw_ctrl -- supply air flow rate control
            sup_air_temp_ctrl --supply air temperature control
            Q_H_des -- deisgn zone heating need to be covered by the mechanical ventilation system
            Q_C_des -- deisgn zone cooling need to be covered by the mechanical ventilation system
            vent_type -- ventilation system type
            specific_fan_power -- in W / (litre / second), inclusive of any in use factors
            design_outdoor_air_flow_rate -- design outdoor air flow rate in m3/h
            simulation_time -- reference to Simulation time object
            energy_supply_conn -- Energy supply connection
            total_volume  -- Total zone volume (m3)
            altitude -- altitude of dwelling above sea level (m)
            ctrl_intermittent_MEV -- reference to Control objject with boolean schedule
                                    defining when the MechVent should be on.
            mvhr_eff -- MVHR efficiency
            theta_ctrl_sys -- Temperature variation based on control system (K)
        
        """
        # Hard coded variables
        self.__f_ctrl = 1 #From table B.4, for residential buildings, default f_ctrl = 1
        self.__f_sys = 1.1 #From table B.5, f_sys = 1.1
        self.__E_v = 1 #Section B.3.3.7 defaults E_v = 1 (this is the assumption for perfect mixing)
        self.theta_z_t = 0 #TODO get Thermal zone temperature - used for LOAD
        self.__sup_air_flw_ctrl = "ODA" #TODO currently hard coded until load comp implemented
        self.__sup_air_temp_ctrl = "NO_CTRL"#TODO currently hard coded until load comp implemented

        # Arguments
        self.__Q_H_des = Q_H_des
        self.__Q_C_des = Q_C_des
        self.__theta_ctrl_sys = theta_ctrl_sys
        self.__vent_type = vent_type
        self.vent_type = vent_type
        self.total_volume = total_volume
        self.__ctrl_intermittent_MEV = ctrl_intermittent_MEV
        self.__sfp = specific_fan_power
        self.__simtime = simulation_time
        self.__energy_supply_conn = energy_supply_conn
        self.__altitude = altitude
        self.design_outdoor_air_flow_rate_m3_h = design_outdoor_air_flow_rate # in m3/h
        self.__mvhr_eff = mvhr_eff

        # Calculated variables
        self.__qv_ODA_req_design = self.calculate_required_outdoor_air_flow_rate()
        self.__p_a_alt = adjust_air_density_for_altitude(altitude)

    def calculate_required_outdoor_air_flow_rate(self):
        """Calculate required outdoor ventilation air flow rates.
        Equation 9 from BS EN 16798-7."""
        # Required outdoor air flow rate in m3/h
        qv_ODA_req = ((self.__f_ctrl * self.__f_sys) / self.__E_v) * self.design_outdoor_air_flow_rate_m3_h
        return qv_ODA_req

    def calc_req_ODA_flow_rates_at_ATDs(self):
        """Calculate required outdoor air flow rates at the air terminal devices
        Equations 10-17 from BS EN 16798-7
        Adjusted to be based on ventilation type instead of vent_sys_op.
        """
        if self.__vent_type== "MVHR":
            qv_SUP_req = self.__qv_ODA_req_design
            qv_ETA_req = -self.__qv_ODA_req_design
            # NOTE: Calculation of effective flow rate of external air (in func
            # calc_mech_vent_air_flw_rates_req_to_supply_vent_zone) assumes that
            # supply and extract are perfectly balanced (as defined above), so
            # any future change to this assumption will need to be considered
            # with that in mind
        elif self.__vent_type == "Intermittent MEV" or self.__vent_type == 'Centralised continuous MEV' or self.__vent_type == 'Decentralised continuous MEV':
            qv_SUP_req = 0
            qv_ETA_req = -self.__qv_ODA_req_design
        elif self.__vent_type == "PIV":
            qv_SUP_req = self.__qv_ODA_req_design
            qv_ETA_req = 0
        else:
            sys.exit('Unrecognised ventilation system type')

        return qv_SUP_req, qv_ETA_req

    def __f_op_v(self):
        """ Returns the fraction of the timestep for which the ventilation is running """
        if self.__vent_type == "Intermittent MEV":
            f_op_V = self.__ctrl_intermittent_MEV.setpnt()
            if not 0 <= f_op_V <= 1:
                sys.exit('Error f_op_V is not between 0 and 1.')
        elif self.__vent_type in ("Decentralised continuous MEV", "Centralised continuous MEV", "MVHR"):
            #Assumed to operate continuously
            f_op_V = 1
        else:
            sys.exit('Unknown mechanical ventlation system type')
        return f_op_V

    def calc_mech_vent_air_flw_rates_req_to_supply_vent_zone(
            self,
            T_z,
            T_e,
            ):
        """Calculate the air flow rates to and from the ventilation zone required from mechanical ventilation.
        T_z -- thermal zone temperature (K)
        T_e -- external air temperature (K)
        """
        # Required air flow at air terminal devices
        qv_SUP_req, qv_ETA_req = self.calc_req_ODA_flow_rates_at_ATDs()

        # Amount of air flow depends on controls
        if self.__sup_air_flw_ctrl == "ODA":
            f_op_V = self.__f_op_v()

            # Based on Equation 18 and 19
            qv_SUP_dis_req = f_op_V * qv_SUP_req
            qv_ETA_dis_req = f_op_V * qv_ETA_req
        elif self.__sup_air_flw_ctrl == "LOAD":
            #TODO load not implementented
            Q_H_V_req = 10 #TODO get (Q_H_V_req) heat to be supplied to thermal zone by the ventilation system at current timestep.
            Q_C_V_req = 10 ##TODO get (Q_C_V_req) heat to be extracted from thermal zone by the ventilation system at current timestep.
            p_a = adjust_air_density_for_altitude(self.__altitude)
            theta_SUP_dis_out = 10 #TODO get supply air temperature from previous timestep.
            Q_H_V_emission_losses = Q_H_V_req * self.theta_ctrl_sys / (self.theta_z_t - self.theta_e_comb)
            Q_C_V_emission_losses = Q_C_V_req * self.theta_ctrl_sys / (self.theta_z_t - self.theta_e_comb)
            qv_SUP_dis_req = self.f_op_V * max(
                (Q_H_V_req + Q_H_V_emission_losses) / (p_a * c_a * (theta_SUP_dis_out - T_z + T_0_abs)),
                (Q_C_V_req + Q_C_V_emission_losses) / (p_a * c_a * (T_z - T_0_abs - theta_SUP_dis_out)),
                qv_SUP_req
                )
            qv_SUP_dis_max_des = max (
                self.Q_H_des / (p_a * c_a * (theta_SUP_dis_out - T_z + T_0_abs)),
                self.Q_C_des / (p_a * c_a * (T_z - T_0_abs - theta_SUP_dis_out)),
                self.qv_ODA_req_design
                )
            qv_SUP_dis_req = min(qv_SUP_dis_req, qv_SUP_dis_max_des)

            if self.vent_type == "MVHR":
                qv_ETA_dis_req = -qv_SUP_dis_req
            else:
                qv_ETA_dis_req = 0
        else:
            sys.exit('Unknown sup_air_flw_ctrl type')

        # Calculate effective flow rate of external air
        # NOTE: Technically, the MVHR system supplies air at a higher
        # temperature than the outside air. However, it is simpler to
        # account for the heat recovery effect using an "equivalent" or
        # "effective" flow rate of external air
        qv_effective_heat_recovery_saving = qv_SUP_dis_req * self.__mvhr_eff

        # Convert volume air flow rate to mass air flow rate
        qm_SUP_dis_req, qm_ETA_dis_req = convert_to_mass_air_flow_rate(
            qv_SUP_dis_req,
            qv_ETA_dis_req,
            T_e,
            T_z,
            self.__p_a_alt
        )
        qm_in_effective_heat_recovery_saving \
            = convert_volume_flow_rate_to_mass_flow_rate(
                qv_effective_heat_recovery_saving,
                T_e,
                self.__p_a_alt,
                )

        return qm_SUP_dis_req, qm_ETA_dis_req, qm_in_effective_heat_recovery_saving

    def fans(self, zone_volume, total_volume, throughput_factor=1.0):
        """ Calculate gains and energy use due to fans
        zone_volume -- volume of the zone (m3)
        total_volume -- volume of the dwelling (m3)
        vent_type -- one of "Intermittent MEV", "Centralised continuous MEV",
            "Decentralised continuous MEV", "MVHR" or "PIV".
        """
        # Calculate energy use by fans
        fan_power_W = (self.__sfp * (self.__qv_ODA_req_design / seconds_per_hour) * litres_per_cubic_metre)\
                      * (zone_volume / total_volume)
        fan_energy_use_kWh = (fan_power_W / W_per_kW) * self.__simtime.timestep() * self.__f_op_v()
        if self.__vent_type in ("Intermittent MEV", "Centralised continuous MEV", "Decentralised continuous MEV"):
            #Fan energy use = 0
            supply_fan_energy_use_kWh = 0.0
            extract_fan_energy_use_in_kWh = fan_energy_use_kWh
        elif self.__vent_type == 'MVHR':
            #Balanced, therefore split power between extract and supply fans
            supply_fan_energy_use_kWh = fan_energy_use_kWh / 2
            extract_fan_energy_use_in_kWh = fan_energy_use_kWh / 2
        elif self.__vent_type == 'PIV':
            #Positive input, supply fans only
            supply_fan_energy_use_kWh = fan_energy_use_kWh
            extract_fan_energy_use_in_kWh = 0
        else:
            sys.exit("Invalid ventilation type input.")
        self.__energy_supply_conn.demand_energy(supply_fan_energy_use_kWh)
        self.__energy_supply_conn.demand_energy(extract_fan_energy_use_in_kWh)

        return supply_fan_energy_use_kWh / (W_per_kW * self.__simtime.timestep())

class InfiltrationVentilation:
    """ A class to represent Infiltration and Ventilation object """
    def __init__(
            self,
            simulation_time,
            f_cross,
            shield_class,
            terrain_class,
            average_roof_pitch,
            windows,
            vents,
            leaks,
            combustion_appliances,
            ATDs,
            mech_vents,
            space_heating_ductworks,
            detailed_output_heating_cooling,
            altitude,
            total_volume,
            ventilation_zone_base_height,
            ):
        """
        Constructs a InfiltrationVentilation object

        Arguments:
            simulation_time -- reference to SimulationTime object
            f_cross -- cross-ventilation factor
            shield_class -- indicates the exposure to wind of an air flow path on a facade 
                (can can be open, normal and shielded)
            ventilation_zone_height -- height of ventilation zone (m)
            windows -- list of windows
            vents -- list of vents
            leaks -- required inputs for leaks
            ATDs -- list of air terminal devices
            mech_vents -- list of mech vents
            space_heating_ductworks -- list of ductworks
            altitude -- altitude of dwelling above sea level (m)
            total_volume -- total zone volume
            ventilation_zone_base_height -- base height of the ventilation zone (m)
        """
        self.__simulation_time = simulation_time
        self.__f_cross = f_cross
        self.__shield_class = shield_class
        self.__ventilation_zone_base_height = ventilation_zone_base_height
        self.ventilation_zone_height = leaks["ventilation_zone_height"]
        self.__C_rgh_site = ter_class_to_roughness_coeff(
            terrain_class, 
            ventilation_zone_base_height + self.ventilation_zone_height / 2,
            )
        self.__windows = []
        self.__vents = []
        self.__leaks = []
        self.__combustion_appliances = []
        self.__ATDs = []
        self.__mech_vents = mech_vents
        self.__space_heating_ductworks = space_heating_ductworks
        for window in windows.values():
            self.__windows.append(window)
        for vent in vents.values():
            self.__vents.append(vent)
        self.__leaks = self.make_leak_objects(leaks, average_roof_pitch, ventilation_zone_base_height)
        for combustion_appliance in combustion_appliances.values():
            self.__combustion_appliances.append(combustion_appliance)
        for ATD in ATDs.values():
            self.__ATDs.append(ATD)
        self.__detailed_output_heating_cooling = detailed_output_heating_cooling
        self.__ventilation_detailed_results = []
        self.__p_a_alt = adjust_air_density_for_altitude(altitude)
        self.total_volume = total_volume
  
    # def temp_supply(self):
    #     """ Calculate supply temperature of the air flow element """
    #     # NOTE: Technically, the MVHR system supplies air at a higher temperature
    #     # than the outside air, i.e.:
    #     #     temp_supply = self.__efficiency * temp_int_air \
    #     #                 + (1 - self.__efficiency) * self.__external_conditions.air_temp()
    #     # However, calculating this requires the internal air temperature, which
    #     # has not been calculated yet. Calculating this properly would require
    #     # the equation above to be added to the heat balance solver. Therefore,
    #     # it is simpler to adjust the heat transfer coefficient h_ve to account
    #     # for the heat recovery effect using an "equivalent" flow rate of
    #     # external air, which is done elsewhere
    #     return self.__external_conditions.air_temp()

    def mech_vents(self):
        """Return the list of mechanical ventilations."""
        return self.__mech_vents

    def space_heating_ductworks(self):
        """Return the list of ductworks."""
        return self.__space_heating_ductworks

    def calculate_total_volume_air_flow_rate_in(self, qm_in, external_air_density):
        """Calculate total volume air flow rate entering ventilation zone 
        Equation 68 from BS EN 16798-7"""
        return qm_in / external_air_density #from weather file?

    def calculate_total_volume_air_flow_rate_out(self, qm_out, zone_air_density):
        """Calculate total volume air flow rate leaving ventilation zone
        Equation 69 from BS EN 16798-7"""
        return qm_out / zone_air_density

    def make_leak_objects(self, leak, average_roof_pitch,ventilation_zone_base_height):
        """Distribute leaks around the dwelling according to Table B.12 from BS EN 16798-7.
        Create 5 leak objects:
            At 0.25*Height of the Ventilation Zone in the Windward facade
            At 0.25*Height of the Ventilation Zone in the Leeward facade
            At 0.75*Height of the Ventilation Zone in the Windward facade
            At 0.75*Height of the Ventilation Zone in the Leeward facade
            At the Height of the Ventilation Zone in the roof
        Arguments:
        leak - dict of leaks input data from JSON file
        average_roof_pitch - calculated in project.py, average pitch of all roof elements weighted by area (degrees)
        """
        h_path1_2 = 0.25 * leak["ventilation_zone_height"]
        h_path3_4 = 0.75 * leak["ventilation_zone_height"]
        h_path5 = leak["ventilation_zone_height"]
        h_path_list = [h_path1_2, h_path1_2, h_path3_4, h_path3_4, h_path5]

        if self.__f_cross:
            if average_roof_pitch < 10:
                roof_pitch = 'Roof10'
            elif average_roof_pitch <= 30:
                roof_pitch = 'Roof10_30'
            elif average_roof_pitch < 60:
                roof_pitch = 'Roof30'
        else:
            roof_pitch = 'Roof'

        facade_direction = ['Windward', 'Leeward', 'Windward', 'Leeward', roof_pitch]

        leaklist = []
        for i in range(0,5):
            leak_obj = Leaks(
                h_path_list[i],
                leak['test_pressure'],
                leak['test_result'],
                facade_direction[i],
                leak['area_roof'],
                leak['area_facades'],
                leak['env_area'],
                leak['altitude'],
                ventilation_zone_base_height,
            )
            leaklist.append(leak_obj)
        return leaklist

    def calculate_qv_pdu(self, qv_pdu, p_z_ref, T_z, T_e, h_z):
        """Implicit solver for qv_pdu"""
        return fsolve(self.implicit_formula_for_qv_pdu, qv_pdu, args = (p_z_ref, T_z, T_e, h_z)) #returns qv_pdu

    def implicit_formula_for_qv_pdu(self, qv_pdu, p_z_ref, T_z, T_e, h_z):
        """Implicit formula solving for qv_pdu as unknown.
        Equation 30 from BS EN 16798-7
        Arguments:
        qv_pdu -- volume flow rate from passive and hybrid ducts (m3/h)
        p_z_ref -- internal reference pressure (Pa)
        T_z -- thermal zone temperature (K)
        T_e -- external air temperature (K)
        h_z -- height of ventilation zone (m)
        """
        external_air_density = air_density_at_temp(T_e, self.__p_a_alt)
        zone_air_density = air_density_at_temp(T_z, self.__p_a_alt)

        #TODO Standard isn't clear if delta_p_ATD can be totalled or not. 
        delta_p_ATD_list = [atd.calculate_pressure_difference_atd(qv_pdu) for atd in self.__ATDs]
        delta_p_ATD = sum(delta_p_ATD_list)

        # Stack effect in passive and hybrid duct. As there is no air transfer 
        # between levels of the ventilation zone Equation B.1 is used.
        h_pdu_stack = h_z + 2

        #TODO include delta_p_dpu and delta_p_cowl in the return.
        return delta_p_ATD - p_z_ref - h_pdu_stack * g * (external_air_density - zone_air_density)

    def calculate_internal_reference_pressure(
                                            self,
                                            initial_p_z_ref_guess,
                                            wind_speed,
                                            wind_direction,
                                            temp_int_air,
                                            temp_ext_air,
                                            R_v_arg,
                                            R_w_arg = None,
                                            ):
        """The root scalar function will iterate until it finds a value of p_z_ref 
        that satisfies the mass balance equation.
        The root scalar solver allows a range of intervals to be entered. 
        The loop begins with a small interval to start with and if no solution is 
        found or the boundary is too small for to cause a sign change then a wider 
        interval is used until a solution is found.
        """
        interval_expansion_list = [1, 5, 10, 15, 20, 40, 50, 100, 200]
        for interval_expansion in interval_expansion_list:
            try:
                with warnings.catch_warnings():
                    warnings.filterwarnings('error',category=RuntimeWarning)
                    sol = root_scalar(
                        self.implicit_mass_balance_for_internal_reference_pressure,
                        args=(wind_speed, wind_direction, temp_int_air, temp_ext_air, R_v_arg, R_w_arg),
                        method='brentq',
                        bracket=[initial_p_z_ref_guess - interval_expansion, initial_p_z_ref_guess + interval_expansion],
                        )
                p_z_ref = sol.root
                return p_z_ref
            except ValueError as e:
                if str(e) == "f(a) and f(b) must have different signs":
                    continue
                # For other ValueError exceptions, re-raise
                raise
            except RuntimeWarning as e:
                continue
            except Exception as e:
                sys.exit("Mass balance solver failed: " +str(e))

    def implicit_mass_balance_for_internal_reference_pressure(
            self,
            p_z_ref,
            wind_speed,
            wind_direction,
            temp_int_air,
            temp_ext_air,
            R_v_arg,
            R_w_arg_min_max,
            flag = None,
            ):
        """Used in calculate_internal_reference_pressure function for p_z_ref solve"""
        qm_in, qm_out, _ = self.__implicit_mass_balance_for_internal_reference_pressure_components(
            p_z_ref,
            wind_speed,
            wind_direction,
            temp_int_air,
            temp_ext_air,
            R_v_arg,
            R_w_arg_min_max,
            flag,
            )
        return qm_in + qm_out

    def incoming_air_flow(
            self,
            p_z_ref,
            wind_speed,
            wind_direction,
            temp_int_air,
            temp_ext_air,
            R_v_arg,
            R_w_arg_min_max,
            reporting_flag = None,
            report_effective_flow_rate = False,
            ):
        """ Calculate incoming air flow, in m3/hr, at specified conditions """
        qm_in, _, qm_effective_flow_rate \
            = self.__implicit_mass_balance_for_internal_reference_pressure_components(
                p_z_ref,
                wind_speed,
                wind_direction,
                temp_int_air,
                temp_ext_air,
                R_v_arg,
                R_w_arg_min_max,
                reporting_flag,
                )
        if report_effective_flow_rate:
            qm_in -= qm_effective_flow_rate
        return convert_mass_flow_rate_to_volume_flow_rate(
            qm_in,
            Celcius2Kelvin(temp_ext_air),
            self.__p_a_alt,
            )

    def __implicit_mass_balance_for_internal_reference_pressure_components(
            self,
            p_z_ref,
            wind_speed,
            wind_direction,
            temp_int_air,
            temp_ext_air,
            R_v_arg,
            R_w_arg_min_max,
            reporting_flag = None,
            ):
        """Implicit mass balance for calculation of the internal reference pressure
        Equation 67 from BS EN 16798-7.

        Arguments:
        p_z_ref -- internal reference pressure (Pa)
        wind_speed -- wind speed, in m/s
        wind_direction -- direction wind is blowing from, in clockwise degrees from North
        temp_int_air -- temperature of air in the zone (Celsius)
        temp_ext_air -- temperature of external air (Celsius)
        reporting_flag -- flag used to give more detailed ventilation outputs (None = no additional reporting)

        Key Variables:
        qm_SUP_to_vent_zone - Supply air mass flow rate going to ventilation zone
        qm_ETA_from_vent_zone - Extract air mass flow rate from a ventilation zone
        qm_in_through_comb - Air mass flow rate entering through combustion appliances
        qm_out_through_comb - Air mass flow rate leaving through combustion appliances
        qm_in_through_passive_hybrid_ducts - Air mass flow rate entering through passive or hybrid duct
        qm_out_through_passive_hybrid_ducts - Air mass flow rate leaving through passive or hybrid duct
        qm_in_through_window_opening - Air mass flow rate entering through window opening
        qm_out_through_window_opening - Air mass flow rate leaving through window opening
        qm_in_through_vents - Air mass flow rate entering through vents (openings in the external envelope)
        qm_out_through_vents - Air mass flow rate leaving through vents (openings in the external envelope)
        qm_in_through_leaks - Air mass flow rate entering through envelope leakage
        qm_out_through_leaks - Air mass flow rate leaving through envelope leakage
        """
        u_site = wind_speed_at_zone_level(self.__C_rgh_site, wind_speed)
        T_e = Celcius2Kelvin(temp_ext_air)
        T_z = Celcius2Kelvin(temp_int_air)
        qm_in_through_window_opening = 0
        qm_out_through_window_opening = 0
        qm_in_through_vents = 0
        qm_out_through_vents = 0
        qm_in_through_leaks = 0
        qm_out_through_leaks = 0
        qm_in_through_comb = 0
        qm_out_through_comb = 0
        qm_in_through_passive_hybrid_ducts = 0
        qm_out_through_passive_hybrid_ducts = 0
        qm_SUP_to_vent_zone = 0
        qm_ETA_from_vent_zone = 0
        qm_in_effective_heat_recovery_saving_total = 0.0
        for window in self.__windows:
            qm_in, qm_out = window.calculate_flow_from_internal_p(wind_direction, u_site, T_e, T_z, p_z_ref, self.__f_cross, self.__shield_class, R_w_arg_min_max)
            qm_in_through_window_opening += qm_in
            qm_out_through_window_opening += qm_out
        for vent in self.__vents:
            qm_in, qm_out = vent.calculate_flow_from_internal_p(wind_direction, u_site, T_e, T_z, p_z_ref, self.__f_cross, self.__shield_class, R_v_arg)
            qm_in_through_vents += qm_in
            qm_out_through_vents += qm_out
        for leak in self.__leaks:
            qm_in, qm_out = leak.calculate_flow_from_internal_p(wind_direction, u_site, T_e, T_z, p_z_ref, self.__f_cross, self.__shield_class)
            qm_in_through_leaks += qm_in
            qm_out_through_leaks += qm_out
        for ATD in self.__ATDs:
            qv_pdu_initial = 0 #TODO get from prev timestep
            h_z = self.ventilation_zone_height
            qv_pdu = self.calculate_qv_pdu(qv_pdu_initial, p_z_ref, T_z, T_e, h_z)
            if qv_pdu >= 0:
                qv_pdu_in = qv_pdu
                qv_pdu_out = 0
            else:
                qv_pdu_in = 0
                qv_pdu_out = qv_pdu
            qm_in_through_phds, qm_out_through_phds = convert_to_mass_air_flow_rate(
                qv_pdu_in,
                qv_pdu_out,
                T_e,
                T_z,
                self.__p_a_alt
            )
            qm_in_through_passive_hybrid_ducts += qm_in_through_phds
            qm_out_through_passive_hybrid_ducts += qm_out_through_phds
        for combustion_appliance in self.__combustion_appliances:
            P_h_fi = 0 #TODO to work out from previous zone temperature? - Combustion appliance heating fuel input power
            f_op_comb = 1 #TODO work out what turns the appliance on or off. Schedule or Logic?
            qv_in, qv_out = combustion_appliance.calculate_air_flow_req_for_comb_appliance(f_op_comb, P_h_fi)
            qm_in_comb, qm_out_comb = convert_to_mass_air_flow_rate(
                qv_in,
                qv_out,
                T_e,
                T_z,
                self.__p_a_alt
            )
            qm_in_through_comb += qm_in_comb
            qm_out_through_comb += qm_out_comb
        for mech_vent in self.__mech_vents:
            qm_SUP, qm_ETA, qm_in_effective_heat_recovery_saving \
                = mech_vent.calc_mech_vent_air_flw_rates_req_to_supply_vent_zone(
                    T_z,
                    T_e,
                    )
            qm_SUP_to_vent_zone += qm_SUP
            qm_ETA_from_vent_zone += qm_ETA
            qm_in_effective_heat_recovery_saving_total += qm_in_effective_heat_recovery_saving

        # Calculate the total mass airflow rate in and out of the zones
        qm_in \
            = qm_in_through_window_opening \
            + qm_in_through_vents \
            + qm_in_through_leaks \
            + qm_in_through_comb \
            + qm_in_through_passive_hybrid_ducts \
            + qm_SUP_to_vent_zone
        qm_out \
            = qm_out_through_window_opening \
            + qm_out_through_vents \
            + qm_out_through_leaks \
            + qm_out_through_comb \
            + qm_out_through_passive_hybrid_ducts \
            + qm_ETA_from_vent_zone

        # Output detailed ventilation file
        if self.__detailed_output_heating_cooling:
            incoming_air_flow = convert_mass_flow_rate_to_volume_flow_rate(
                qm_in,
                T_e,
                self.__p_a_alt,
                )
            air_changes_per_hour = incoming_air_flow / self.total_volume

            if reporting_flag is not None:
                self.__ventilation_detailed_results.append(
                    [self.__simulation_time.index(), reporting_flag, R_v_arg,
                     incoming_air_flow, self.total_volume, air_changes_per_hour,
                     temp_int_air,p_z_ref,
                     qm_in_through_window_opening, qm_out_through_window_opening,
                     qm_in_through_vents, qm_out_through_vents,
                     qm_in_through_leaks, qm_out_through_leaks,
                     qm_in_through_comb, qm_out_through_comb,
                     qm_in_through_passive_hybrid_ducts, qm_out_through_passive_hybrid_ducts,
                     qm_SUP_to_vent_zone, qm_ETA_from_vent_zone, qm_in_effective_heat_recovery_saving_total,
                     qm_in , qm_out]
                    )

        return qm_in, qm_out, qm_in_effective_heat_recovery_saving_total

    def output_vent_results(self):
        """ Return the data dictionary containing detailed ventilation results"""
        return self.__ventilation_detailed_results

    def calc_air_changes_per_hour(
            self,
            wind_speed,
            wind_direction,
            temp_int_air,
            temp_ext_air,
            R_v_arg,
            R_w_arg,
            initial_p_z_ref_guess,
            reporting_flag=None,
            ):

        internal_reference_pressure = self.calculate_internal_reference_pressure(
            initial_p_z_ref_guess,
            wind_speed,
            wind_direction,
            temp_int_air,
            temp_ext_air,
            R_v_arg,
            R_w_arg,
        )

        incoming_air_flow = self.incoming_air_flow(
                                                internal_reference_pressure,
                                                wind_speed,
                                                wind_direction,
                                                temp_int_air,
                                                temp_ext_air,
                                                R_v_arg,
                                                R_w_arg,
                                                reporting_flag,
                                                report_effective_flow_rate = True,
                                                )
        air_changes_per_hour = incoming_air_flow / self.total_volume
        return air_changes_per_hour


    def calc_diff_ach_target(
            self,
            R_v_arg: float,
            wind_speed: float,
            wind_direction: float,
            temp_int_air: float,
            temp_ext_air: float,
            ach_target: float,
            R_w_arg: float,
            initial_p_z_ref_guess: float,
            reporting_flag=None,
            ) -> float:
        """
        Calculates the difference between the target air changes per hour (ACH) and the current ACH.

        Arguments:
            R_v_arg -- Current vent position, where 0 means vents are fully closed and 1 means vents are fully open.
            wind_speed -- Speed of the wind.
            wind_direction -- Direction of the wind.
            temp_int_air -- Interior air temperature.
            temp_ext_air -- Exterior air temperature.
            ach_target -- The desired target ACH value that needs to be achieved.
            R_w_arg -- Parameter related to the wind or building ventilation.
            initial_p_z_ref_guess --Initial guess for reference pressure.
            reporting_flag -- Flag indicating whether to report detailed output

        Returns:
            The adjusted absolute difference between the calculated ACH and the target ACH.
                   The difference is rounded to the 10th decimal place and a small gradient adjustment is applied
                   to help avoid numerical issues and local minima.
        """
        ach = self.calc_air_changes_per_hour(
                wind_speed,
                wind_direction,
                temp_int_air,
                temp_ext_air,
                R_v_arg,
                R_w_arg,
                initial_p_z_ref_guess,
                reporting_flag,
                )
        # To avoid the solver finding local minimums & numerically stagnating:
        # 1. The residuals of this function (ach- ach_target) are rounded to the 10th decimal place
        # 2. A very small gradient (1e-10 * R_v_arg) is added to the residuals to slightly 'tilt' 
        #    the surface of the function towards higher R_v_arg values. This is because it can be flat
        #    at low R_v_arg values when flow is dominated by other components.
        ach_diff_adjusted = round(abs(ach - ach_target),10) - (1e-10 * R_v_arg)
        return ach_diff_adjusted

    def find_R_v_arg_within_bounds(
            self,
            ach_min: float,
            ach_max: float,
            initial_R_v_arg: float,
            wind_speed: float,
            wind_direction: float,
            temp_int_air: float,
            temp_ext_air: float,
            R_w_arg: float,
            initial_p_z_ref_guess: float,
            reporting_flag,
            ) -> float:
        """
        Determines the optimal vent position (R_v_arg) to achieve a desired air 
        changes per hour (ACH) within specified bounds.

        Arguments:
            ach_min -- Minimum ACH limit.
            ach_max -- Maximum ACH limit.
            initial_R_v_arg -- Initial vent position, 0 = vents closed and 1 = vents fully open.
            wind_speed -- Speed of the wind.
            wind_direction -- Direction of the wind.
            temp_int_air -- Interior air temperature.
            temp_ext_air -- Exterior air temperature.
            R_w_arg -- Parameter related to the wind or building ventilation.
            initial_p_z_ref_guess -- Initial guess for reference pressure.
            reporting_flag -- Flag indicating whether to report detailed output.

        Returns:
            The optimal vent position (R_v_arg) that brings the ACH within the specified bounds.
        """
        # First, check if the vent position from previous timestep gives an ach within bounds
        initial_ach = self.calc_air_changes_per_hour(
                wind_speed,
                wind_direction,
                temp_int_air,
                temp_ext_air,
                initial_R_v_arg,
                R_w_arg,
                initial_p_z_ref_guess,
                reporting_flag,
                )
        
        # Determine if initial_ach is within the bounds
        if ach_min is not None and ach_max is not None:
            if ach_min > ach_max:
                sys.exit('ERROR: Max ach limit is below the min ach limit for vent opening.')
            if ach_min <= initial_ach <= ach_max:
                return initial_R_v_arg

        ach_target = None
        # Check extremes with fully open or closed vents
        if ach_min is not None and initial_ach < ach_min:
            # If initial ACH is less than ach_min, check ach with vents fully open
            ach_vent_open = self.calc_air_changes_per_hour(
                wind_speed,
                wind_direction,
                temp_int_air,
                temp_ext_air,
                1, # vents fully open
                R_w_arg,
                initial_p_z_ref_guess,
                reporting_flag,
                )
            if ach_vent_open < ach_min:
                # If the maximum achievable ACH with vents fully open is less than ach_min
                return 1.0

            # If current ACH is too low but ACH with vents fully open is higher than the threshold, set ach_target to ach_min
            ach_target = ach_min

        if ach_max is not None and initial_ach > ach_max:
            ach_vent_closed = self.calc_air_changes_per_hour(
                wind_speed,
                wind_direction,
                temp_int_air,
                temp_ext_air,
                0, # vents fully closed
                R_w_arg,
                initial_p_z_ref_guess,
                reporting_flag,
                )
            if ach_vent_closed > ach_max:
                # If the minimum achievable ACH with vents fully closed is less than ach_max
                return 0

            # If current ACH is too high but ACH with vents fully closed is lower than the threshold, set ach_target to ach_max
            ach_target = ach_max

        # If ach_target is still None, no need for further adjustment
        if ach_target is None:
            return initial_R_v_arg

        # With ach_target set to either ach_min or ach_max, run the minimize_scalar solver
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings('error', category=RuntimeWarning)
                result = minimize_scalar(
                    self.calc_diff_ach_target,
                    args=(wind_speed, wind_direction, temp_int_air, temp_ext_air,
                       ach_target, R_w_arg, initial_p_z_ref_guess, reporting_flag),
                    bounds=(0,1),
                    method='bounded',
                    options={'xatol': 1e-10},
                )
            R_v_arg_solution = max(0.0, min(1.0, result.x))

            return R_v_arg_solution

        except Exception as e:
            print('Vent opening ratio solver failed:' +str(e))

def create_infiltration_ventilation(
        infiltration_ventilation_dict: dict,
        zones_dict: dict,
        simtime: SimulationTime,    
        detailed_output_heating_cooling: bool,
        energy_supplies,
        controls,
):
    
    ventilation_zone_base_height = infiltration_ventilation_dict['ventilation_zone_base_height']

    windows_dict = {}
    for zone in zones_dict.values():
        for building_element_name, building_element in zone['BuildingElement'].items():
            if building_element['type'] == 'BuildingElementTransparent':
                # Check control for window open exists
                if building_element.get('Control_WindowOpenable') is None:
                    on_off_ctrl_obj = None
                else:
                    on_off_ctrl_obj = controls[building_element['Control_WindowOpenable']]
                windows_dict[building_element_name] = Window(
                    building_element['free_area_height'],
                    building_element['mid_height'],
                    building_element['max_window_open_area'],
                    building_element['window_part_list'],
                    building_element['orientation360'],
                    building_element['pitch'],
                    infiltration_ventilation_dict['altitude'],
                    on_off_ctrl_obj,
                    ventilation_zone_base_height,
                )

    pitches = []
    areas = []
    for zone in zones_dict.values():
        for building_element_name, building_element in zone['BuildingElement'].items():
            if building_element['type'] == 'BuildingElementOpaque':
                if BuildingElement.pitch_class(building_element['pitch']) == \
                        HeatFlowDirection.UPWARDS:
                    pitches.append(building_element['pitch'])
                    areas.append(building_element['area'])
    # Work out the average pitch, weighted by area.
    area_tot = sum(areas)
    if len(pitches) > 0:
        weighting = [x / area_tot for x in areas]
        weighted_pitches = list(map(lambda x, y: x * y, weighting, pitches))
        average_pitch = sum(weighted_pitches)
    else:
        # This case doesn't matter as if the area of roof = 0, the leakage coefficient = 0 anyway.
        average_pitch = 0

    surface_area_facades_list = []
    surface_area_roof_list = []
    for zone in zones_dict.values():
        for building_element_name, building_element in zone['BuildingElement'].items():
            # If wall
            if BuildingElement.pitch_class(building_element['pitch']) == \
                    HeatFlowDirection.HORIZONTAL:
                if building_element['type'] == 'BuildingElementOpaque':
                    surface_area_facades_list.append(building_element['area'])
                elif building_element['type'] == 'BuildingElementTransparent':
                    area = building_element['height'] * building_element['width']
                    surface_area_facades_list.append(area)
            # If roof:
            if BuildingElement.pitch_class(building_element['pitch']) == \
                    HeatFlowDirection.UPWARDS:
                if building_element['type'] == 'BuildingElementOpaque':
                    surface_area_roof_list.append(building_element['area'])
                elif building_element['type'] == 'BuildingElementTransparent':
                    area = building_element['height'] * building_element['width']
                    surface_area_roof_list.append(area)

    surface_area_facades = sum(surface_area_facades_list)
    surface_area_roof = sum(surface_area_roof_list)

    # Loop trough zones to sum up volume to avoid infiltration redundant input.
    total_volume = 0
    for zones, zone_data in zones_dict.items():
        total_volume += zone_data['volume']

    vents_dict = {}
    for vent_name, vent_data in infiltration_ventilation_dict['Vents'].items():
        vents_dict[vent_name] = Vent(
            vent_data['mid_height_air_flow_path'],
            vent_data['area_cm2'],
            vent_data['pressure_difference_ref'],
            vent_data['orientation360'],
            vent_data['pitch'],
            infiltration_ventilation_dict['altitude'],
            ventilation_zone_base_height,
        )

    leaks_dict = infiltration_ventilation_dict['Leaks']
    leaks_dict['area_facades'] = surface_area_facades
    leaks_dict['area_roof'] = surface_area_roof
    leaks_dict['altitude'] = infiltration_ventilation_dict['altitude']

    combustion_appliances_dict = {}
    # Handle case where CombustionAppliances might be missing or empty
    if infiltration_ventilation_dict.get('CombustionAppliances'):
        for combustion_appliances_name, combustion_appliances_data in infiltration_ventilation_dict[
            'CombustionAppliances'].items():
            combustion_appliances_dict[combustion_appliances_name] = CombustionAppliances(
                combustion_appliances_data['supply_situation'],
                combustion_appliances_data['exhaust_situation'],
                combustion_appliances_data['fuel_type'],
                combustion_appliances_data['appliance_type'],
            )
    # Empty dictionary for air terminal devices until passive ducts work
    atds_dict = {}
    # if infiltration_ventilation.get('AirTerminalDevices') is not None:
    #     for atd_name, atds_data in infiltration_ventilation['AirTerminalDevices'].items():
    #         atds_dict[atd_name] = AirTerminalDevices(
    #         atds_data['area_cm2'],
    #         atds_data['pressure_difference_ref'],
    #         )

    mech_vents_dict = {}
    space_heating_ductwork_dict = {}
    # Check if Mechanical Ventilation exists
    if infiltration_ventilation_dict.get('MechanicalVentilation') is not None:
        for mech_vents_name, mech_vents_data in infiltration_ventilation_dict['MechanicalVentilation'].items():
            # Assign the appropriate control object
            if mech_vents_data.get('Control') is not None:
                ctrl_intermittent_MEV = controls[mech_vents_data['Control']]
            else:
                ctrl_intermittent_MEV = None

            energy_supply = energy_supplies[mech_vents_data['EnergySupply']]
            # TODO Need to handle error if EnergySupply name is invalid.
            energy_supply_conn = energy_supply.connection(mech_vents_name)

            if mech_vents_data['vent_type'] == 'MVHR':
                mech_vents_dict[mech_vents_name] = MechanicalVentilation(
                    mech_vents_data['sup_air_flw_ctrl'],
                    mech_vents_data['sup_air_temp_ctrl'],
                    0,  # mech_vents_data['design_zone_cooling_covered_by_mech_vent'],
                    0,  # mech_vents_data['design_zone_heating_covered_by_mech_vent'],
                    mech_vents_data['vent_type'],
                    mech_vents_data['SFP'],
                    mech_vents_data['design_outdoor_air_flow_rate'],
                    simtime,
                    energy_supply_conn,
                    total_volume,
                    infiltration_ventilation_dict['altitude'],
                    ctrl_intermittent_MEV=ctrl_intermittent_MEV,
                    mvhr_eff=mech_vents_data['mvhr_eff'],
                )
            elif mech_vents_data['vent_type'] in (
            "Intermittent MEV", "Centralised continuous MEV", "Decentralised continuous MEV"):
                mech_vents_dict[mech_vents_name] = MechanicalVentilation(
                    mech_vents_data['sup_air_flw_ctrl'],
                    mech_vents_data['sup_air_temp_ctrl'],
                    0,  # mech_vents_data['design_zone_cooling_covered_by_mech_vent'],
                    0,  # mech_vents_data['design_zone_heating_covered_by_mech_vent'],
                    mech_vents_data['vent_type'],
                    mech_vents_data['SFP'],
                    mech_vents_data['design_outdoor_air_flow_rate'],
                    simtime,
                    energy_supply_conn,
                    total_volume,
                    infiltration_ventilation_dict['altitude'],
                    ctrl_intermittent_MEV,
                )
            else:
                sys.exit("Mechanical ventilation type not recognised")

            # TODO not all dwellings have mech vents - update to make mech vents optional
            if mech_vents_data['vent_type'] == "MVHR":
                if mech_vents_name not in space_heating_ductwork_dict:
                    space_heating_ductwork_dict[mech_vents_name] = []
                for ductwork_data in mech_vents_data["ductwork"]:
                    if ductwork_data['cross_section_shape'] == 'circular':
                        duct_perimeter = None
                        internal_diameter = ductwork_data['internal_diameter_mm'] / mm_per_m
                        external_diameter = ductwork_data['external_diameter_mm'] / mm_per_m
                    elif ductwork_data['cross_section_shape'] == 'rectangular':
                        duct_perimeter = ductwork_data['duct_perimeter_mm'] / mm_per_m
                        internal_diameter = None
                        external_diameter = None
                    else:
                        sys.exit("Duct shape not valid")

                    ductwork = Ductwork(
                        ductwork_data['cross_section_shape'],
                        duct_perimeter,
                        internal_diameter,
                        external_diameter,
                        ductwork_data['length'],
                        ductwork_data['insulation_thermal_conductivity'],
                        ductwork_data['insulation_thickness_mm'] / mm_per_m,
                        ductwork_data['reflective'],
                        ductwork_data['duct_type'],
                        mech_vents_data['mvhr_location'],
                        mech_vents_data['mvhr_eff'],
                    )
                    space_heating_ductwork_dict[mech_vents_name].append(ductwork)

    return InfiltrationVentilation(
        simtime,
        infiltration_ventilation_dict['cross_vent_possible'],
        infiltration_ventilation_dict['shield_class'],
        infiltration_ventilation_dict['terrain_class'],
        average_pitch,
        windows_dict,
        vents_dict,
        leaks_dict,
        combustion_appliances_dict,
        atds_dict,
        mech_vents_dict.values(),
        space_heating_ductwork_dict.values(),
        detailed_output_heating_cooling,
        infiltration_ventilation_dict['altitude'],
        total_volume,
        ventilation_zone_base_height,
    )
