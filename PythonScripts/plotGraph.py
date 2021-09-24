import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
x = data[:, 0]
y = data[:, 3]
# errorbar expects array of shape 2xN and not Nx2 (N = len(x)) for xerr and yerr
xe = data[:, 1:3].T
ye= data[:, 4:].T

plt.errorbar(x, y, xerr=xe, yerr=ye, fmt=".-")

# if you want a log plot:
plt.xscale("log")
plt.yscale("log")

plt.show()
