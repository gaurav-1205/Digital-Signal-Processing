import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift as sh

n = np.linspace(-3, 7, 11)
#x(n)
xn = np.array([0, 0, 0, 0, 2, 3, 1, 0, 0, 0, 0])

#x(-n)
xflip = (-1)*xn

#x(3-n)
xflip_right = sh(xflip, 3, cval = 0)
plt.stem(n, xflip_right)
plt.xlabel('$n$')
plt.ylabel('$x(3-n)$')
plt.ylim(0, -4)

plt.show()