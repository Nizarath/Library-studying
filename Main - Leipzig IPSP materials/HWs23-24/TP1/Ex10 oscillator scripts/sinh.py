# to use, launch 
# python3 <this file> <amplitude>
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def num_integrate(A):
    x=A
    v=0
    dt=0.01 # time on which F is const
    x_vals = []
    t_vals = []
    for t in np.arange(0, 100, dt):
        x_vals.append(x)
        t_vals.append(t)
        x=x+v*dt
        a=-math.sinh(x)
        v=v+a*dt
    return t_vals, x_vals

A = float(sys.argv[1])

figure, axis = plt.subplots(2,2)

plt.title("Inharmonic oscillator: x''=-sinh(x), period decreases with amplitude")
plt.xlabel('(t-t0)/root(mL/f)')
plt.ylabel('x/L')
                
axis[0, 0].plot(*num_integrate(A))
axis[1, 0].plot(*num_integrate(A*2))
axis[0, 1].plot(*num_integrate(A*5))
axis[1, 1].plot(*num_integrate(A*10))

plt.show()
