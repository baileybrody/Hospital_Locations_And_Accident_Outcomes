#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:05:13 2022

@author: brodybailey
"""
#importing modules 

import pandas as pd 
import geopandas as gpd 
import numpy as np

#importing data from Census prior to 2010 

cd = pd.read_excel("Population-by-County-1850-2010.xlsx", header = 4)

#eliminating missing space from dataframe

cleaned = cd.dropna(subset = 1850)

#Moving axis 1 to column titles 

cleaned = cleaned.replace("na",np.nan)

#%% 
#Importing 2020 data via API 





