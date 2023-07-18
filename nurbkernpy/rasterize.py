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

print(nurb.control_points)

rasterized_curve = nurb.rasterize_to_numpy(1000)

plt.figure()
plt.plot(
    np.sin(np.linspace(0, 2 * np.pi, 1000)),
    np.cos(np.linspace(0, 2 * np.pi, 1000)),
)
plt.plot(
    rasterized_curve[:, 0],
    rasterized_curve[:, 1],
)
plt.gca().set_aspect(1)
plt.savefig("nurbkernpy/curve.png")