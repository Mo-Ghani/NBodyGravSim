# NBodyGravSim
N-Body gravity simulator (with animations)

This program uses Newtonian mechanics to simulate N-body motion with gravity. All units are base SI units.

CREATE A BODY (EXAMPLES ON LINES 58-60):
  Use the GramSim(Position, Velocity, Mass, Name, Colour, Relative Size) function to create objects. Mass and Relative Size should be
  integers. Name and Colour should be strings (Colour uses Matplotlib's naming scheme). Position and Velocity should be 3-vectors, as lists
  representing x,y,z components. After creating an object, add it's variable to the list "objs" on line 63. 
  
TWEAK LENGTH AND STEPSIZE OF ANIMATION:
  Use the GravSim.time_set(time, stepsize) to set the timings for the animation. Both should be an integer value.
  
"GravSIm1.gif" is an example of a 3 body simulation produced by this program.
