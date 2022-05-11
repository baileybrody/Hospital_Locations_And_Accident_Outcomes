#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:18:18 2022

@author: brodybailey
"""

import pandas as pd 
import geopandas as gpd 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

plt.rcParams["figure.dpi"] = 300



#%% 

#filtering out healthcare facilities that are not hospitals 

facilities = gpd.read_file("Utah_Health_Care_Facilities.zip")

keep_cols = ["NAME", "TYPE", "geometry"]

facilities = facilities[keep_cols]

hospitals = facilities.query("TYPE == 'HOSPITAL'")

hospitals.to_file("hospitals.gpkg", layer="hospitals", index=False)


#%% 

#cleaning up accident data 

utah_deaths = pd.read_table("Accident_Deaths.txt")

keep_cols_2 = ["County","County Code","Deaths","Population"]

utah_deaths = utah_deaths[keep_cols_2]

utah_deaths["County"] = utah_deaths["County"].str.replace(" County, UT","")

utah_deaths = utah_deaths.dropna(axis=0)

#%%
#calculating yearly death and average population 

years = 2020-1998

utah_deaths["Yearly Average Deaths"] = utah_deaths["Deaths"]/years

utah_deaths["Yearly Average Population"] = utah_deaths["Population"]/years

utah_deaths["Average Deaths as % of Population"]= utah_deaths["Yearly Average Deaths"]/utah_deaths["Yearly Average Population"]*100

#sorting in ascending order

utah_deaths = utah_deaths.sort_values("Average Deaths as % of Population", ascending=False)

#%%
#creating bar graph of death rates 

average = 100*utah_deaths["Deaths"].sum()/utah_deaths["Population"].sum() 

fig, ax1= plt.subplots(figsize=(6,6), dpi=300)

fig.suptitle("Mortality Risk by County")

bar_plot = utah_deaths.plot.barh(x="County", y="Average Deaths as % of Population", ax=ax1, legend=False)

ax1.axvline(average)

ax1.set_xlabel("Average Deaths as % of Population")

fig.tight_layout()

fig.savefig("death_rates_plot.png")


#%%
#converting distance to miles 

lines = gpd.read_file("reprojected.gpkg", layer="lines")

lines["Miles"] = lines["distance"]/1609.344

lines["County"] = lines["NAME"].str.title()

lines = lines[["County","Miles"]]

#importing distance information into utah_deaths

utah_deaths = utah_deaths.merge(lines, on="County", how="outer", indicator=True)

print(utah_deaths["_merge"].value_counts())

utah_deaths = utah_deaths.drop(columns="_merge")


#%%
#creating bar graph of distance 

fig, ax1= plt.subplots(figsize=(6,6), dpi=300)

fig.suptitle("Distance From Centroid to Hospital")

ax1.set_xlabel("Miles")

lines = lines.sort_values("Miles", ascending=False)

bar_plot = lines.plot.barh(x="County", y="Miles", ax=ax1, legend=False)

fig.tight_layout()

fig.savefig("distance_bar_plot.png")


#%%
#creating scatter plot 

fig, ax1= plt.subplots(figsize=(6,6), dpi=300)

utah_deaths.plot.scatter(x="Miles", y="Average Deaths as % of Population", ax=ax1)

fig.tight_layout()

fig.savefig("scatter_plot.png")

#%%

fg = sns.lmplot(data= utah_deaths, x="Miles", y="Average Deaths as % of Population", ci = 95)

reg = scipy.stats.linregress(utah_deaths["Miles"],utah_deaths["Average Deaths as % of Population"])

fg.savefig("regression.png")

print("Intercept", reg.intercept)

print("Slope", reg.slope)

print("P-value", reg.pvalue)

print("stderr", reg.stderr)









                          

