
.. _creating_a_minimum_input_file_part_2_HEM_v0.36_FHS_v0.27:

2. Creating a minimum Input File: Part 2
========================================

Overview
--------

This tutorial creates a HEM minimum input file which runs a full 12-month HEM calculation.

A minimum input file is the smallest input file possible which is valid and will run a simulation without an errors occuring.

This tutorial provides:

* The JSON for a HEM minimum input file.
* The Python code used to create the HEM minimum input file.

Method
------

This was done by taking the 'demo.json' example file provided in the official HEM respository and then removing or editing items.

* If an item was removed and an error occured when running a simulation,  then the item was placed back in the input file.
* If the value of an item was set to zero and an error occurred when running a simulation, then the value was set to a non-zero value.

Points to note
--------------

* This minimum input file takes around 10 seconds to run a 12-month simulation.
* It doesn't seem to be possible to use schedules for defining some hourly input values such as the ColdWaterSource temperatures. Instead a 8,760-item Python list was created using ``[0] * 8760`` or similar.
* Some inputs are required even if they are not used, such as the Event 'Other' item or the HotWaterDemand 'Distribution' item.
* The HotWaterSource 'hw cylinder' item is required, even if there is no hot water cylinder present in the dwelling.

The HEM minimum input JSON
--------------------------

This input file represents a dwelling with a single wall, no ventilation, no hot water demand, no internal gains, no appliance gains and no solar gains through windows.

.. code-block:: JSON
   :caption: The HEM minimum input file as a JSON file.

   {
      "ApplianceGains": {},
      "ColdWaterSource": {
         "MAINS_WATER": {
               "start_day": 0,
               "temperatures": [
                  0,
                  0,
                  0,
                  "... [extra rows deleted here] ...",
                  0,
                  0,
                  0
               ],
               "time_series_step": 1
         }
      },
      "Control": {
         "HW_SETPOINT_TEMP_MAX": {
               "type": "SetpointTimeControl",
               "start_day": 0,
               "time_series_step": 1,
               "schedule": {
                  "main": [
                     {
                           "value": 55,
                           "repeat": 8760
                     }
                  ]
               }
         },
         "HEATING_SETPOINT_TEMP": {
               "type": "SetpointTimeControl",
               "start_day": 0,
               "time_series_step": 1,
               "schedule": {
                  "main": [
                     {
                           "value": 21,
                           "repeat": 8760
                     }
                  ]
               }
         },
         "HW_SETPOINT_TEMP_MIN": {
               "type": "SetpointTimeControl",
               "start_day": 0,
               "time_series_step": 1,
               "schedule": {
                  "main": [
                     {
                           "value": 45,
                           "repeat": 8760
                     }
                  ]
               }
         }
      },
      "EnergySupply": {
         "MAINS_ELEC": {
               "fuel": "electricity",
               "is_export_capable": true
         }
      },
      "Events": {
         "Other": {
               "OTHER": [
                  {
                     "start": 1,
                     "duration": 8760,
                     "temperature": 0
                  }
               ]
         }
      },
      "ExternalConditions": {
         "shading_segments": [
               {
                  "start360": 0,
                  "end360": 360
               }
         ]
      },
      "HotWaterDemand": {
         "Distribution": []
      },
      "HotWaterSource": {
         "hw cylinder": {
               "type": "StorageTank",
               "volume": 0.001,
               "daily_losses": 0,
               "init_temp": 55,
               "ColdWaterSource": "MAINS_WATER",
               "HeatSource": {
                  "IMMERSION": {
                     "type": "ImmersionHeater",
                     "power": 3,
                     "EnergySupply": "MAINS_ELEC",
                     "Controlmin": "HW_SETPOINT_TEMP_MIN",
                     "Controlmax": "HW_SETPOINT_TEMP_MAX",
                     "heater_position": 0.1,
                     "thermostat_position": 0.33
                  }
               }
         }
      },
      "InternalGains": {},
      "InfiltrationVentilation": {
         "cross_vent_possible": true,
         "shield_class": "Normal",
         "terrain_class": "OpenField",
         "ventilation_zone_base_height": 2.5,
         "altitude": 30,
         "Vents": {},
         "Leaks": {
               "ventilation_zone_height": 0,
               "test_pressure": 50,
               "test_result": 0,
               "env_area": 0
         }
      },
      "SimulationTime": {
         "start": 0,
         "end": 8760,
         "step": 1
      },
      "SpaceHeatSystem": {
         "MAIN_HEATING": {
               "type": "InstantElecHeater",
               "rated_power": 6.0,
               "frac_convective": 0.4,
               "Control": "HEATING_SETPOINT_TEMP",
               "EnergySupply": "MAINS_ELEC"
         }
      },
      "Zone": {
         "ZONE_1": {
               "SpaceHeatSystem": "MAIN_HEATING",
               "area": 80,
               "volume": 250,
               "temp_setpnt_init": 21,
               "BuildingElement": {
                  "WALL_0": {
                     "type": "BuildingElementOpaque",
                     "solar_absorption_coeff": 0.6,
                     "thermal_resistance_construction": 0.7,
                     "areal_heat_capacity": 19000,
                     "mass_distribution_class": "IE",
                     "pitch": 90,
                     "orientation360": 90,
                     "base_height": 0,
                     "height": 2.5,
                     "width": 10,
                     "area": 20
                  }
               },
               "ThermalBridging": {}
         }
      },
      "temp_internal_air_static_calcs": 0
   }



Python code
-----------

.. code-block:: python
   :caption: Python code to create the minimum HEM input file as above

   # This creates a minimum HEM input file from scratch.
   # - `in_dict` is a dictionary representing the Input (root) JSON object.
   # - CAPITALS are used for any user-defined names.

   import json
   in_dict = {}

   # ApplianceGains
   in_dict['ApplianceGains'] = {}

   # ColdWaterSource
   in_dict['ColdWaterSource'] = {}
   in_dict['ColdWaterSource']['MAINS_WATER'] = {}
   in_dict['ColdWaterSource']['MAINS_WATER']['start_day'] = 0
   in_dict['ColdWaterSource']['MAINS_WATER']['temperatures'] = [0] * 8760
   in_dict['ColdWaterSource']['MAINS_WATER']['time_series_step'] = 1

   # Control
   in_dict['Control'] = {}
   in_dict['Control']['HW_SETPOINT_TEMP_MAX'] = {}
   in_dict['Control']['HW_SETPOINT_TEMP_MAX']['type'] = 'SetpointTimeControl'
   in_dict['Control']['HW_SETPOINT_TEMP_MAX']['start_day'] = 0
   in_dict['Control']['HW_SETPOINT_TEMP_MAX']['time_series_step'] = 1
   in_dict['Control']['HW_SETPOINT_TEMP_MAX']['schedule'] = {}
   in_dict['Control']['HW_SETPOINT_TEMP_MAX']['schedule']['main'] = [{'value': 55, 'repeat': 8760}]
   in_dict['Control']['HEATING_SETPOINT_TEMP'] = {}
   in_dict['Control']['HEATING_SETPOINT_TEMP']['type'] = 'SetpointTimeControl'
   in_dict['Control']['HEATING_SETPOINT_TEMP']['start_day'] = 0
   in_dict['Control']['HEATING_SETPOINT_TEMP']['time_series_step'] = 1
   in_dict['Control']['HEATING_SETPOINT_TEMP']['schedule'] = {}
   in_dict['Control']['HEATING_SETPOINT_TEMP']['schedule']['main'] = [{'value': 21, 'repeat': 8760}]
   in_dict['Control']['HW_SETPOINT_TEMP_MIN'] = {}
   in_dict['Control']['HW_SETPOINT_TEMP_MIN']['type'] = 'SetpointTimeControl'
   in_dict['Control']['HW_SETPOINT_TEMP_MIN']['start_day'] = 0
   in_dict['Control']['HW_SETPOINT_TEMP_MIN']['time_series_step'] = 1
   in_dict['Control']['HW_SETPOINT_TEMP_MIN']['schedule'] = {}
   in_dict['Control']['HW_SETPOINT_TEMP_MIN']['schedule']['main'] = [{'value': 45, 'repeat': 8760}]

   # EnergySupply
   in_dict['EnergySupply'] = {}
   in_dict['EnergySupply']['MAINS_ELEC'] = {}
   in_dict['EnergySupply']['MAINS_ELEC']['fuel'] = 'electricity'
   in_dict['EnergySupply']['MAINS_ELEC']['is_export_capable'] = True

   # Events
   in_dict['Events'] = {}
   in_dict['Events']['Other'] = {}
   in_dict['Events']['Other']['OTHER'] = [{'start': 1, 'duration': 8760, 'temperature': 0}]

   # ExternalConditions
   in_dict['ExternalConditions'] = {}
   in_dict['ExternalConditions']['shading_segments'] = []
   in_dict['ExternalConditions']['shading_segments'].append({'start360': 0, 'end360': 360})

   # HotWaterDemand
   in_dict['HotWaterDemand'] = {}
   in_dict['HotWaterDemand']['Distribution'] = []

   # HotWaterSource
   in_dict['HotWaterSource'] = {}
   in_dict['HotWaterSource']['hw cylinder'] = {}
   in_dict['HotWaterSource']['hw cylinder']['type'] = 'StorageTank'
   in_dict['HotWaterSource']['hw cylinder']['volume'] = 0.001
   in_dict['HotWaterSource']['hw cylinder']['daily_losses'] = 0
   in_dict['HotWaterSource']['hw cylinder']['init_temp'] = 55
   in_dict['HotWaterSource']['hw cylinder']['ColdWaterSource'] = "MAINS_WATER"
   in_dict['HotWaterSource']['hw cylinder']['HeatSource'] = {}
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION'] = {}
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['type'] = 'ImmersionHeater'
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['power'] = 3
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['EnergySupply'] = 'MAINS_ELEC'
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['Controlmin'] = 'HW_SETPOINT_TEMP_MIN'
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['Controlmax'] = 'HW_SETPOINT_TEMP_MAX'
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['heater_position'] = 0.1
   in_dict['HotWaterSource']['hw cylinder']['HeatSource']['IMMERSION']['thermostat_position'] = 0.33

   # InternalGains
   in_dict['InternalGains'] = {}

   # InfiltrationVentilation
   in_dict['InfiltrationVentilation'] = {}
   in_dict['InfiltrationVentilation']['cross_vent_possible'] = True
   in_dict['InfiltrationVentilation']['shield_class'] = 'Normal'
   in_dict['InfiltrationVentilation']['terrain_class'] = 'OpenField'
   in_dict['InfiltrationVentilation']['ventilation_zone_base_height'] = 2.5
   in_dict['InfiltrationVentilation']['altitude'] = 30
   in_dict['InfiltrationVentilation']['Vents'] = {}
   in_dict['InfiltrationVentilation']['Leaks'] = {}
   in_dict['InfiltrationVentilation']['Leaks']['ventilation_zone_height'] = 0
   in_dict['InfiltrationVentilation']['Leaks']['test_pressure'] = 50
   in_dict['InfiltrationVentilation']['Leaks']['test_result'] = 0
   in_dict['InfiltrationVentilation']['Leaks']['env_area'] = 0

   # SimulationTime
   in_dict['SimulationTime'] = {}
   in_dict['SimulationTime']['start'] = 0
   in_dict['SimulationTime']['end'] = 8760
   in_dict['SimulationTime']['step'] = 1

   # SpaceHeatSystem
   in_dict['SpaceHeatSystem'] = {}
   in_dict['SpaceHeatSystem']['MAIN_HEATING'] = {}
   in_dict['SpaceHeatSystem']['MAIN_HEATING']['type'] = 'InstantElecHeater'
   in_dict['SpaceHeatSystem']['MAIN_HEATING']['rated_power'] = 6.0
   in_dict['SpaceHeatSystem']['MAIN_HEATING']['frac_convective'] = 0.4
   in_dict['SpaceHeatSystem']['MAIN_HEATING']['Control'] = 'HEATING_SETPOINT_TEMP'
   in_dict['SpaceHeatSystem']['MAIN_HEATING']['EnergySupply'] = 'MAINS_ELEC'

   # Zone
   in_dict['Zone'] = {}
   in_dict['Zone']['ZONE_1'] = {}
   in_dict['Zone']['ZONE_1']['SpaceHeatSystem'] = 'MAIN_HEATING'
   in_dict['Zone']['ZONE_1']['area'] = 80
   in_dict['Zone']['ZONE_1']['volume'] = 250
   in_dict['Zone']['ZONE_1']['temp_setpnt_init'] = 21
   in_dict['Zone']['ZONE_1']['BuildingElement'] = {}
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0'] = {}
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['type'] = 'BuildingElementOpaque'
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['solar_absorption_coeff'] = 0.6
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['thermal_resistance_construction'] = 0.7
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['areal_heat_capacity'] = 19000
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['mass_distribution_class'] = 'IE'
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['pitch'] = 90
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['orientation360'] = 90
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['base_height'] = 0
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['height'] = 2.5
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['width'] = 10
   in_dict['Zone']['ZONE_1']['BuildingElement']['WALL_0']['area'] = 20
   in_dict['Zone']['ZONE_1']['ThermalBridging'] = {}

   # temp_internal_air_static_calcs
   in_dict['temp_internal_air_static_calcs'] = 0

   # --- save file ---
   fp_in = 'in_temp.json'
   with open(fp_in, 'w') as f:
      json.dump(in_dict, f, indent = 4)











Conclusions
-----------

* We can create a minimum input file which passes the HEM schema validation and which runs a full 12-month HEM calculaton. 
* This minimum input file provides a template or foundation which can be used to construct more complex input files.

