#!/usr/bin/env python
# coding: utf-8

#/******************************************************************************
#*Title:Grouped bar chart with labels source code
#*Author:Hunter, J., Dale, D., Firin, E., Droettboom, M., Matplotlib developement team
#*Date:2020
#Code version:3.2.2
#Availability:https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
#*
#******************************************************************************/

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

countries = ['Iceland', 'Ireland', 'Slovenia', 'Croatia', 'Cuba', 'Bahrain', 'Japan', 'United States']
mens_avg_height = [181, 177, 180.3, 180.4, 168, 165.1, 172, 175.3]
womens_avg_height = [168, 163, 167.4, 166.5, 156, 154.2, 158, 161.5]

x = np.arange(len(countries))
width = 0.35

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, mens_avg_height, width, label='Men')
bars2 = ax.bar(x + width/2, womens_avg_height, width, label='Women')

ax.set_ylabel('Height (cm)')
ax.set_title('Average Height of Men and Women in Eight Countries')
ax.set_xticks(x)
plt.xticks(rotation=90)
ax.set_xticklabels(countries)
ax.set_xlabel('Country')
ax.legend()
ax.legend(handles=[bars1, bars2], title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')

def htlabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(1, -25),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    size='small',
                    rotation=90,
                    c='white', fontweight='semibold')

htlabel(bars1)
htlabel(bars2)

fig.tight_layout()

plt.show()



