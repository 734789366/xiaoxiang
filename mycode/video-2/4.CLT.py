import numpy as np
import matplotlib.pyplot as plt

a = np.random.uniform(0, 1, 10000)
plt.hist(a, 100, facecolor='g', alpha=0.75)
plt.show()

times = 10000
for i in range(times):
    a += np.random.uniform(0, 1, 10000)
print a
print a/times
plt.hist(a, 100, facecolor='g', alpha=0.75)
plt.grid(True)
plt.show()