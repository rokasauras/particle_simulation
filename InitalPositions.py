from Particle import Particle
import numpy as np
import random

"""
This module generates a set of random initial positions and velocities of particles.

Args:
numberOfParticles (int): the total number of particles to be generated
XLimit (int): the maximum limit of the x-coordinate for the initial positions (being the x border). Default is 10.
YLimit (int): the maximum limit of the y-coordinate for the initial positions (being the y border). Default is 10.
ZLimit (int): the maximum limit of the z-coordinate for the initial positions (being the z border). Default is 10.

Returns:
Particles (list): A list of Particle objects with randomly generated initial positions and velocities.

"""

def InitalPositions(numberOfParticles, XLimit = 10, YLimit = 10, ZLimit = 10):

    Particles = []

    for i in range(numberOfParticles):
        Particles.append(Particle(id = i))

    for particle in Particles:
        
        x = random.randint(1, XLimit - 1)
        y = random.randint(1, YLimit - 1)
        z = random.randint(1, ZLimit - 1)
        xv = random.randint(-4, 4)
        yv = random.randint(-4, 4)
        zv = random.randint(-4, 4)

        particle.position = np.array([x, y, z], dtype = float)
        particle.velocity =  np.array([xv, yv, zv], dtype = float)

    return Particles