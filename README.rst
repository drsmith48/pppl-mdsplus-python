About
========

This repo contains resources to build and test Python packages for MDSplus on the PPPL linux cluster.
The source code is located in ``/u/drsmith/mdsplus-python/`` on the PPPL cluster.

The packages are tested with python2 and python3 and with modules ``nstx/mdsplus`` and ``nstx/mdsplus_alpha`` as appropriate.  All building and testing is performed locally.  A production installation can be reverse-engineered from the ``build`` target in ``Makefile``.

Try it yourself on the PPPL cluster. Copy or clone::

	$ git clone git@github.com:drsmith48/pppl-mdsplus-python.git
	
or::

	$ cp --recursive /u/drsmith/mdsplus-python/ <destination directory>

Then run the shell script in the repo/directory::

	$ source build.csh


Repo structure
====================

* ``build.csh`` - configure modules and call ``Makefile`` to run build/test recipes
* ``Makefile`` - build Python packages with py2/py3 (as appropriate) and test packages with py2/py3 (as appropriate) by running test-mdsplus.py
* ``test-mdsplus.py`` - Python test script to import MDSplus and get MPTS data
* ``pylib/`` - contains Python libraries from several MDSplus releases

  * ``pylib/mdsplus/`` - Python library copied from /u/gtchilin/sandbox/mdsplus/R5_64/mdsplus
  * ``pylib/mdsplus_alpha/`` - Python library copied from /usr/pppl/nstx/R6_64/mdsplus_alpha
  * ``pylib/v6.1.84/`` - Python library from MDSplus v6.1.84
  * ``pylib/v7.0.71/`` - Python library from MDSplus v7.0.71
  * ``pylib/v7.1.13/`` - Python library from MDSplus v7.1.13


Other notes
==================

1. The module ``nstx/mdsplus`` is MDSplus v5, and it only supports python2. Accordingly, the Makefile only builds and tests with python2.
2. The module ``nstx/mdsplus_alpha`` is MDSplus v6 and it supports python2 and python3.  The Makefile builds a 'universal wheel' with python3 and tests with python2 and python3.
3. The file ``setup.py`` in the Python library for the module ``nstx/mdsplus_alpha`` contains an error that breaks the build.  Simple fix: change the line ``setup(name=name,`` to ``setup(name=pname,``.
4. PyPI (python package index) contains packages for MDSplus >= v6.1, so I obtained a few Python libraries from old MDSplus releases on Github.  The libraries are in ``pylib/vX.Y.ZZ`` and the libraries work with the module ``nstx/mdsplus_alpha``. The packages are built as a 'universal wheel' with python3 and tested with python2 and python3 in the Makefile.

