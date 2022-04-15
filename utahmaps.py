#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:05:13 2022

@author: brodybailey
"""
#importing modules 

import pandas as pd 
import geopandas as gpd 

#importing data from Census prior to 2010 

cd = pd.read_excel("Population-by-County-1850-2010.xlsx")

#eliminating missing space from dataframe

cleancd = cd.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

#Moving axis 1 to column titles 





