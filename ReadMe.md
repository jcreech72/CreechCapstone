# Creech Capstone Project
## Analysis of Lives Saved When Wearing a Proper Helmet

Author: Julie L Creech

Date: April 6, 2023

## Data Sets
https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/

Using data set Fars2021NationalCSV, Fars2018NationalCSV, Fars2015NationalCSV, Fars2012NationalCSV, Fars2009NationalCSV
Within each set of data, used two files: person.csv and accident.csv
The data is linked together with a field called ST_CASE



## Report
Link to OverLeaf report: https://www.overleaf.com/read/mzdkvqkytrmg

## File Descriptions

StatesReqHelmetList.Xlsx: Scraped data from website https://thebradleylawfirm.com/personal-injury-resources/helmet-laws-in-missouri/#Missouri_and_Helmet_Laws/ 
Formatted the data so that it was columnar data

Fars2021NationalCSV: Origional Data Set = #records --> After Cleanup = #records
person2021.csv 
accident2021.csv --Used a vLookup to populate the longitude and latitude data to the person file

Fars2018NationalCSV: Origional Data Set = #records --> After Cleanup = #records
person2018.csv
accident2018.csv--Used a vLookup to populate the longitude and latitude data to the person file

Fars2015NationalCSV: Origional Data Set = #records --> After Cleanup = #records
person2015.csv
accident2015.csv--Used a vLookup to populate the longitude and latitude data to the person file

Fars2012NationalCSV: Origional Data Set = #records --> After Cleanup = #records
person2012.csv
accident2012.csv--Used a vLookup to populate the longitude and latitude data to the person file

Fars2020NationalCSV: Origional Data Set = #records --> After Cleanup = #records
person2020.csv
accident2020.csv--Used a vLookup to populate the longitude and latitude data to the person file

Used Excel to clean the data, but used a Macro so that this would only have to be done manually one time. 
Removed column that will not be used. Removed rows that were not motorcycle data. Used the VPICBodylassName as the column to filter and identify motorcycles only. 
Deleted the rest of the data that would never be a resource.
Ended up not able to use some of the files because the formatting was different. As it was, column titles were different, and had to do a lot more cleaning than origionally thought. 
Remaining Fields: 
From Person.csv
STATE
STATENAME
*ST_CASE
MAKENAME
MAK_MOD
BODY_TYPNAME
AGE
SEX
SEXNAME
INJ_SEVNAME
DOA
DOANAME
HELM_USE
HELM_USENAME
HELM_MIS
HELM_MISNAME
VPICBODYCLASSNAME

From Accident.csv
*ST_CASE
Longitude
Latitude

![image](https://user-images.githubusercontent.com/89232631/230538411-ff73f101-2d70-4593-a2fd-e1fadbc481b9.png)

Used Excel to do a vLookup function to pull in longitude and latitude data into one table. 
Move the cleaned data to one file within each folder named FARS[year]National.csv
Pull data all together into either one Tableau file or into PostgresSQL

[file].py will be the python file that I use for statistics and visualizations



## Count of Deaths Based on Helmet Choice in 2020
Pivot Data provided some initial data points:
Count of fatalities in the year 2020 was a sampling used; however, the dataset will not be used for the analysis. 
During the sampling data, found that there was a total of 5,776 deaths across the united states. 
Removing data that does not pertain to the data because it is uncertain data, totals 202
Motorcyclists not wearing a helmet at all was 2,275 --> 39% of the fatalities were not wearing a helmet at all.
Motoryclists wearing a non-DOT approved helmet or novelty helmet totaled 1,836 --> 32% of the fatalities were wearing a non-approved helmet
Motorcycles wearing a DOT approved helmet totaled 1,463 --> 25% of the fatalities were wearing an approved helmet
71% of the fatalities were due to decisions to wear a non-approved or no helmet
25% of the fatalities wore an approved helmet
3% of the data was unuseful. 

##  Cleaning Data
Data was found in multiple years of CSV files that did not follow a formatting standard. Cleaning specifics are detailed in Latex file https://www.overleaf.com/read/mzdkvqkytrmg
Pulled all data into one file. Using Python, created a script to clean the file: reference "data_cleaning.ipynb. Next, removed null values and dropped nulls totally only 22. ![alt text](https://github.com/jcreech72/CreechCapstone/blob/main/Cleaning1.png)
Checked the data type and checked for outliers. 
As expected, noted the SEX to show more males than females, years to be split out between 2015 and 2021, an "Age" range median of 43 with a top range of 96. I was suprised to see the minimum range as 1. Without assuming it was an anomily or outlier due to there being other low-range ages as well. ![alt text](https://github.com/jcreech72/CreechCapstone/blob/main/Cleaning2.png)

## Python Notebook
Review Data & Statistics (loaded cleaned csv file into Python notebook)
Vizualizations & Finding Outliers
Remove Outliers & Look at Distributions Without Outliers
Visualizations & Correlations
