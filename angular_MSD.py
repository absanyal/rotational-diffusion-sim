import numpy as np
import modules.filament as flm
import modules.brownian as brn
import modules.parameters as prm
import modules.angle_filter as af
from numpy import pi

f = flm.filament(prm.monomers, radius=prm.radius)

theta0 = f.theta
phi0 = f.phi
dir0 = f.get_direction()

t_max = 1000

t_list = np.zeros(t_max)

for t in range(t_max):
    t_list[t] = t * prm.dt

n_trials = 500

ang_disp_list = np.zeros(t_max)
theta_disp_list = np.zeros(t_max)
phi_disp_list = np.zeros(t_max)
ang_cumu_list = np.zeros(t_max)

p = f.contour_length() / (2.0 * f.radius)
print("p = ", p)
print("D_rot(p) = ", brn.D_rot(p) / brn.D_rot_0())


for trial in range(n_trials):
    if trial % 100 == 0:
        print("Trial: ", trial, " of ", n_trials)
    f.theta = theta0
    f.phi = phi0
    ang_cumu = 0.0
    dir_old = f.get_direction()
    for t in range(len(t_list)):
        f = brn.perturb_filament_angle(f)
        dir_new = f.get_direction()
        ang_disp = np.arccos(np.dot(f.get_direction(), dir0))
        theta_disp = (f.theta - theta0)
        phi_disp = (f.phi - phi0)
        ang_incremental = np.arccos(np.dot(dir_new, dir_old))
        ang_cumu = ang_incremental
        ang_disp_list[t] += ang_disp**2
        theta_disp_list[t] += theta_disp**2
        phi_disp_list[t] += phi_disp**2
        ang_cumu_list[t] += ang_cumu**2

print("Trial: ", n_trials, " of ", n_trials)
print("Done")

ang_disp_list /= n_trials
theta_disp_list /= n_trials
phi_disp_list /= n_trials
ang_cumu_list /= n_trials

with open("data/ang_disp.dat", "w") as file:
    for t in range(len(t_list)):
        file.write("{}\t{}\t{}\t{}\t{}\n".format(t_list[t], ang_disp_list[t], theta_disp_list[t], phi_disp_list[t], ang_cumu_list[t]))

    