#!/usr/bin/env python3

# The integrator function with pure Python. To observe the plots in better way 
# the last three lines of this script need to be uncommented

import os, sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Initial function given
def f(x):
    return x**2

# Definite integral of the function from a to b
def F(a,b):
    if a > b:
        raise ValueError('b must be greater than a')
    elif a == b:
        return 0
    else:
        return (b**3-a**3)/3

# Approximating function using numerical methods:
def integrate(f,a,b,N):
    if N < 2:
        raise ValueError('Number of N must be greater than 2')
    if a == b:
        return 0
    width = float(b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*width)
    return sum * width


# Plotting function for a visual representation
def plot_dat(f,a,b,N):
    n = np.linspace(a,b,N)
    plt.plot(n,f(n),color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Numerical approximation: Rectangular')
    for i in range(1,len(n)):
        c = n[i-1]
        d = n[i]
        plt.plot([c,c],[0,f((c+d)/2)],color='blue')
        plt.plot([d,d],[0,f(d)],color='blue')
        plt.plot([c,d],[f((c+d)/2),f((c+d)/2)],color='blue') 
    plt.savefig('quadratic_error.png')
    plt.show()    
    return 0
    
# Approximate area with a given precision
def precision(f,a,b,printf=False):
    e = 100
    p = 10                                  # Smaller the value of p, better the rectangular plot
    iterationMax = 3                        # Maximum iteration is set to 3 times. Change the value if you like to get narrower rectangles
    iteration = 1    
    while True:
        area = integrate(f,a,b,N=p)        
        p += 10
        iteration += 1
        if printf:
            print('Approximating using rectangular rule with',p,'N and the area is',area)
            plot_dat(f,a,b,N=p)
        if iteration > iterationMax:
            print('Number of iterations exceeded: '+ str(iterationMax))
            break        
    return area

#-----------------------------Run the program----------------------------------
# Initial parameters: xmin, xmax, N (used)

xmin = 0
xmax = 1
N = 100


# Please uncomment these following three lines to observe the plots in better way

#print('Actual area:',F(xmin,xmax))
#print('Approximation:',integrate(f,xmin,xmax,N))
#print(precision(f,xmin,xmax,printf=True))
