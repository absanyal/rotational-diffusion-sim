import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from scipy.optimize import curve_fit
import modules.brownian as brn
import modules.parameters as prm
import modules.filament as flm

test_filament = flm.filament(prm.monomers, radius=prm.radius)

t, ang_disp, theta_disp, phi_disp, ang_cumu = np.loadtxt(
    "data/ang_disp.dat", unpack=True)


def fit_function(x, m, c):
    return m * x + c

t_fit = np.linspace(min(t), max(t), 10000)


popt, pcov = curve_fit(fit_function, t, ang_disp)

p = test_filament.contour_length() / (2.0 * test_filament.radius)
# print("p = ", p)
D_rot_input = brn.D_rot(p) / brn.D_rot_0()
# print("D_rot(p) = {:.2e}".format(D_rot_input))

plt.figure(tight_layout=True)

plt.plot(t, ang_disp, label=r"$\langle ( dot )^2 \rangle$",
         linewidth=2.0, color="red")
plt.plot(t_fit, fit_function(t_fit, *popt), label="Linear fit",
         linestyle=":", linewidth=1.5, color="black")

plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel(r"MSD", fontsize=18)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(axis="y", linestyle="--")
plt.legend()
plt.savefig("plots/angular_MSD_fit.pdf")

#### Slope analysis ####

slope = popt[0]
# print("Slope: {:.2e}".format(slope))

D_rot_measured = slope / 2.0
err = abs((D_rot_input - D_rot_measured) / D_rot_input) * 100.0

print("p = ", p)
print("D_rot(p) = {:.4e}".format(D_rot_input))
print("D_rot_measured: {:.4e}".format(D_rot_measured))
print("Error: {:.4f} %".format(err))


with open("data/Drot_meas_reduced.dat", "w") as file:
    file.write("# D_rot_input\tD_rot_measured\tError(%)\n")
    file.write("{}\t{}\t{:.4f}".format(D_rot_input, D_rot_measured, err))

D_rot_input_scaled = D_rot_input * brn.D_rot_0()
D_rot_measured_scaled = D_rot_measured * brn.D_rot_0()
err = abs((D_rot_input_scaled - D_rot_measured_scaled) /
          D_rot_input_scaled) * 100.0

print("D_rot_input_scaled: {:.4e}".format(D_rot_input_scaled))
print("D_rot_measured_scaled: {:.4e}".format(D_rot_measured_scaled))

with open("data/Drot_meas_scaled.dat", "w") as file:
    file.write("# D_rot_input\tD_rot_measured\tError(%)\n")
    file.write("{}\t{}\t{:.4f}".format(D_rot_input_scaled,
                                      D_rot_measured_scaled, err))
