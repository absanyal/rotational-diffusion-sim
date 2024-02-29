import numpy as np
from numpy import sin, cos

class filament:
    def __init__(self, monomers, radius=1.0, theta=0.0, phi=0.0):
        self.monomers = monomers
        self.radius = radius
        
        self.theta = theta
        self.phi = phi
        
    def get_direction(self):
        return np.array([sin(self.theta) * cos(self.phi), sin(self.theta) * sin(self.phi), cos(self.theta)])

    def contour_length(self):
        return self.monomers * self.radius * 2