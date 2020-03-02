from scipy.constants import gravitational_constant
import numpy as np

class Forcefield:
    """ 
    A class to create a gravitational potential object given the position and mass of each planets. The forcefield should take a list of each position vector, and a list of each mass as arguements
    to create the field. The gravField method will return both the gravitational potential and acceleration, given a position vector from the origin. 
    
    """

    conditions = [[],[]]

    def __init__(self, position, mass):
        self.position = position
        self.mass = mass

        Forcefield.conditions[0] = self.position     #creates a list for the Verlet method in the Particle class to use
        Forcefield.conditions[1] = self.mass


    def gravField(self,d):
        
        if type(self.mass) is int:
            m = np.ones(1)*(self.mass)
        else: m = np.array(self.mass)

        if type(self.position[0]) is int:
            r = np.asarray([self.position])  
        else: r = np.array(self.position)                         #makes sure the arrays are in the correct format to make generalising the process to n bodies easier

        dist = []
        ndist = []
        disthat = []
        d = np.array(d)         #This section calculates the gravitational potential energy at the given distance from the origin, and the acceleration on the mass at that point in space.
        V = 0

        for i in r:
            dist.append(d-i)

        for i in dist:
            ndist.append(np.linalg.norm(i))

        for i in range(len(r)):
            if ndist[i] == 0:
                disthat.append([0,0,0])                     #finds the separation and direction of separation between point d and every body in the system.
            else: disthat.append(dist[i]/ndist[i])

        for i in range(len(r)):
            if ndist[i] != 0:
                V += -gravitational_constant * (m[i]/ndist[i])
            else: V += 0

        accel = []
        for i in range(len(r)):

            u = (ndist[i])*(ndist[i])

            if u != 0:
                accel.append((-6.67408e-11)*((m[i])/u)*disthat[i])   #The acceleration on a mass in the field
            else: 
                accel.append([0,0,0])        #If statement to avoid dividing by zero

        accel = np.array(accel)

        acceleration = sum(accel)

        return V,acceleration

