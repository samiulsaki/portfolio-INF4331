# cython: cdivision=True

cimport cython

cdef double f(double x):
    return x * x
    
cpdef cython_integrate(f, double a, double b, int N):
    cdef:
        double width = (b - a) / N
        double sum = 0
        ssize_t i
    for i in range(N):
        sum += f(a + i*width)
    return sum * width