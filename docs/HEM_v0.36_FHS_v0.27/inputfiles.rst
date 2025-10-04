.. _input_files_HEM_v0.36_FHS_v0.27:

Working with Input Files
========================

What is a HEM Input JSON file?
------------------------------

HEM input files are JSON files which contains all the data (except, in some cases, the weather data) which a HEM calculation requires.

This typically includes:

* Information about the building geometry and location.
* Information about the constructions used in the walls, roof, floors and windows.
* Information about the heating and cooling systems.
* Information about many other things which impact on the energy consumption of the building.

What is a JSON file?
--------------------

A JSON file is a standard file format used extensively in computer science.

It is a text file in the same way as a CSV file. But where CSV files are good at storing tabular data, JSON files are good at storing nested data.

JSON files are constructed according to: https://www.json.org/json-en.html

Why use JSON files?
-------------------

The nested data property of JSON files is useful for building energy models.

This is because buildings are often made up of a variable number of objects. For example:

* A building can have a variable number of rooms.
* Each room can have a variable number of lights.

This variable-length, nested information is difficult to store in a tabular data structure like CSV files, but works well in JSON using the object (dictionaries) and array (lists) JSON components.

What are the rules when creating a HEM input file?
--------------------------------------------------

The contents of the HEM input files are structured according to a schema.

There are three schemas currently available for HEM:

* `core-input.json <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/schemas/core-input.json>`__: this is used for validating input files to the core HEM engine.
* `core-input-allowing-future-homes-standard-input.json <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?version=GTHEM_v0.36_FHS_v0.27&path=/schemas/core-input-allowing-future-homes-standard-input.json>`__: this is used for validating input files to the core HEM engine which have been created using the HEM FHS (Future Home Standard) wrapper.
* `FHS_schema.json <https://dev.azure.com/Sustenic/Home%20Energy%20Model%20Reference/_git/Home%20Energy%20Model?path=/src/wrappers/future_homes_standard/FHS_schema.json&version=GTHEM_v0.36_FHS_v0.27>`__: this is used for validating input files to the HEM FHS  wrapper.

These schemas are also written in JSON and follow the `JSON Schema <https://json-schema.org/>`__ standard.

How do I use these schema?
--------------------------

The schemas themselves are long text documents which are difficult to use directly.

Instead I have converted these JSON Schema documents into an online reference which contains the same content and is easier to navigate.

* :ref:`input_reference_core_hem_HEM_v0.36_FHS_v0.27`
* :ref:`input_reference_core_hem_allowing_fhs_HEM_v0.36_FHS_v0.27`
* [The *FHS_schema.json* online reference will be added here when complete]

I can then use these online references to either manually create an input JSON file in a text editor or to write a Python script to create an input JSON file.
