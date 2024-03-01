import numpy as np
import modules.filament as flm
import modules.brownian as brn
import modules.parameters as prm
import modules.angle_filter as af
from numpy import pi
import matplotlib.pyplot as plt

f = flm.filament(prm.monomers, radius=prm.radius)

theta0 = f.theta
phi0 = f.phi
dir0 = f.get_direction()

t_max = 3000

t_list = np.zeros(t_max)

for t in range(t_max):
    t_list[t] = t * prm.dt

p = f.contour_length() / (2.0 * f.radius)
print("p = ", p)
print("D_rot(p) = ", brn.D_rot(p) / brn.D_rot_0())

ang_disp_list = np.zeros(t_max)
ang_disp_sq_list = np.zeros(t_max)

dir0 = f.get_direction()

for t in range(t_max):
    f = brn.perturb_filament_angle(f)
    ang_disp = np.arccos(np.dot(f.get_direction(), dir0))
    ang_disp_list[t] = ang_disp
    ang_disp_sq_list[t] = ang_disp**2
    
print("Writing data...")
with open("data/single_window_theta.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t{}\t{}\n".format(t_list[t], ang_disp_list[t], ang_disp_sq_list[t]))

sampling_window = 100

# n_samples is only used for random sampling
n_samples = 500

t, ang_disp, ang_disp_sq = np.loadtxt("data/single_window_theta.dat", unpack=True)

ang_disp_sq_avg_sampled = np.zeros(sampling_window)

# t0_iter_list = np.random.randint(0, t_max - sampling_window, n_samples)
t0_iter_list = np.arange(0, t_max - sampling_window)

print("t0_iter_list = ", t0_iter_list)

print("Number of samples = ", len(t0_iter_list))

t_shortened = t[:sampling_window]

# temp_ang_disp_sq = np.zeros(len(ang_disp_sq_avg_sampled))

for t0_i in t0_iter_list:
    for t_i in range(sampling_window):
        init_theta = ang_disp[t0_i]
        ang_disp_sq_avg_sampled[t_i] += (ang_disp[t0_i + t_i] - init_theta)**2
        # temp_ang_disp_sq[t_i] = (ang_disp[t0_i + t_i] - init_theta)**2
    # plt.plot(t_shortened, temp_ang_disp_sq, label = "t0 = {}".format(t[t0_i]))

# plt.legend()
# plt.show()

ang_disp_sq_avg_sampled /= len(t0_iter_list)

print("Writing data...")
with open("data/single_window_theta_sampled.dat", "w") as file:
    for t_i in range(sampling_window):
        file.write("{}\t{}\n".format(t_shortened[t_i], ang_disp_sq_avg_sampled[t_i]))

with open("data/Drot_from_sampling_run.dat", "w") as file:
    file.write("# p \t\t\t D_rot(p)/D_rot(0)\n")
    file.write("{}\t{}".format(p, brn.D_rot(p) / brn.D_rot_0()))