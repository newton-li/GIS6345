#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[1]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[7]:


map1 = gis.map('Kaneohe, HI')
map1


# In[8]:


# Item Added From Toolbar
# Title: Annual Rainfall (in) | Type: Feature Service | Owner: HawaiiStateGIS
item = gis.content.get("f0cadb44d59a495298cebe80247bff80")
item


# In[9]:


map1.add_layer(item)

