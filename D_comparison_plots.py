import numpy as np
import modules.filament as flm
import modules.brownian as brn
import modules.parameters as prm
import modules.angle_filter as af
from numpy import pi
import matplotlib.pyplot as plt

f = flm.filament(prm.monomers, radius=prm.radius)

p_list = np.linspace(1.0, 20.0, 100)

D_par_list = np.zeros(len(p_list))
D_perp_list = np.zeros(len(p_list))
D_rot_list = np.zeros(len(p_list))

D_par_p1 = brn.D_par(1.0)
D_perp_p1 = brn.D_perp(1.0)
D_rot_p1 = brn.D_rot(1.0)

for i, p in enumerate(p_list):
    D_par_list[i] = brn.D_par(p) / D_par_p1
    D_perp_list[i] = brn.D_perp(p) / D_perp_p1
    D_rot_list[i] = brn.D_rot(p) / D_rot_p1

plt.figure(tight_layout=True)
plt.plot(p_list, D_par_list, label=r"$D_{par} (p) / D_{par} (1)$")
plt.plot(p_list, D_perp_list, label=r"$D_{perp} (p) / D_{perp} (1)$")
plt.plot(p_list, D_rot_list, label=r"$D_{rot} (p) / D_{rot} (1)$")
plt.xlabel(r"$p$", fontsize=18)
plt.ylabel("Scaled Diffusion Coefficient", fontsize=16)
plt.xscale("log")
plt.legend(fontsize=14)

plt.savefig("plots/D_comparison.pdf")