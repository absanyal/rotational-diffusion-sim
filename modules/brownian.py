import numpy as np
from modules.constants import *
import modules.parameters as prm
from numpy import pi as PI, log, sqrt


def D_0():
    d = 2.0 * prm.radius * SIGMA0
    return (KB0 * T0) / (6.0 * PI * (ETA0 * prm.eta) * (d / 2.0))


def D_rot_0():
    return D_0() / (SIGMA0 ** 2)


def D_rot(p):
    d = 2.0 * prm.radius * SIGMA0
    eta = prm.eta * ETA0
    delta_rot = -0.622 + 0.917 / p - 0.050 / (p * p)
    return 3.0 * KB0 * prm.T * (delta_rot + log(p)) / (pow(d, 3) * pow(p, 3) * PI * eta)


def D_perp(p):
    d = 2.0 * prm.radius * SIGMA0
    eta = prm.eta * ETA0
    nu_perp = 0.839 + (0.185 / p) + (0.233 / (p * p))
    return (KB0 * (prm.T) * (nu_perp + log(p))) / (4.0 * d * p * PI * eta)

def D_par(p):
    d = 2.0 * prm.radius * SIGMA0
    eta = prm.eta * ETA0
    nu_par = -0.207 + (0.980 / p) - (0.133 / (p * p))
    return (KB0 * (prm.T) * (nu_par + log(p))) / (2.0 * d * p * PI * eta)

def brownian_translate(F_cons_component, D):
    kB = 1.0
    T = prm.T / T0
    W = np.random.normal(0, 1)
    c1 = D / (kB * T) * prm.dt
    c2 = sqrt(2 * D * prm.dt)
    return c1 * F_cons_component + c2 * W


def global_brownian_angle(f):
    p = f.contour_length() / (2.0 * f.radius)
    val_D_rot = D_rot(p) / D_rot_0()
    d_theta = brownian_translate(0, val_D_rot)

    return d_theta


def perturb_filament_angle(f):
    d_theta = global_brownian_angle(f)
    d_phi = global_brownian_angle(f)
    f.theta += d_theta
    f.phi += d_phi
    return f
