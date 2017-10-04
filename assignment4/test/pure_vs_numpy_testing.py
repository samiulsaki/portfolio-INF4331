#!/usr/bin/env python3

import os, sys
import timeit
os.system("clear")

f1 = lambda x: x**2
f2 = lambda x: 3*x + 2

args = [[f1, 0, 1, 1000], 
        [f1, 1, 3, 10000], 
        [f2, 0, 2, 10000], 
        [f2, 0, 3, 1000000] ]

print('Test comparison: Pure vs Numpy\n\n')
for i in range(len(args)):
    g = "(*args[" + str(i) + "])"   
    pure = timeit.timeit("integrate"+g, setup='from integrators.integrator import integrate; from __main__ import args', number=1)
    numpy = timeit.timeit("numpy_integrate"+g, setup='from integrators.numpy_integrator import numpy_integrate; from __main__ import args', number=1)
    print('-------------------------------------------------')
    if args[i][0] == f1:
        arg0 = str('x**2')
    else:
        arg0 = str('3*x + 4')
    print('Arguments given: [ f(x)={}, a={}, b={}, N={} ]'.format(arg0,args[i][1] , args[i][2], args[i][3]))
    print("\nPure \t: {:.5f} sec".format(pure))
    print("Numpy \t: {:.5f} sec".format(numpy))  
    minimum = min(float(pure), float(numpy))
    if (minimum == float(pure)):
        print('\nPure Python function is the fastest')
        print('Pure function is {:.3f}x faster than Numpy function'.format(numpy/pure))
    else:
        print('\nNumpy function is the fastest')
        print('Numpy function is {:.3f}x faster than Pure function'.format(pure/numpy))
    print('-------------------------------------------------\n')