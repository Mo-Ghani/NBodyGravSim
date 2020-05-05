import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pylab
plt.style.use('dark_background')


class GravSim(object):

    G = 6.674e-11
    bodies = []

    dt = 1
    n = 100

    def __init__(self, pos, vel, mass, name, colour, size):
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.mass = mass
        self.name = name
        self.colour = colour
        self.size = size
        GravSim.bodies.append(self)

    def forcefield(self):
        force = np.array([0.0, 0.0, 0.0])
        for body in GravSim.bodies:
            r = body.pos - self.pos
            r32 = (np.linalg.norm(r)) ** (3 / 2)
            if r32 == 0:
                force += 0
            else:
                force += (GravSim.G*(body.mass*self.mass) / r32)*r
        return force

    @staticmethod
    def time_set(t, n):
        GravSim.dt = t / n
        GravSim.n = n

    def evolve(self):
        dt = GravSim.dt
        u = self.vel
        m = self.mass
        a = self.forcefield() / m
        self.pos += u*dt + 0.5*a*(dt**2)
        self.vel += a*dt


def animate(i, bodies, plots):
    for body in bodies:
        body.evolve()
    for j in range(len(bodies)):
        plots[j].set_data(bodies[j].pos[0], bodies[j].pos[1])
    return plots


A = GravSim([0.0,0.0,0.0],[0.0,0.0,0.0],600000000,"A","y",30)
B = GravSim([1.50,0.0,0.0],[0.10,0.10,0.0],5000,"B","b",10)
C = GravSim([-1.50,0.0,0.0],[-0.10,-0.10,0.0],5000,"C","g",10)
GravSim.time_set(100, 500)

objs = [A, B, C]
plots = [None] * len(objs)
fig = pylab.figure(figsize=(8,8))
ax = pylab.subplot()
for i in range(len(objs)):
        plots[i], = ax.plot(objs[i].pos[0], objs[i].pos[1],
        marker='o', color=objs[i].colour, ms=objs[i].size,
        label=objs[i].name)

ani = FuncAnimation(fig, animate, frames=500,
                    fargs=[objs, plots], interval=20, blit=True, repeat=True)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
legend = ax.legend(loc=9, bbox_to_anchor=(0.5, 1.1), ncol=3)
legend.legendHandles[0]._legmarker.set_markersize(6)

pylab.show()