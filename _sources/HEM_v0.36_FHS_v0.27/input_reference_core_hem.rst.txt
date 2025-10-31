
.. _input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Input Reference - core HEM
==========================

* This is the schema for input files to the core HEM engine.
* The text below has been automatically generated from `core-input.json <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/schemas/core-input.json>`__.
* The root object is the first JSON object below named "Input".

.. _input_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Input
-----

<JSON object>

* Named name/value pairs:

  * ``ApplianceGains``: :ref:`appliancegains_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control`` **(required)**: :ref:`control_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Events`` **(required)**: :ref:`waterheatingevents_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ExternalConditions`` **(required)**: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSourceWet``: :ref:`heatsourcewet_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HotWaterDemand`` **(required)**: :ref:`hotwaterdemand_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HotWaterSource`` **(required)**: :ref:`hotwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``InfiltrationVentilation`` **(required)**: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``InternalGains`` **(required)**: :ref:`internalgains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``OnSiteGeneration``: :ref:`onsitegeneration_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``PreHeatedWaterSource``: :ref:`preheatedwatersource_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SimulationTime`` **(required)**: :ref:`simulationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SmartApplianceControls``: :ref:`smartappliancecontrols_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SpaceCoolSystem``: :ref:`spacecoolsystem_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SpaceHeatSystem``: :ref:`spaceheatsystem_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``WWHRS``: :ref:`wwhrs_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Zone`` **(required)**: :ref:`zone_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_internal_air_static_calcs`` **(required)**: :ref:`temp_internal_air_static_calcs_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _appliancegains_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ApplianceGains collection
-------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _coldwatersource_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ColdWaterSource collection
--------------------------

<JSON object>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs:  {ANY_NAME: :ref:`coldwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}

.. _control_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control collection
------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control choice
--------------

<JSON value>

* Parent: :ref:`control_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* OneOf:

  * :ref:`controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`controlcombinationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'ChargeControl': '#/$defs/ControlChargeTarget', 'CombinationTimeControl': '#/$defs/ControlCombinationTime', 'OnOffCostMinimisingTimeControl': '#/$defs/ControlOnOffCostMinimising', 'OnOffTimeControl': '#/$defs/ControlOnOffTimer', 'SetpointTimeControl': '#/$defs/ControlSetpointTimer'}, 'propertyName': 'type'}

.. _energysupply_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EnergySupply collection
-----------------------

<JSON object>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs:  {ANY_NAME: :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}

.. _heatsourcewet_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWet collection
------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`heatsourcewet_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _heatsourcewet_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWet choice
--------------------

<JSON value>

* Parent: :ref:`heatsourcewet_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* OneOf:

  * :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'Boiler': '#/$defs/HeatSourceWetBoiler', 'HIU': '#/$defs/HeatSourceWetHIU', 'HeatBattery': '#/$defs/HeatSourceWetHeatBattery', 'HeatPump': '#/$defs/HeatSourceWetHeatPump'}, 'propertyName': 'type'}

.. _onsitegeneration_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

OnSiteGeneration collection
---------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`onsitegeneration_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _onsitegeneration_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

OnSiteGeneration choice
-----------------------

<JSON value>

* Parent: :ref:`onsitegeneration_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* OneOf:

  * :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'PhotovoltaicSystem': '#/$defs/PhotovoltaicSystem'}, 'propertyName': 'type'}

.. _preheatedwatersource_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

PreHeatedWaterSource collection
-------------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _smartappliancecontrols_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SmartApplianceControls collection
---------------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _spacecoolsystem_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceCoolSystem collection
--------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`spacecoolsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _spacecoolsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceCoolSystem choice
----------------------

<JSON value>

* Parent: :ref:`spacecoolsystem_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* OneOf:

  * :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'AirConditioning': '#/$defs/SpaceCoolSystemAirConditioning'}, 'propertyName': 'type'}

.. _spaceheatsystem_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystem collection
--------------------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`spaceheatsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _spaceheatsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystem choice
----------------------

<JSON value>

* Parent: :ref:`spaceheatsystem_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* OneOf:

  * :ref:`spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`spaceheatsystemwarmair_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'ElecStorageHeater': '#/$defs/SpaceHeatSystemElectricStorageHeater', 'InstantElecHeater': '#/$defs/SpaceHeatSystemInstantElectricHeater', 'WarmAir': '#/$defs/SpaceHeatSystemWarmAir', 'WetDistribution': '#/$defs/SpaceHeatSystemWetDistribution'}, 'propertyName': 'type'}

.. _wwhrs_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WWHRS collection
----------------

<JSON value>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _zone_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Zone collection
---------------

<JSON object>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs:  {ANY_NAME: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}

.. _temp_internal_air_static_calcs_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Internal Air Static Calcs
------------------------------

<JSON number>

* Parent: :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _airflowtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

AirFlowType
-----------

<JSON string>

* Parent(s): :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['fan-assisted', 'damper-only']

.. _appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ApplianceGains
--------------

<JSON object>

* Parent(s): :ref:`appliancegains_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Events``: :ref:`events_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Standby``: :ref:`standby_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``gains_fraction`` **(required)**: :ref:`gains_fraction_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``loadshifting``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``priority``: :ref:`priority_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``schedule``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``start_day`` **(required)**: :ref:`start_day_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _events_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Events
------

<JSON value>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of appliance usage events

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`appliancegainsevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _standby_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Standby
-------

<JSON value>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Appliance power consumption when not in use (unit: W)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _energysupply_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _gains_fraction_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Gains Fraction
--------------

<JSON number>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Proportion of appliance demand turned into heat gains (no unit)

.. _priority_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Priority
--------

<JSON value>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON integer>
    
    
  * <JSON null>

.. _start_day_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

* Description: First day of the time series, day of the year, 0 to 365

.. _time_series_step_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Timestep of the time series data (unit: hours)

.. _appliancegainsevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ApplianceGainsEvent
-------------------

<JSON object>

* Parent(s): :ref:`events_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``demand_W`` **(required)**: :ref:`demand_w_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``duration`` **(required)**: :ref:`duration_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start`` **(required)**: :ref:`start_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _demand_w_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Demand W
--------

<JSON number>

* Parent: :ref:`appliancegainsevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _duration_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Duration
--------

<JSON number>

* Parent: :ref:`appliancegainsevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _start_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start
-----

<JSON number>

* Parent: :ref:`appliancegainsevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ApplianceLoadShifting
---------------------

<JSON object>

* Parent(s): :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Control``: :ref:`control_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``demand_limit_weighted`` **(required)**: :ref:`demand_limit_weighted_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_shift_hrs`` **(required)**: :ref:`max_shift_hrs_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``priority``: :ref:`priority_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``weight_timeseries`` **(required)**: :ref:`weight_timeseries_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _control_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON value>

* Parent: :ref:`applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _demand_limit_weighted_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Demand Limit Weighted
---------------------

<JSON number>

* Parent: :ref:`applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _max_shift_hrs_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Shift Hrs
-------------

<JSON number>

* Parent: :ref:`applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _priority_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Priority
--------

<JSON value>

* Parent: :ref:`applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON integer>
    
    
  * <JSON null>

.. _weight_timeseries_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Weight Timeseries
-----------------

<JSON array>

* Parent: :ref:`applianceloadshifting_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON number>



.. _bath_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Bath
----

<JSON object>

* Parent(s): :ref:`bath_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``flowrate`` **(required)**: :ref:`flowrate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``size`` **(required)**: :ref:`size_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _coldwatersource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`bath_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _flowrate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Flowrate
--------

<JSON number>

* Parent: :ref:`bath_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tap/outlet flow rate (unit: litre/minute)

.. _size_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Size
----

<JSON number>

* Parent: :ref:`bath_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Volume held by bath (unit: litre)

.. _batterylocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BatteryLocation
---------------

<JSON string>

* Parent(s): :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['inside', 'outside']

.. _boilercostschedulehybrid_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BoilerCostScheduleHybrid
------------------------

<JSON object>

* Parent(s): :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``cost_schedule_boiler`` **(required)**: :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cost_schedule_hp`` **(required)**: :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cost_schedule_start_day`` **(required)**: :ref:`cost_schedule_start_day_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cost_schedule_time_series_step`` **(required)**: :ref:`cost_schedule_time_series_step_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _cost_schedule_start_day_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Cost Schedule Start Day
-----------------------

<JSON integer>

* Parent: :ref:`boilercostschedulehybrid_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

.. _cost_schedule_time_series_step_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Cost Schedule Time Series Step
------------------------------

<JSON number>

* Parent: :ref:`boilercostschedulehybrid_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _boilerhotwatertest_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BoilerHotWaterTest
------------------

<JSON string>

* Parent(s): :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['M&L', 'M&S', 'M_only', 'No_additional_tests']

.. _buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementAdjacentConditionedSpace
---------------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_construction``: :ref:`thermal_resistance_construction_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value``: :ref:`u_value_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementAdjacentConditionedSpace'

.. _area_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _areal_heat_capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity (unit: J/m².K)

.. _pitch_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thermal_resistance_construction_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Construction
-------------------------------

<JSON value>

* Parent: :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance (unit: m².K/W)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _u_value_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON value>

* Parent: :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementAdjacentUnconditionedSpace_Simple
------------------------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_construction``: :ref:`thermal_resistance_construction_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_unconditioned_space`` **(required)**: :ref:`thermal_resistance_unconditioned_space_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value``: :ref:`u_value_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementAdjacentUnconditionedSpace_Simple'

.. _area_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of this building element (unit: m²)

.. _areal_heat_capacity_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity (unit: J/m2.K)

.. _pitch_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thermal_resistance_construction_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Construction
-------------------------------

<JSON value>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance (unit: m2.K/W)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _thermal_resistance_unconditioned_space_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Unconditioned Space
--------------------------------------

<JSON number>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Effective thermal resistance of unheated space (unit: m².K/W)

.. _u_value_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON value>

* Parent: :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementGroundHeatedBasement
-----------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Heated basement - uses init_heated_basement()

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``total_area`` **(required)**: :ref:`total_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``perimeter`` **(required)**: :ref:`perimeter_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_floor_construction`` **(required)**: :ref:`thermal_resistance_floor_construction_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value`` **(required)**: :ref:`u_value_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``psi_wall_floor_junc`` **(required)**: :ref:`psi_wall_floor_junc_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thickness_walls`` **(required)**: :ref:`thickness_walls_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_upper_surface``: :ref:`height_upper_surface_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shield_fact_location``: 

    * <JSON value>
      
      * Description: Wind shielding factor
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`windshieldlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``floor_type`` **(required)**: :ref:`floor_type_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``depth_basement_floor`` **(required)**: :ref:`depth_basement_floor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resist_walls_base`` **(required)**: :ref:`thermal_resist_walls_base_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_basement_walls``: :ref:`height_basement_walls_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_transm_envi_base``: :ref:`thermal_transm_envi_base_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_transm_walls``: :ref:`thermal_transm_walls_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_insulation``: :ref:`edge_insulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementGround'

.. _area_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of this building element within the zone (unit: m²)

.. _total_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Total Area
----------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total area of the building element across entire dwelling; if the Floor is divided among several zones, this is the total area across all zones (unit: m²)

.. _perimeter_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Perimeter
---------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Perimeter of the floor; calculated for the entire ground floor, even if it is distributed among several zones (unit: m)

.. _areal_heat_capacity_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity of the ground floor element (unit: J/m2.K)

.. _thermal_resistance_floor_construction_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Floor Construction
-------------------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total thermal resistance of all layers in the floor construction (unit: m².K/W)

.. _u_value_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Steady-state thermal transmittance of floor, including the effect of the ground (calculated for the entire ground floor, even if it is distributed among several zones) (unit: W/m2.K)

.. _psi_wall_floor_junc_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Psi Wall Floor Junc
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Linear thermal transmittance of the junction between the floor and the walls (unit: W/m.K)

.. _pitch_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thickness_walls_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thickness Walls
---------------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thickness of the walls (unit: m)

.. _height_upper_surface_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Upper Surface
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _floor_type_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Floor Type
----------

<JSON string>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'Heated_basement'

.. _depth_basement_floor_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Depth Basement Floor
--------------------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Depth of basement floor below ground level (unit: m)

.. _thermal_resist_walls_base_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resist Walls Base
-------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance of walls of the basement (unit: m².K/W)

.. _height_basement_walls_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Basement Walls
---------------------

<JSON value>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Height of the basement walls above ground level (unit: m)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _thermal_transm_envi_base_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Transm Envi Base
------------------------

<JSON value>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal transmittance of floor above basement (unit: W/m².K)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _thermal_transm_walls_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Transm Walls
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal transmittance of walls above ground (unit: W/m².K)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _edge_insulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Insulation
---------------

<JSON value>

* Parent: :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON value>
    
    * OneOf:
    
      * :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'horizontal': '#/$defs/EdgeInsulationHorizontal', 'vertical': '#/$defs/EdgeInsulationVertical'}, 'propertyName': 'type'}
    
    
    
    
  * <JSON null>

.. _buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementGroundSlabEdgeInsulation
---------------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Slab floor with edge insulation - uses init_slab_on_ground_floor_edge_insulated()

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``total_area`` **(required)**: :ref:`total_area_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``perimeter`` **(required)**: :ref:`perimeter_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_floor_construction`` **(required)**: :ref:`thermal_resistance_floor_construction_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value`` **(required)**: :ref:`u_value_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``psi_wall_floor_junc`` **(required)**: :ref:`psi_wall_floor_junc_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thickness_walls`` **(required)**: :ref:`thickness_walls_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_upper_surface``: :ref:`height_upper_surface_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shield_fact_location``: 

    * <JSON value>
      
      * Description: Wind shielding factor
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`windshieldlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``floor_type`` **(required)**: :ref:`floor_type_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_insulation``: :ref:`edge_insulation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementGround'

.. _area_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of this building element within the zone (unit: m²)

.. _total_area_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Total Area
----------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total area of the building element across entire dwelling; if the Floor is divided among several zones, this is the total area across all zones (unit: m²)

.. _perimeter_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Perimeter
---------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Perimeter of the floor; calculated for the entire ground floor, even if it is distributed among several zones (unit: m)

.. _areal_heat_capacity_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity of the ground floor element (unit: J/m2.K)

.. _thermal_resistance_floor_construction_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Floor Construction
-------------------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total thermal resistance of all layers in the floor construction (unit: m².K/W)

.. _u_value_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Steady-state thermal transmittance of floor, including the effect of the ground (calculated for the entire ground floor, even if it is distributed among several zones) (unit: W/m2.K)

.. _psi_wall_floor_junc_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Psi Wall Floor Junc
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Linear thermal transmittance of the junction between the floor and the walls (unit: W/m.K)

.. _pitch_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thickness_walls_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thickness Walls
---------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thickness of the walls (unit: m)

.. _height_upper_surface_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Upper Surface
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _floor_type_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Floor Type
----------

<JSON string>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'Slab_edge_insulation'

.. _edge_insulation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Insulation
---------------

<JSON value>

* Parent: :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON value>
    
    * OneOf:
    
      * :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'horizontal': '#/$defs/EdgeInsulationHorizontal', 'vertical': '#/$defs/EdgeInsulationVertical'}, 'propertyName': 'type'}
    
    
    
    
  * <JSON null>

.. _buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementGroundSlabNoEdgeInsulation
-----------------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Slab floor with no edge insulation - uses init_slab_on_ground_floor_uninsulated_or_all_insulation()

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``total_area`` **(required)**: :ref:`total_area_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``perimeter`` **(required)**: :ref:`perimeter_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_floor_construction`` **(required)**: :ref:`thermal_resistance_floor_construction_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value`` **(required)**: :ref:`u_value_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``psi_wall_floor_junc`` **(required)**: :ref:`psi_wall_floor_junc_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thickness_walls`` **(required)**: :ref:`thickness_walls_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_upper_surface``: :ref:`height_upper_surface_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shield_fact_location``: 

    * <JSON value>
      
      * Description: Wind shielding factor
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`windshieldlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``floor_type`` **(required)**: :ref:`floor_type_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_insulation``: :ref:`edge_insulation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementGround'

.. _area_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of this building element within the zone (unit: m²)

.. _total_area_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Total Area
----------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total area of the building element across entire dwelling; if the Floor is divided among several zones, this is the total area across all zones (unit: m²)

.. _perimeter_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Perimeter
---------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Perimeter of the floor; calculated for the entire ground floor, even if it is distributed among several zones (unit: m)

.. _areal_heat_capacity_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity of the ground floor element (unit: J/m2.K)

.. _thermal_resistance_floor_construction_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Floor Construction
-------------------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total thermal resistance of all layers in the floor construction (unit: m².K/W)

.. _u_value_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Steady-state thermal transmittance of floor, including the effect of the ground (calculated for the entire ground floor, even if it is distributed among several zones) (unit: W/m2.K)

.. _psi_wall_floor_junc_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Psi Wall Floor Junc
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Linear thermal transmittance of the junction between the floor and the walls (unit: W/m.K)

.. _pitch_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thickness_walls_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thickness Walls
---------------

<JSON number>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thickness of the walls (unit: m)

.. _height_upper_surface_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Upper Surface
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _floor_type_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Floor Type
----------

<JSON string>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'Slab_no_edge_insulation'

.. _edge_insulation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Insulation
---------------

<JSON value>

* Parent: :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON value>
    
    * OneOf:
    
      * :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'horizontal': '#/$defs/EdgeInsulationHorizontal', 'vertical': '#/$defs/EdgeInsulationVertical'}, 'propertyName': 'type'}
    
    
    
    
  * <JSON null>

.. _buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementGroundSuspendedFloor
-----------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Suspended floor - uses init_suspended_floor()

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``total_area`` **(required)**: :ref:`total_area_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``perimeter`` **(required)**: :ref:`perimeter_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_floor_construction`` **(required)**: :ref:`thermal_resistance_floor_construction_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value`` **(required)**: :ref:`u_value_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``psi_wall_floor_junc`` **(required)**: :ref:`psi_wall_floor_junc_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thickness_walls`` **(required)**: :ref:`thickness_walls_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_upper_surface``: :ref:`height_upper_surface_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shield_fact_location``: 

    * <JSON value>
      
      * Description: Wind shielding factor
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`windshieldlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``floor_type`` **(required)**: :ref:`floor_type_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area_per_perimeter_vent``: :ref:`area_per_perimeter_vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resist_insul``: :ref:`thermal_resist_insul_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_transm_walls``: :ref:`thermal_transm_walls_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_insulation``: :ref:`edge_insulation_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementGround'

.. _area_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of this building element within the zone (unit: m²)

.. _total_area_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Total Area
----------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total area of the building element across entire dwelling; if the Floor is divided among several zones, this is the total area across all zones (unit: m²)

.. _perimeter_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Perimeter
---------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Perimeter of the floor; calculated for the entire ground floor, even if it is distributed among several zones (unit: m)

.. _areal_heat_capacity_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity of the ground floor element (unit: J/m2.K)

.. _thermal_resistance_floor_construction_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Floor Construction
-------------------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total thermal resistance of all layers in the floor construction (unit: m².K/W)

.. _u_value_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Steady-state thermal transmittance of floor, including the effect of the ground (calculated for the entire ground floor, even if it is distributed among several zones) (unit: W/m2.K)

.. _psi_wall_floor_junc_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Psi Wall Floor Junc
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Linear thermal transmittance of the junction between the floor and the walls (unit: W/m.K)

.. _pitch_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thickness_walls_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thickness Walls
---------------

<JSON number>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thickness of the walls (unit: m)

.. _height_upper_surface_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Upper Surface
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _floor_type_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Floor Type
----------

<JSON string>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'Suspended_floor'

.. _area_per_perimeter_vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area Per Perimeter Vent
-----------------------

<JSON value>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of ventilation openings per perimeter (unit: m²/m)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _thermal_resist_insul_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resist Insul
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance of insulation on base of underfloor space (unit: m².K/W)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _thermal_transm_walls_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Transm Walls
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal transmittance of walls above ground (unit: W/m².K)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _edge_insulation_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Insulation
---------------

<JSON value>

* Parent: :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON value>
    
    * OneOf:
    
      * :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'horizontal': '#/$defs/EdgeInsulationHorizontal', 'vertical': '#/$defs/EdgeInsulationVertical'}, 'propertyName': 'type'}
    
    
    
    
  * <JSON null>

.. _buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementGroundUnheatedBasement
-------------------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Unheated basement - uses init_unheated_basement()

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``total_area`` **(required)**: :ref:`total_area_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``perimeter`` **(required)**: :ref:`perimeter_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_floor_construction`` **(required)**: :ref:`thermal_resistance_floor_construction_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value`` **(required)**: :ref:`u_value_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``psi_wall_floor_junc`` **(required)**: :ref:`psi_wall_floor_junc_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thickness_walls`` **(required)**: :ref:`thickness_walls_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_upper_surface``: :ref:`height_upper_surface_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shield_fact_location``: 

    * <JSON value>
      
      * Description: Wind shielding factor
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`windshieldlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``floor_type`` **(required)**: :ref:`floor_type_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``depth_basement_floor`` **(required)**: :ref:`depth_basement_floor_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height_basement_walls`` **(required)**: :ref:`height_basement_walls_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resist_walls_base`` **(required)**: :ref:`thermal_resist_walls_base_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_transm_envi_base`` **(required)**: :ref:`thermal_transm_envi_base_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_transm_walls`` **(required)**: :ref:`thermal_transm_walls_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_insulation``: :ref:`edge_insulation_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementGround'

.. _area_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Area of this building element within the zone (unit: m²)

.. _total_area_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Total Area
----------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total area of the building element across entire dwelling; if the Floor is divided among several zones, this is the total area across all zones (unit: m²)

.. _perimeter_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Perimeter
---------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Perimeter of the floor; calculated for the entire ground floor, even if it is distributed among several zones (unit: m)

.. _areal_heat_capacity_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity of the ground floor element (unit: J/m2.K)

.. _thermal_resistance_floor_construction_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Floor Construction
-------------------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total thermal resistance of all layers in the floor construction (unit: m².K/W)

.. _u_value_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Steady-state thermal transmittance of floor, including the effect of the ground (calculated for the entire ground floor, even if it is distributed among several zones) (unit: W/m2.K)

.. _psi_wall_floor_junc_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Psi Wall Floor Junc
-------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Linear thermal transmittance of the junction between the floor and the walls (unit: W/m.K)

.. _pitch_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _thickness_walls_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thickness Walls
---------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thickness of the walls (unit: m)

.. _height_upper_surface_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Upper Surface
--------------------

<JSON value>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _floor_type_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Floor Type
----------

<JSON string>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'Unheated_basement'

.. _depth_basement_floor_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Depth Basement Floor
--------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Depth of basement floor below ground level (unit: m)

.. _height_basement_walls_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height Basement Walls
---------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Height of the basement walls above ground level (unit: m)

.. _thermal_resist_walls_base_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resist Walls Base
-------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance of walls of the basement (unit: m².K/W)

.. _thermal_transm_envi_base_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Transm Envi Base
------------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal transmittance of floor above basement (unit: W/m².K)

.. _thermal_transm_walls_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Transm Walls
--------------------

<JSON number>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal transmittance of walls above ground (unit: W/m².K)

.. _edge_insulation_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Insulation
---------------

<JSON value>

* Parent: :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON value>
    
    * OneOf:
    
      * :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'horizontal': '#/$defs/EdgeInsulationHorizontal', 'vertical': '#/$defs/EdgeInsulationVertical'}, 'propertyName': 'type'}
    
    
    
    
  * <JSON null>

.. _buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementOpaque
---------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``areal_heat_capacity`` **(required)**: :ref:`areal_heat_capacity_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``base_height`` **(required)**: :ref:`base_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height`` **(required)**: :ref:`height_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``is_unheated_pitched_roof``: :ref:`is_unheated_pitched_roof_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mass_distribution_class`` **(required)**: :ref:`massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``orientation360`` **(required)**: :ref:`orientation360_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``solar_absorption_coeff`` **(required)**: :ref:`solar_absorption_coeff_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_construction``: :ref:`thermal_resistance_construction_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value``: :ref:`u_value_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``width`` **(required)**: :ref:`width_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementOpaque'

.. _area_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Net area of the opaque building element (i.e. minus any windows / doors / etc.) (unit: m²)

.. _areal_heat_capacity_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Areal Heat Capacity
-------------------

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Areal heat capacity (unit: J/m².K)

.. _base_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Base Height
-----------

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The distance between the ground and the lowest edge of the element (unit: m)

.. _height_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height
------

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The height of the building element (unit: m)

.. _is_unheated_pitched_roof_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Is Unheated Pitched Roof
------------------------

<JSON value>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON boolean>
    
    
  * <JSON null>

.. _orientation360_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Orientation360
--------------

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The orientation angle of the inclined surface, expressed as the geographical azimuth angle of the horizontal projection of the inclined surface normal, 0 to 360 (unit: ˚)

.. _pitch_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _solar_absorption_coeff_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Solar Absorption Coeff
----------------------

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Solar absorption coefficient at the external surface (dimensionless)

.. _thermal_resistance_construction_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Construction
-------------------------------

<JSON value>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance (unit: m².K/W)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _u_value_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON value>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _width_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Width
-----

<JSON number>

* Parent: :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The width of the building element (unit: m)

.. _buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

BuildingElementTransparent
--------------------------

<JSON object>

* Parent(s): :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control_WindowOpenable``: :ref:`control_windowopenable_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``base_height`` **(required)**: :ref:`base_height_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frame_area_fraction`` **(required)**: :ref:`frame_area_fraction_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``free_area_height`` **(required)**: :ref:`free_area_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``g_value`` **(required)**: :ref:`g_value_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height`` **(required)**: :ref:`height_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_window_open_area`` **(required)**: :ref:`max_window_open_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mid_height`` **(required)**: :ref:`mid_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``orientation360`` **(required)**: :ref:`orientation360_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shading`` **(required)**: :ref:`shading_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_resistance_construction``: :ref:`thermal_resistance_construction_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``treatment``: :ref:`treatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``u_value``: :ref:`u_value_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``width`` **(required)**: :ref:`width_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``window_part_list`` **(required)**: :ref:`window_part_list_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'BuildingElementTransparent'

.. _control_windowopenable_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Windowopenable
----------------------

<JSON value>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _base_height_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Base Height
-----------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The distance between the ground and the lowest edge of the element (unit: m)

.. _frame_area_fraction_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frame Area Fraction
-------------------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The frame area fraction of window, ratio of the projected frame area to the overall projected area of the glazed element of the window

.. _free_area_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Free Area Height
----------------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _g_value_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

G Value
-------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total solar energy transmittance of the transparent part of the window

.. _height_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height
------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The height of the building element (unit: m)

.. _max_window_open_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Window Open Area
--------------------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _mid_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Mid Height
----------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _orientation360_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Orientation360
--------------

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The orientation angle of the inclined surface, expressed as the geographical azimuth angle of the horizontal projection of the inclined surface normal, 0 to 360 (unit: ˚)

.. _pitch_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _shading_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Shading
-------

<JSON array>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON value>

* AnyOf:

  * :ref:`windowshadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27`



.. _thermal_resistance_construction_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Resistance Construction
-------------------------------

<JSON value>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Thermal resistance (unit: m².K/W)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _treatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Treatment
---------

<JSON value>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _u_value_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

U Value
-------

<JSON value>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _width_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Width
-----

<JSON number>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The width of the building element (unit: m)

.. _window_part_list_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Window Part List
----------------

<JSON array>

* Parent: :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: :ref:`windowpart_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _chargelevel_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ChargeLevel
-----------

<JSON value>

* Parent(s): :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON number>
    
    
  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _coldwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ColdWaterSource
---------------

<JSON object>

* Parent(s): :ref:`coldwatersource_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``start_day`` **(required)**: :ref:`start_day_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temperatures`` **(required)**: :ref:`temperatures_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _start_day_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`coldwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

* Description: First day of the time series, day of the year, 0 to 365

.. _temperatures_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temperatures
------------

<JSON array>

* Parent: :ref:`coldwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of cold water temperatures, one entry per hour (unit: ˚C)

* Items: <JSON number>



.. _time_series_step_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`coldwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Timestep of the time series data (unit: hours)

.. _controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlChargeTarget
-------------------

<JSON object>

* Parent(s): :ref:`control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``charge_level``: 

    * <JSON value>
      
      * Description: Proportion of the charge targeted for each day
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`chargelevel_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``external_sensor``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`externalsensor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``logic_type``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`controllogictype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``schedule`` **(required)**: :ref:`scheduleforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start_day`` **(required)**: :ref:`start_day_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_charge_cut``: :ref:`temp_charge_cut_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_charge_cut_delta``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``time_series_step`` **(required)**: :ref:`time_series_step_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'ChargeControl'

.. _start_day_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

* Description: First day of the time series, day of the year, 0 to 365

.. _temp_charge_cut_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Charge Cut
---------------

<JSON value>

* Parent: :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _time_series_step_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Timestep of the time series data (unit: hours)

.. _controlcombination_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlCombination
------------------

<JSON object>

* Parent(s): :ref:`controlcombinations_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``controls`` **(required)**: :ref:`controls_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``operation`` **(required)**: :ref:`controlcombinationoperation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _controls_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controls
--------

<JSON array>

* Parent: :ref:`controlcombination_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* MinItems: 1

* Items: <JSON string>



.. _controlcombinationoperation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlCombinationOperation
---------------------------

<JSON string>

* Parent(s): :ref:`controlcombination_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['AND', 'OR', 'XOR', 'NOT', 'MAX', 'MIN', 'MEAN']

.. _controlcombinationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlCombinationTime
----------------------

<JSON object>

* Parent(s): :ref:`control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``combination`` **(required)**: :ref:`controlcombinations_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`controlcombinationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'CombinationTimeControl'

.. _controlcombinations_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlCombinations
-------------------

<JSON object>

* Parent(s): :ref:`controlcombinationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: A dictionary of control combinations where: - Keys are user-defined names (e.g., "main", "week", "weekday", "weekend") - Values conform to the ControlCombination schema - The "main" entry is required

* User-named name/value pairs:  {ANY_NAME: :ref:`controlcombination_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}

.. _controllogictype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlLogicType
----------------

<JSON string>

* Parent(s): :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['celect', 'heat_battery', 'hhrsh', 'automatic', 'manual']

.. _controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlOnOffCostMinimising
--------------------------

<JSON object>

* Parent(s): :ref:`control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_11_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``schedule`` **(required)**: :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start_day`` **(required)**: :ref:`start_day_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_on_daily`` **(required)**: :ref:`time_on_daily_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_11_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'OnOffCostMinimisingTimeControl'

.. _start_day_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

* Description: First day of the time series, day of the year, 0 to 365

.. _time_on_daily_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time On Daily
-------------

<JSON number>

* Parent: :ref:`controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Number of 'on' hours to be set per day

.. _time_series_step_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Timestep of the time series data (unit: hours)

.. _controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlOnOffTimer
-----------------

<JSON object>

* Parent(s): :ref:`control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_12_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``allow_null``: :ref:`allow_null_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``schedule`` **(required)**: :ref:`scheduleforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start_day`` **(required)**: :ref:`start_day_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_12_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'OnOffTimeControl'

.. _allow_null_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Allow Null
----------

<JSON value>

* Parent: :ref:`controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON boolean>
    
    
  * <JSON null>

.. _start_day_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

* Description: First day of the time series, day of the year, 0 to 365

.. _time_series_step_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Timestep of the time series data (unit: hours)

.. _controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ControlSetpointTimer
--------------------

<JSON object>

* Parent(s): :ref:`control_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_13_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``advanced_start``: :ref:`advanced_start_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``default_to_max``: :ref:`default_to_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``schedule`` **(required)**: :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``setpoint_max``: :ref:`setpoint_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``setpoint_min``: :ref:`setpoint_min_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start_day`` **(required)**: :ref:`start_day_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_13_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'SetpointTimeControl'

.. _advanced_start_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Advanced Start
--------------

<JSON value>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: How long before heating period the system should switch on (unit: hours)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _default_to_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Default To Max
--------------

<JSON value>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: If both min and max limits are set but setpoint is not, whether to default to min (false) or max (true)

* Default: <JSON null>

* AnyOf:

  * <JSON boolean>
    
    
  * <JSON null>

.. _setpoint_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Setpoint Max
------------

<JSON value>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Maximum setpoint allowed

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _setpoint_min_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Setpoint Min
------------

<JSON value>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Minimum setpoint allowed

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _start_day_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

* Description: First day of the time series, day of the year, 0 to 365

.. _time_series_step_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Timestep of the time series data (unit: hours)

.. _customenergysourcefactor_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

CustomEnergySourceFactor
------------------------

<JSON object>

* Parent(s): :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Emissions Factor kgCO2e/kWh`` **(required)**: :ref:`emissions_factor_kgco2e/kwh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Emissions Factor kgCO2e/kWh including out-of-scope emissions`` **(required)**: :ref:`emissions_factor_kgco2e/kwh_including_out-of-scope_emissions_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Primary Energy Factor kWh/kWh delivered`` **(required)**: :ref:`primary_energy_factor_kwh/kwh_delivered_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _emissions_factor_kgco2e/kwh_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Emissions Factor Kgco2E/Kwh
---------------------------

<JSON number>

* Parent: :ref:`customenergysourcefactor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _emissions_factor_kgco2e/kwh_including_out-of-scope_emissions_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Emissions Factor Kgco2E/Kwh Including Out-Of-Scope Emissions
------------------------------------------------------------

<JSON number>

* Parent: :ref:`customenergysourcefactor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _primary_energy_factor_kwh/kwh_delivered_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Primary Energy Factor Kwh/Kwh Delivered
---------------------------------------

<JSON number>

* Parent: :ref:`customenergysourcefactor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _ductshape_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

DuctShape
---------

<JSON string>

* Parent(s): :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['circular', 'rectangular']

.. _ducttype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

DuctType
--------

<JSON string>

* Parent(s): :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['intake', 'supply', 'extract', 'exhaust']

.. _ecodesigncontroller_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EcoDesignController
-------------------

<JSON object>

* Parent(s): :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``ecodesign_control_class`` **(required)**: :ref:`ecodesigncontrollerclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_outdoor_temp``: :ref:`max_outdoor_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_flow_temp``: :ref:`min_flow_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_outdoor_temp``: :ref:`min_outdoor_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _max_outdoor_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Outdoor Temp
----------------

<JSON value>

* Parent: :ref:`ecodesigncontroller_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_flow_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Flow Temp
-------------

<JSON value>

* Parent: :ref:`ecodesigncontroller_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_outdoor_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Outdoor Temp
----------------

<JSON value>

* Parent: :ref:`ecodesigncontroller_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _ecodesigncontrollerclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EcoDesignControllerClass
------------------------

<JSON integer>

* Parent(s): :ref:`ecodesigncontroller_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: [1, 2, 3, 4, 5, 6, 7, 8]

.. _edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EdgeInsulationHorizontal
------------------------

<JSON object>

* Parent(s): :ref:`edge_insulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_14_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_thermal_resistance`` **(required)**: :ref:`edge_thermal_resistance_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``width`` **(required)**: :ref:`width_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_14_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'horizontal'

.. _edge_thermal_resistance_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Thermal Resistance
-----------------------

<JSON number>

* Parent: :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _width_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Width
-----

<JSON number>

* Parent: :ref:`edgeinsulationhorizontal_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EdgeInsulationVertical
----------------------

<JSON object>

* Parent(s): :ref:`edge_insulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`edge_insulation_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_15_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``edge_thermal_resistance`` **(required)**: :ref:`edge_thermal_resistance_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``depth`` **(required)**: :ref:`depth_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_15_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'vertical'

.. _edge_thermal_resistance_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Edge Thermal Resistance
-----------------------

<JSON number>

* Parent: :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _depth_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Depth
-----

<JSON number>

* Parent: :ref:`edgeinsulationvertical_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ElectricBattery
---------------

<JSON object>

* Parent(s): :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``battery_age`` **(required)**: :ref:`battery_age_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``battery_location`` **(required)**: :ref:`batterylocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``capacity`` **(required)**: :ref:`capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``charge_discharge_efficiency_round_trip`` **(required)**: :ref:`charge_discharge_efficiency_round_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``grid_charging_possible`` **(required)**: :ref:`grid_charging_possible_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``maximum_charge_rate_one_way_trip`` **(required)**: :ref:`maximum_charge_rate_one_way_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``maximum_discharge_rate_one_way_trip`` **(required)**: :ref:`maximum_discharge_rate_one_way_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``minimum_charge_rate_one_way_trip`` **(required)**: :ref:`minimum_charge_rate_one_way_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _battery_age_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Battery Age
-----------

<JSON number>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Capacity
--------

<JSON number>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _charge_discharge_efficiency_round_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Charge Discharge Efficiency Round Trip
--------------------------------------

<JSON number>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _grid_charging_possible_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Grid Charging Possible
----------------------

<JSON boolean>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _maximum_charge_rate_one_way_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Maximum Charge Rate One Way Trip
--------------------------------

<JSON number>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _maximum_discharge_rate_one_way_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Maximum Discharge Rate One Way Trip
-----------------------------------

<JSON number>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _minimum_charge_rate_one_way_trip_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Minimum Charge Rate One Way Trip
--------------------------------

<JSON number>

* Parent: :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energydiverter_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EnergyDiverter
--------------

<JSON object>

* Parent(s): :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Controlmax`` **(required)**: :ref:`controlmax_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSource`` **(required)**: :ref:`heatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _controlmax_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmax
----------

<JSON string>

* Parent: :ref:`energydiverter_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heatsource
----------

<JSON string>

* Parent: :ref:`energydiverter_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EnergySupply
------------

<JSON object>

* Parent(s): :ref:`energysupply_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``ElectricBattery``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`electricbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``diverter``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`energydiverter_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``factor``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`customenergysourcefactor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``fuel`` **(required)**: :ref:`fueltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``is_export_capable`` **(required)**: :ref:`is_export_capable_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``priority``: :ref:`priority_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``tariff``: :ref:`tariff_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``threshold_charges``: :ref:`threshold_charges_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``threshold_prices``: :ref:`threshold_prices_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _is_export_capable_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Is Export Capable
-----------------

<JSON boolean>

* Parent: :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Denotes that this energy supply can export its surplus supply

.. _priority_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Priority
--------

<JSON value>

* Parent: :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`energysupplypriorityentry_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _tariff_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Tariff
------

<JSON value>

* Parent: :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _threshold_charges_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Threshold Charges
-----------------

<JSON value>

* Parent: :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * MaxItems: 12
    
    * MinItems: 12
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _threshold_prices_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Threshold Prices
----------------

<JSON value>

* Parent: :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * MaxItems: 12
    
    * MinItems: 12
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _energysupplypriorityentry_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

EnergySupplyPriorityEntry
-------------------------

<JSON string>

* Parent(s): :ref:`priority_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['ElectricBattery', 'diverter']

.. _externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ExternalConditionsInput
-----------------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``air_temperatures``: :ref:`air_temperatures_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``diffuse_horizontal_radiation``: :ref:`diffuse_horizontal_radiation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``direct_beam_conversion_needed``: :ref:`direct_beam_conversion_needed_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``direct_beam_radiation``: :ref:`direct_beam_radiation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``latitude``: :ref:`latitude_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``longitude``: :ref:`longitude_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shading_segments``: :ref:`shading_segments_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``solar_reflectivity_of_ground``: :ref:`solar_reflectivity_of_ground_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``wind_directions``: :ref:`wind_directions_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``wind_speeds``: :ref:`wind_speeds_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _air_temperatures_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Air Temperatures
----------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of external air temperatures, one entry per hour (unit: ˚C)

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _diffuse_horizontal_radiation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Diffuse Horizontal Radiation
----------------------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of diffuse horizontal radiation values, one entry per hour (unit: W/m²)

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _direct_beam_conversion_needed_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Direct Beam Conversion Needed
-----------------------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: A flag to indicate whether direct beam radiation from climate data needs to be converted from horizontal to normal incidence; if normal direct beam radiation values are provided then no conversion is needed

* Default: <JSON null>

* AnyOf:

  * <JSON boolean>
    
    
  * <JSON null>

.. _direct_beam_radiation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Direct Beam Radiation
---------------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of direct beam radiation values, one entry per hour (unit: W/m²)

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _latitude_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Latitude
--------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Latitude of weather station, angle from south (unit: ˚)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _longitude_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Longitude
---------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Longitude of weather station, easterly +ve westerly -ve (unit: ˚)

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _shading_segments_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Shading Segments
----------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Data splitting the ground plane into segments (8-36) and giving height and distance to shading objects surrounding the building

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`shadingsegment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _solar_reflectivity_of_ground_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Solar Reflectivity Of Ground
----------------------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of ground reflectivity values, 0 to 1, one entry per hour

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _wind_directions_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Wind Directions
---------------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of wind directions in degrees where North=0, East=90, South=180, West=270. Values range: 0 to 360. Wind direction is reported by the direction from which it originates, e.g. a southerly (180 degree) wind blows from the south to the north. (unit: ˚)

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _wind_speeds_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Wind Speeds
-----------

<JSON value>

* Parent: :ref:`externalconditionsinput_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: List of wind speeds, one entry per hour (unit: m/s)

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
  * <JSON null>

.. _externalsensor_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ExternalSensor
--------------

<JSON object>

* Parent(s): :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``correlation`` **(required)**: :ref:`correlation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _correlation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Correlation
-----------

<JSON array>

* Parent: :ref:`externalsensor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: :ref:`externalsensorcorrelation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _externalsensorcorrelation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ExternalSensorCorrelation
-------------------------

<JSON object>

* Parent(s): :ref:`correlation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``temperature`` **(required)**: :ref:`temperature_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_charge`` **(required)**: :ref:`max_charge_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _temperature_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temperature
-----------

<JSON number>

* Parent: :ref:`externalsensorcorrelation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _max_charge_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Charge
----------

<JSON number>

* Parent: :ref:`externalsensorcorrelation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _fanspeeddata_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

FanSpeedData
------------

<JSON object>

* Parent(s): :ref:`fan_speed_data_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``power_output`` **(required)**: :ref:`power_output_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temperature_diff`` **(required)**: :ref:`temperature_diff_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _power_output_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Output
------------

<JSON array>

* Parent: :ref:`fanspeeddata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON number>



.. _temperature_diff_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temperature Diff
----------------

<JSON number>

* Parent: :ref:`fanspeeddata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _fancoiltestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

FancoilTestData
---------------

<JSON object>

* Parent(s): :ref:`wetemitterfancoil_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``fan_power_W`` **(required)**: :ref:`fan_power_w_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``fan_speed_data`` **(required)**: :ref:`fan_speed_data_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _fan_power_w_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Fan Power W
-----------

<JSON array>

* Parent: :ref:`fancoiltestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON number>



.. _fan_speed_data_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Fan Speed Data
--------------

<JSON array>

* Parent: :ref:`fancoiltestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: :ref:`fanspeeddata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _fueltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

FuelType
--------

<JSON string>

* Parent(s): :ref:`energysupply_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['LPG_bottled', 'LPG_bulk', 'LPG_condition_11F', 'custom', 'electricity', 'energy_from_environment', 'mains_gas', 'unmet_demand']

.. _heatpumpbackupcontroltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpBackupControlType
-------------------------

<JSON string>

* Parent(s): :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['None', 'TopUp', 'Substitute']

.. _heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpBoiler
--------------

<JSON object>

* Parent(s): :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Boiler used as backup for heat pump systems

* Named name/value pairs:

  * ``EnergySupply`` **(required)**: :ref:`energysupply_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply_aux`` **(required)**: :ref:`energysupply_aux_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``boiler_location`` **(required)**: :ref:`heatsourcelocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiency_full_load`` **(required)**: :ref:`efficiency_full_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiency_part_load`` **(required)**: :ref:`efficiency_part_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_circ_pump`` **(required)**: :ref:`electricity_circ_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_full_load`` **(required)**: :ref:`electricity_full_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_part_load`` **(required)**: :ref:`electricity_part_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_standby`` **(required)**: :ref:`electricity_standby_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``modulation_load`` **(required)**: :ref:`modulation_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rated_power`` **(required)**: :ref:`rated_power_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cost_schedule_hybrid``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`boilercostschedulehybrid_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      

* User-named name/value pairs: NONE_ALLOWED

.. _energysupply_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_aux_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply Aux
----------------

<JSON string>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _efficiency_full_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiency Full Load
--------------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _efficiency_part_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiency Part Load
--------------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_circ_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Circ Pump
---------------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_full_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Full Load
---------------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_part_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Part Load
---------------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_standby_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Standby
-------------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _modulation_load_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Modulation Load
---------------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _rated_power_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rated Power
-----------

<JSON number>

* Parent: :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatpumpbuffertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpBufferTank
------------------

<JSON object>

* Parent(s): :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``daily_losses`` **(required)**: :ref:`daily_losses_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pump_fixed_flow_rate`` **(required)**: :ref:`pump_fixed_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pump_power_at_flow_rate`` **(required)**: :ref:`pump_power_at_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``volume`` **(required)**: :ref:`volume_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _daily_losses_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Daily Losses
------------

<JSON number>

* Parent: :ref:`heatpumpbuffertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _pump_fixed_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pump Fixed Flow Rate
--------------------

<JSON number>

* Parent: :ref:`heatpumpbuffertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _pump_power_at_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pump Power At Flow Rate
-----------------------

<JSON number>

* Parent: :ref:`heatpumpbuffertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _volume_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Volume
------

<JSON number>

* Parent: :ref:`heatpumpbuffertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpHotWaterOnly
--------------------

<JSON object>

* Parent(s): :ref:`heatsource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`heatsource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_16_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmax`` **(required)**: :ref:`controlmax_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmin`` **(required)**: :ref:`controlmin_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``daily_losses_declared`` **(required)**: :ref:`daily_losses_declared_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_exchanger_surface_area_declared`` **(required)**: :ref:`heat_exchanger_surface_area_declared_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heater_position`` **(required)**: :ref:`heater_position_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``in_use_factor_mismatch`` **(required)**: :ref:`in_use_factor_mismatch_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_max`` **(required)**: :ref:`power_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``tank_volume_declared`` **(required)**: :ref:`tank_volume_declared_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``test_data`` **(required)**: :ref:`heatpumphotwatertestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermostat_position``: :ref:`thermostat_position_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``vol_hw_daily_average`` **(required)**: :ref:`vol_hw_daily_average_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_16_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HeatPump_HWOnly'

.. _controlmax_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmax
----------

<JSON string>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of maximum temperature setpoints

.. _controlmin_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmin
----------

<JSON string>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of minimum temperature setpoints

.. _energysupply_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _daily_losses_declared_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Daily Losses Declared
---------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heat_exchanger_surface_area_declared_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Exchanger Surface Area Declared
------------------------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heater_position_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heater Position
---------------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _in_use_factor_mismatch_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

In Use Factor Mismatch
----------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Max
---------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _tank_volume_declared_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Tank Volume Declared
--------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _thermostat_position_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermostat Position
-------------------

<JSON value>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Required for StorageTank but not for SmartHotWaterTank

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _vol_hw_daily_average_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Vol Hw Daily Average
--------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpHotWaterOnlyTestDatum
-----------------------------

<JSON object>

* Parent(s): :ref:`heatpumphotwatertestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`heatpumphotwatertestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``cop_dhw`` **(required)**: :ref:`cop_dhw_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``energy_input_measured`` **(required)**: :ref:`energy_input_measured_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``hw_tapping_prof_daily_total`` **(required)**: :ref:`hw_tapping_prof_daily_total_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``hw_vessel_loss_daily`` **(required)**: :ref:`hw_vessel_loss_daily_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_standby`` **(required)**: :ref:`power_standby_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _cop_dhw_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Cop Dhw
-------

<JSON number>

* Parent: :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energy_input_measured_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energy Input Measured
---------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _hw_tapping_prof_daily_total_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Hw Tapping Prof Daily Total
---------------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _hw_vessel_loss_daily_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Hw Vessel Loss Daily
--------------------

<JSON number>

* Parent: :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_standby_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Standby
-------------

<JSON number>

* Parent: :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatpumphotwatertestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpHotWaterTestData
------------------------

<JSON object>

* Parent(s): :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``L``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``M`` **(required)**: :ref:`heatpumphotwateronlytestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _heatpumpsinktype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpSinkType
----------------

<JSON string>

* Parent(s): :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['Water', 'Air', 'Glycol25']

.. _heatpumpsourcetype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpSourceType
------------------

<JSON string>

* Parent(s): :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['Ground', 'OutsideAir', 'ExhaustAirMEV', 'ExhaustAirMVHR', 'ExhaustAirMixed', 'WaterGround', 'WaterSurface', 'HeatNetwork']

.. _heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatPumpTestDatum
-----------------

<JSON object>

* Parent(s): :ref:`test_data_en14825_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``air_flow_rate``: :ref:`air_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``capacity`` **(required)**: :ref:`capacity_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cop`` **(required)**: :ref:`cop_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``degradation_coeff`` **(required)**: :ref:`degradation_coeff_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``design_flow_temp`` **(required)**: :ref:`design_flow_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``eahp_mixed_ext_air_ratio``: :ref:`eahp_mixed_ext_air_ratio_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_outlet`` **(required)**: :ref:`temp_outlet_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_source`` **(required)**: :ref:`temp_source_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_test`` **(required)**: :ref:`temp_test_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``test_letter`` **(required)**: :ref:`testletter_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _air_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Air Flow Rate
-------------

<JSON value>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _capacity_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Capacity
--------

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _cop_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Cop
---

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _degradation_coeff_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Degradation Coeff
-----------------

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _design_flow_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Design Flow Temp
----------------

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _eahp_mixed_ext_air_ratio_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Eahp Mixed Ext Air Ratio
------------------------

<JSON value>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _temp_outlet_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Outlet
-----------

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temp_source_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Source
-----------

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temp_test_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Test
---------

<JSON number>

* Parent: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcelocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceLocation
------------------

<JSON string>

* Parent(s): :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['internal', 'external']

.. _heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWetBoiler
-------------------

<JSON object>

* Parent(s): :ref:`heatsourcewet_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Standalone boiler heat source

* Named name/value pairs:

  * ``EnergySupply`` **(required)**: :ref:`energysupply_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply_aux`` **(required)**: :ref:`energysupply_aux_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``boiler_location`` **(required)**: :ref:`heatsourcelocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiency_full_load`` **(required)**: :ref:`efficiency_full_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiency_part_load`` **(required)**: :ref:`efficiency_part_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_circ_pump`` **(required)**: :ref:`electricity_circ_pump_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_full_load`` **(required)**: :ref:`electricity_full_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_part_load`` **(required)**: :ref:`electricity_part_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_standby`` **(required)**: :ref:`electricity_standby_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``modulation_load`` **(required)**: :ref:`modulation_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rated_power`` **(required)**: :ref:`rated_power_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``type`` **(required)**: :ref:`type_17_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _energysupply_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_aux_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply Aux
----------------

<JSON string>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _efficiency_full_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiency Full Load
--------------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _efficiency_part_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiency Part Load
--------------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_circ_pump_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Circ Pump
---------------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_full_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Full Load
---------------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_part_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Part Load
---------------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_standby_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Standby
-------------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _modulation_load_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Modulation Load
---------------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _rated_power_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rated Power
-----------

<JSON number>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _type_17_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`heatsourcewetboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'Boiler'

.. _heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWetHIU
----------------

<JSON object>

* Parent(s): :ref:`heatsourcewet_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_18_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HIU_daily_loss`` **(required)**: :ref:`hiu_daily_loss_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``building_level_distribution_losses`` **(required)**: :ref:`building_level_distribution_losses_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_max`` **(required)**: :ref:`power_max_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_18_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HIU'

.. _energysupply_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _hiu_daily_loss_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Hiu Daily Loss
--------------

<JSON number>

* Parent: :ref:`heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _building_level_distribution_losses_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Building Level Distribution Losses
----------------------------------

<JSON number>

* Parent: :ref:`heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_max_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Max
---------

<JSON number>

* Parent: :ref:`heatsourcewethiu_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWetHeatBattery
------------------------

<JSON object>

* Parent(s): :ref:`heatsourcewet_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_19_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``A`` **(required)**: :ref:`a_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``B`` **(required)**: :ref:`b_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ControlCharge`` **(required)**: :ref:`controlcharge_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``capillary_diameter_m`` **(required)**: :ref:`capillary_diameter_m_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_circ_pump`` **(required)**: :ref:`electricity_circ_pump_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``electricity_standby`` **(required)**: :ref:`electricity_standby_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``flow_rate_l_per_min`` **(required)**: :ref:`flow_rate_l_per_min_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_exchanger_surface_area_m2`` **(required)**: :ref:`heat_exchanger_surface_area_m2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_storage_zone_material_kJ_per_K_above_Phase_transition`` **(required)**: :ref:`heat_storage_zone_material_kj_per_k_above_phase_transition_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_storage_zone_material_kJ_per_K_below_Phase_transition`` **(required)**: :ref:`heat_storage_zone_material_kj_per_k_below_phase_transition_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_storage_zone_material_kJ_per_K_during_Phase_transition`` **(required)**: :ref:`heat_storage_zone_material_kj_per_k_during_phase_transition_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_rated_losses`` **(required)**: :ref:`max_rated_losses_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_temperature`` **(required)**: :ref:`max_temperature_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``number_of_units`` **(required)**: :ref:`number_of_units_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``phase_transition_temperature_upper`` **(required)**: :ref:`phase_transition_temperature_upper_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``phase_transition_temperature_lower`` **(required)**: :ref:`phase_transition_temperature_lower_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rated_charge_power`` **(required)**: :ref:`rated_charge_power_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``simultaneous_charging_and_discharging`` **(required)**: :ref:`simultaneous_charging_and_discharging_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``velocity_in_HEX_tube_at_1_l_per_min_m_per_s`` **(required)**: :ref:`velocity_in_hex_tube_at_1_l_per_min_m_per_s_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_19_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HeatBattery'

.. _a_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

A
-

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _b_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

B
-

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _controlcharge_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlcharge
-------------

<JSON string>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _capillary_diameter_m_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Capillary Diameter M
--------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_circ_pump_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Circ Pump
---------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _electricity_standby_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Electricity Standby
-------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _flow_rate_l_per_min_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Flow Rate L Per Min
-------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heat_exchanger_surface_area_m2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Exchanger Surface Area M2
------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heat_storage_zone_material_kj_per_k_above_phase_transition_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Storage Zone Material Kj Per K Above Phase Transition
----------------------------------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heat_storage_zone_material_kj_per_k_below_phase_transition_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Storage Zone Material Kj Per K Below Phase Transition
----------------------------------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heat_storage_zone_material_kj_per_k_during_phase_transition_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Storage Zone Material Kj Per K During Phase Transition
-----------------------------------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _max_rated_losses_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Rated Losses
----------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _max_temperature_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Temperature
---------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _number_of_units_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Number Of Units
---------------

<JSON integer>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Minimum: 0

.. _phase_transition_temperature_upper_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Phase Transition Temperature Upper
----------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _phase_transition_temperature_lower_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Phase Transition Temperature Lower
----------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _rated_charge_power_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rated Charge Power
------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _simultaneous_charging_and_discharging_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Simultaneous Charging And Discharging
-------------------------------------

<JSON boolean>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _velocity_in_hex_tube_at_1_l_per_min_m_per_s_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Velocity In Hex Tube At 1 L Per Min M Per S
-------------------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWetHeatPump
---------------------

<JSON object>

* Parent(s): :ref:`heatsourcewet_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_20_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``BufferTank``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`heatpumpbuffertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``EnergySupply`` **(required)**: :ref:`energysupply_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply_heat_network``: :ref:`energysupply_heat_network_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``MechanicalVentilation``: :ref:`mechanicalventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``backup_ctrl_type`` **(required)**: :ref:`heatpumpbackupcontroltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``boiler``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`heatpumpboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``eahp_mixed_max_temp``: :ref:`eahp_mixed_max_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``eahp_mixed_min_temp``: :ref:`eahp_mixed_min_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_modulation_rate_20``: :ref:`min_modulation_rate_20_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_modulation_rate_35``: :ref:`min_modulation_rate_35_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_modulation_rate_55``: :ref:`min_modulation_rate_55_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_temp_diff_flow_return_for_hp_to_operate`` **(required)**: :ref:`min_temp_diff_flow_return_for_hp_to_operate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``modulating_control`` **(required)**: :ref:`modulating_control_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_crankcase_heater`` **(required)**: :ref:`power_crankcase_heater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_heating_circ_pump``: :ref:`power_heating_circ_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_heating_warm_air_fan``: :ref:`power_heating_warm_air_fan_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_max_backup``: :ref:`power_max_backup_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_off`` **(required)**: :ref:`power_off_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_source_circ_pump`` **(required)**: :ref:`power_source_circ_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_standby`` **(required)**: :ref:`power_standby_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``sink_type`` **(required)**: :ref:`heatpumpsinktype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``source_type`` **(required)**: :ref:`heatpumpsourcetype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_distribution_heat_network``: :ref:`temp_distribution_heat_network_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_lower_operating_limit`` **(required)**: :ref:`temp_lower_operating_limit_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_return_feed_max``: :ref:`temp_return_feed_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``test_data_EN14825`` **(required)**: :ref:`test_data_en14825_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_constant_onoff_operation`` **(required)**: :ref:`time_constant_onoff_operation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_delay_backup``: :ref:`time_delay_backup_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``var_flow_temp_ctrl_during_test`` **(required)**: :ref:`var_flow_temp_ctrl_during_test_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_20_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HeatPump'

.. _energysupply_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_heat_network_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply Heat Network
-------------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _mechanicalventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Mechanicalventilation
---------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _eahp_mixed_max_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Eahp Mixed Max Temp
-------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _eahp_mixed_min_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Eahp Mixed Min Temp
-------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_modulation_rate_20_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Modulation Rate 20
----------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_modulation_rate_35_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Modulation Rate 35
----------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_modulation_rate_55_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Modulation Rate 55
----------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_temp_diff_flow_return_for_hp_to_operate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Temp Diff Flow Return For Hp To Operate
-------------------------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _modulating_control_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Modulating Control
------------------

<JSON boolean>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_crankcase_heater_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Crankcase Heater
----------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_heating_circ_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Heating Circ Pump
-----------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _power_heating_warm_air_fan_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Heating Warm Air Fan
--------------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _power_max_backup_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Max Backup
----------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _power_off_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Off
---------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_source_circ_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Source Circ Pump
----------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_standby_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Standby
-------------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temp_distribution_heat_network_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Distribution Heat Network
------------------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _temp_lower_operating_limit_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Lower Operating Limit
--------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temp_return_feed_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Return Feed Max
--------------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _test_data_en14825_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Test Data En14825
-----------------

<JSON array>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _time_constant_onoff_operation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Constant Onoff Operation
-----------------------------

<JSON number>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _time_delay_backup_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Delay Backup
-----------------

<JSON value>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _var_flow_temp_ctrl_during_test_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Var Flow Temp Ctrl During Test
------------------------------

<JSON boolean>

* Parent: :ref:`heatsourcewetheatpump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HeatSourceWetServiceWaterRegular
--------------------------------

<JSON object>

* Parent(s): :ref:`heatsource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`heatsource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_21_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmax`` **(required)**: :ref:`controlmax_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmin`` **(required)**: :ref:`controlmin_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heater_position`` **(required)**: :ref:`heater_position_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``name`` **(required)**: :ref:`name_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_flow_limit_upper``: :ref:`temp_flow_limit_upper_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermostat_position``: :ref:`thermostat_position_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_21_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HeatSourceWet'

.. _controlmax_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmax
----------

<JSON string>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of maximum temperature setpoints

.. _controlmin_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmin
----------

<JSON string>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of minimum temperature setpoints

.. _energysupply_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heater_position_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heater Position
---------------

<JSON number>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _name_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Name
----

<JSON string>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temp_flow_limit_upper_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Flow Limit Upper
---------------------

<JSON value>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _thermostat_position_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermostat Position
-------------------

<JSON value>

* Parent: :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Required for StorageTank but not for SmartHotWaterTank

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _hotwaterdemand_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterDemand
--------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Bath``: :ref:`bath_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Distribution``: :ref:`distribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Other``: :ref:`other_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Shower``: :ref:`shower_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _bath_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Bath
----

<JSON value>

* Parent: :ref:`hotwaterdemand_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`bath_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _distribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Distribution
------------

<JSON value>

* Parent: :ref:`hotwaterdemand_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`waterpipeworksimple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _other_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Other
-----

<JSON value>

* Parent: :ref:`hotwaterdemand_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`otherwateruse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _shower_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Shower
------

<JSON value>

* Parent: :ref:`hotwaterdemand_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs: 
    
      * {ANY_NAME:
    
        * <JSON value>
        
        * OneOf:
        
          * :ref:`showermixer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
          * :ref:`showerinstantelectric_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        
        * Non-JSON Schema keywords:
        
          * discriminator: {'mapping': {'InstantElecShower': '#/$defs/ShowerInstantElectric', 'MixerShower': '#/$defs/ShowerMixer'}, 'propertyName': 'type'}
        
        
        }
    
    
  * <JSON null>

.. _hotwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterSource
--------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``hw cylinder`` **(required)**: :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Hw Cylinder
-----------

<JSON value>

* Parent: :ref:`hotwatersource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* OneOf:

  * :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`hotwatersourcehui_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`hotwatersourceheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'CombiBoiler': '#/$defs/HotWaterSourceCombiBoiler', 'HIU': '#/$defs/HotWaterSourceHUI', 'HeatBattery': '#/$defs/HotWaterSourceHeatBattery', 'PointOfUse': '#/$defs/HotWaterSourcePointOfUse', 'SmartHotWaterTank': '#/$defs/HotWaterSourceSmartHotWaterTank', 'StorageTank': '#/$defs/StorageTank'}, 'propertyName': 'type'}

.. _hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterSourceCombiBoiler
-------------------------

<JSON object>

* Parent(s): :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_22_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSourceWet`` **(required)**: :ref:`heatsourcewet_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``daily_HW_usage`` **(required)**: :ref:`daily_hw_usage_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rejected_energy_1``: :ref:`rejected_energy_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rejected_factor_3``: :ref:`rejected_factor_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``separate_DHW_tests`` **(required)**: :ref:`boilerhotwatertest_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``setpoint_temp`` **(required)**: :ref:`setpoint_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``storage_loss_factor_2``: :ref:`storage_loss_factor_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_22_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'CombiBoiler'

.. _coldwatersource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcewet_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heatsourcewet
-------------

<JSON string>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _daily_hw_usage_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Daily Hw Usage
--------------

<JSON number>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _rejected_energy_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rejected Energy 1
-----------------

<JSON value>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _rejected_factor_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rejected Factor 3
-----------------

<JSON value>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _setpoint_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Setpoint Temp
-------------

<JSON number>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _storage_loss_factor_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Storage Loss Factor 2
---------------------

<JSON value>

* Parent: :ref:`hotwatersourcecombiboiler_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _hotwatersourcehui_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterSourceHUI
-----------------

<JSON object>

* Parent(s): :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_23_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSourceWet`` **(required)**: :ref:`heatsourcewet_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``setpoint_temp``: :ref:`setpoint_temp_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_23_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`hotwatersourcehui_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HIU'

.. _coldwatersource_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`hotwatersourcehui_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcewet_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heatsourcewet
-------------

<JSON string>

* Parent: :ref:`hotwatersourcehui_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _setpoint_temp_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Setpoint Temp
-------------

<JSON value>

* Parent: :ref:`hotwatersourcehui_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _hotwatersourceheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterSourceHeatBattery
-------------------------

<JSON object>

* Parent(s): :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_24_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSourceWet`` **(required)**: :ref:`heatsourcewet_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_24_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`hotwatersourceheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'HeatBattery'

.. _coldwatersource_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`hotwatersourceheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsourcewet_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heatsourcewet
-------------

<JSON string>

* Parent: :ref:`hotwatersourceheatbattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterSourcePointOfUse
------------------------

<JSON object>

* Parent(s): :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_25_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiency`` **(required)**: :ref:`efficiency_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``setpoint_temp`` **(required)**: :ref:`setpoint_temp_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_25_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'PointOfUse'

.. _coldwatersource_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _efficiency_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiency
----------

<JSON number>

* Parent: :ref:`hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _setpoint_temp_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Setpoint Temp
-------------

<JSON number>

* Parent: :ref:`hotwatersourcepointofuse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

HotWaterSourceSmartHotWaterTank
-------------------------------

<JSON object>

* Parent(s): :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_26_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply_pump`` **(required)**: :ref:`energysupply_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSource`` **(required)**: :ref:`heatsource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``daily_losses`` **(required)**: :ref:`daily_losses_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``init_temp`` **(required)**: :ref:`init_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_flow_rate_pump_l_per_min`` **(required)**: :ref:`max_flow_rate_pump_l_per_min_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_pump_kW`` **(required)**: :ref:`power_pump_kw_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``primary_pipework``: :ref:`primary_pipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_setpnt_max`` **(required)**: :ref:`temp_setpnt_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_usable`` **(required)**: :ref:`temp_usable_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``volume`` **(required)**: :ref:`volume_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_26_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'SmartHotWaterTank'

.. _coldwatersource_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply Pump
-----------------

<JSON string>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heatsource
----------

<JSON object>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON value>
    
    * OneOf:
    
      * :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'HeatPump_HWOnly': '#/$defs/HeatPumpHotWaterOnly', 'HeatSourceWet': '#/$defs/HeatSourceWetServiceWaterRegular', 'ImmersionHeater': '#/$defs/ImmersionHeater', 'SolarThermalSystem': '#/$defs/SolarThermalSystem'}, 'propertyName': 'type'}
    
    
    }

.. _daily_losses_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Daily Losses
------------

<JSON number>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _init_temp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Init Temp
---------

<JSON number>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _max_flow_rate_pump_l_per_min_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Flow Rate Pump L Per Min
----------------------------

<JSON number>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_pump_kw_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Pump Kw
-------------

<JSON number>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _primary_pipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Primary Pipework
----------------

<JSON value>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _temp_setpnt_max_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Setpnt Max
---------------

<JSON string>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of maximum state of charge values

.. _temp_usable_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Usable
-----------

<JSON number>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _volume_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Volume
------

<JSON number>

* Parent: :ref:`hotwatersourcesmarthotwatertank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ImmersionHeater
---------------

<JSON object>

* Parent(s): :ref:`heatsource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`heatsource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_27_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmax`` **(required)**: :ref:`controlmax_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmin`` **(required)**: :ref:`controlmin_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heater_position`` **(required)**: :ref:`heater_position_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power`` **(required)**: :ref:`power_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermostat_position``: :ref:`thermostat_position_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_27_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'ImmersionHeater'

.. _controlmax_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmax
----------

<JSON string>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of maximum temperature setpoints

.. _controlmin_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmin
----------

<JSON string>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of minimum temperature setpoints

.. _energysupply_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heater_position_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heater Position
---------------

<JSON number>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power
-----

<JSON number>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _thermostat_position_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermostat Position
-------------------

<JSON value>

* Parent: :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

InfiltrationVentilation
-----------------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Control_VentAdjustMax``: :ref:`control_ventadjustmax_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control_VentAdjustMin``: :ref:`control_ventadjustmin_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control_WindowAdjust``: :ref:`control_windowadjust_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Leaks`` **(required)**: :ref:`ventilationleaks_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``MechanicalVentilation``: :ref:`mechanicalventilation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Vents`` **(required)**: :ref:`vents_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ach_max_static_calcs``: :ref:`ach_max_static_calcs_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ach_min_static_calcs``: :ref:`ach_min_static_calcs_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``altitude`` **(required)**: :ref:`altitude_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cross_vent_possible`` **(required)**: :ref:`cross_vent_possible_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shield_class`` **(required)**: :ref:`ventilationshieldclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``terrain_class`` **(required)**: :ref:`terrainclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ventilation_zone_base_height`` **(required)**: :ref:`ventilation_zone_base_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``vent_opening_ratio_init``: :ref:`vent_opening_ratio_init_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _control_ventadjustmax_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Ventadjustmax
---------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _control_ventadjustmin_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Ventadjustmin
---------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _control_windowadjust_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Windowadjust
--------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _mechanicalventilation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Mechanicalventilation
---------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs:  {ANY_NAME: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}
    
    
  * <JSON null>

.. _vents_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Vents
-----

<JSON object>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs:  {ANY_NAME: :ref:`vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}

.. _ach_max_static_calcs_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Ach Max Static Calcs
--------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _ach_min_static_calcs_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Ach Min Static Calcs
--------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _altitude_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Altitude
--------

<JSON number>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _cross_vent_possible_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Cross Vent Possible
-------------------

<JSON boolean>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _ventilation_zone_base_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Ventilation Zone Base Height
----------------------------

<JSON number>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Base height of the ventilation zone relative to ground (m)

.. _vent_opening_ratio_init_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Vent Opening Ratio Init
-----------------------

<JSON value>

* Parent: :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _internalgains_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

InternalGains
-------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: A dictionary of internal gains entries where: - Keys are user-defined names (e.g., "ColdWaterLosses", "EvaporativeLosses", "metabolic gains", etc.) - Values conform to the InternalGainsDetails schema - No specific entries are required - all entries are optional and user-defined

* User-named name/value pairs:  {ANY_NAME: :ref:`internalgainsdetails_input_reference_core_hem_HEM_v0.36_FHS_v0.27`}

.. _internalgainsdetails_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

InternalGainsDetails
--------------------

<JSON object>

* Parent(s): :ref:`internalgains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``schedule`` **(required)**: :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start_day`` **(required)**: :ref:`start_day_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _start_day_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start Day
---------

<JSON integer>

* Parent: :ref:`internalgainsdetails_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Maximum: 365

* Minimum: 0

.. _time_series_step_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`internalgainsdetails_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _invertertype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

InverterType
------------

<JSON string>

* Parent(s): :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['optimised_inverter', 'string_inverter']

.. _mvhrlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

MVHRLocation
------------

<JSON string>

* Parent(s): :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['inside', 'outside']

.. _massdistributionclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

MassDistributionClass
---------------------

<JSON string>

* Parent(s): :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['D', 'E', 'I', 'IE', 'M']

.. _mechventtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

MechVentType
------------

<JSON string>

* Parent(s): :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['Intermittent MEV', 'Centralised continuous MEV', 'Decentralised continuous MEV', 'MVHR']

.. _mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

MechanicalVentilation
---------------------

<JSON object>

* Parent(s): :ref:`mechanicalventilation_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Control``: :ref:`control_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_11_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SFP`` **(required)**: :ref:`sfp_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``design_outdoor_air_flow_rate`` **(required)**: :ref:`design_outdoor_air_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ductwork``: :ref:`ductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mvhr_eff``: :ref:`mvhr_eff_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mvhr_location``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`mvhrlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``sup_air_flw_ctrl`` **(required)**: :ref:`supplyairflowratecontroltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``sup_air_temp_ctrl`` **(required)**: :ref:`supplyairtemperaturecontroltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``vent_type`` **(required)**: :ref:`mechventtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _control_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON value>

* Parent: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _energysupply_11_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _sfp_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Sfp
---

<JSON number>

* Parent: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Specific fan power, inclusive of any in use factors (unit: W/l/s)

.. _design_outdoor_air_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Design Outdoor Air Flow Rate
----------------------------

<JSON number>

* Parent: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: (unit: m³/hour)

.. _ductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Ductwork
--------

<JSON value>

* Parent: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _mvhr_eff_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Mvhr Eff
--------

<JSON value>

* Parent: :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: MVHR efficiency

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

MechanicalVentilationDuctwork
-----------------------------

<JSON object>

* Parent(s): :ref:`ductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``cross_section_shape`` **(required)**: :ref:`ductshape_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``duct_perimeter_mm``: :ref:`duct_perimeter_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``duct_type`` **(required)**: :ref:`ducttype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``external_diameter_mm``: :ref:`external_diameter_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``insulation_thermal_conductivity`` **(required)**: :ref:`insulation_thermal_conductivity_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``insulation_thickness_mm`` **(required)**: :ref:`insulation_thickness_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``internal_diameter_mm``: :ref:`internal_diameter_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``length`` **(required)**: :ref:`length_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``reflective`` **(required)**: :ref:`reflective_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _duct_perimeter_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Duct Perimeter Mm
-----------------

<JSON value>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _external_diameter_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

External Diameter Mm
--------------------

<JSON value>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _insulation_thermal_conductivity_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Insulation Thermal Conductivity
-------------------------------

<JSON number>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _insulation_thickness_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Insulation Thickness Mm
-----------------------

<JSON number>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _internal_diameter_mm_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Internal Diameter Mm
--------------------

<JSON value>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _length_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Length
------

<JSON number>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _reflective_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Reflective
----------

<JSON boolean>

* Parent: :ref:`mechanicalventilationductwork_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _otherwateruse_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

OtherWaterUse
-------------

<JSON object>

* Parent(s): :ref:`other_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``flowrate`` **(required)**: :ref:`flowrate_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _coldwatersource_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`otherwateruse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _flowrate_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Flowrate
--------

<JSON number>

* Parent: :ref:`otherwateruse_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tap/outlet flow rate (unit: litre/minute)

.. _photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

PhotovoltaicSystem
------------------

<JSON object>

* Parent(s): :ref:`onsitegeneration_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_28_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_12_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``base_height`` **(required)**: :ref:`base_height_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height`` **(required)**: :ref:`height_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``inverter_is_inside`` **(required)**: :ref:`inverter_is_inside_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``inverter_peak_power_ac`` **(required)**: :ref:`inverter_peak_power_ac_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``inverter_peak_power_dc`` **(required)**: :ref:`inverter_peak_power_dc_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``inverter_type`` **(required)**: :ref:`invertertype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``orientation360`` **(required)**: :ref:`orientation360_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``peak_power`` **(required)**: :ref:`peak_power_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shading`` **(required)**: :ref:`shading_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ventilation_strategy`` **(required)**: :ref:`photovoltaicventilationstrategy_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``width`` **(required)**: :ref:`width_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_28_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'PhotovoltaicSystem'

.. _energysupply_12_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _base_height_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Base Height
-----------

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The distance between the ground and the lowest edge of the PV array (unit: m)

.. _height_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height
------

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Height of the PV array (unit: m)

.. _inverter_is_inside_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Inverter Is Inside
------------------

<JSON boolean>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Whether the inverter is considered inside the building

.. _inverter_peak_power_ac_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Inverter Peak Power Ac
----------------------

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _inverter_peak_power_dc_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Inverter Peak Power Dc
----------------------

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _orientation360_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Orientation360
--------------

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The orientation angle of the inclined surface, expressed as the geographical azimuth angle of the horizontal projection of the inclined surface normal, 0 to 360 (unit: ˚)

.. _peak_power_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Peak Power
----------

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Peak power; represents the electrical power of a photovoltaic system with a given area for a solar irradiance of 1 kW/m² on this surface (at 25 degrees) (unit: kW)

.. _pitch_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The tilt angle (inclination) of the PV panel from horizontal, measured upwards facing, 0 to 90 (unit: ˚)

.. _shading_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Shading
-------

<JSON array>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON value>

* AnyOf:

  * :ref:`windowshadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27`



.. _width_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Width
-----

<JSON number>

* Parent: :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Width of the PV panel (unit: m)

.. _photovoltaicventilationstrategy_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

PhotovoltaicVentilationStrategy
-------------------------------

<JSON string>

* Parent(s): :ref:`photovoltaicsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['unventilated', 'moderately_ventilated', 'strongly_or_forced_ventilated', 'rear_surface_free']

.. _scheduleentryforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleEntryForBoolean
-----------------------

<JSON value>

* Parent(s): :ref:`scheduleforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON boolean>
    
    
  * :ref:`schedulerepeaterforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * <JSON string>
    
    
  * <JSON null>

.. _scheduleentryfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleEntryForDouble
----------------------

<JSON value>

* Parent(s): :ref:`schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON number>
    
    
  * :ref:`schedulerepeaterfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * <JSON string>
    
    
  * <JSON null>

.. _scheduleforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleForBoolean
------------------

<JSON object>

* Parent(s): :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`controlonofftimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: A dictionary of schedule entries where: - Keys are user-defined names (e.g., "main", "week", "weekday", "weekend") - Values are lists of ScheduleEntryForBoolean - The "main" entry is required

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: :ref:`scheduleentryforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
    }

.. _schedulefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleForDouble
-----------------

<JSON object>

* Parent(s): :ref:`appliancegains_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`boilercostschedulehybrid_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`boilercostschedulehybrid_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`chargelevel_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`controlchargetarget_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`controlonoffcostminimising_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`controlsetpointtimer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`internalgainsdetails_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: A dictionary of schedule entries where: - Keys are user-defined names (e.g., "main", "week", "weekday", "weekend") - Values are lists of ScheduleEntryForDouble - The "main" entry is required

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: :ref:`scheduleentryfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
    }

.. _schedulerepeaterentryforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleRepeaterEntryForBoolean
-------------------------------

<JSON value>

* Parent(s): :ref:`schedulerepeatervalueforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON boolean>
    
    
  * <JSON null>

.. _schedulerepeaterentryfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleRepeaterEntryForDouble
------------------------------

<JSON value>

* Parent(s): :ref:`schedulerepeatervaluefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _schedulerepeaterforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleRepeaterForBoolean
--------------------------

<JSON object>

* Parent(s): :ref:`scheduleentryforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``repeat`` **(required)**: :ref:`repeat_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``value`` **(required)**: :ref:`schedulerepeatervalueforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _repeat_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Repeat
------

<JSON integer>

* Parent: :ref:`schedulerepeaterforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Minimum: 0

.. _schedulerepeaterfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleRepeaterForDouble
-------------------------

<JSON object>

* Parent(s): :ref:`scheduleentryfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``repeat`` **(required)**: :ref:`repeat_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``value`` **(required)**: :ref:`schedulerepeatervaluefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _repeat_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Repeat
------

<JSON integer>

* Parent: :ref:`schedulerepeaterfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Minimum: 0

.. _schedulerepeatervalueforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleRepeaterValueForBoolean
-------------------------------

<JSON value>

* Parent(s): :ref:`schedulerepeaterforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON string>
    
    
  * :ref:`schedulerepeaterentryforboolean_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _schedulerepeatervaluefordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ScheduleRepeaterValueForDouble
------------------------------

<JSON value>

* Parent(s): :ref:`schedulerepeaterfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON string>
    
    
  * :ref:`schedulerepeaterentryfordouble_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _shadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ShadingObject
-------------

<JSON object>

* Parent(s): :ref:`shading_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``distance`` **(required)**: :ref:`distance_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height`` **(required)**: :ref:`height_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``type`` **(required)**: :ref:`shadingobjecttype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _distance_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Distance
--------

<JSON number>

* Parent: :ref:`shadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _height_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height
------

<JSON number>

* Parent: :ref:`shadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _shadingobjecttype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ShadingObjectType
-----------------

<JSON string>

* Parent(s): :ref:`shadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['obstacle', 'overhang']

.. _shadingsegment_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ShadingSegment
--------------

<JSON object>

* Parent(s): :ref:`shading_segments_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``end360`` **(required)**: :ref:`end360_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``shading``: :ref:`shading_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start360`` **(required)**: :ref:`start360_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _end360_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

End360
------

<JSON number>

* Parent: :ref:`shadingsegment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _shading_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Shading
-------

<JSON value>

* Parent: :ref:`shadingsegment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`shadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _start360_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start360
--------

<JSON number>

* Parent: :ref:`shadingsegment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _showerinstantelectric_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ShowerInstantElectric
---------------------

<JSON object>

* Parent(s): :ref:`shower_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_29_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_13_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rated_power`` **(required)**: :ref:`rated_power_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_29_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`showerinstantelectric_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'InstantElecShower'

.. _coldwatersource_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`showerinstantelectric_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_13_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`showerinstantelectric_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _rated_power_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rated Power
-----------

<JSON number>

* Parent: :ref:`showerinstantelectric_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _showermixer_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ShowerMixer
-----------

<JSON object>

* Parent(s): :ref:`shower_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_30_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``WWHRS``: :ref:`wwhrs_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``flowrate`` **(required)**: :ref:`flowrate_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_30_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`showermixer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'MixerShower'

.. _coldwatersource_9_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`showermixer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _wwhrs_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Wwhrs
-----

<JSON value>

* Parent: :ref:`showermixer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a key in Input.WWHRS

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _flowrate_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Flowrate
--------

<JSON number>

* Parent: :ref:`showermixer_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Shower flow rate (unit: litre/minute)

.. _simulationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SimulationTime
--------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``end`` **(required)**: :ref:`end_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start`` **(required)**: :ref:`start_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``step`` **(required)**: :ref:`step_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _end_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

End
---

<JSON number>

* Parent: :ref:`simulationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _start_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start
-----

<JSON number>

* Parent: :ref:`simulationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _step_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Step
----

<JSON number>

* Parent: :ref:`simulationtime_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _smartappliancebattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SmartApplianceBattery
---------------------

<JSON object>

* Parent(s): :ref:`smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``battery_state_of_charge`` **(required)**: :ref:`battery_state_of_charge_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``energy_into_battery_from_generation`` **(required)**: :ref:`energy_into_battery_from_generation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``energy_into_battery_from_grid`` **(required)**: :ref:`energy_into_battery_from_grid_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``energy_out_of_battery`` **(required)**: :ref:`energy_out_of_battery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _battery_state_of_charge_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Battery State Of Charge
-----------------------

<JSON object>

* Parent: :ref:`smartappliancebattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
    }

.. _energy_into_battery_from_generation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energy Into Battery From Generation
-----------------------------------

<JSON object>

* Parent: :ref:`smartappliancebattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
    }

.. _energy_into_battery_from_grid_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energy Into Battery From Grid
-----------------------------

<JSON object>

* Parent: :ref:`smartappliancebattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
    }

.. _energy_out_of_battery_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energy Out Of Battery
---------------------

<JSON object>

* Parent: :ref:`smartappliancebattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
    }

.. _smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SmartApplianceControl
---------------------

<JSON object>

* Parent(s): :ref:`smartappliancecontrols_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Appliances`` **(required)**: :ref:`appliances_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``battery24hr`` **(required)**: :ref:`smartappliancebattery_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``non_appliance_demand_24hr`` **(required)**: :ref:`non_appliance_demand_24hr_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_timeseries`` **(required)**: :ref:`power_timeseries_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``time_series_step`` **(required)**: :ref:`time_series_step_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _appliances_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Appliances
----------

<JSON array>

* Parent: :ref:`smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON string>



.. _non_appliance_demand_24hr_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Non Appliance Demand 24Hr
-------------------------

<JSON object>

* Parent: :ref:`smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
    }

.. _power_timeseries_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Timeseries
----------------

<JSON object>

* Parent: :ref:`smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON array>
    
    * Items: <JSON number>
    
    
    
    
    }

.. _time_series_step_7_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Time Series Step
----------------

<JSON number>

* Parent: :ref:`smartappliancecontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _solarcollectorlooplocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SolarCollectorLoopLocation
--------------------------

<JSON string>

* Parent(s): :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['OUT', 'HS', 'NHS']

* Description: Location of the main part of the solar thermal collector loop piping.  This affects the ambient temperature used for heat loss calculations in the collector loop piping.

.. _solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SolarThermalSystem
------------------

<JSON object>

* Parent(s): :ref:`heatsource_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`heatsource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_31_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Controlmax`` **(required)**: :ref:`controlmax_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_14_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area_module`` **(required)**: :ref:`area_module_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``collector_mass_flow_rate`` **(required)**: :ref:`collector_mass_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``first_order_hlc`` **(required)**: :ref:`first_order_hlc_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heater_position`` **(required)**: :ref:`heater_position_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``incidence_angle_modifier`` **(required)**: :ref:`incidence_angle_modifier_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``modules`` **(required)**: :ref:`modules_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``orientation360`` **(required)**: :ref:`orientation360_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``peak_collector_efficiency`` **(required)**: :ref:`peak_collector_efficiency_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_pump`` **(required)**: :ref:`power_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``power_pump_control`` **(required)**: :ref:`power_pump_control_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``second_order_hlc`` **(required)**: :ref:`second_order_hlc_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``sol_loc`` **(required)**: :ref:`solarcollectorlooplocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``solar_loop_piping_hlc`` **(required)**: :ref:`solar_loop_piping_hlc_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermostat_position``: :ref:`thermostat_position_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``tilt`` **(required)**: :ref:`tilt_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_31_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'SolarThermalSystem'

.. _controlmax_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlmax
----------

<JSON string>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference to a control schedule of maximum temperature setpoints

.. _energysupply_14_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _area_module_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area Module
-----------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _collector_mass_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Collector Mass Flow Rate
------------------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _first_order_hlc_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

First Order Hlc
---------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heater_position_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heater Position
---------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _incidence_angle_modifier_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Incidence Angle Modifier
------------------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _modules_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Modules
-------

<JSON integer>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Minimum: 1

.. _orientation360_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Orientation360
--------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The orientation angle of the inclined surface, expressed as the geographical azimuth angle of the horizontal projection of the inclined surface normal, 0 to 360 (unit: ˚)

.. _peak_collector_efficiency_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Peak Collector Efficiency
-------------------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_pump_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Pump
----------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _power_pump_control_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Power Pump Control
------------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _second_order_hlc_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Second Order Hlc
----------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _solar_loop_piping_hlc_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Solar Loop Piping Hlc
---------------------

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _thermostat_position_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermostat Position
-------------------

<JSON value>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Required for StorageTank but not for SmartHotWaterTank

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _tilt_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Tilt
----

<JSON number>

* Parent: :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceCoolSystemAirConditioning
------------------------------

<JSON object>

* Parent(s): :ref:`spacecoolsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_32_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control`` **(required)**: :ref:`control_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_15_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``cooling_capacity`` **(required)**: :ref:`cooling_capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiency`` **(required)**: :ref:`efficiency_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_32_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'AirConditioning'

.. _control_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON string>

* Parent: :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_15_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _cooling_capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Cooling Capacity
----------------

<JSON number>

* Parent: :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Maximum cooling capacity of the system (unit: kW)

.. _efficiency_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiency
----------

<JSON number>

* Parent: :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _frac_convective_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`spacecoolsystemairconditioning_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Convective fraction for cooling

.. _spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystemElectricStorageHeater
------------------------------------

<JSON object>

* Parent(s): :ref:`spaceheatsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_33_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ControlCharger`` **(required)**: :ref:`controlcharger_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ESH_max_output`` **(required)**: :ref:`esh_max_output_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ESH_min_output`` **(required)**: :ref:`esh_min_output_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_16_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``air_flow_type`` **(required)**: :ref:`airflowtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control`` **(required)**: :ref:`control_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``fan_pwr`` **(required)**: :ref:`fan_pwr_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``n_units`` **(required)**: :ref:`n_units_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pwr_in`` **(required)**: :ref:`pwr_in_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rated_power_instant`` **(required)**: :ref:`rated_power_instant_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``storage_capacity`` **(required)**: :ref:`storage_capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Zone`` **(required)**: :ref:`zone_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_setback``: :ref:`temp_setback_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``advanced_start``: :ref:`advanced_start_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_33_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'ElecStorageHeater'

.. _controlcharger_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Controlcharger
--------------

<JSON string>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _esh_max_output_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Esh Max Output
--------------

<JSON array>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON array>

* MaxItems: 2

* MinItems: 2

* Items: <JSON number>





.. _esh_min_output_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Esh Min Output
--------------

<JSON array>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON array>

* MaxItems: 2

* MinItems: 2

* Items: <JSON number>





.. _energysupply_16_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _control_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON string>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _fan_pwr_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Fan Pwr
-------

<JSON number>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Fan power (unit: W)

.. _frac_convective_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Convective fraction for heating

.. _n_units_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

N Units
-------

<JSON integer>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Minimum: 0

.. _pwr_in_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pwr In
------

<JSON number>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _rated_power_instant_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rated Power Instant
-------------------

<JSON number>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: (instant backup) (unit: kW)

.. _storage_capacity_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Storage Capacity
----------------

<JSON number>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _zone_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Zone
----

<JSON string>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The zone where the unit(s) is/are installed

.. _temp_setback_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Setback
------------

<JSON value>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _advanced_start_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Advanced Start
--------------

<JSON value>

* Parent: :ref:`spaceheatsystemelectricstorageheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _spaceheatsystemheatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystemHeatSource
-------------------------

<JSON object>

* Parent(s): :ref:`spaceheatsystemwarmair_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``name`` **(required)**: :ref:`name_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_flow_limit_upper``: :ref:`temp_flow_limit_upper_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _name_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Name
----

<JSON string>

* Parent: :ref:`spaceheatsystemheatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temp_flow_limit_upper_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Flow Limit Upper
---------------------

<JSON value>

* Parent: :ref:`spaceheatsystemheatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystemInstantElectricHeater
------------------------------------

<JSON object>

* Parent(s): :ref:`spaceheatsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_34_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply`` **(required)**: :ref:`energysupply_17_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control`` **(required)**: :ref:`control_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``rated_power`` **(required)**: :ref:`rated_power_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_34_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'InstantElecHeater'

.. _energysupply_17_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON string>

* Parent: :ref:`spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _control_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON string>

* Parent: :ref:`spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _frac_convective_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Convective fraction for heating

.. _rated_power_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Rated Power
-----------

<JSON number>

* Parent: :ref:`spaceheatsysteminstantelectricheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: (unit: kW)

.. _spaceheatsystemwarmair_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystemWarmAir
----------------------

<JSON object>

* Parent(s): :ref:`spaceheatsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_35_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSource`` **(required)**: :ref:`spaceheatsystemheatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control`` **(required)**: :ref:`control_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_35_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`spaceheatsystemwarmair_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'WarmAir'

.. _control_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON string>

* Parent: :ref:`spaceheatsystemwarmair_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _frac_convective_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`spaceheatsystemwarmair_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SpaceHeatSystemWetDistribution
------------------------------

<JSON object>

* Parent(s): :ref:`spaceheatsystem_choice_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_36_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSource`` **(required)**: :ref:`spaceheatsystemheatsource_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``bypass_percentage_recirculated``: :ref:`bypass_percentage_recirculated_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``design_flow_rate``: :ref:`design_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``design_flow_temp`` **(required)**: :ref:`design_flow_temp_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``emitters`` **(required)**: :ref:`emitters_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ecodesign_controller`` **(required)**: :ref:`ecodesigncontroller_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``max_flow_rate``: :ref:`max_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``min_flow_rate``: :ref:`min_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_diff_emit_dsgn`` **(required)**: :ref:`temp_diff_emit_dsgn_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``thermal_mass``: :ref:`thermal_mass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``variable_flow`` **(required)**: :ref:`variable_flow_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control`` **(required)**: :ref:`control_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``EnergySupply``: :ref:`energysupply_18_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Zone`` **(required)**: :ref:`zone_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_36_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'WetDistribution'

.. _bypass_percentage_recirculated_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Bypass Percentage Recirculated
------------------------------

<JSON value>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _design_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Design Flow Rate
----------------

<JSON value>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _design_flow_temp_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Design Flow Temp
----------------

<JSON integer>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _emitters_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Emitters
--------

<JSON array>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* MinItems: 1

* Items: <JSON value>

* OneOf:

  * :ref:`wetemitterradiator_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * :ref:`wetemitterfancoil_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Non-JSON Schema keywords:

  * discriminator: {'mapping': {'fancoil': '#/$defs/WetEmitterFanCoil', 'radiator': '#/$defs/WetEmitterRadiator', 'ufh': '#/$defs/WetEmitterUFH'}, 'propertyName': 'wet_emitter_type'}



.. _max_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Max Flow Rate
-------------

<JSON value>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _min_flow_rate_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Min Flow Rate
-------------

<JSON value>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _temp_diff_emit_dsgn_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Diff Emit Dsgn
-------------------

<JSON number>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _thermal_mass_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermal Mass
------------

<JSON value>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _variable_flow_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Variable Flow
-------------

<JSON boolean>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _control_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control
-------

<JSON string>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _energysupply_18_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Energysupply
------------

<JSON value>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _zone_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Zone
----

<JSON string>

* Parent: :ref:`spaceheatsystemwetdistribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

StorageTank
-----------

<JSON object>

* Parent(s): :ref:`preheatedwatersource_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`hw_cylinder_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_37_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``HeatSource`` **(required)**: :ref:`heatsource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``daily_losses`` **(required)**: :ref:`daily_losses_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_exchanger_surface_area``: :ref:`heat_exchanger_surface_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``init_temp`` **(required)**: :ref:`init_temp_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``primary_pipework``: :ref:`primary_pipework_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``volume`` **(required)**: :ref:`volume_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_37_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'StorageTank'

.. _coldwatersource_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _heatsource_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heatsource
----------

<JSON object>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON value>
    
    * OneOf:
    
      * :ref:`immersionheater_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`solarthermalsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`heatsourcewetservicewaterregular_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`heatpumphotwateronly_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'HeatPump_HWOnly': '#/$defs/HeatPumpHotWaterOnly', 'HeatSourceWet': '#/$defs/HeatSourceWetServiceWaterRegular', 'ImmersionHeater': '#/$defs/ImmersionHeater', 'SolarThermalSystem': '#/$defs/SolarThermalSystem'}, 'propertyName': 'type'}
    
    
    }

.. _daily_losses_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Daily Losses
------------

<JSON number>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Measured standby losses due to cylinder insulation at standardised conditions (unit: kWh/24h)

.. _heat_exchanger_surface_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Exchanger Surface Area
---------------------------

<JSON value>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _init_temp_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Init Temp
---------

<JSON number>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _primary_pipework_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Primary Pipework
----------------

<JSON value>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON array>
    
    * Items: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    
  * <JSON null>

.. _volume_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Volume
------

<JSON number>

* Parent: :ref:`storagetank_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Total volume of tank (unit: litre)

.. _supplyairflowratecontroltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SupplyAirFlowRateControlType
----------------------------

<JSON string>

* Parent(s): :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['ODA']

.. _supplyairtemperaturecontroltype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

SupplyAirTemperatureControlType
-------------------------------

<JSON string>

* Parent(s): :ref:`mechanicalventilation_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['CONST', 'NO_CTRL', 'LOAD_COM']

.. _terrainclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

TerrainClass
------------

<JSON string>

* Parent(s): :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['OpenWater', 'OpenField', 'Suburban', 'Urban']

.. _testletter_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

TestLetter
----------

<JSON string>

* Parent(s): :ref:`heatpumptestdatum_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['A', 'B', 'C', 'D', 'F']

.. _thermalbridginglinear_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ThermalBridgingLinear
---------------------

<JSON object>

* Parent(s): :ref:`thermalbridging_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_38_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``length`` **(required)**: :ref:`length_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``linear_thermal_transmittance`` **(required)**: :ref:`linear_thermal_transmittance_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_38_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`thermalbridginglinear_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'ThermalBridgeLinear'

.. _length_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Length
------

<JSON number>

* Parent: :ref:`thermalbridginglinear_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _linear_thermal_transmittance_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Linear Thermal Transmittance
----------------------------

<JSON number>

* Parent: :ref:`thermalbridginglinear_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _thermalbridgingpoint_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ThermalBridgingPoint
--------------------

<JSON object>

* Parent(s): :ref:`thermalbridging_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_39_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``heat_transfer_coeff`` **(required)**: :ref:`heat_transfer_coeff_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_39_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`thermalbridgingpoint_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'ThermalBridgePoint'

.. _heat_transfer_coeff_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Heat Transfer Coeff
-------------------

<JSON number>

* Parent: :ref:`thermalbridgingpoint_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Vent
----

<JSON object>

* Parent(s): :ref:`vents_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``area_cm2`` **(required)**: :ref:`area_cm2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``mid_height_air_flow_path`` **(required)**: :ref:`mid_height_air_flow_path_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``orientation360`` **(required)**: :ref:`orientation360_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pitch`` **(required)**: :ref:`pitch_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pressure_difference_ref`` **(required)**: :ref:`pressure_difference_ref_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _area_cm2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area Cm2
--------

<JSON number>

* Parent: :ref:`vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _mid_height_air_flow_path_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Mid Height Air Flow Path
------------------------

<JSON number>

* Parent: :ref:`vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _orientation360_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Orientation360
--------------

<JSON number>

* Parent: :ref:`vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: The orientation angle of the inclined surface, expressed as the geographical azimuth angle of the horizontal projection of the inclined surface normal, 0 to 360 (unit: ˚)

.. _pitch_10_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pitch
-----

<JSON number>

* Parent: :ref:`vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)

.. _pressure_difference_ref_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Pressure Difference Ref
-----------------------

<JSON number>

* Parent: :ref:`vent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference pressure difference for an air terminal device (unit: Pa)

.. _ventilationleaks_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

VentilationLeaks
----------------

<JSON object>

* Parent(s): :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``env_area`` **(required)**: :ref:`env_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``test_pressure`` **(required)**: :ref:`test_pressure_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``test_result`` **(required)**: :ref:`test_result_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ventilation_zone_height`` **(required)**: :ref:`ventilation_zone_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _env_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Env Area
--------

<JSON number>

* Parent: :ref:`ventilationleaks_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference area of the envelope airtightness index

.. _test_pressure_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Test Pressure
-------------

<JSON number>

* Parent: :ref:`ventilationleaks_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Reference pressure difference (unit: Pa)

.. _test_result_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Test Result
-----------

<JSON number>

* Parent: :ref:`ventilationleaks_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Flow rate through

.. _ventilation_zone_height_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Ventilation Zone Height
-----------------------

<JSON number>

* Parent: :ref:`ventilationleaks_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _ventilationshieldclass_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

VentilationShieldClass
----------------------

<JSON string>

* Parent(s): :ref:`infiltrationventilation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['Open', 'Normal', 'Shielded']

.. _wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WasteWaterHeatRecoverySystem
----------------------------

<JSON object>

* Parent(s): :ref:`wwhrs_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``ColdWaterSource`` **(required)**: :ref:`coldwatersource_11_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``efficiencies`` **(required)**: :ref:`efficiencies_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``flow_rates`` **(required)**: :ref:`flow_rates_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``type`` **(required)**: :ref:`wastewaterheatrecoverysystemtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``utilisation_factor`` **(required)**: :ref:`utilisation_factor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _coldwatersource_11_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Coldwatersource
---------------

<JSON string>

* Parent: :ref:`wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _efficiencies_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Efficiencies
------------

<JSON array>

* Parent: :ref:`wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON number>



.. _flow_rates_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Flow Rates
----------

<JSON array>

* Parent: :ref:`wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Items: <JSON number>



.. _utilisation_factor_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Utilisation Factor
------------------

<JSON number>

* Parent: :ref:`wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _wastewaterheatrecoverysystemtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WasteWaterHeatRecoverySystemType
--------------------------------

<JSON string>

* Parent(s): :ref:`wastewaterheatrecoverysystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['WWHRS_InstantaneousSystemA', 'WWHRS_InstantaneousSystemB', 'WWHRS_InstantaneousSystemC']

.. _waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WaterHeatingEvent
-----------------

<JSON object>

* Parent(s): :ref:`shower_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`bath_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`other_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``duration``: :ref:`duration_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``start`` **(required)**: :ref:`start_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temperature`` **(required)**: :ref:`temperature_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``volume``: :ref:`volume_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _duration_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Duration
--------

<JSON value>

* Parent: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _start_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Start
-----

<JSON number>

* Parent: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _temperature_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temperature
-----------

<JSON number>

* Parent: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _volume_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Volume
------

<JSON value>

* Parent: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _waterheatingevents_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WaterHeatingEvents
------------------

<JSON object>

* Parent(s): :ref:`input_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Shower``: :ref:`shower_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Bath``: :ref:`bath_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Other``: :ref:`other_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _shower_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Shower
------

<JSON value>

* Parent: :ref:`waterheatingevents_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs: 
    
      * {ANY_NAME:
    
        * <JSON array>
        
        * Items: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        
        
        }
    
    
  * <JSON null>

.. _bath_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Bath
----

<JSON value>

* Parent: :ref:`waterheatingevents_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs: 
    
      * {ANY_NAME:
    
        * <JSON array>
        
        * Items: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        
        
        }
    
    
  * <JSON null>

.. _other_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Other
-----

<JSON value>

* Parent: :ref:`waterheatingevents_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON object>
    
    * User-named name/value pairs: 
    
      * {ANY_NAME:
    
        * <JSON array>
        
        * Items: :ref:`waterheatingevent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        
        
        }
    
    
  * <JSON null>

.. _waterpipecontentstype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WaterPipeContentsType
---------------------

<JSON string>

* Parent(s): :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['water', 'glycol25']

.. _waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WaterPipework
-------------

<JSON object>

* Parent(s): :ref:`primary_pipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`primary_pipework_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``external_diameter_mm`` **(required)**: :ref:`external_diameter_mm_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``insulation_thermal_conductivity`` **(required)**: :ref:`insulation_thermal_conductivity_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``insulation_thickness_mm`` **(required)**: :ref:`insulation_thickness_mm_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``internal_diameter_mm`` **(required)**: :ref:`internal_diameter_mm_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``length`` **(required)**: :ref:`length_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``location`` **(required)**: :ref:`waterpipeworklocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``pipe_contents`` **(required)**: :ref:`waterpipecontentstype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``surface_reflectivity`` **(required)**: :ref:`surface_reflectivity_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _external_diameter_mm_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

External Diameter Mm
--------------------

<JSON number>

* Parent: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _insulation_thermal_conductivity_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Insulation Thermal Conductivity
-------------------------------

<JSON number>

* Parent: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _insulation_thickness_mm_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Insulation Thickness Mm
-----------------------

<JSON number>

* Parent: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _internal_diameter_mm_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Internal Diameter Mm
--------------------

<JSON number>

* Parent: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _length_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Length
------

<JSON number>

* Parent: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _surface_reflectivity_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Surface Reflectivity
--------------------

<JSON boolean>

* Parent: :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _waterpipeworklocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WaterPipeworkLocation
---------------------

<JSON string>

* Parent(s): :ref:`waterpipework_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`waterpipeworksimple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['internal', 'external']

.. _waterpipeworksimple_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WaterPipeworkSimple
-------------------

<JSON object>

* Parent(s): :ref:`distribution_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``internal_diameter_mm`` **(required)**: :ref:`internal_diameter_mm_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``length`` **(required)**: :ref:`length_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``location`` **(required)**: :ref:`waterpipeworklocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _internal_diameter_mm_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Internal Diameter Mm
--------------------

<JSON number>

* Parent: :ref:`waterpipeworksimple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _length_3_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Length
------

<JSON number>

* Parent: :ref:`waterpipeworksimple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _wetemitterfancoil_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WetEmitterFanCoil
-----------------

<JSON object>

* Parent(s): :ref:`emitters_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``wet_emitter_type`` **(required)**: :ref:`wet_emitter_type_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``fancoil_test_data`` **(required)**: :ref:`fancoiltestdata_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``n_units``: :ref:`n_units_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _wet_emitter_type_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Wet Emitter Type
----------------

<JSON string>

* Parent: :ref:`wetemitterfancoil_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'fancoil'

.. _frac_convective_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`wetemitterfancoil_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _n_units_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

N Units
-------

<JSON value>

* Parent: :ref:`wetemitterfancoil_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: 1

* AnyOf:

  * <JSON integer>
    
    * ExclusiveMinimum: 0
    
    
  * <JSON null>

.. _wetemitterradiator_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WetEmitterRadiator
------------------

<JSON object>

* Parent(s): :ref:`emitters_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``wet_emitter_type`` **(required)**: :ref:`wet_emitter_type_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``c`` **(required)**: :ref:`c_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``n`` **(required)**: :ref:`n_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _wet_emitter_type_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Wet Emitter Type
----------------

<JSON string>

* Parent: :ref:`wetemitterradiator_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'radiator'

.. _c_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

C
-

<JSON number>

* Parent: :ref:`wetemitterradiator_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _frac_convective_5_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`wetemitterradiator_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _n_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

N
-

<JSON number>

* Parent: :ref:`wetemitterradiator_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WetEmitterUFH
-------------

<JSON object>

* Parent(s): :ref:`emitters_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``wet_emitter_type`` **(required)**: :ref:`wet_emitter_type_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``emitter_floor_area`` **(required)**: :ref:`emitter_floor_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``equivalent_specific_thermal_mass`` **(required)**: :ref:`equivalent_specific_thermal_mass_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``frac_convective`` **(required)**: :ref:`frac_convective_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``system_performance_factor`` **(required)**: :ref:`system_performance_factor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _wet_emitter_type_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Wet Emitter Type
----------------

<JSON string>

* Parent: :ref:`wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'ufh'

.. _emitter_floor_area_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Emitter Floor Area
------------------

<JSON number>

* Parent: :ref:`wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _equivalent_specific_thermal_mass_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Equivalent Specific Thermal Mass
--------------------------------

<JSON number>

* Parent: :ref:`wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _frac_convective_6_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Frac Convective
---------------

<JSON number>

* Parent: :ref:`wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _system_performance_factor_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

System Performance Factor
-------------------------

<JSON number>

* Parent: :ref:`wetemitterufh_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _windshieldlocation_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindShieldLocation
------------------

<JSON string>

* Parent(s): :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['Sheltered', 'Average', 'Exposed']

.. _windowpart_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowPart
----------

<JSON object>

* Parent(s): :ref:`window_part_list_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``mid_height_air_flow_path`` **(required)**: :ref:`mid_height_air_flow_path_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _mid_height_air_flow_path_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Mid Height Air Flow Path
------------------------

<JSON number>

* Parent: :ref:`windowpart_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _windowshadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowShadingObject
-------------------

<JSON object>

* Parent(s): :ref:`shading_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`shading_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`windowshadingtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``depth`` **(required)**: :ref:`depth_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``distance`` **(required)**: :ref:`distance_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _depth_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Depth
-----

<JSON number>

* Parent: :ref:`windowshadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _distance_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Distance
--------

<JSON number>

* Parent: :ref:`windowshadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowShadingObstacle
---------------------

<JSON object>

* Parent(s): :ref:`shading_input_reference_core_hem_HEM_v0.36_FHS_v0.27`, :ref:`shading_1_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``type`` **(required)**: :ref:`type_40_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``height`` **(required)**: :ref:`height_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``distance`` **(required)**: :ref:`distance_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``transparency`` **(required)**: :ref:`transparency_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _type_40_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Type
----

<JSON string>

* Parent: :ref:`windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Const: 'obstacle'

.. _height_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Height
------

<JSON number>

* Parent: :ref:`windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _distance_2_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Distance
--------

<JSON number>

* Parent: :ref:`windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _transparency_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Transparency
------------

<JSON number>

* Parent: :ref:`windowshadingobstacle_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _windowshadingtype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowShadingType
-----------------

<JSON string>

* Parent(s): :ref:`windowshadingobject_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['overhang', 'sidefinright', 'sidefinleft', 'reveal']

.. _windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowTreatment
---------------

<JSON object>

* Parent(s): :ref:`treatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``Control_closing_irrad``: :ref:`control_closing_irrad_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control_open``: :ref:`control_open_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``Control_opening_irrad``: :ref:`control_opening_irrad_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``controls`` **(required)**: :ref:`windowtreatmentcontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``delta_r`` **(required)**: :ref:`delta_r_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``is_open``: :ref:`is_open_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``opening_delay_hrs``: :ref:`opening_delay_hrs_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``trans_red`` **(required)**: :ref:`trans_red_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``type`` **(required)**: :ref:`windowtreatmenttype_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _control_closing_irrad_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Closing Irrad
---------------------

<JSON value>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _control_open_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Open
------------

<JSON value>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _control_opening_irrad_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Control Opening Irrad
---------------------

<JSON value>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON null>

.. _delta_r_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Delta R
-------

<JSON number>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _is_open_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Is Open
-------

<JSON value>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: This field should be a boolean - any string provided will be ignored and treated as a null.

* Default: <JSON null>

* AnyOf:

  * <JSON boolean>
    
    
  * <JSON null>

.. _opening_delay_hrs_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Opening Delay Hrs
-----------------

<JSON value>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON number>
    
    
  * <JSON null>

.. _trans_red_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Trans Red
---------

<JSON number>

* Parent: :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _windowtreatmentcontrol_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowTreatmentControl
----------------------

<JSON string>

* Parent(s): :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['auto_motorised', 'combined_light_blind_HVAC', 'manual', 'manual_motorised']

.. _windowtreatmenttype_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

WindowTreatmentType
-------------------

<JSON string>

* Parent(s): :ref:`windowtreatment_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['blinds', 'curtains']

.. _zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Zone
----

<JSON object>

* Parent(s): :ref:`zone_collection_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Named name/value pairs:

  * ``BuildingElement`` **(required)**: :ref:`buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SpaceCoolSystem``: :ref:`spacecoolsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``SpaceHeatSystem``: :ref:`spaceheatsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``ThermalBridging`` **(required)**: :ref:`thermalbridging_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``area`` **(required)**: :ref:`area_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``temp_setpnt_basis``: 

    * <JSON value>
      
      * Default: <JSON null>
      
      * AnyOf:
      
        * :ref:`zonetemperaturecontrolbasis_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        * <JSON null>
      
      
  * ``temp_setpnt_init`` **(required)**: :ref:`temp_setpnt_init_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
  * ``volume`` **(required)**: :ref:`volume_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: NONE_ALLOWED

.. _buildingelement_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Buildingelement
---------------

<JSON object>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* User-named name/value pairs: 

  * {ANY_NAME:

    * <JSON value>
    
    * OneOf:
    
      * :ref:`buildingelementopaque_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`buildingelementtransparent_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * <JSON value>
        
        * OneOf:
        
          * :ref:`buildingelementgroundslabnoedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
          * :ref:`buildingelementgroundslabedgeinsulation_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
          * :ref:`buildingelementgroundsuspendedfloor_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
          * :ref:`buildingelementgroundheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
          * :ref:`buildingelementgroundunheatedbasement_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        
        * Non-JSON Schema keywords:
        
          * discriminator: {'mapping': {'Heated_basement': '#/$defs/BuildingElementGroundHeatedBasement', 'Slab_edge_insulation': '#/$defs/BuildingElementGroundSlabEdgeInsulation', 'Slab_no_edge_insulation': '#/$defs/BuildingElementGroundSlabNoEdgeInsulation', 'Suspended_floor': '#/$defs/BuildingElementGroundSuspendedFloor', 'Unheated_basement': '#/$defs/BuildingElementGroundUnheatedBasement'}, 'propertyName': 'floor_type'}
        
        
      * :ref:`buildingelementadjacentconditionedspace_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
      * :ref:`buildingelementadjacentunconditionedspace_simple_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
    
    * Non-JSON Schema keywords:
    
      * discriminator: {'mapping': {'BuildingElementAdjacentConditionedSpace': '#/$defs/BuildingElementAdjacentConditionedSpace', 'BuildingElementAdjacentUnconditionedSpace_Simple': '#/$defs/BuildingElementAdjacentUnconditionedSpace_Simple', 'BuildingElementGround': {'discriminator': {'mapping': {'Heated_basement': '#/$defs/BuildingElementGroundHeatedBasement', 'Slab_edge_insulation': '#/$defs/BuildingElementGroundSlabEdgeInsulation', 'Slab_no_edge_insulation': '#/$defs/BuildingElementGroundSlabNoEdgeInsulation', 'Suspended_floor': '#/$defs/BuildingElementGroundSuspendedFloor', 'Unheated_basement': '#/$defs/BuildingElementGroundUnheatedBasement'}, 'propertyName': 'floor_type'}, 'oneOf': [{'$ref': '#/$defs/BuildingElementGroundSlabNoEdgeInsulation'}, {'$ref': '#/$defs/BuildingElementGroundSlabEdgeInsulation'}, {'$ref': '#/$defs/BuildingElementGroundSuspendedFloor'}, {'$ref': '#/$defs/BuildingElementGroundHeatedBasement'}, {'$ref': '#/$defs/BuildingElementGroundUnheatedBasement'}]}, 'BuildingElementOpaque': '#/$defs/BuildingElementOpaque', 'BuildingElementTransparent': '#/$defs/BuildingElementTransparent'}, 'propertyName': 'type'}
    
    
    }

.. _spacecoolsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Spacecoolsystem
---------------

<JSON value>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON array>
    
    * UniqueItems: True
    
    * Items: <JSON string>
    
    
    
    
  * <JSON null>

.. _spaceheatsystem_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Spaceheatsystem
---------------

<JSON value>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Default: <JSON null>

* AnyOf:

  * <JSON string>
    
    
  * <JSON array>
    
    * UniqueItems: True
    
    * Items: <JSON string>
    
    
    
    
  * <JSON null>

.. _thermalbridging_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Thermalbridging
---------------

<JSON value>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* AnyOf:

  * <JSON number>
    
    
  * <JSON object>
    
    * User-named name/value pairs: 
    
      * {ANY_NAME:
    
        * <JSON value>
        
        * OneOf:
        
          * :ref:`thermalbridginglinear_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
          * :ref:`thermalbridgingpoint_input_reference_core_hem_HEM_v0.36_FHS_v0.27`
        
        * Non-JSON Schema keywords:
        
          * discriminator: {'mapping': {'ThermalBridgeLinear': '#/$defs/ThermalBridgingLinear', 'ThermalBridgePoint': '#/$defs/ThermalBridgingPoint'}, 'propertyName': 'type'}
        
        
        }
    
    

.. _area_8_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Area
----

<JSON number>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Useful floor area of the zone (unit: m²)

.. _temp_setpnt_init_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Temp Setpnt Init
----------------

<JSON number>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Description: Setpoint temperature to use during initialisation (unit: ˚C)

.. _volume_4_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

Volume
------

<JSON number>

* Parent: :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

.. _zonetemperaturecontrolbasis_input_reference_core_hem_HEM_v0.36_FHS_v0.27:

ZoneTemperatureControlBasis
---------------------------

<JSON string>

* Parent(s): :ref:`zone_input_reference_core_hem_HEM_v0.36_FHS_v0.27`

* Enum: ['air', 'operative']

