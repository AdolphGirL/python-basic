# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt


# 預設值測試
fig = plt.figure()
plt.plot([1, 2, 3])
plt.show()

# 有設定值
fig = plt.figure(
    figsize=[10, 5], dpi=96, facecolor='whitesmoke', edgecolor='r', frameon=True
)
plt.grid(True)
plt.plot([1, 2, 3])
plt.show()