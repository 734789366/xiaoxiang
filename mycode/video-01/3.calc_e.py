import matplotlib.pyplot as plt
import numpy as np

'''Taylor:e**x = 1+x+x**2/2!+x**3/3!+...+x**n/n!'''
def calc_e_small(x):
    n = 10
    f = np.arange(1, n+1).cumprod() # factorial
    b = np.array([x]*n).cumprod() # x, x**2, x**3, ..., x**n
    print "f:", f
    print "b:", b
    return np.sum(b/f) +1

if __name__ == '__main__':
    x = np.arange(0, 10, 0.2)
    y = [calc_e_small(i) for i in x]
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()