# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt


def plot():
    x = [1, 2, 4, 5]
    y = [4, 6, 8, 10]
    plt.plot(x, y, linestyle='-', label='測試label')

    # 中文顯示處理
    plt.rcParams['font.sans-serif'] = "Microsoft JhengHei"
    plt.title('測試標題')

    # 使用到label時需要加上
    plt.legend()

    plt.show()


if __name__ == '__main__':
    plot()