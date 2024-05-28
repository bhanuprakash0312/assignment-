#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as  pd
df=pd.read_csv("Used_Bikes.csv")
print(df)
count= (df['owner'].value_counts())
count


# In[17]:


df[(df['city']=='Jaipur')&(df['price']<=60000)]


# In[27]:


df[(df['owner']=='First Owner')&(df['age']<=5)]


# In[46]:


min_price_bike = df[(df['brand']=='KTM') & (df['price'] == df[df['brand'] == 'KTM']['price'].min())]
print(min_price_bike)


# In[45]:


max_price_bike = df[(df['brand']=='KTM') & (df['price'] == df[df['brand'] == 'KTM']['price'].max())]
print(max_price_bike)

