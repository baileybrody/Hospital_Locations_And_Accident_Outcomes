# Hospital Locations and Deaths as the Result of Accidents In Utah

What is the relationship between the distance to the nearest hosptial and deaths as a result of accidents in Utah? 

## Summary:

One of the topics gaining attention in the Utah Legislature is the difference in outcomes between those living in Northern 
Utah (particularly along the Wasatch Front) and those living in Southern Utah. The Wasatch Front is a set of four counties
that collecitvely account for 75% of Utah's population: Salt Lake County, Davis County, Weber County, and Utah County. Since
a large portion of services are concentrated in these counties, I wanted to examine the relationship between distance to the 
nearest hospital and deaths as a result of accidents as a percentage of population for each county.

This project takes advantage of CDC Wonder, a collection of data compiled by the CDC that contains 
mortality and population counts for all U.S. counties, as well as causes of death. I retrieved all 
deaths that resulted from external causes for all Utah counties from 1999-2020. Because the output 
aggregates death counts and population totals in each county from 1999-2020, I divided both by 20 to 
get the yearly average deaths as a result of external cuases and population. I then retrieved county
shapefile data from the Utah Geospacial Resource Center to get the location of all healthcare facilities
in the state as well as a shapefile for all counties. I then used QGIS to calculate the distance from 
the centroid of each county to the nearest hospital. 

## Data Locations:
- Visit https://wonder.cdc.gov/ucd-icd10.html to retrieve cause of death data 
- Visit the Utah Geospatial Resource Center at https://gis.utah.gov/data/boundaries/citycountystate/
to retrieve the county shapefile, and at https://gis.utah.gov/data/health/health-care-facilities/ to 
retrieve a shapefile with all healthcare facilities in Utah.

**Instructions**

1. Import and edit Utah_heath_Care_Facilities.zip to keep only the NAME, TYPE, and geometry columns,
then filter to remove all healthcare facilities from the list besides hospitals. After that, save the 
file as a geopackage so it can be used in QGIS. 

2. In QGIS import the hospital shapefile, the county shapefile, and use centroids to calculate
the distance from the center of each county to the nearest hospital. Save the layer as lines

3. Import the accident information Underlying_Cause_of_Death, and edit the file to remove
extra text, and keep only the County, County Code, Deaths, and Population columns. Divide 
both the deaths and population columns by 20 to get average yearly deaths and average yearly
population 

4. Import layer lines and divide distance by 1609.344 to change meters to miles

5. Create plots, including barh plot to show difference in deaths as a reuslt of accidents in each
county, barh plot showing distance to nearest hospital in miles for each county, and scatterplot
showing relationship between deaths and distance to the nearest hospital

**Results and Analysis**

1. There are major differences in hospital access

![image](https://user-images.githubusercontent.com/98329892/167708468-26cfee6b-3b25-4007-89b6-cbacc43936d0.png)

One of the major takeaways from this project is the major difference in hospital distances
across the state. Those living in Wayne county have to travel over 70 miles to reach their
nearest hospital, while those living in Salt Lake County have to travel just over a mile. 

2. There are major differences in death rates 

![image](https://user-images.githubusercontent.com/98329892/167709968-17515f58-d45b-4df2-a7e7-dfeed68d559a.png)

There was a surprising difference in death rates as a result of accidents across counties.
The death rate as a result of accidents was almost three times higher in Carbon county than
in Cache county. It's also interesting to note that the county with the furthest distance to
a hopspital is not the county with the highest death rate as a result of accidents; that
distinciton belongs to Carbon county. One potential explanation for this is the extensive 
mining that occurs there. 

3. The relationship between death rates and proxmity to hospitals was not as clear as expected

![image](https://user-images.githubusercontent.com/98329892/167710516-a6a3c182-ebb3-4b08-b667-221ff8e4ef3c.png)

I was expecting a far more linear relationship between deaths as a result of accidents and 
the distance to the nearest hospital. Instead there is a bifurcation in the data that is rather striking. 

**Policy Implications**

This script provides a tool to examine the relationship between hosptial distance and death
rates as a result of accidents. The relationship between the speed with which a person receives treatment after an accident and their potential for surviving seems intuitive, and is well documented.(see artcile below) This simple model is a way to visualize that relationship and identity the strength of the relationship. In the case of Utah, it seems that other factors may play a major role given the bifurcation in the dataset. 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2464671/








