#!/usr/bin/env python
# coding: utf-8

# In[1]:


from shapely.geometry import mapping, shape


# In[2]:


from fiona import collection


# In[3]:


with collection('sample.shp', 'r') as input:
    #schema = input.schema.copy()
    schema = { 'geometry': 'Polygon', 'properties': { 'name': 'str'} }
    with collection(
    'some_buffer.shp', 'w', 'ESRI Shapefile', schema) as output:
        for point in input:
            output.write({
                'properties': {
                    'name': point['properties']['name']
                },
                'geometry': mapping(shape(point['geometry']).buffer(5.0))
            })

