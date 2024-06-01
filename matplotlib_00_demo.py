#!/usr/bin/python3

import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

print(mp.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()