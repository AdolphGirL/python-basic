# -*- coding: utf-8 -*-


import numpy as np

x = np.arange(1, 10).reshape(3, 3)
y = np.arange(10, 19).reshape(3, 3)
print(x)
print(y)

# 對元素加上一個數值
print(x + 1)

# 陣列中元素取平方
print(x ** 2)

# 對陣列中元素進行判斷，返回一個布林陣列
print(y > 10)

# 對第一個row + 1
print(y[0, :] + 1)

# 對第一個col + 1
print(y[:, 0] + 1)

print(x + y)

# print(x.max())
print(np.max(x, axis=0))