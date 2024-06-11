import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Sushant@03',
                             database='crime_data')

print(connection)

# Define SQL query
sql_query = "SELECT * FROM crimetable"

# Execute SQL query and read results into a DataFrame
crime_df = pd.read_sql(sql_query, connection)

print("\n# Dataset")
print(crime_df)

# Statistical analysis on dataframe
print("\n# Description of our dataset")
print(crime_df.describe(include='all'))

print(crime_df.describe())

# Gives the info about the dataset
print("\n# Information of our dataset")
print(crime_df.info())

# Checking if any null value is there in data or not
print("\n# Null values in dataset")
print(crime_df.isnull().sum())

# Getting unique values from some specific columns
print("\n# Common Area names")
print(crime_df['AREA_NAME'].unique())   #Common areas

print("\n# Common victim ages")
print(crime_df['Vict_Age'].unique())    #Common ages

print("\n# Common crime status")
print(crime_df['Status'].unique())      #Common status

print("\n# Common premis description")
print(crime_df['Premis_Desc'].unique()) #Common premis_Desc

print("\n# Common locations")
print(crime_df['Location'].unique())    #Common locations

#Most common victim age
print("\n# Count of victim ages")
print(crime_df['Vict_Age'].value_counts())

#Getting Crm_Cd and Crm_Cd_Desc distinct
print("\n# Getting crime code and crime code description")
distinct_crm = crime_df[['Crm_Cd','Crm_Cd_Desc']].drop_duplicates()
print(distinct_crm)

#Max occurence of crime
print("\n# Max crime occurence date")
print(crime_df['DATE_OCC'].value_counts())

#Victim sex crime analysis
plt.figure(figsize=(15,3))
sns.histplot(crime_df['Vict_Sex'],bins=3,kde=True)  #histogram  plot
plt.show()

# Day of week crime analysis
crime_df['Date'] = pd.to_datetime(crime_df['DATE_OCC'])
crime_df['day_of_week'] = crime_df['Date'].dt.day_name()
print("\n# Day of week count\n")
print(crime_df['day_of_week'].value_counts())

sns.countplot(x=crime_df['day_of_week'])
plt.show()

#Monthly crime analysis
crime_df['Date'] = pd.to_datetime(crime_df['DATE_OCC'])
crime_df['month_name'] = crime_df['Date'].dt.month_name()
print("\n# Month name count")
print(crime_df['month_name'].value_counts())

sns.countplot(x=crime_df['month_name'])
plt.show()

# Common premis desc
print("\n# Top 10 Premis location")
print(crime_df['Premis_Desc'].value_counts().head(10))

plt.pie(crime_df['Vict_Sex'].value_counts().values,labels=crime_df['Vict_Sex'].value_counts().index,autopct="%4.2f%%")
plt.title("Sex proportion of Victims")
plt.show()

# crime status analysis
print("\n# Status value count")
print(crime_df['Status'].value_counts())

sns.countplot(x=crime_df['Status'])
plt.show()
