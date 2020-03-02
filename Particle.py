import numpy as np 
import math
from Forcefield import Forcefield

class Particle:
    """Class to describe the motion of a particle in 3 dimentions, given that the particle has a constant acceleration."""

    def __init__(self, initialPosition, initialVelocity, initialAcceleration, Name, mass, method):

        self.position = initialPosition
        self.velocity = initialVelocity
        self.acceleration = initialAcceleration
        self.Name = Name
        self.mass = mass
        self.setMethod(method)

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def setMethod(self,method):
        self.Method = self.updateSUVAT
        if method == 1:
            self.Method = self.updateEuler
        elif method == 2:
            self.Method = self.updateSUVAT
        elif method == 3:
            self.Method = self.updateVerlet
        else: raise ValueError("Invalid method")

    def update(self,deltaT):
        self.Method(deltaT)
        return self.position,self.velocity

    def updateEuler(self, deltaT):

        N = deltaT/10
        j = (np.ones(10))*N   #splits up delta T into small sections, so that delta T can be iterated over

        s = np.array(self.position)
        v = np.array(self.velocity)
        a = np.asarray(self.acceleration)    #gets each variable into the correct format, to make calculations smoother

        for i in j:
            v = v + (a)*(i) 
            s = s + (v)*(i)        #Eulers method

        self.position = s
        self.velocity = v


    def updateSUVAT(self,deltaT):

        N = deltaT/10
        j = (np.ones(10))*N

        s = np.array(self.position)
        v = np.array(self.velocity)
        a = np.asarray(self.acceleration)         

        for i in j:
            s = s + v*(i) + (0.5)*a*(i*i)      #implicit method using Newtonian kinematics
            v = v + a*(i)

        self.position = s
        self.velocity = v


    def updateVerlet(self,deltaT):

        N = deltaT/10
        j = (np.ones(10))*N

        s = np.array(self.position)
        v = np.array(self.velocity)
        Am = np.asarray(self.acceleration) 
        
        self.updateSUVAT(deltaT)

        pos = []
        mass = []

        for i in Forcefield.conditions[0]:
            if np.all(i == s):
                continue
            else: pos.append(i)
        pos.append(self.position)                   #removes the old position of the body being integrated, and adds the new estimated position instead.
        for i in Forcefield.conditions[1]:          #creates a new gravitational field using the positions and masses of all bodies
            if i == self.mass:
                continue
            else: mass.append(i)                    #Mass stays the same, but the index of the objects mass must be the same as that of its position.
        mass.append(self.mass)

        f = Forcefield(pos,mass)
        An = f.gravField(self.position)[1]

        for T in j:
            s = s + v*(T) + (0.5)*(Am)*(T*T)        #Verlet algorithm
            v = v + (0.5)*(Am+An)*(T)

        self.position = s
        self.velocity = v



        




