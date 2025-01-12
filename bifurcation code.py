import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#first define the Ricker map
ricker = lambda r,x: r*x*np.exp(-x)

plt.close('all')

#define various space parameters
n = 10_000
iterations = 1000
last = 100
r = np.linspace(0, 20, n)
x = 1e-5 * np.ones(n)

fig, ax = plt.subplots(1, 1, figsize=(10,7)) #makes the plot

#work out the transient points and plot them
for i in range(iterations):
    x = ricker(r, x)
    if i >= (iterations - last):
        ax.plot(r, x, ',k', alpha=.25)
ax.set_xlim(0, 20);

#this section will find the bifurcation points of the map using scipy's fsolve function (newtons method). Add more equations to find higher period bifurcations.
def system(p):
    
    ricker = lambda r,x: r*x*np.exp(-x)
    
    x, y, r = p
    
    #defines the system of equations to solve
    eq1 = x - ricker(r,y)
    eq2 = y - ricker(r,x)
    #eq5 = -r**2*(x-1)*(np.exp(x) +r*x)*np.exp(x*(r*np.exp(-x)-1))
    eq3 = -r*np.exp(-x)*(1-x) - 1
    
    return [eq1,eq2,eq3]

x,y,r = fsolve(system, (4,1,12.5) )
print(x,r)
