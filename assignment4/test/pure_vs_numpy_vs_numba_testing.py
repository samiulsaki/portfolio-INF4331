#!/usr/bin/env python3

import os, sys
import timeit
os.system("clear")

f1 = lambda x: x**2
f2 = lambda x: 3*x + 2

args = [[f1, 0, 1, 10000000], 
        [f1, 1, 3, 100000000], 
        [f2, 0, 2, 200000000], 
        [f1, 0, 3, 300000000] ]

print('Test comparison: Pure vs Numpy vs Numba\n\n')
for i in range(len(args)):
    g = "(*args[" + str(i) + "])"    
    pure = timeit.timeit("integrate"+g, setup='from integrators.integrator import integrate; from __main__ import args', number=1)
    numpy = timeit.timeit("numpy_integrate"+g, setup='from integrators.numpy_integrator import numpy_integrate; from __main__ import args', number=1)
    numba = timeit.timeit("numba_integrate_j"+g, setup='from integrators.numba_integrator import numba_integrate_j; from __main__ import args', number=1)
    print('-------------------------------------------------')
    if args[i][0] == f1:
        arg0 = str('x**2')
    else:
        arg0 = str('3*x + 4')
    print('Arguments given: [ f(x)={}, a={}, b={}, N={} ]'.format(arg0,args[i][1] , args[i][2], args[i][3]))
    print("\nPure \t: {:.5f} sec".format(pure))
    print("Numpy \t: {:.5f} sec".format(numpy))
    print("Numba \t: {:.5f} sec".format(numba))
    minimum = min(float(pure), float(numpy), float(numba))
    if (minimum == float(pure)):
        print('\nPure Python function is the fastest')
        print('Pure function is {:.3f}x faster than Numpy function and {:.3f}x faster than Numba function'.format((numpy/pure), (numba/pure)))
    elif (minimum == float(numpy)):
        print('\nNumpy function is the fastest')
        print('Numpy function is {:.3f}x faster than Pure function and {:.3f}x faster than Numba function'.format((pure/numpy), (numba/numpy)))
    else:
        print('\nNumba function is the fastest')
        print('Numba function is {:.3f}x faster than Pure function and {:.3f}x faster than Numpy function'.format((pure/numba), (numpy/numba)))
    
    print('-------------------------------------------------\n')