#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt

mens_avg_height = [181, 177, 180.3, 180.4, 168, 165.1, 172, 175.3]
womens_avg_height = [168, 163, 167.4, 166.5, 156, 154.2, 158, 161.5]
data = [mens_avg_height, womens_avg_height]

fig, ax = plt.subplots()
ax.set_ylabel('Height (cm)')
ax.set_xlabel('Gender')
ax.set_title('Average Height of Men and Women in Eight Countries')

ax.boxplot(data)
plt.xticks([1, 2], ['Men', 'Women'])

plt.show()

