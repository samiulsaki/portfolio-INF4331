import os, sys
from math import exp


def f(x):
    return x**2

def F(x):
    return 

def midpoint_integrate(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result
