import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)
y = x**x
y_min = np.min(y)
print "y_min:", y_min
print "x(y_min):", x[np.argmin(y)]
print "y_min-e**(-1/e) = ", y_min-np.e**(-1/np.e)
plt.plot(x, y, label='y = x**x')
plt.title("y = x**x")
plt.legend(loc= 'lower right')
plt.show()