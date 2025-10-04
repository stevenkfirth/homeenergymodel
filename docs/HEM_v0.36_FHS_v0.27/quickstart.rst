
.. _quick_start_HEM_v0.36_FHS_v0.27:

Quick Start
===========

The HEM help guide
------------------

Once HEM is installed, we can view the help guide of the `hem.py <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/src/hem.py>`__ module using ``-h`` or ``--help`` argument.

Use one of the following command prompts (they do the same thing):

* ``python [PATH_TO_HEM_ROOT_DIRECTORY]\src\hem.py -h``
* ``python [PATH_TO_HEM_ROOT_DIRECTORY]\src\hem.py --help``

This prints the following help text:

.. code-block:: bash

    usage: hem.py [-h] [--epw-file EPW_FILE] [--CIBSE-weather-file CIBSE_WEATHER_FILE] [--tariff-file TARIFF_FILE] [--parallel PARALLEL] [--preprocess-only]
                [--future-homes-standard | --future-homes-standard-FEE | --future-homes-standard-notA | --future-homes-standard-notB | --future-homes-standard-FEE-notA | --future-homes-standard-FEE-notB]
                [--heat-balance] [--detailed-output-heating-cooling] [--no-fast-solver] [--display-progress] [--no-validate-json]
                input_file [input_file ...]

    Home Energy Model (HEM)

    positional arguments:
    input_file            path(s) to file(s) containing building specifications to run

    options:
    -h, --help            show this help message and exit
    --epw-file EPW_FILE, -w EPW_FILE
                            path to weather file in .epw format
    --CIBSE-weather-file CIBSE_WEATHER_FILE
                            path to CIBSE weather file in .csv format
    --tariff-file TARIFF_FILE
                            path to tariff data file in .csv format
    --parallel PARALLEL, -p PARALLEL
                            run calculations for different input files in parallel(specify no of files to run simultaneously)
    --preprocess-only     run prepocessing step only
    --future-homes-standard
                            use Future Homes Standard calculation assumptions
    --future-homes-standard-FEE
                            use Future Homes Standard Fabric Energy Efficiency assumptions
    --future-homes-standard-notA
                            use Future Homes Standard calculation assumptions for notional option A
    --future-homes-standard-notB
                            use Future Homes Standard calculation assumptions for notional option B
    --future-homes-standard-FEE-notA
                            use Future Homes Standard Fabric Energy Efficiency assumptions for notional option A
    --future-homes-standard-FEE-notB
                            use Future Homes Standard Fabric Energy Efficiency assumptions for notional option B
    --heat-balance        output heat balance for each zone
    --detailed-output-heating-cooling
                            output detailed calculation results for heating and cooling system objects (including HeatSourceWet objects) where the relevant objects have this functionality
    --no-fast-solver      disable optimised solver (results may differ slightly due to reordering of floating-point ops); this option is provided to facilitate verification and debugging of the    
                            optimised version
    --display-progress    display progress for the json input file currently running
    --no-validate-json    disable JSON schema validation (useful during development)

This tells us that when calling the `hem.py <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/src/hem.py>`__ module, we should provide the ``input_file`` argument (as it is a 'positional argument') and we can also supply many different options arguments (``-h``, ``--epw-file``, ``--CIBSE-weather-file`` etc.).

What do all these arguments do? This doesn't seem to be documentented anywhere but we can make reasonable guesses given the descriptions above.

.. _an_example_simulation_HEM_v0.36_FHS_v0.27:

An example simulation
---------------------

This simulation uses:

* the `demo.json <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/test/demo_files/core/demo.json>`__ input file from the HEM repository.
* the `London_weather_CIBSE_format.csv <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/test/demo_files/London_weather_CIBSE_format.csv>`__ weather data file from the HEM repository.

The steps are:

1. Save the *demo.json* and *London_weather_CIBSE_format.csv* files in the same folder on your local computer.
2. Open the Command Prompt.
3. Change the directory of the Command Prompt to where the files are stored using ``cd [PATH_TO_MY_DIRECTORY]``. 
4. Run the prompt: ``python [PATH_TO_HEM_ROOT_DIRECTORY]\src\hem.py --CIBSE-weather-file London_weather_CIBSE_format.csv demo.json``.
  
  * ``python`` calls the Python interpreter. 
  * ``[PATH_TO_HEM_ROOT_DIRECTORY]`` is the directory where the HEM repository is stored on your computer. Please replace this text with the local path you have used.
  * ``src\hem.py`` is the path to Python module `hem.py <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/src/hem.py>`__ which provides the point of access to the HEM calculations.
  * ``--CIBSE-weather-file`` is the CIBSE weather data flag as described in the help text above.
  * ``London_weather_CIBSE_format.csv`` is the filepath to the CIBSE weather file (this must follow directly after ``--CIBSE-weather-file``).
  * ``demo.json`` is the filepath to the input file.

This results in the following text printed in the Command Prompt.

.. code-block:: 

   Running 1 cases in series

This also creates a new subfolder named *demo__results* (the name of the input file plus '__results') which contains the following results files:

* *demo.json*
* *demo__core__results.csv*
* *demo__core__results_static.csv*
* *demo__core__results_summary.csv*



