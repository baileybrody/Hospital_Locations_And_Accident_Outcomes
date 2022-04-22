#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:18:18 2022

@author: brodybailey
"""

import pandas as pd 
import geopandas as gpd 
import numpy as np

#importing data from Census prior to 2010 

hospitals = pd.read_excel("new_york_hospital_data.xlsx")

#selecting all open hospitals

open_hospitals = pd.DataFrame() 

#creating new dataframe with just open hospitals 

open_hospitals = hospitals.query("Status == 'OPEN'")

#saving hopsital data as CSV 

open_hospitals.to_csv("open_hospitals.csv")

#%% 

#filtering out healthcare facilities that are not hospitals 

facilities = gpd.read_file("Utah_Health_Care_Facilities.zip")

keep_cols = ["NAME", "geometry"]

facilities = facilities[keep_cols]













                          

