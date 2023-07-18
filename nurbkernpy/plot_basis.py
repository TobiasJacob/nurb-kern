import nurbkern
import numpy as np
import matplotlib.pyplot as plt

# maturin develop && python -m nurbkernpy.plot_basis

# Create a 2D B-spline curve
plt.figure()
p = 3
knots = [0.0, 0.0, 0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0, 1.0, 1.0]
X = np.linspace(0, 1, 200)
Y = np.zeros((X.shape[0], len(knots) - p - 1))

for k in range(len(knots) - p - 1):
    for i, x in enumerate(X):
        n = nurbkern.nurb_naive(x, k, p,knots)
        print(n)
        Y[i, k] = n

# Plot all basis functions
plt.plot(X, Y)
plt.savefig("nurbkernpy/basis.png")

# Create a 2D B-spline curve
plt.figure()
p = 3
knots = [0.0, 0.0, 0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0, 1.0, 1.0]
X = np.linspace(0, 1, 200)
Y = np.zeros((X.shape[0], len(knots) - p - 1))

for k in range(len(knots) - p - 1):
    for i, x in enumerate(X):
        n = nurbkern.nurb_iterative(x, k, p,knots)
        print(n)
        Y[i, k] = n

# Plot all basis functions
plt.plot(X, Y)
plt.savefig("nurbkernpy/basis2.png")

# Create a 2D B-spline curve
plt.figure()
p = 3
knots = [0.0, 0.0, 0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0, 1.0, 1.0]
X = np.linspace(0, 1, 200)
Y = np.zeros((X.shape[0], len(knots) - p - 1))

for k in range(len(knots) - p - 1):
    for i, x in enumerate(X):
        n = nurbkern.nurb_fast(x, k, p,knots)
        print(n)
        Y[i, k] = n

# Plot all basis functions
plt.plot(X, Y)
plt.savefig("nurbkernpy/basis3.png")
