#!/usr/bin/env python
# coding: utf-8

import geopandas as gpd
import matplotlib.pyplot as plt

shp = "C:/osds.shp/osds_oah.shp"
data = gpd.read_file(shp)

data.head()

fig, ax = plt.subplots()

data['TYPE'].value_counts().plot.bar()
plt.xticks(rotation=0)
ax.set_xlabel('Sewage Disposal Type')
ax.set_ylabel('Count')
ax.set_title('On-Site Sewage Disposal Systems for the Island of Oahu, HI')

plt.show()



