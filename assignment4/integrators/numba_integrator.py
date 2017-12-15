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


