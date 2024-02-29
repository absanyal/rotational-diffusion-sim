import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

data = np.loadtxt("data/single_run.dat")

t_list = data[:, 0]

#########  Angular displacement  #########

ang_disp_list = data[:, 1:]

n_trials = len(ang_disp_list[1])

# labelmax = (180/pi)*max(ang_disp_list)
y_labels = np.arange(0, 181, 90)

plt.figure(tight_layout=True)

for n in range(n_trials):
    plt.plot(t_list, (180/pi)*ang_disp_list[:, n], linewidth=0.5)

plt.xlabel("Time")
plt.ylabel(r"Angular displacement ($\degree$)")
plt.yticks(y_labels)
plt.grid(axis="y")

plt.savefig("plots/single_ang.pdf")

plt.clf()
plt.cla()

#########  Angular displacement squared  #########

data_sq = np.loadtxt("data/single_run_sq.dat")

ang_disp_sq_list = data_sq[:, 1:]

n_trials = len(ang_disp_sq_list[1])

plt.figure(tight_layout=True)

for n in range(n_trials):
    plt.plot(t_list, ang_disp_sq_list[:, n], linewidth=0.5)

plt.xlabel("Time")
plt.ylabel("Angular displacement squared")

plt.grid(axis="y")

plt.savefig("plots/single_ang_sq.pdf")

plt.clf()
plt.cla()

#########  Theta displacement  #########

data = np.loadtxt("data/single_run_theta.dat")

theta_list = data[:, 1:]

n_trials = len(theta_list[1])

plt.figure(tight_layout=True)

for n in range(n_trials):
    plt.plot(t_list, theta_list[:, n], linewidth=0.5)

plt.xlabel("Time")
plt.ylabel("Theta displacement")

plt.grid(axis="y")

plt.savefig("plots/single_theta.pdf")

plt.clf()
plt.cla()

#########  Theta displacement squared  #########

data_sq = np.loadtxt("data/single_run_theta_sq.dat")

theta_sq_list = data_sq[:, 1:]

n_trials = len(theta_sq_list[1])

plt.figure(tight_layout=True)

for n in range(n_trials):
    plt.plot(t_list, theta_sq_list[:, n], linewidth=0.5)

plt.xlabel("Time")
plt.ylabel("Theta displacement squared")

plt.grid(axis="y")

plt.savefig("plots/single_theta_sq.pdf")

plt.clf()
plt.cla()

#########  Phi displacement  #########

data = np.loadtxt("data/single_run_phi.dat")

phi_list = data[:, 1:]

n_trials = len(phi_list[1])

plt.figure(tight_layout=True)

for n in range(n_trials):
    plt.plot(t_list, phi_list[:, n], linewidth=0.5)

plt.xlabel("Time")
plt.ylabel("Phi displacement")

plt.grid(axis="y")

plt.savefig("plots/single_phi.pdf")

plt.clf()
plt.cla()

#########  Phi displacement squared  #########

data_sq = np.loadtxt("data/single_run_phi_sq.dat")

phi_sq_list = data_sq[:, 1:]

n_trials = len(phi_sq_list[1])

plt.figure(tight_layout=True)

for n in range(n_trials):
    plt.plot(t_list, phi_sq_list[:, n], linewidth=0.5)

plt.xlabel("Time")
plt.ylabel("Phi displacement squared")

plt.grid(axis="y")

plt.savefig("plots/single_phi_sq.pdf")

