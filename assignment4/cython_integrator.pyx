# cython: cdivision=True

cimport cython

cdef double f(double x):
    return x * x
    
def cython_integrate(f, double a, double b, int N):
    cdef:
        double height = (b - a) / N
        double sum = 0
        int i
    for i in range(N):
        sum = f(a + i*height)
    return sum * height
