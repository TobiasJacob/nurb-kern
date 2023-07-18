import nurbkern
import numpy as np
import matplotlib.pyplot as plt

# maturin develop && python -m nurbkernpy.rasterize

nurb = nurbkern.Nurb(
    degree=3,
    knots=[0, 0, 0, 1, 1, 1],
    control_points=[
        nurbkern.ControlPoint(-1, 0, 0, 1),
        nurbkern.ControlPoint(-1, 1, 0, 1 / np.sqrt(2)),
        nurbkern.ControlPoint(0, 1, 0, 1),
    ]
)
cp2 = np.array([
    [-1, 0, 0, 1],
    [-1, 1 + 2 / np.sqrt(2), 0, np.sin(np.pi / 4 / 2)],
    [1 / np.sqrt(2), 1 / np.sqrt(2), 0, 1]
])
nurb2 = nurbkern.Nurb(
    degree=3,
    knots=[0, 0, 0, 1, 1, 1],
    control_points=[
        nurbkern.ControlPoint(c[0], c[1], c[2], c[3]) for c in cp2
    ]
)
cp3 = np.array([
    [-1, 0, 0, 1],
    [-1, 1 / np.sqrt(2) - (1 - 1 / np.sqrt(2)), 0, np.sin(3 * np.pi / 4 / 2)],
    [-1 / np.sqrt(2), 1 / np.sqrt(2), 0, 1]
])
nurb3 = nurbkern.Nurb(
    degree=3,
    knots=[0, 0, 0, 1, 1, 1],
    control_points=[
        nurbkern.ControlPoint(c[0], c[1], c[2], c[3]) for c in cp3
    ]
)

print(nurb.control_points)


plt.figure(figsize=(8, 8))
plt.plot(
    np.sin(np.linspace(0, 2 * np.pi, 1000)),
    np.cos(np.linspace(0, 2 * np.pi, 1000)),
)
rasterized_curve = nurb.rasterize_to_numpy(1000)
plt.plot(
    rasterized_curve[:, 0],
    rasterized_curve[:, 1],
)
rasterized_curve = nurb2.rasterize_to_numpy(10)
plt.plot(
    rasterized_curve[:, 0],
    rasterized_curve[:, 1],
    "o"
)
plt.plot(
    cp2[:, 0],
    cp2[:, 1],
)
rasterized_curve = nurb3.rasterize_to_numpy(1000)
plt.plot(
    rasterized_curve[:, 0],
    rasterized_curve[:, 1],
)
plt.plot(
    cp3[:, 0],
    cp3[:, 1],
)
plt.gca().set_aspect(1)
# plt.xlim(-1.1, 0.1)
# plt.ylim(-0.1, 1.1)
plt.savefig("nurbkernpy/curve.png")