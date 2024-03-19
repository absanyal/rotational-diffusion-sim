import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, ang_disp, ang_disp_sq = np.loadtxt("data/single_window_theta.dat", unpack=True)

plt.figure(tight_layout=True)
plt.plot(t, ang_disp)
plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel(r"$\Delta \theta$", fontsize=18)
plt.savefig("plots/single_window_theta.pdf")

plt.figure(tight_layout=True)
plt.plot(t, ang_disp_sq)
plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel(r"$\Delta \theta^2$", fontsize=18)
plt.savefig("plots/single_window_theta_sq.pdf")

t, theta_sq_sampled = np.loadtxt("data/single_window_theta_sampled.dat", unpack=True)

def f(x, m, c):
    return m * x + c

popt, pcov = curve_fit(f, t, theta_sq_sampled)

D_measured = popt[0] / 2.0

p, D_input = np.loadtxt("data/Drot_from_sampling_run.dat", unpack=True)

print("D_input = {:.4e}".format(D_input))
print("D_measured = {:.4e}".format(D_measured))
error = np.abs((D_input - D_measured) / D_input) * 100
print("Error = {:.2f} %".format(error))

fitline = f(t, *popt)

with open("data/Drot_from_sampling_measured.dat", "w") as file:
    file.write("# Drot(input) \t\t Drot(measured) \t Error(%)\n")
    file.write("{:.4e}\t{:.4e}\t{:.2f}".format(D_input, D_measured, error))

mean_sq_err = 0
for i in range(len(t)):
    mean_sq_err += ((theta_sq_sampled[i] - fitline[i]))**2

mean_sq_err /= len(t)

print("rms error in fitting= {:.4e}".format((mean_sq_err)**0.5))


plt.figure(tight_layout=True)
plt.plot(t, theta_sq_sampled, 'k-' , label=r"$\langle \Delta \theta^2 \rangle$")
plt.plot(t, fitline, 'r--', label="Fit")
plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel(r"$\langle \Delta \theta^2 \rangle$", fontsize=18)
plt.legend(fontsize=14)
plt.savefig("plots/single_window_theta_sampled.pdf")