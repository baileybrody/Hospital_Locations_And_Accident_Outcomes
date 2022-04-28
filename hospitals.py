#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:18:18 2022

@author: brodybailey
"""

import pandas as pd 
import geopandas as gpd 
import numpy as np



#%% 

#filtering out healthcare facilities that are not hospitals 

facilities = gpd.read_file("Utah_Health_Care_Facilities.zip")

keep_cols = ["NAME", "TYPE", "geometry"]

facilities = facilities[keep_cols]

hospitals = facilities.query("TYPE == 'HOSPITAL'")

hospitals.to_file("hospitals.gpkg", layer="geometry", index=False)

#%% 

#cleaning up accident data 

utah_deaths = pd.read_table("Underlying_Cause_of_Death")

keep_cols_2 = ["County","County Code","Deaths","Population"]

utah_deaths = utah_deaths[keep_cols_2]

#%%
#calcylating yearly death and average population 

utah_deaths["Yearly Average Deaths"] = utah_deaths["Deaths"]/20

utah_deaths["Yearly Average Population"] = utah_deaths["Population"]/20

utah_deaths["Average Deaths as % of Population"]= utah_deaths["Yearly Average Deaths"]/utah_deaths["Yearly Average Population"]*100









                          

