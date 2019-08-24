import numpy as np 
import matplotlib.pyplot as plt
x = np.array([0, 0, 0, 0, 2, 3, 1, 0, 0, 0, 0])
n = np.linspace(-3, 7, 11)
#print(n, x)
plt.stem(n, x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.ylim((0, 3))

plt.show()