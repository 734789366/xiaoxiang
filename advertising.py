# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:36:44 2017

@author: tensorflow
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Advertising.csv')
feature_columns = ['TV', 'Radio', 'Newspaper']

x = data[feature_columns]
y = data['Sales']

plt.figure(figsize=(9, 12))
plt.subplot(511)
plt.plot(data['TV'], y, 'ro')
plt.title('TV')
plt.grid()

plt.subplot(512)
plt.plot(data['Radio'], y, 'g^')
plt.title('Radio')
plt.grid()

plt.subplot(513)
plt.plot(data['Newspaper'], y, 'b*')
plt.title('Newspaper')
plt.grid()

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=1)
linreg = LinearRegression()
model = linreg.fit(X_train, y_train)

print model
print linreg.intercept_
print linreg.coef_

zip(feature_columns, linreg.coef_)

y_predict = model.predict(X_test)

plt.subplot(514)
plt.plot(range(len(y_test)), y_test, 'b')
plt.plot(range(len(y_predict)), y_predict, 'y-')
plt.title('predict_real')
plt.grid()

loss = y_test - y_predict
plt.subplot(515)
plt.plot(range(len(loss)), loss, 'y-')
plt.title('loss')
plt.grid()

plt.tight_layout()
plt.show()

sum_mean = 0

for i in range(len(y_test)):
    sum_mean += (y_predict[i]- y_test.values[i])**2
print ('Root Mean Squared Error', np.sqrt(sum_mean/len(y_predict)))