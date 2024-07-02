import numpy as np
"""
This module contains a Particle class that represents a particle in a 3D Space.

Classes:
Particle
A class that represents a particle in a 3D Space.

"""
class Particle(object):
    """
    A class that represents a particle in a 3D Space.

    Attributes:
        totalEnergy (float): The total energy of all particles in the pace.
        position (ndarray): A numpy array containing the x, y, and z coordinates of the particle's position.
        velocity (ndarray): A numpy array containing the x, y, and z components of the particle's velocity.
        mass (float): The mass of the particle.
        energy (float): The energy of the particle.
        id (int): The ID of the particle.
        dt (float): The time step of the simulation.
        positionlog (list): A list of numpy arrays containing the iteration number, and the x, y, and z coordinates of the particle's position at that iteration.
        dataLog (list): A list of numpy arrays containing the iteration number, total energy, and total pressure of the 3D Space at that iteration.
        iteration (int): The current iteration number (used similarly to time)/
        collisionIncrement (int): The number of collisions the particle has experienced against the x, y, and z boundaries.
        radius (float): The radius of the particle.
    """
    totalEnergy = 0

    def __init__(self, id = 0):
        """
        Initializes a particle object.

        Args:
            id (int): The ID of the particle.
        
        Returns:
            None
        """
        self.position = np.zeros(3, dtype=float)
        self.velocity = np.zeros(3, dtype=float)
        self.mass = 1.33 #(6.63 x 2, divide 10)
        self.energy = 0 # 1/2 (mass / velocity **2)
        self.id = id
        self.dt = 0.01
        self.positionlog = []
        self.dataLog = []
        self.iteration = 0
        self.collisionIncrement = 0
        self.radius = 0.38 #(0.19 x 2)

    def updatePosition(self, particles, dt=0.01):
            """
            Updates the particle's position.

            Args:
                particles (list): A list of particle objects.
                dt (float): The time step of the simulation.
            
            Returns:
                None
            """
            force = np.zeros(3, dtype=float)
            for particle in particles:
                if not np.array_equal(particle.position, self.position):
                    distance = np.linalg.norm(particle.position - self.position)
                    if distance <= 2 * self.radius:
                        # calculate the normalized direction vector of the collision
                        direction = (self.position - particle.position) / distance
                        
                        # calculate the component of the velocity of each particle in the collision direction
                        v1 = np.dot(self.velocity, direction)
                        v2 = np.dot(particle.velocity, direction)
                        
                        # calculate the new velocities after the collision
                        m1, m2 = self.mass, particle.mass
                        u1 = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
                        u2 = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)
                        v1_new = self.velocity - (v1 - u1) * direction
                        v2_new = particle.velocity - (v2 - u2) * direction
                        self.velocity = v1_new
                        particle.velocity = v2_new
                    
                    else:
                        force += (self.mass * particle.mass * (particle.position - self.position)) / distance**3

            acceleration = force / self.mass
            self.velocity += acceleration * dt
            self.position += self.velocity * dt

    def updateEnergy(self):
        self.energy = np.round(0.5 * (self.mass * (self.velocity**2))) #sqroot, all (array)**2 added together,
        # Particle.totalEnergy += self.energy

    def updateCollisions(self, particles, dt =0.01, XLimit=10, YLimit=10, ZLimit=10):

        if not 0 <= self.position[0] <= XLimit:
            self.velocity[0] = -self.velocity[0]
            self.collisionIncrement += 1

        if not 0 <= self.position[1] <= YLimit:
            self.velocity[1] = -self.velocity[1]
            self.collisionIncrement += 1

        if not 0 <= self.position[2] <= ZLimit:
            self.velocity[2] = -self.velocity[2]
            self.collisionIncrement += 1
    
    def update(self, particles, k=1, dt=0.01, XLimit=10, YLimit=10, ZLimit=10):
        data = np.array([self.iteration, self.position[0], self.position[1], self.position[2]], dtype=float)
        self.positionlog.append(data)

        self.updatePosition(particles, dt)
        self.updateCollisions(particles)
        self.updateEnergy()

        data = np.array([self.iteration, self.position[0], self.position[1], self.position[2]], dtype=float)
        self.positionlog.append(data)
        self.iteration += 1

    def updateEnergyPressure(self, particles, dt=0.01):
        dataPressure = np.array([self.iteration, self.getEnergy(particles), self.getPressure(particles)], dtype =object)
        self.dataLog.append(dataPressure)

        self.updatePosition(particles, dt)
        self.updateCollisions(particles)
        self.updateEnergy()

        dataPressure = np.array([self.iteration, self.getEnergy(particles), self.getPressure(particles)], dtype =object)
        self.dataLog.append(dataPressure)


    def getPressure(self, particles):
        totalCollision = sum([p.collisionIncrement for p in particles])
        return totalCollision

    def getEnergy(self, particles):
        totalEnergy = sum([p.energy for p in particles])
        newTotalEnergy = np.sqrt((totalEnergy[0]**2) + (totalEnergy[1]**2) + (totalEnergy[2]**2))
        return newTotalEnergy
