import matplotlib.pyplot as plt
import numpy as np
import time

def first_digit1(x):
    while x >= 10:
        x /= 10
    return x

def first_digit2(x):
    return int(str(x)[0])

if __name__ == '__main__':
    n = 1
    count = [0] * 9
    start = time.time()
    # for i in range(1, 1000):
    #     n *= i
    #     count[first_digit1(n) - 1] += 1
    # print time.time()-start

    start = time.time()
    for i in range(1, 10000):
        n *= i
        count[first_digit2(n) - 1] += 1
    print time.time()-start

    x = range(1, 10)
    plt.plot(x, count)
    plt.show()