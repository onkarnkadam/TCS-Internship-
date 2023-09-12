#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[8]:


#importing the dataset
hrdf=pd.read_csv("C:/Users/Onkar Kadam/Desktop/TCS Internship 2023/HR DATASET TCS INTERNSHIP.csv")


# In[9]:


#print the top 5 rows of the imported dataset
hrdf.head()


# In[10]:


df=pd.DataFrame(hrdf)
df.head()
#df.Employee_Name.value_counts()


# In[11]:


df_new=df.drop(['EmpID','Employee_Name','MarriedID','MaritalStatusID','ManagerName','ManagerID'], axis=1)
df_new.head()


# In[12]:


dfnew=df_new.drop(['Termd','MaritalDesc','EmpStatusID','FromDiversityJobFairID','MaritalDesc',
                  'HispanicLatino','RaceDesc','DateofHire','DateofTermination','EmploymentStatus',
                   'TermReason'], axis=1)
dfnew.head()


# In[13]:


#checking for null values
dfnew.isnull()


# In[14]:


from datetime import datetime

def calculate_age_from_column(timestamp):
    # Convert the Timestamp object to a string in the format 'YYYY-MM-DD'
    date_str = timestamp.strftime('%Y-%m-%d')

    # Split the date string into year, month, and day components
    year, month, day = map(int, date_str.split('-'))

    # Get the current date
    current_date = datetime.today().date()

    # Create a datetime.date object from the components
    birthdate_obj = datetime(year, month, day).date()

    # Calculate the difference between the current date and birthdate
    age_delta = current_date - birthdate_obj

    # Extract the age in years from the difference
    age_years = age_delta.days // 365

    return age_years


# Convert the 'DOB' column to pandas Timestamp object
dfnew['DOB'] = pd.to_datetime(dfnew['DOB'])

# Apply the function to the 'DOB' column and store the result in a new column 'Age'
dfnew['Age'] = dfnew['DOB'].apply(calculate_age_from_column)

print(dfnew)


# In[15]:


# Convert the 'DOB' column to pandas Timestamp object
dfnew['LastPerformanceReview_Date'] = pd.to_datetime(dfnew['LastPerformanceReview_Date'])

# Apply the function to the 'DOB' column and store the result in a new column 'Age'
dfnew['LPRD_years'] = dfnew['LastPerformanceReview_Date'].apply(calculate_age_from_column)

print(dfnew)


# In[17]:


dfnew.to_csv("C:/Users/Onkar Kadam/Desktop/TCS Internship 2023/HRData.csv")


# In[ ]:




