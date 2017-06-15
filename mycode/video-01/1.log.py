import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    x = np.arange(0.05, 5, 0.05)
    y1 = [math.log(a, 1.5) for a in x]
    y2 = [math.log(a, 2) for a in x]
    y3 = [math.log(a, 3) for a in x]

    plt.plot(x, y1, linewidth=2, label='log1.5(x)')
    plt.plot(x, y2, linewidth=2, label='log2(x)')
    plt.plot(x, y3, linewidth=2, label='log3(x)')
    print y1[0], y1[-1]
    plt.plot((1, 1), (-10, 10), '--')

    plt.title('math log')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()