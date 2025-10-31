.. _installation_HEM_v0.36_FHS_v0.27:

Installing HEM
==============

Is HEM a Python package?
------------------------

No, HEM is written in Python but it is not a standard Python package.

Standard Python packages are typically hosted on `PyPi <https://pypi.org/>`__, can be installed using the command prompt ``pip install ...`` and are called using Python ``import`` statements.

Instead HEM is written as a standalone Python programme that is is called using the Command Prompt.

How to download HEM?
--------------------

HEM is hosted as a repository here: https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27

The entire HEM repository can be downloaded by following the link above and selecting the 'Download as Zip' option (available in the More Actions button).

There are some long filenames in the HEM repository, so you may need to place it in a directory with a short pathname before extracting the files from the ZIP file.

How to run HEM?
---------------

A quick test of HEM can be done by:

* Opening the Command Prompt
* Type the command ``python [PATH_TO_HEM_ROOT_DIRECTORY]\src\hem.py``

  * ``python`` calls the Python interpreter. 
  * ``[PATH_TO_HEM_ROOT_DIRECTORY]`` is the directory where the HEM repository is stored on your computer. Please replace this text with the local path you have used.
  * ``src\hem.py`` is the path to Python module `hem.py <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/src/hem.py>`__ which provides the point of access to the HEM calculations.

* On my computer, this prompt looks like ``python "C:\Users\cvskf\HEM\HEM_v0.36_FHS_v0.27\src\hem.py"``.

You should see the following output in the Command Prompt window:

.. code-block:: bash
   
   usage: hem.py [-h] [--epw-file EPW_FILE]
               [--CIBSE-weather-file CIBSE_WEATHER_FILE]   
               [--tariff-file TARIFF_FILE]
               [--parallel PARALLEL] [--preprocess-only]   
               [--future-homes-standard | --future-homes-standard-FEE | --future-homes-standard-notA | --future-homes-standard-notB | --future-homes-standard-FEE-notA | --future-homes-standard-FEE-notB]
               [--heat-balance]
               [--detailed-output-heating-cooling]
               [--no-fast-solver] [--display-progress]     
               [--no-validate-json]
               input_file [input_file ...]
   hem.py: error: the following arguments are required: input_file

This means that the `hem.py <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/src/hem.py>`__ module was successfully called and it returned its standard help text and an error message (as no input file was supplied).

For an example of a complete simulation run, see :ref:`an_example_simulation_HEM_v0.36_FHS_v0.27`.

Help! I get an error
--------------------

If you get an error when trying to run HEM as described, this is likely to be one of two things:

1. The filepath supplied to the Command Prompt was incorrect. The error message should say that the file cannot be found, for example: ``[Errno 2] No such file or directory``.

2. There is an ``import`` error. This is likely because HEM uses additional Python packages and these need installing as well. If a required package is not installed, then an ``import`` error will occur. These packages are listed in the `requirements_3-12.txt <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/requirements_3-12.txt>`__ file:

   .. code-block::

      Cython==3.0.6
      numpy==2.1.0
      scipy==1.14.1
      pandas==2.2.2
      matplotlib==3.9.3
      pytest==8.3.2
      ruff==0.11.8
      pre-commit==4.2.0
      jsonschema==4.23.0
      pydantic==2.11.4

   For standard PyPi Python packages installed using ``pip install ...`` these additional requirements are installed automatically.

   But as HEM is only available as a downloaded repository, we need to install these packages manually. You can either:
   
   * use ``pip install`` to install any missing packages into your current Python environment, or;
   * create a new Python virtual environment (perhaps one dedicated to running HEM) and use ``pip install -r requirements_3-12.txt`` to install all packages at once (see official instructions `here <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&anchor=installing-dependencies>`__).


