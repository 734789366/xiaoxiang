import matplotlib.pyplot as plt
import numpy as np
from scipy import special

if __name__ == '__main__':
    p = 0.6
    a, b, c = 0, 0, 0
    t, T = 0, 1000000
    while t < T:
        a = b = 0
        while (a <= 11) and (b <= 11):
            if np.random.uniform() < p:
                a += 1
            else:
                b += 1

        if a > b:
            c += 1
        t += 1
    print float(c)/float(T)

    answer = 0
    N = 11
    for x in np.arange(N):
        answer += special.comb(N + x - 1, x) * ((1-p) **x) * (p ** N)
    print answer

    answer = 0
    for x in np.arange(N-1):
        answer += special.comb(N+x-1, x) * ((1-p)**x)*(p**N)
    p10 = special.comb(2*(N-1), N-1) * ((1-p)*p)**(N-1)
    t = 0
    for n in np.arange(100):
        t += (2*p*(1-p)) ** n *p**2
    answer += p10 * t
    print answer