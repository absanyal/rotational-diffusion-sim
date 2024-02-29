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

t_max = 10000

t_list = np.zeros(t_max)

for t in range(t_max):
    t_list[t] = t * prm.dt

n_trials = 50

p = f.contour_length() / (2.0 * f.radius)
print("p = ", p)
print("D_rot(p) = ", brn.D_rot(p) / brn.D_rot_0())

ang_disp_list = np.zeros((n_trials, t_max))
ang_disp_sq_list = np.zeros((n_trials, t_max))
theta_list = np.zeros((n_trials, t_max))
theta_sq_list = np.zeros((n_trials, t_max))
phi_list = np.zeros((n_trials, t_max))
phi_sq_list = np.zeros((n_trials, t_max))

for trial in range(n_trials):
    print("Trial {} of {}".format(trial+1, n_trials))
    f.theta = theta0
    f.phi = phi0
    for t in range(t_max):
        f = brn.perturb_filament_angle(f)
        ang_disp = np.arccos(np.dot(f.get_direction(), dir0))
        ang_disp_list[trial, t] = ang_disp
        ang_disp_sq_list[trial, t] = ang_disp**2
        
        theta_disp = (f.theta - theta0)
        theta_list[trial, t] = theta_disp
        theta_sq_list[trial, t] = theta_disp**2
        
        phi_disp = (f.phi - phi0)
        phi_list[trial, t] = phi_disp
        phi_sq_list[trial, t] = phi_disp**2

print("Writing data...")

with open("data/single_run.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t".format(t_list[t]))
        for trial in range(n_trials):
            file.write("{}\t".format(ang_disp_list[trial, t]))
        file.write("\n")

with open("data/single_run_sq.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t".format(t_list[t]))
        for trial in range(n_trials):
            file.write("{}\t".format(ang_disp_sq_list[trial, t]))
        file.write("\n")

with open("data/single_run_theta.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t".format(t_list[t]))
        for trial in range(n_trials):
            file.write("{}\t".format(theta_list[trial, t]))
        file.write("\n")

with open("data/single_run_theta_sq.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t".format(t_list[t]))
        for trial in range(n_trials):
            file.write("{}\t".format(theta_sq_list[trial, t]))
        file.write("\n")

with open("data/single_run_phi.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t".format(t_list[t]))
        for trial in range(n_trials):
            file.write("{}\t".format(phi_list[trial, t]))
        file.write("\n")

with open("data/single_run_phi_sq.dat", "w") as file:
    for t in range(t_max):
        file.write("{}\t".format(t_list[t]))
        for trial in range(n_trials):
            file.write("{}\t".format(phi_sq_list[trial, t]))
        file.write("\n")
            



