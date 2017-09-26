
from numpy import linspace, sum

cpdef float cython_integrate(f, float a, float b, int N):
    cdef float height
    height = float(b-a)/N
    cdef double x
    x = linspace(a, b, N+1)
    cdef float s 
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return height*s


