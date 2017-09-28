#!/usr/bin/env python3

import os, sys

import numpy as np
import matplotlib.pyplot as plt

os.system("clear")

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
    # rectangular

N=1000
def integrate(f,a,b,N):
    #if N < 2:
    #    raise ValueError('Number of N must be greater than 2')
    if a == b:
        return 0
    n = np.linspace(0,1,N)
    
    sum = 0
    def smallArea(c,d):
        return (d-c)*f((c+d)/2)
    for i in range(1,len(n)):
        sum += smallArea(n[i-1],n[i])
    #e = (sum-F(a,b))/F(a,b) *100   
    plot_dat(f,a,b,N)        
    return sum

# Plotting function for a visual representation
def plot_dat(f,a,b,N):
    n = np.linspace(a,b,N)
    plt.plot(n,f(n),color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Numerical approximation: Rectangular')
    #if mod == 'rectangular':    
    for i in range(1,len(n)):
        c = n[i-1]
        d = n[i]
        plt.plot([c,c],[0,f((c+d)/2)],color='blue')
        plt.plot([d,d],[0,f(d)],color='blue')
        plt.plot([c,d],[f((c+d)/2),f((c+d)/2)],color='blue')
    plt.show()
    return 0
    
    
# Approximate area with a given precision
def approxGivenPrecision(f,a,b,printf=False):
    e = 100
    p = 10                                  # Smaller the value of p, better the rectangular plot
    iterationMax = 5                        # Maximum iteration is set to 5. Change the value if you like
    iteration = 0
    
    while True:
        area = integrate(f,a,b,N=p)
        p += 10
        iteration += 1
        if printf:
            print('Approximating using rectangular rule with:',p,'N with area:',area)
        if iteration > iterationMax:
            print('Number of iterations exceeded: '+str(iterationMax))
            break
        
    return area

#-----------------------------Run the program----------------------------------

# Initial parameters: xmin, xmax, N (used)

xmin = 0
xmax = 1
N = 100

print('Actual area:',F(xmin,xmax))
print('Approximation:',integrate(f,xmin,xmax,N))
#print('Approximation:',integrate(m,M,p,mod='trapezoidal',error=True,plt_data=True))
#print('#############################################################')
print(approxGivenPrecision(f,xmin,xmax,printf=True))
#print(approxGivenPrecision(m,M,error=0.05,mod='trapezoidal',printf=True))