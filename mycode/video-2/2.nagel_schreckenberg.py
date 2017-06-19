# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

'''
环形公路交通堵塞情况模拟
'''

def clip(x, path):
    for i in range(len(x)):
        if x[i] >= path:
            x[i] %= path

path = 5000 # 环形公路长度
n = 100 # 公路上的车数量
v0 = 5 # 车辆的初始速度
p = [0.2, 0.4, 0.6, 0.8] # 车辆的随机减速概率
times = 3000 # 观察的时间

np.random.seed(0)
x = np.random.rand(n) * path # 100辆车的不同初始位置
x.sort()
v = np.tile(v0, n).astype(float) # 100辆车的初始速度数组，np.tile(v0, n)，重复v0， n次

fig, axes = plt.subplots(ncols=2, nrows=2)
plt.figure(figsize=(10, 8))
axes = axes.ravel()

for i in range(len(p)):
    for t in range(times): # 分析每个时刻的情况
        axes[i].scatter(x, [t]*n, s=1, c='k', alpha=0.05, label=p[i])
        for car in range(n): # 分析每辆车的情况
            if x[(car+1)%n] > x[car]:
                d = x[(car+1)%n] - x[car]
            else:
                d = path - (x[car] - x[(car+1)%n])

            if v[car] < d:
                print i
                if np.random.rand() > p[i]:
                    v[car] += 1
                else:
                    v[car] -= 1
            else:
                v[car] = d - 1
        v = v.clip(0, 150)
        x += v
        clip(x, path)

plt.xlim(0, path)
plt.ylim(0, times)
plt.xlabel(u'车辆位置', fontsize=16)
plt.ylabel(u'模拟时间', fontsize=16)
plt.title(u'环形公路车辆模拟', fontsize=20)
plt.tight_layout(pad=2)

plt.show()