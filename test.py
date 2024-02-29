import numpy as np
import matplotlib.pyplot as plt
import modules.angle_filter as af

theta = np.linspace(-360, 360, 1000)

theta_f = np.zeros(len(theta))
for i in range(len(theta)):
    theta_f[i] = af.angle_filter(theta[i], 0, 180)

plt.plot(theta, theta_f)
plt.show()