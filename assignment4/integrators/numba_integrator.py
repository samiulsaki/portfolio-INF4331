
#from numpy import linspace, sum

from numba import jit

@jit
def f(x):
    return x**2

@jit
def numba_integrate_j(f, a, b, N):
    height = (b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*height)
    return sum * height
