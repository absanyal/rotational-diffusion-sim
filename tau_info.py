import numpy as np
import modules.filament as flm
import modules.brownian as brn
import modules.parameters as prm
from modules.constants import *

f = flm.filament(prm.monomers, radius=prm.radius)
p = f.contour_length() / (2.0 * f.radius)

print("p = ", p)

print("D_0 = {} (micro-m)^2 / s".format(brn.D_0() * 1e12))

tau = (SIGMA0 ** 2) / (brn.D_0())

print("tau = {:.4f} ns".format(tau * 1e9))

with open("data/tau_info.dat", "w") as file:
    file.write("# tau (nano seconds)\n")
    file.write("{}\n".format(tau * 1e9))