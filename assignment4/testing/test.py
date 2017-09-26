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
    # trapezoidal
def approximateNumerical(a,b,points=10,error=False,mod='rectangular',plt_data=False):
    if points < 2:
        raise ValueError('Number of points must be greater than 2')
    if a == b:
        return 0
    n = np.linspace(a,b,points)
    partialSum = 0
    if mod == 'rectangular':
        def miniArea(c,d):
            return (d-c)*f((c+d)/2)
    elif mod == 'trapezoidal':
        def miniArea(c,d):
            return (d-c)*(f(c)+f(d))/2
    else:
        raise ValueError('Method '+mod+' unknown')
    
    for i in range(1,len(n)):
        partialSum += miniArea(n[i-1],n[i])
    e = (partialSum-F(a,b))/F(a,b) *100
    if error:
        print('\nApproximating using '+ mod+' rule...')
        print('Percentage error: ',e,'%')

    if plt_data:
        plot_dat(a,b,points,mod=mod)
        
    return partialSum,e

# Plotting function for a visual representation
def plot_dat(a,b,points,mod='rectangular'):

    n = np.linspace(a,b,points)
    plt.plot(n,f(n),color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Numerical approximation: '+mod)
    if mod == 'rectangular':    
        for i in range(1,len(n)):
            c = n[i-1]
            d = n[i]
            plt.plot([c,c],[0,f((c+d)/2)],color='blue')
            plt.plot([d,d],[0,f(d)],color='blue')
            plt.plot([c,d],[f((c+d)/2),f((c+d)/2)],color='blue')
        plt.show()
    if mod == 'trapezoidal':
        for i in range(1,len(n)):
            c = n[i-1]
            d = n[i]
            plt.plot([d,d],[0,f(d)],color='blue')
            plt.plot([c,c],[0,f(c)],color='blue')
            plt.plot([c,d],[f(c),f(d)],color='blue')
        plt.show()
    return 0
    
    
# Approximate area with a given precision
def approxGivenPrecision(a,b,error=0.5,mod='rectangular',printf=False):
    e = 100
    p = 5
    itMax = 500
    it = 0
    while abs(e) > error:
        area,e = approximateNumerical(a,b,mod=mod,points=p)
        p += 10
        it += 1
        if printf:
            print('Approximating using '+mod+' rule with:',p,'points, percentage error:',e,'%')
        if it > itMax:
            print('Number of iterations exceeded: '+str(itMax))
            break
    return area

#-----------------------------Run the program----------------------------------

# Initial parameters:
    # xmin = m
    # xmax = M
    # points used = p

m = 0
M = 25
p = 50


print('Actual area:',F(m,M))
print('Approximation:',approximateNumerical(m,M,p,error=True,plt_data=True))
print('Approximation:',approximateNumerical(m,M,p,mod='trapezoidal',error=True,plt_data=True))
print('#############################################################')
print(approxGivenPrecision(m,M,error=0.05,printf=True))
print(approxGivenPrecision(m,M,error=0.05,mod='trapezoidal',printf=True))