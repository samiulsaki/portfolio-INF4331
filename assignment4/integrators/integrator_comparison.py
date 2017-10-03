#!/usr/bin/env python3

import os, sys
from math import exp, sin, cos, pi
from numpy import linspace, vectorize
from numba import jit
import timeit
import cython

os.system('clear')

def f(x):
    return sin(x)

def F(x):
    return -cos(x)

# for numba
@jit("f8(f8)", nopython=True)
def f_j(x):
    return sin(x)

@jit("f8(f8)", nopython=True)
def F_j(x):
    return -cos(x)


def midpoint_integrate(f, a, b, N):
    height = float(b-a)/N
    sum = 0
    for i in range(N):
        sum += f((a + height/2.0) + i*height)
    sum *= height
    return sum

def midpoint_numpy_integrate(f,a,b,N):
    height = float(b-a) /N
    x = linspace(a+height/2, b-height/2, N-1)
    f2 = vectorize(f)
    area = sum(f2(x)) * height
    return area

@jit("f8(void,f8,f8,i8)")
def midpoint_numba_integrate(f_j,a,b,N):
    height = (b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + height/2.0 + i*height)
    sum *= height
    return sum

''' def midpoint_cython_integrate(f, double a, double b, int N):
    cdef:
        double height = (b - a) / N
        double sum = 0
        ssize_t i
    for i in range(N):
        sum += f(a + height/2.0 + i*height)
    sum *= height
    return sum '''


def error():
    a=0
    b=pi
    N=20000
    expected = F(b) - F(a)
    expected_j = F_j(b) - F_j(a)        # For Numba   
    Integrate = (midpoint_integrate(f,a,b,N))    
    Numpy = (midpoint_numpy_integrate(f,a,b,N))
    Numba = (midpoint_numba_integrate(f_j,a,b,N))
    
    print('The expected value is', expected)
    print('Computed Midpoint with Pure Python gives', Integrate,'. The difference is {:.10f}'.format(abs(Integrate - expected)))
    print('Computed Midpoint with Numpy Python gives', Numpy,'.The difference is {:.10f}'.format(abs(Numpy - expected)))
    print('Computed Midpoint with Numba Python gives', Numba,'.The difference is {:.10f}'.format(abs(Numba - expected_j)))
    list = ['Integrate', 'Numpy', 'Numba']
    check = [Integrate, Numpy, Numba]
    s = [i for i,x in enumerate(check) if x == max(check)]
    for i in s:        
        print('The best midpoint error is with {} function'.format(list[i]))

args = [[f, 0, 1, 1000],
        [f_j,0,1,1000]] 


def performance():
    for i in range(len(args)):
        g1 = "(*args[" + str(0) + "])"
        g2 =  "(*args[" + str(1) + "])"
        
        Integrate_time = timeit.timeit("midpoint_integrate"+g1, setup='from __main__ import midpoint_integrate; from __main__ import args', number=1)
        Numpy_Integrate_time = timeit.timeit("midpoint_numpy_integrate"+g2, setup='from __main__ import midpoint_numpy_integrate; from __main__ import args', number=1)
        Numba_Integrate_time = timeit.timeit("midpoint_numba_integrate"+g1, setup='from __main__ import midpoint_numba_integrate; from __main__ import args', number=1)
        print('-------------------------------------------------')
        print("\nMidpoint Integration time \t: {:.5f} sec".format(Integrate_time))
        print("Midpoint Numpy time \t\t: {:.5f} sec".format(Numpy_Integrate_time))
        print("Midpoint Numba time \t\t: {:.5f} sec".format(Numba_Integrate_time))
        minimum = min(float(Integrate_time), float(Numpy_Integrate_time), float(Numba_Integrate_time))
        if (minimum == float(Integrate_time)):
            print('\nMidpoint Pure Python funtion is the fastest')
        elif (minimum == float(Numpy_Integrate_time)):
            print('\nMidpoint Numpy function is the fastest')
        else:
            print('\nMidpoint Numba function is the fastest')
        print('-------------------------------------------------\n')

def find_n(x):
    a=0
    b=pi
    N = 10
    expected = F(b) - F(a)
    til = 1e-10     # Finding such a large number as 1e-10 takes quite a long time to get the computed values. I recommend using smaller target like 1e-06
    float_formatter = lambda x: "%.20f" % x
    
    if x == midpoint_numba_integrate:
        Integrate = x(f_j,a,b,N)
    else:
        Integrate = x(f,a,b,N)
    
    while float(Integrate) > float(til*expected):
        Integrate = x(f,a,b,N)
        Integrate = Integrate/N
        print(float_formatter(Integrate), '\t', N)
        N *=10        
    print('Value is found at N =',N,'with this: {} value'.format(Integrate))

print('Midpoint Integration Comparison: Pure vs Numpy vs Numba\n')
print('\n-----------------------------------------\n')
print('Midpoint Pure Python Function:\n')
find_n(midpoint_integrate)
print('\n-----------------------------------------\n')
print('Midpoint Numpy Function:\n')
find_n(midpoint_numpy_integrate)
print('\n-----------------------------------------\n')
print('Midpoint Numba Function:\n')
find_n(midpoint_numba_integrate)
print('\n-----------------------------------------\n')


# Just incase you want to see more informations
#error()
#performance()
