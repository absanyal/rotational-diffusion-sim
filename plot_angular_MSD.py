import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

t, ang_disp, theta_disp, phi_disp, ang_cumu = np.loadtxt(
    "data/ang_disp.dat", unpack=True)

plt.figure(tight_layout=True)

labelinterval = pi
labelmax = max([max(ang_disp), max(theta_disp), max(phi_disp)])
labelmax = int(180/pi*labelmax + labelinterval)
print(labelmax)
y_labels = np.arange(0, labelmax, labelinterval)

plt.plot(t, ang_disp, label=r"$\langle ( dot )^2 \rangle$", linewidth=1.5)
plt.plot(t, theta_disp, label=r"$\langle \Delta \theta^2 \rangle$", linewidth=1.5)
plt.plot(t, phi_disp, label=r"$\langle \Delta \phi^2 \rangle$", linewidth=1.5)
# plt.plot(t, ang_cumu, label=r"$\langle ( cumulative )^2 \rangle$", linestyle="--", linewidth=1.5)

plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel(r"MSD", fontsize=18)
plt.xlim(left=0)
plt.ylim(bottom=0)
# plt.yticks(y_labels)
plt.grid(axis="y", linestyle="--")
plt.legend()
plt.savefig("plots/angular_MSD.pdf")
