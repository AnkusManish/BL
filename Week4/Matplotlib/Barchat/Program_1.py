#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:19:35 2019

@author: ankusmanish
"""

#Write a Python programming to display a bar chart of the popularity of programming Languages

"""Languages,Popularity 
Java,22.2
Python,17.6
PHP,8.8 
JavaScript,8
C#,7.7
C++,6.7
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_clipboard(sep = ',')
print(data)

b = np.arange(len(data['Popularity ']))

plt.bar(b, height = data['Popularity '])
plt.xticks(b, data['Languages'])

plt.show()