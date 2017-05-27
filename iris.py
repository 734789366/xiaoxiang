# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:36:08 2017

@author: tensorflow
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]

if __name__ == '__main__':
    path = 'iris.data'
    
    data = np.loadtxt(path, dtype=np.float32, delimiter=',', converters={4: iris_type})
    x, y = np.split(data, (4,), axis=1)
    x = x[:, :2]
    
    logreg = LogisticRegression()
    logreg.fit(x, y.ravel())
    
    N, M = 500, 500
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, N)
    x1, x2 = np.meshgrid(t1, t2)
    t_test = np.stack((x1.flat, x2.flat), axis=1)