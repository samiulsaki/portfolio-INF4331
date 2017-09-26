import timeit
from math import sin

f1 = lambda x: x**2
f2 = lambda x: 3*x + 2

args = [[f1, 0, 1, 1000], [f1, 0, 1, 1000000], [f2, 0, 2, 1000], [f1, 0, 3, 100000] ]
print('Test comparison: Pure vs Numpy vs Cython\n')
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
    cython = timeit.timeit("cython_integrate"+g, setup='from cython_integrator import cython_integrate; from __main__ import args', number=1)
    print("\nPure \t: {:.5f} sec".format(pure))
    print("Numpy \t: {:.5f} sec".format(numpy))
    print("Cython \t: {:.5f} sec".format(cython))
    maximum = max(float(pure), float(numpy), float(cython))
    
    if (maximum == pure):
        print('\nPure funtion is the fastest')
    elif (maximum == numpy):
        print('\nNumpy is the fastest')
        print('Numpy is {:.3f}x {} than pure function'.format(pure/numpy, result))
    else:
        print('\nCython is the fastest')
        print('Cython is {:.3f}x {} than pure function'.format(pure/cython, result))
        

    
    print('-----------------------------------------\n')
