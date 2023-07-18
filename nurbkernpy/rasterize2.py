import nurbkern
import numpy as np
import matplotlib.pyplot as plt

# maturin develop && python -m nurbkernpy.rasterize

cp1 = np.array([
    [-1, 0, 0, 1],
    [-1, 3, 0, 2],
    [4, 1, 0, 0.5]
])
nurb1 = nurbkern.Nurb(
    degree=3,
    knots=[0, 0, 0, 1, 1, 1],
    control_points=[
        nurbkern.ControlPoint(c[0], c[1], c[2], c[3]) for c in cp1
    ]
)

N = 1000
plt.figure(figsize=(8, 8))
rasterized_curve = nurb1.rasterize_to_numpy(N)
plt.plot(
    rasterized_curve[:, 0],
    rasterized_curve[:, 1],
    "o"
)
deriv = np.diff(rasterized_curve, axis=0) * N
derivAnalytic = nurb1.derivative().rasterize_to_numpy(N)
print(deriv)
print(derivAnalytic)
derivderiv = np.diff(deriv, axis=0) * N
derivderivderiv = np.diff(derivderiv, axis=0) * N
plt.quiver(
    rasterized_curve[:-2, 0],
    rasterized_curve[:-2, 1],
    derivderiv[:, 0],
    derivderiv[:, 1],
    # Do not normalize the arrows
    angles='xy',
)
plt.plot(
    cp1[:, 0],
    cp1[:, 1],
)
plt.gca().set_aspect(1)
# plt.xlim(-1.1, 0.1)
# plt.ylim(-0.1, 1.1)
plt.savefig("nurbkernpy/curve2.png")