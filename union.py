#!/usr/bin/env python
# coding: utf-8

# In[1]:


from shapely.geometry import mapping, shape


# In[2]:


from shapely.ops import cascaded_union


# In[3]:


from fiona import collection


# In[4]:


with collection("some_buffer.shp", "r") as input:
    schema = input.schema.copy()
    with collection(
            "some_union.shp", "w", "ESRI Shapefile", schema) as output:
        shapes = []
        for f in input:
            shapes.append(shape(f['geometry']))
        merged = cascaded_union(shapes)
        output.write({
            'properties': {
                'name': 'Buffer Area'
                },
            'geometry': mapping(merged)
            })

