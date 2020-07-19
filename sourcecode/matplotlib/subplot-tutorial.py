# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# tight_layout防止圖表相疊
fig = plt.figure(figsize=[10, 5], tight_layout=True)
plt.subplot(211)
plt.title(label='chart 1', fontsize=20)
plt.plot([1, 2, 3], 'r:o')

plt.subplot(212)
plt.title(label='chart 2', fontsize=20)
plt.plot([1, 2, 3], 'r:o')

plt.show()