#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as ny 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('LargestCompaniesInUSAbyReveneue.csv')


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.head()


# In[7]:


print(df.isnull().sum())


# In[8]:


df['Revenue growth'] = df['Revenue growth'].str.rstrip('%').astype(float)


# In[9]:


df['Revenue (USD millions)'] = df['Revenue (USD millions)'].str.replace(',', '').astype(int)


# In[10]:


df.head()


# In[11]:


df['Employees'] = df['Employees'].str.replace(',', '').astype(int)



# In[12]:


df.head()


# In[13]:


import matplotlib.pyplot as plt


# In[15]:


import seaborn as sns


# In[17]:


plt.figure(figsize=(10, 6))
sns.barplot(x='Revenue (USD millions)', y='Name', data=df.head(10))
plt.title('Top 10 Companies by Revenue')
plt.xlabel('Revenue (USD millions)')
plt.ylabel('Company Name')
plt.show()


# In[18]:


plt.figure(figsize=(10, 6))
sns.countplot(y='Industry', data=df, order=df['Industry'].value_counts().index)
plt.title('Number of Companies in Each Industry')
plt.xlabel('Number of Companies')
plt.ylabel('Industry')
plt.show()


# In[19]:


top_5_companies = df.head(5)
print(top_5_companies)


# In[20]:


print("Summary Statistics of Revenue Growth:")
print(df['Revenue growth'].describe())


# In[21]:


industry_revenue = df.groupby('Industry')['Revenue (USD millions)'].sum().sort_values(ascending=False)
print(industry_revenue)


# In[ ]:




