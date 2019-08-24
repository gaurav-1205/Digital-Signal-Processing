import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift as sh

n = np.linspace(-3, 7, 11)

#x(n)
xn = np.array([0, 0, 0, 0, 2, 3, 1, 0, 0, 0, 0])

xn_right = sh(xn, 2, cval = 0)
#print(xn_right)
plt.stem(n, xn_right)
plt.xlabel('$n$')
plt.ylabel('$x(n-2)$')
plt.ylim(0, 4)

plt.show()