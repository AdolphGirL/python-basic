# -*- coding: utf-8 -*-


import numpy as np


x = [1, 2]
print('x * 2 = {}'.format(x * 2))

# ndarray，其中元素的資料，必須是同一類型
y = np.array([1, 2])
print('y * 2 = {}'.format(y * 2))

# 建立的方式
z1 = np.array([1, 2, 3])
z2 = np.array((1, 2, 3))
print(z1)
print(z2)

z3 = np.arange(1, 10, 2)
z4 = np.linspace(1, 10, 15)
print(z3)
print(z4)

# reshape
z5 = np.arange(1, 17)
print(z5.size)
z6 = z5.reshape(4, -1)
z7 = z5.reshape(-1, 2, 2)
print(z6)
print(z7.shape)