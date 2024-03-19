import numpy as np
import matplotlib.pyplot as plt
from modules.distributions import firstpassage

def fp_norm(t, theta0, D):
    return D * firstpassage(D * t, theta0)

t_list = np.linspace(0.01, 30, 500)

fp_list = np.zeros_like(t_list)

D = 0.05

theta0 = 45

theta0_rad = np.deg2rad(theta0)

for i, t in enumerate(t_list):
    fp_list[i] = fp_norm(t, theta0_rad, D)

plt.plot(t_list, fp_list)
plt.xlabel('t')
plt.ylabel('P(t)')
plt.ylim(bottom=0)
plt.savefig('plots/firstpassage.pdf')

def integrate(fp_list, t_list):
    return np.trapz(fp_list, t_list)
    

area_trap = integrate(fp_list, t_list)
print('Area under the curve (trapezoid) = {:.4f}'.format(area_trap))

area_reimann = 0
t_min = t_list[0]
t_max = t_list[-1]
slices = 1000
dt = (t_max - t_min) / slices

for i in range(slices):
    t = t_min + i * dt
    area_reimann += fp_norm(t, theta0_rad, D) * dt

print('Area under the curve (Reimann) = {:.4f}'.format(area_reimann))