#!/usr/bin/env python
# coding: utf-8

# # Analysis of air quality of Bhopal
# 
# In this project I have analysed data pertaining to air quality of Bhopal, capital of Madhya Pradesh, India. Dataset used in this project was collected from https://aqicn.org/city/india/bhopal/t-t-nagar web address. The objective of this project was to see variation in different pollutants over months. The data was collected from 2 December 2019 to 1 April 2021. Libraries used in this project were numpy, pandas, matplotlib and seaborn. This is an exploratory data analysis project which includes data cleaning, data visualization etc.

# ## Importing relevant libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Reading, Data Preparation and cleaning the data
# 
# Dataset was downloaded earlier, so it was present locally. I just uploaded the data into Jupyter notebook. I used "read_csv" method of pandas library to load csv file into our project. In this section we will clean the data for further analysis.

# In[2]:


aqi_bhopal_df = pd.read_csv('t-t nagar, bhopal, india-air-quality.csv')


# In[3]:


aqi_bhopal_df


# In[4]:


# Name of attributes in dataset.
aqi_bhopal_df.columns


# We can observe that name of the columns contain unnecessary spacings.

# Each column signifies following things in dataset :
# #### 1. Date :
# This column contains date on which data is collected. This comprise of the date, month and year of data collection.
# 
# #### 2. pm25:
# This column contains data for the particulate matter of size than 2.5 micrometers. The unit used in India microgram per meter cube. Although it was not specified in dataset but we are assuming this for further analysis.
# 
# #### 3. pm10:
# This column contains data for the particulate matter of size than 10 micrometers. The unit used in India microgram per meter cube. Although it was not specified in dataset but we are assuming this for further analysis.
# 
# #### 4. o3:
# This column contains data for the ground level ozone. It is a secondary pollutant. The unit used in India microgram per meter cube. Although it was not specified in dataset but we are assuming this for further analysis.
# 
# #### 5. no2:
# This column contains data for the concentration of nitrogen dioxide. It is a primary pollutant. The unit used in India microgram per meter cube. Although it was not specified in dataset but we are assuming this for further analysis.
# 
# #### 6. so2:
# This column contains data for the concentration of sulphur dioxide. It is a primary pollutant. The unit used in India microgram per meter cube. Although it was not specified in dataset but we are assuming this for further analysis.
# 
# #### 7. co:
# This column contains data for the concentration of carbon monoxide. It is a primary pollutant. The unit used in India microgram per meter cube. Although it was not specified in dataset but we are assuming this for further analysis.

# In[5]:


## I created a copy of the dataset so that our original file should remain unaltered.
aqi_bhopal_df1 = aqi_bhopal_df.copy()


# In[6]:


aqi_bhopal_df1


# Now we will analyze our dataset for amount of null values and data types of the attributes. We will use "info" method for this purpose. We also want to know about number of entries in our dataset, for this purpose we have to use "shape" method to calculate number of rows and columns.

# In[7]:


aqi_bhopal_df1.info()


# In[8]:


aqi_bhopal_df1.shape


# It seems that data type of the attributes is different than what is desired. Since data type of all the columns are of object type in the csv file, it is very necessary to change data type of all the columns for further operations. We will use pandas method "to_datetime" and "to_numeric" to change data types of attributes in desired format.

# In[9]:


aqi_bhopal_df1['date'] = pd.to_datetime(aqi_bhopal_df1.date, errors='coerce')
aqi_bhopal_df1[' o3'] = pd.to_numeric(aqi_bhopal_df1[" o3"], errors='coerce')
aqi_bhopal_df1[' so2'] = pd.to_numeric(aqi_bhopal_df1[" so2"], errors='coerce')
aqi_bhopal_df1[' no2'] = pd.to_numeric(aqi_bhopal_df1[" no2"], errors='coerce')
aqi_bhopal_df1[' co'] = pd.to_numeric(aqi_bhopal_df1[" co"], errors='coerce')
aqi_bhopal_df1[' pm10'] = pd.to_numeric(aqi_bhopal_df1[" pm10"], errors='coerce')
aqi_bhopal_df1[' pm25'] = pd.to_numeric(aqi_bhopal_df1[" pm25"], errors='coerce')


# In[10]:


## You can observe the change in data types of columns.
aqi_bhopal_df1.info()


# In[11]:


## Let's take a random sample from dataset.
aqi_bhopal_df1.sample(10)


# You can observe that header in our dataset contains unnecessary spaces. So I remove those defects by renaming column names and we will use "rename" method for this purpose.

# In[12]:


aqi_bhopal_df1.rename(columns = {' pm25':'pm25'},inplace = True)
aqi_bhopal_df1.rename(columns = {' pm10':'pm10'},inplace = True)
aqi_bhopal_df1.rename(columns = {' so2':'so2'},inplace = True)
aqi_bhopal_df1.rename(columns = {' no2':'no2'},inplace = True)
aqi_bhopal_df1.rename(columns = {' o3':'o3'},inplace = True)
aqi_bhopal_df1.rename(columns = {' co':'co'},inplace = True)


# In[13]:


aqi_bhopal_df1


# There are some missing values in our dataset so it will be very useful to deal with those values. This will help in further analysis. Since our data is continuous and if we drop those values it will lead to serious data loss, we will try to fill those null values with average of the attributes of that column.

# In[14]:


aqi_bhopal_df2 = aqi_bhopal_df1.fillna(aqi_bhopal_df1.mean()) 


# In[15]:


aqi_bhopal_df2.info()


# In[16]:


aqi_bhopal_df2.tail(5)


# We can see that our data is free from null values now. Now we will do descriptive statistical analysis on the cleaned dataset. We will take help of "describe" method for this purpose.

# In[17]:


aqi_bhopal_df2.describe()


# We will compare above mentioned values with acceptable limits of pollutants. I have taken help of http://www.indiaenvironmentportal.org.in for comparison.
# 
# By looking the above analysis we can conclude following things:
# 1. For particulate matter 2.5 category acceptance limit is 60 microgram per meter cube. But even mean of this pm25 category is 109 with standard devation of 42.8, which is way more than acceptance limit.
# 2. For particulate matter 10 category acceptance limit is 100 microgram per meter cube. Bhopal's air did pretty well in this category of pollutant. Mean for this category came out to be 79.7 with standard deviation of 33.05.
# 3. Maximum concentration for pm25 and pm10 for a day is quiet high than acceptable limit.

# Next, I tried to aggregate our data on the basis of time. This will add 3 different columns for year, month, number of days from starting of dataset and it's position in week. For this purpose I have use "DatetimeIndex" mrthod of pandas library. Next, I have used "groupby" method to build a dataframe which will provide air pollutant information on the basis of months.

# In[18]:


aqi_bhopal_df2['year'] = pd.DatetimeIndex(aqi_bhopal_df2.date).year
aqi_bhopal_df2['month'] = pd.DatetimeIndex(aqi_bhopal_df2.date).month
aqi_bhopal_df2['day'] = pd.DatetimeIndex(aqi_bhopal_df2.date).day
aqi_bhopal_df2['weekday'] = pd.DatetimeIndex(aqi_bhopal_df2.date).weekday


# In[19]:


aqi_bhopal_df2_mean = aqi_bhopal_df2.groupby('month')[['pm25','pm10','so2','no2','o3']].mean()


# In[20]:


aqi_bhopal_df2


# In[21]:


aqi_bhopal_df2_mean


# ## Conclusion
# 
# Effect of air pollutants cannot be observed in a day, we need at least a range of a month to compare air pollutants concentration. In the following section we will see variation of various air pollutants over the months or we can say monthly variation. 
# 

# #### Ozone
# 
# We can see from the bar plot that concentraion of ozone gets reduced from months 6 to 9. These are the months of rainy season in Bhopal. We can correlate from the graph below that in rainy season ozone contributes very less to air pollution of Bhopal.

# In[22]:


x = aqi_bhopal_df2_mean.index
y = aqi_bhopal_df2_mean.o3
plt.figure(figsize=(12, 6))
plt.title("Variation of ozone")
plt.xlabel('Month')
plt.ylabel('Concentration of ozone')
plt.bar(x,y);


# #### Pariculate matter
# 
# Variation of particulate matter throughout the months is similar to ozone. Since there was two types of particulate matter present in this dataset I have tried to show the variation among them. Although pm25 is present more than pm10 but they follow similar pattern.

# In[23]:


plt.plot(aqi_bhopal_df2_mean.index, aqi_bhopal_df2_mean.pm25)
plt.plot(aqi_bhopal_df2_mean.index, aqi_bhopal_df2_mean.pm10)
plt.xlabel('Month')
plt.ylabel('Variation of particulate matter')
plt.legend(['pm25', 'pm10']);


# #### Pollutants contributing to acid rain
# 
# In this section I have analysed sulphur dioxide(so2) and nitrogen dioxide(no2). These gases are one of the main contributor of acid rain. I have used stacked barplot for representing both so2 and no2 in same graph and to show their variation throughout the months. You can see the concentration of both of these pollutants was quiet less for months May, June, July, August, September. Rain may be one of the reason for this less concentration but we can also note that these were the months when there was lockdown. In lockdown number of vehicles were quiet less on the roads and most of the industries were closed.

# In[24]:


x = aqi_bhopal_df2_mean.index
y1 = aqi_bhopal_df2_mean.so2
y2 = aqi_bhopal_df2_mean.no2
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.legend(['so2', 'no2'])
plt.xlabel('Month')
plt.ylabel('Variation of so2 and no2');


# In[26]:


jovian.commit()

