#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:46:22 2019

@author: ankusmanish
"""

d = {'val_1':8,'val_2':21,'val_3':7,'val_4':20,'val_5':47,'val_6':53,'val_7':29,'val_8':88,'val_9':30,}

#sorting the dictionary with respect to the value
d = dict(sorted(d.items(), key = lambda x : x[1]))

print(d)
