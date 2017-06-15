import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    p = np.arange(0.001, 1, 0.001)
    gini = 2 * p * (1 - p)
    h = -(p * np.log2(p) + (1-p)*np.log2((1-p)))/2
    err = 1- np.max(np.vstack((p, 1-p)), 0)
    print p.shape
    print np.max(np.vstack((p, 1-p)), 0)
    plt.plot(p, gini, label='Gini')
    plt.plot(p, h, label='Entropy')
    plt.plot(p, err, '--', label='Error')
    plt.legend()
    plt.grid(True)
    plt.show()