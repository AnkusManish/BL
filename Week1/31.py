#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:44:49 2019

@author: ankusmanish
"""

import subprocess

result = subprocess.check_output("ls", universal_newlines=True)
print(result)
