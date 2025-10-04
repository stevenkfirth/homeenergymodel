
.. _my_thoughts_HEM_v0.36_FHS_v0.27:

My thoughts
===========

This is a running list of any bugs, issues, gotchas and feature improvements that occur to me as I am working with HEM.

This is based on my personal views of what makes good software. Please let me know if you think I have got anything wrong here.

How would I describe the HEM repository to a Python developer?
--------------------------------------------------------------

I would probably start with...

  The HEM repository is a Python command line programme which is called from the Command Prompt. It cannot be directly installed from PyPi or directly imported. In essence it is a file conversion programme which takes a series of input files and creates a series of output files. For the same set of inputs, the same outputs will occur. The main input file is a JSON file which is defined by a JSON schema document. The repository documentation and JSON schema documentation are somewhat incomplete, making it difficult to create valid input files or have confidence in the meaning of the input file values. There is no API reference documentation to the Python modules or classes in the repository. 

Is HEM open source?
-------------------

No, not really.

I would say that HEM is:

* Open - as the underlying source code can be accessed.
* Free software - as the HEM repository is online and publicly available.

However, it's not really an open source project because there is minimal documentation, no easy place to report bugs (such as a GitHub issues page) and no opportunity for contributions from the wider developer community. Plus, in my view, the underlying source code is not written in an accessible, easy-to-understand manner.

Key features which are missing
------------------------------

* Schema documentation: It would be very useful to have full description of all objects in the JSON schema, including the meaning of physical quantities and their units where approriate.
* API documentation: It would also be useful to have full documentation for the *hem.py* file, with much more description than provided in the ``--help`` text.
* Software design documentation: Many packages discuss the high-level design choices made for the software and the reasons for these choices. This is very helpful in understanding the internal workings of the package.
* Internal docstrings: There doesn't seem to be consistent documentation of the Python modules, classes and functions in the source code. There also doesn't seem to be a consistent docstring format style used, such as the reST, Google or Numpydoc formats.

.. * Co-simulation: Established building simulation software, such as EnergyPlus, provides access to the main time step loop of the calculations which enables users to alter state variables (such as temperatures or a control signal) as the simulation is underway. This doesn't seem to be present in core HEM and would probably have needed to be implemented at the early stages of the software development.

Software design choices
-----------------------

* Package design: HEM has been designed as a command line programme rather than an importable Python package. This might well be needed as HEM is going to be used as a web API service. However it is possible to design Python packages which work both as command line programmes and importable Python packages. By not being importable, HEM misses out on many Python ecosystem features, such as profiling, automatic documentation generation and user access to internal modules and classes.
* Wrapper design: HEM-FHS is presented as "wrapper" of core HEM. However it isn't implemented as might be expected in standard software practice. We might expect the HEM-FHS wrapper to fully enclose the core HEM engine, act as a separate process and export a core HEM input file which is then used in a separate core HEM call. Instead the HEM FHS wrapper is actually called in the same location as the core HEM call (i.e. the *hem.py* module) and the interaction between HEM-FHS and core HEM is not visible.

.. * Class design: The use of classes in the source code can be useful as they provide reusable code components.

 



.. Input file schemas
.. ------------------





.. Input file validation
.. ---------------------


