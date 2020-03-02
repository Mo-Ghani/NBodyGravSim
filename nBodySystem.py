import numpy as np 
import copy
from Forcefield import Forcefield
from Particle import Particle

"""
This program collects the data and saves each body's position,velocity,acceleration, along with the total energy and total angular momentum of the system.

Bodies are created using the planetMaker function.
The simulation is run and saved using the simulator function.

"""

Instances = []    
masses = []
positions = []
Planet = {}       

def planetMaker(r,v,Name,mass,method):

    Instances.append(Name)
    masses.append(mass)
    positions.append(r)

    forcefield = Forcefield(positions,masses)
    a = forcefield.gravField(r)[1]
    Planet[Name] = Particle(r,v,a,Name,mass,method)        #Function used to add as many bodies to the simulation as is needed, uses a dictionary to easily access each body.

    return Planet

def simulator(T,N):

    t = (T/N)           #T is the time wanted to simulate over, Nis the number of data points wanted.
    Data = []           #This function processes the passage of the given time, and tracks the propertiesof each body.

    for k in range(N):

        item = [(t*(k+1))]
        E = 0
        L = 0

        pos = []
        for i in Instances:
            pos.append(Planet[i].position)
        forcefield = Forcefield(pos,masses)         #Takes planets locations, creates a new gravitational field and sets a new acceleration.
        for i in Instances:
            Planet[i].acceleration = (forcefield.gravField(Planet[i].position)[1])
            E += 0.5*(forcefield.gravField(Planet[i].position)[0]*(Planet[i].mass))     #Calculates sum of gravitational potential energy, and the sum of kinetic energy of the system.
            L += (Planet[i].mass)*(np.linalg.norm(np.cross(Planet[i].position,Planet[i].velocity)))    #Sums the angular momentum about the origin for each time step.
            new = Planet[i].update(t)
            Planet[i].position = new[0]         #Update new position and velocity vectors.
            Planet[i].velocity = new[1]
        item.append(E) 
        item.append(L)
        for i in Instances:
            item.append(copy.deepcopy(Planet[i]))    #Adds all the collected data to an array, which will then be saved.
        Data.append(item)
        print("Progress: ",k+1, "/", N)

    np.save("nBodySim.npy" , Data)

    print("Finished")

#The user only needs to make changes to the called functions below this point.



#The bodies that are used in this simulation - planetMaker([Position,Velocity,Name,Mass,IntegrationMethod]) :

planetMaker([0,0,0],[0,0,0],"Sun",1.969e30,3)
planetMaker([1.905462419390697E+09,4.594922818817316E+10,3.579864619632607E+09],[-5.844480276385760E+04,3.796092094129211E+03,5.671804752172480E+03],"Mercury",3.302e23,3)
planetMaker([4.488170977655086E+08,1.076511275226072E+11,1.451200825628854E+09],[-3.513985716083181E+04,-3.789857794015905E+01,2.027321602532556E+03],"Venus",48.685e23,3)
planetMaker([5.414027493012605E+10,1.372304133308239E+11,-6.720296917095780E+06],[-2.819413196023475E+04,1.083185630314278E+04,-1.113449639701170E+00],"Earth",5.97219e24,3)
planetMaker([1.952259586552520E+11,8.368551241751020E+10,-3.036861226130497E+09],[-8.621845326042482E+03,2.433960061781588E+04,7.215744966915238E+02],"Mars",6.4171e23,3)
planetMaker([-3.506762325767074E+11,-7.208182858010772E+11,1.084037182371709E+10],[1.160373252732590E+04,-5.106372378822687E+03,-2.384335433913760E+02],"Jupiter",1898.13e24,3)
planetMaker([2.691218841027125E+11,-1.480843896378232E+12,1.502867723500806E+10],[8.984018432947694E+03,1.694279704230089E+03,-3.872738776008459E+02],"Saturn",5.6834e26,3)
planetMaker([2.555030967199185E+12,1.517554415579635E+12,-2.744996858625275E+10],[-3.516254060352929E+03,5.532713825363554E+03,6.599870988408707E+01],"Uranus",86.813e24,3)
planetMaker([4.332102722348220E+12,-1.134450363275356E+12,-7.648716830117375E+10],[1.353641213012540E+03,5.287341309266702E+03,-1.402108961186170E+02],"Neptune",102.413e24,3)

#Calls the function that runs the simulation and collects+saves the data - simulator([TotalRunTime,NumberOfDataPoints]) :

simulator(365*86400,63072)
