#!/usr/bin/env python3

import numba as numba
from numba import jit

@jit("f8(f8)", nopython=True)
def f(x):
    return x**2

@jit("f8(void,f8,f8,i8)")
def numba_integrate_j(f, a, b, N):
    width = (b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*width)
    return sum * width


