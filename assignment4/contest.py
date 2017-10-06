#!/usr/bin/env python3

# This python script runs the integration of the given equation 5. 
# Since it is a sine function the script will produce a small curve 
# which will have half section on the left side of Y axis and the other
# half on the right side of Y axis. Please read the report.txt on the 
# assignment4 root folder in order to understand what this script does.

import os, sys
from math import sin, pi
from numpy import linspace
import cython
os.system("clear")

@cython.locals(x=cython.double)
def f_cy(x):
    return (1/pi) * (sin(x)/x) * (sin(x/3)/(x/3)) *  (sin(x/5)/(x/5)) * (sin(x/7)/(x/7)) * (sin(x/9)/(x/9)) * (sin(x/11)/(x/11)) * (sin(x/13)/(x/13)) * (sin(x/15)/(x/15))

@cython.locals(x=cython.double)
def F_cy(x):
    return (2027025 * ( sin(x/15) * sin(x/13) * sin(x/11) * sin(x/9) * sin(x/7) * sin(x/5) * sin(x/3) * sin(x) ) ) / (pi * ( x**8 ))

@cython.locals(f_cy=cython.double, a_cy=cython.double, 
                b_cy=cython.double, N_cy=cython.Py_ssize_t, 
                width_cy=cython.double, sum_cy=cython.double, 
                i_cy=cython.Py_ssize_t)
def midpoint_cython_integrate(f_cy, a_cy, b_cy, N_cy):
    width_cy = (b_cy - a_cy) / N_cy
    sum_cy = 0    
    for i_cy in range(N_cy):
        sum_cy += f_cy(a_cy + width_cy/2.0 + i_cy*width_cy)
    sum_cy *= width_cy
    return sum_cy


a_cy=1E-20
b_cy=1E07
N_cy=1000000

expected_cy = F_cy(b_cy) - F_cy(a_cy)
computed_cy = (midpoint_cython_integrate(f_cy,a_cy,b_cy,N_cy))

print('N =',N_cy)
print('---------------------------------------')
print('Computed\t:', computed_cy,'\nExpected\t:', expected_cy)
print('---------------------------------------')