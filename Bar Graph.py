#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas


# In[9]:


import pandas


# In[20]:


csv = 'C:/Users/likne/OneDrive/Documents/GIS 6345/Week 5/Newton_Week5/Storm_Water_-_Structure.csv'


# In[22]:


geopandas.read_file(csv)


# In[23]:


df = geopandas.read_file(csv)


# In[24]:


top = df.head(10)


# In[25]:


top


# In[26]:


pddf = pandas.DataFrame(top)


# In[36]:


pddf.flow_rate = pandas.to_numeric(pddf.flow_rate)


# In[38]:


pddf.plot.bar(x= 'type_name', y= 'flow_rate')


# In[ ]:




