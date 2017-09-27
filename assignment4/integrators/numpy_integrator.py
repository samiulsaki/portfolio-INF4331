import os, sys
from math import exp
#os.system("clear")


from numpy import linspace, sum

def f(x):
    return x**2

''' def numpy_integrate(f, a, b, N):
    height = float(b-a)/N
    x = linspace(a, b, N+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)    
    return height*s '''

def numpy_integrate(f, a, b, N):
    height = float(b-a) / N
    x = linspace(a, b, N)
    #fx = f(x)
    area = sum(f(x))*height
    return area

''' 

N=100
a=0
b=1
print(numpy_integrate(f,a,b,N))  '''