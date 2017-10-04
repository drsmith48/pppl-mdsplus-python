#!/bin/csh


# nstx/mdsplus + py2
#
# The module 'nstx/mdsplus' is MDSplus v5 and supports only python2.
#
module purge
module load slurm ppplcluster nstx/mdsplus
make mdsplus
module unload nstx/mdsplus nstx/treedefs java


# nstx/mdsplus_alpha + py2/py3
#
# The module 'nstx/mdsplus_alpha' is MDSplus v6 and supports both py2/3.
# The makefile builds a 'universal wheel' with py3 and tests with py2 and py3.
#
module load nstx/mdsplus_alpha
make mdsplus_alpha v6.1.84 v7.0.71 v7.1.13
module unload nstx/mdsplus_alpha nstx/mdsplus_treedefs nstx/mdsplus_idl_alpha \
freetds java

