#!/usr/bin/env python3

# The error and performance function shows the error difference of each midpoint function 
# and compare the performance of the function respectively. In both cases we can see that 
# Cython midpoint function is always the fastest to calculate. Specially in the find_n 
# function the Cython function with target 1e-10 does the calculation in split second while 
# other functions takes a considerable amount of time before find the N that gives the closest 
# targeted result. Just running with a lower target (may be 1e-06) will show how quickly Cython 
# function is calculating. The performance can also be noticable in performance calculation 
# function.

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

# for numba
@jit("f8(f8)", nopython=True)
def f_j(x):
    return sin(x)

@jit("f8(f8)", nopython=True)
def F_j(x):
    return -cos(x)

@jit("f8(void,f8,f8,i8)")
def midpoint_numba_integrate(f_j,a,b,N):
    height = (b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + height/2.0 + i*height)
    sum *= height
    return sum

# for cython
@cython.locals(x=cython.double)
def f_cy(x):
    return sin(x)

@cython.locals(x=cython.double)
def F_cy(x):
    return -cos(x)

@cython.locals(f_cy=cython.double, a_cy=cython.double, 
                b_cy=cython.double, N_cy=cython.Py_ssize_t, 
                height_cy=cython.double, sum_cy=cython.double, 
                i_cy=cython.Py_ssize_t)
def midpoint_cython_integrate(f_cy, a_cy, b_cy, N_cy):
    height_cy = (b_cy - a_cy) / N_cy
    sum_cy = 0    
    for i_cy in range(N_cy):
        sum_cy += f_cy(a_cy + height_cy/2.0 + i_cy*height_cy)
    sum_cy *= height_cy
    return sum_cy


def error():
    a=0
    a_cy=0
    b=pi
    b_cy=pi
    N=20000
    N_cy=20000
    expected = F(b) - F(a)
    expected_j = F_j(b) - F_j(a)                    # For Numba   
    expected_cy = F_cy(b_cy) - F_cy(a_cy)           # For Cython 
    Integrate = (midpoint_integrate(f,a,b,N))    
    Numpy = (midpoint_numpy_integrate(f,a,b,N))
    Numba = (midpoint_numba_integrate(f_j,a,b,N))
    Cython = (midpoint_cython_integrate(f_cy,a_cy,b_cy,N_cy))
    #print(Cython)
    print('The expected value is', expected)
    print('Computed Midpoint with Pure Python gives', Integrate,'. The difference is {:.10f}'.format(abs(Integrate - expected)))
    print('Computed Midpoint with Numpy gives', Numpy,'.The difference is {:.10f}'.format(abs(Numpy - expected)))
    print('Computed Midpoint with Numba gives', Numba,'.The difference is {:.10f}'.format(abs(Numba - expected_j)))
    print('Computed Midpoint with Cython gives', Cython,'.The difference is {:.10f}'.format(abs(Cython - expected_cy)))
    list = ['Integrate', 'Numpy', 'Numba', 'Cython']
    check = [Integrate, Numpy, Numba, Cython]
    s = [i for i,x in enumerate(check) if x == max(check)]
    for i in s:        
        print('The best midpoint error is with {} function'.format(list[i]))

args = [[f, 0, 1, 1000],
        [f_j,0,1,1000],
        [f_cy,0,1,1000]] 


def performance():
    for i in range(len(args)):
        g1 = "(*args[" + str(0) + "])"
        g2 =  "(*args[" + str(1) + "])"
        g3 =  "(*args[" + str(2) + "])"
        Integrate_time = timeit.timeit("midpoint_integrate"+g1, setup='from __main__ import midpoint_integrate; from __main__ import args', number=1)
        Numpy_Integrate_time = timeit.timeit("midpoint_numpy_integrate"+g1, setup='from __main__ import midpoint_numpy_integrate; from __main__ import args', number=1)
        Numba_Integrate_time = timeit.timeit("midpoint_numba_integrate"+g2, setup='from __main__ import midpoint_numba_integrate; from __main__ import args', number=1)
        Cython_Integrate_time = timeit.timeit("midpoint_cython_integrate"+g3, setup='from __main__ import midpoint_cython_integrate; from __main__ import args', number=1)
        print('-------------------------------------------------')
        print("\nMidpoint Integration time \t: {:.8f} sec".format(Integrate_time))
        print("Midpoint Numpy time \t\t: {:.8f} sec".format(Numpy_Integrate_time))
        print("Midpoint Numba time \t\t: {:.8f} sec".format(Numba_Integrate_time))
        print("Midpoint Cython time \t\t: {:.8f} sec".format(Cython_Integrate_time))
        minimum = min(float(Integrate_time), float(Numpy_Integrate_time), float(Numba_Integrate_time), float(Cython_Integrate_time))
        if (minimum == float(Integrate_time)):
            print('\nMidpoint Pure Python funtion is the fastest')
        elif (minimum == float(Numpy_Integrate_time)):
            print('\nMidpoint Numpy function is the fastest')
        elif (minimum == float(Numba_Integrate_time)):
            print('\nMidpoint Numba function is the fastest')
        else:
            print('\nMidpoint Cython function is the fastest')
        print('-------------------------------------------------\n')

def find_n(x):
    a=0
    a_cy=0
    b=pi
    b_cy=pi
    N = 10
    N_cy=10
    
    expected = F(b) - F(a)
    til = 1e-10     # Finding such a large number as 1e-10 takes quite a long time to get the computed values. I recommend using smaller target like 1e-06
    float_formatter = lambda x: "%.20f" % x
    
    if x == midpoint_numba_integrate:
        Integrate = x(f_j,a,b,N)
    elif x == midpoint_cython_integrate:
        Integrate =x(f_cy,a_cy,b_cy,N_cy)
    else:
        Integrate = x(f,a,b,N)
    
    while float(Integrate) > float(til*expected):
        if x == midpoint_numba_integrate:
            Integrate = x(f_j,a,b,N)
        elif x == midpoint_cython_integrate:
            Integrate = x(f_cy,a_cy,b_cy,N_cy)
        else:
            Integrate = x(f,a,b,N)
        Integrate = Integrate/N
        print(float_formatter(Integrate), '\t', N)
        N *=10        
    print('Value is found at N =',N,'with this: {} value'.format(Integrate))

print('Midpoint Integration Comparison: Pure vs Numpy vs Numba vs Cython\n')
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
print('Midpoint Cython Function:\n')
find_n(midpoint_cython_integrate)
print('\n-----------------------------------------\n')

# Just in case you want to see more information
#error()
#performance()
