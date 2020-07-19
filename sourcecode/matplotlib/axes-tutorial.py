# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# 疊加圖表
fig = plt.figure(figsize=[10, 4])

plt.axes([0, 0, 0.8, 1])
plt.title(label='chart1')
plt.plot([1, 2, 3], 'r-o')

plt.axes([0.55, 0.1, 0.2, 0.2])
plt.title(label='chart2')
plt.plot([1, 2, 3], 'r-o')
plt.show()