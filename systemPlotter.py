import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

"""
Analysis program - used to plot data obtained from nBodySystem.py - Will plot Angular Momentum and Total Energy by default. 
"""


Data = np.load("nBodySim.npy")

L = []
E = []
t = []

for i in range(0,len(Data),1):

    L.append(Data[i][2])
    E.append(Data[i][1])
    t.append(Data[i][0])

plt.plot(t,E,"bo")
plt.xlabel("Time/s")
plt.ylabel("Total Energy/J")
plt.title("Total Mechanical Energy Of The System",y=1.08)
plt.axis([min(t),max(t),min(E),max(E)])
plt.savefig("TotalMechanicalEnergy.jpg")
plt.show()

plt.plot(t,L,"bo")
plt.xlabel("Time/s")
plt.ylabel("Angular Momentum/kg m^2 s^-1")
plt.title("Total Angular Momentum Of The System",y=1.08)
plt.axis([min(t),max(t),min(L),max(L)])
plt.savefig("TotalAngularMomentum.jpg")
plt.show()
