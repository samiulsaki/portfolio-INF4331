import timeit
from math import sin

f1 = lambda x: x**2
f2 = lambda x: 3*x + 2

args = [[f1, 0, 1, 1000], 
        [f1, 1, 3, 10000], 
        [f2, 0, 2, 10000], 
        [f1, 0, 3, 1000000] ]

print('Test comparison: Pure vs Numpy vs Numba\n')
for i in range(len(args)):
    #print("\nRunning test {} time".format(i))
    g = "(*args[" + str(i) + "])"
    print('-----------------------------------------')
    if args[i][0] == f1:
        arg0 = str('x**2')
    else:
        arg0 = str('3*x + 4')
    print('Arguments given: [ f(x)={}, a={}, b={}, N={} ]'.format(arg0,args[i][1] , args[i][2], args[i][3]))
    pure = timeit.timeit("integrate"+g, setup='from integrator import integrate; from __main__ import args', number=1)
    numpy = timeit.timeit("numpy_integrate"+g, setup='from numpy_integrator import numpy_integrate; from __main__ import args', number=1)
    numba = timeit.timeit("numba_integrate_j"+g, setup='from numba_integrator import numba_integrate_j; from __main__ import args', number=1)
    print("\nPure \t: {:.5f} sec".format(pure))
    print("Numpy \t: {:.5f} sec".format(numpy))
    print("Numba \t: {:.5f} sec".format(numba))

    if (numpy) < (numba):
        print('\nNumba is faster')
        if (pure < numba):
            result = 'faster'
        else:
            result = 'slower'
        print('Numba is {:.3f}x {} than pure function'.format(pure/numba, result))
    else:
        print('\nNumpy is faster')
        if (pure < numpy):
            result = 'faster'
        else:
            result = 'slower'
        print('Numpy is {:.3f}x {} than pure function'.format(pure/numpy, result))
    print('-----------------------------------------\n')
