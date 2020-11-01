#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


from shapely.geometry import Point, mapping


# In[3]:


from fiona import collection


# In[4]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str'} }


# In[7]:


with collection(
    'sample.shp', 'w', 'ESRI Shapefile', schema) as output:
    with open(r"C:\sample.csv", 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['lon']), float(row['lat']))
            output.write({ 
                'properties': {
                    'name': row['name']
                },
                'geometry': mapping(point)
            })

