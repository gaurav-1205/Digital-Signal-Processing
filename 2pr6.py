import numpy as np
import matplotlib.pyplot as plt

#|t| < 1
t1 = np.linspace(-1, 1, 25)
x1 = 2+abs(t1)

#1<|t|<4
t2a = np.linspace(-4, -1, 25)
t2b = np.linspace(1, 4, 25)
x2 = 4 - abs(t2a)
x3 = 4 - abs(t2b)

#x(t)
np.concatenate(x2, x1, x3)
