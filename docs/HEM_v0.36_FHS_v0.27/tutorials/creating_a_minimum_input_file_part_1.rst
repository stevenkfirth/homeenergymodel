
.. _creating_a_minimum_input_file_part_1_HEM_v0.36_FHS_v0.27:

1. Creating a minimum Input File: Part 1 
========================================

A useful way to start to understand the input files for building simulation models is to create the smallest possible input file from scratch.

This section creates a minimum input file for core HEM which validates against the core HEM JSON Schema.

An empty input file
-------------------

For the core HEM model, if we first take an empty input file:

.. code-block:: JSON
   :caption: in.json

   

... and then run a simulation using an EPW weather file named *in.epw*:

.. code-block:: bash
   :caption: Command prompt input

   python -m hem.py -w in.epw in.json

This gives the following output:

.. code-block::
   :caption: Command Prompt output

   ---stdout---

   Running 1 cases in series

   ---stderr---

   Traceback (most recent call last):

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 1104, in <module>

      run_project(

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 141, in run_project

      shading_segments = project_dict["ExternalConditions"].get("shading_segments")

                        ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

   TypeError: string indices must be integers, not 'str'

Hmm... not a good start. Given an empty input file and an EPW weather file, we get an uncaught exception (an error) and the programme code stops executing with automatically generated error message.

This isn't good practice. Errors are a normal part of programming, but good software will return an error message that provides information to the user on how to fix the problem.

This problem occurs because we have provided an empty file (an empty string) as the input file and HEM is expecting an JSON object as the root object in the input file. The *TypeError* occurs because ``project_dict`` is now a string, whereas the HEM code is expecting it to be a dictionary. A useful error message in this case would be:

  "The root object in the input file should be a JSON object, not a JSON string."

Looking at the source code in *hem.py* this issue should be picked up by the validation of the JSON input on line 162. The issue is that the error is happening on line 141, i.e. the input JSON is being queried by the code before the validation takes place.

An input file with an empty JSON object
---------------------------------------

Let's change the input file to an empty JSON object:

.. code-block:: JSON
   :caption: in.json

   {}

We now see a new error message:

.. code-block::
   :caption: Command Prompt output

   ---stdout---

   Running 1 cases in series

   ---stderr---

   Traceback (most recent call last):

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 1104, in <module>

      run_project(

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 141, in run_project

      shading_segments = project_dict["ExternalConditions"].get("shading_segments")

                        ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

   KeyError: 'ExternalConditions'

The uncaught exception has changed from *TypeError* to *KeyError*. In this case `project_dict` is the correct type, a dictionary, but it is an empty dictionary which doesn't contain an item with a key 'ExternalConditions'.

Similar to the last example, this would be picked up by the JSON validation. The schema states that 'ExternalConditions' is a required property of the root object.

An input file with "ExternalConditions" key/value pair
------------------------------------------------------

OK, let's fix this particular bug by including an "ExternalConditions" key/value pair in the root JSON object.

.. code-block:: JSON
   :caption: in.json

   {
      "ExternalConditions": {}
   }

Now we get a much larger, but more meaningful error message:

.. code-block::
   :caption: Command Prompt output

   ---stdout---

   Running 1 cases in series

   ---stderr---

   Traceback (most recent call last):

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 85, in validate_json_input

      InputFHS.model_validate(project_dict)

   File "C:\ProgramData\Anaconda3\Lib\site-packages\pydantic\main.py", line 503, in model_validate

      return cls.__pydantic_validator__.validate_python(

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   pydantic_core._pydantic_core.ValidationError: 11 validation errors for InputFHS

   ColdWaterSource

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   Control

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   EnergySupply

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   Events

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   HotWaterDemand

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   HotWaterSource

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   InfiltrationVentilation

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   InternalGains

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   SimulationTime

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   Zone

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing

   temp_internal_air_static_calcs

   Field required [type=missing, input_value={'ExternalConditions': {'...version_needed': False}}, input_type=dict]

      For further information visit https://errors.pydantic.dev/2.5/v/missing



   During handling of the above exception, another exception occurred:



   Traceback (most recent call last):

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 1104, in <module>

      run_project(

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 162, in run_project

      validate_json_input(project_dict, inp_filename, display_progress)

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 89, in validate_json_input

      print(f"\u2717 JSON validation failed for {filename}:")

   File "C:\ProgramData\Anaconda3\Lib\encodings\cp1252.py", line 19, in encode

      return codecs.charmap_encode(input,self.errors,encoding_table)[0]

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   UnicodeEncodeError: 'charmap' codec can't encode character '\u2717' in position 0: character maps to <undefined>

There are two separate errors here.

The first is a *ValidationError* which tells us that there are 11 key/value pairs missing in the root JSON object. These are listed as "ColdWaterSource", "Control", "EnergySupply" etc. This is a useful error message and tells us what we need to change in the input file.

.. note::

   This validation is actually being done accoring to the `core-input-allowing-future-homes-standard-input.json <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/schemas/core-input-allowing-future-homes-standard-input.json>`__ schema (see *hem.py*, line 85). 

.. note::

   Internally, the validation is done using the Pydantic classmethod `BaseModel.model_validate <https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate>`__. This is because the input schema is actually defined using Pydantic classes in the *core/input.py* and *core/input_allowing_future_homes_standard_input.py* modules. The JSON schemas in the folder 'schemas' is automatically generated from these Pydantic classes using *tools/generate_json_schemas.py*.
   
The second error message is a *UnicodeEncodeError* message. This is an internal error in the source code, as *hem.py* line 89 attempts to print a message with an unusual character in it (unicode \u2717 which looks like a cross mark). This may work on other operating systems, but for the Python interpreter on my Windows laptop this results in an uncaught exception. It would be easily fixed by removing the unicode character.

An input file which meets the source code internal validation requirements
--------------------------------------------------------------------------

OK, let's create an input file which will pass the internal validation process of the HEM source code. I created this file by fixing the errors in the previous error message, fixing any subsequent error messages that occurred and by studying the requirements of the :ref:`inputfhs_input_reference_core_hem_allowing_fhs_HEM_v0.36_FHS_v0.27` JSON object in :ref:`input_reference_core_hem_allowing_fhs_HEM_v0.36_FHS_v0.27`.

Here is the new input file:

.. code-block:: JSON
   :caption: in.json

   {
      "ColdWaterSource": {
         "my_cold_water_source_1": {
               "start_day": 0,
               "temperatures": [
                  8.0
               ],
               "time_series_step": 1
         }
      },
      "Control": null,
      "EnergySupply": {
         "my_energy_supply_1": {
               "fuel": "electricity",
               "is_export_capable": false
         }
      },
      "Events": {},
      "ExternalConditions": {},
      "HotWaterDemand": {},
      "HotWaterSource": {
         "hw cylinder": {
               "type": "PointOfUse",
               "ColdWaterSource": "my_cold_water_source_1",
               "EnergySupply": "my_energy_supply_1",
               "efficiency": 90,
               "setpoint_temp": 21
         }
      },
      "InfiltrationVentilation": {
         "Leaks": {
               "env_area": 0,
               "test_pressure": 0,
               "test_result": 0,
               "ventilation_zone_height": 0
         },
         "Vents": {},
         "altitude": 0,
         "cross_vent_possible": false,
         "shield_class": "Normal",
         "terrain_class": "Suburban",
         "ventilation_zone_base_height": 3
      },
      "InternalGains": {},
      "SimulationTime": {
         "end": 8760,
         "start": 0,
         "step": 1
      },
      "Zone": {},
      "temp_internal_air_static_calcs": 20
   }

Now when we run HEM there is a new error message:

.. code-block::
   :caption: Command Prompt output

   ---stdout---

   Running 1 cases in series

   ---stderr---

   Traceback (most recent call last):

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 1104, in <module>

      run_project(

   File "C:\\Users\\cvskf\\HEM\\HEM_v0.36_FHS_v0.27\\src\\hem.py", line 175, in run_project

      project = Project(project_dict, heat_balance, detailed_output_heating_cooling, use_fast_solver, tariff_data_filename, display_progress)

               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   File "C:\Users\cvskf\HEM\HEM_v0.36_FHS_v0.27\src\core\project.py", line 537, in __init__

      for name, data in proj_dict['Control'].items():

                        ^^^^^^^^^^^^^^^^^^^^^^^^^^

   AttributeError: 'NoneType' object has no attribute 'items'

There are now no validation errors occurring, so in the input file passes the schema validation stage.

However there is now an uncaught *AttributeError* exception. This is because the code is expecting ``proj_dict['Control']`` to be a dictionary, whereas in this example it is ``None``. 

Setting the :ref:`control_collection_input_reference_core_hem_allowing_fhs_HEM_v0.36_FHS_v0.27` JSON value of the ``Control`` key/value pair to ``None`` is allowed by the schema, but this option raises an error in the code. So it seems there is a mismatch between the schema and the source code here.

This seems a good place to end this section. The next step will be to create a minimum input file which both meets the schema validation and which results in a simulation run with no errors.

Conclusion
----------

* We can create a minimum Input File which passes the HEM schema validation. 
* However this is not enough to run a simulation as uncaught exceptions still occur.

