#!/usr/bin/env python3
import numba as numba
from numba import jit

@jit("f8(f8)", nopython=True)
def f(x):
    return x**2

@jit("f8(void,f8,f8,i8)")
def numba_integrate_j(f, a, b, N):
    height = (b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*height)
    return sum * height


''' def linear_func(x):
    """Python function."""
    return 2*x

def call_me_maybe_numba(f, x, N):
    """Take a Python function as argument, and maybe call f(x) N times"""
    f_jit = numba.jit("f8(f8)", nopython=True)(f)
    
    @numba.jit("void(f8, i8)", nopython=True)
    def call(x, N):
        for _ in range(N):
            f_jit(x)
    
    call(x, N) '''