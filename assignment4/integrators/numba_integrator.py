#!/usr/bin/env python3

#import numba as numba
from numba import jit
import timeit
import time

def numba_integrate_j(f, a, b, N):
    """Take a Python function as argument, and maybe call f(x) N times"""
    f_jit = jit("f8(f8)", nopython=True)(f)

    @jit("f8(f8,f8,i8)", nopython=True)
    def integrate(a, b, N):
        width = float(b-a)/N
        area = float(0)
        for i in range(N):
            area += f_jit(a + i*width)
        return (float(area * width))
    return integrate(a, b, N)


import os, sys
from math import exp
from numpy import linspace, sum

def f(x):
    return x**2

def numpy_integrate(f, a, b, N):
    width = float(b-a) / N
    x = linspace(a, b, N)
    area = sum(f(x))*width
    return area
''' 
print('Numpy: ', numpy_integrate(f,0,1,300000))
print('Numba: ', numba_integrate_j(f,0,1,300000))


args = [[f, 0, 1, 10000000]]
F = lambda x: x ** 3 / 3
expected_answer = F(1) - F(0)
a, b, N = 0, 1, 10000000

t0 = time.clock()
#assert abs(numpy_integrate(f, a, b, N) - expected_answer) < 1E-5
numpy_integrate(f,a,b,N)
t1 = time.clock()

#assert abs(numba_integrate_j(f, a, b, N) - expected_answer) < 1E-5
numba_integrate_j(f,a,b,N)
t2 = time.clock()


print('\nNumpy time:',(t1-t0),'\nNumba Time:',(t2-t1))

print(min((t1-t0),(t2-t1)))
for i in range(len(args)):
    g = "(*args[" + str(i) + "])"
    numpy_time = timeit.timeit("numpy_integrate"+g, setup='from __main__ import numpy_integrate, args', number=1)
    numba_time = timeit.timeit("numba_integrate_j"+g, setup='from __main__ import numba_integrate_j, args', number=1)
    print(numpy_time,numba_time)
    print(min(numpy_time,numba_time)) '''