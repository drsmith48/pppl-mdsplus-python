#! python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:17:12 2017

@author: drsmith
"""

import MDSplus as mds

print(mds.__file__)

connection = mds.Connection('skylark.pppl.gov:8501')
connection.openTree('activespec',204620)
te = connection.get('\\top.mpts.output_data.best.fit_te')
tev = te.value
assert tev.shape == (42,27)
