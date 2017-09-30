#!/usr/bin/env python3

# This python script runs the integration of the given equation 5. 
# Since it is a sine function the script will produce a small curve 
# which will have half section on the left side of Y axis and the other
# half on the right side of Y axis. Please read the report.txt on the 
# assignment 4 folder in order to understand what this script does.

import os, sys
from math import sin, pi
from numpy import linspace
#os.system("clear")


def f(x):
    return (1/pi) * (sin(x)/x) * (sin(x/3)/(x/3)) *  (sin(x/5)/(x/5)) * (sin(x/7)/(x/7)) * (sin(x/9)/(x/9)) * (sin(x/11)/(x/11)) * (sin(x/13)/(x/13)) * (sin(x/15)/(x/15))
def F(x):
    return (2027025 * ( sin(x/15) * sin(x/13) * sin(x/11) * sin(x/9) * sin(x/7) * sin(x/5) * sin(x/3) * sin(x) ) ) / (pi * ( x**8 ))

def integrate(f, a, b, N):
    height = float(b-a) / N 
    sum = 0.1*f(a) + 0.1*f(b)
    for i in range(N):
        # Avoiding ZeroDivisionError. i.e., float division by zero or division by zero
        try:                                            
            sum += f( float(a) + i*float(height) )        
        except ZeroDivisionError:
            return 0
    return sum * height
#print(sin(2),sin(-2))        
a=1E-20
b=1E07
N=100000000000
computed_value = integrate( f, a, b, N )
expected_value = F(b) - F(a)
#error = abs(computed_value) - abs(expected_value)
print('---------------------------------------')
print('Computed\t:', computed_value,'\nExpected\t:', expected_value)
print('---------------------------------------')