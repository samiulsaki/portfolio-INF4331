cdef class Integrand:
    cdef double f(self, double x):
        raise NotImplementedError()

cdef class MyFunc(Integrand):
    cdef double f(self, double x):
        return x*x

def cython_integrate(Integrand integrand, double a, double b, int N):
    cdef double s = 0
    cdef double dx = (b - a) / N
    cdef ssize_t i
    for i in range(N):
        s += integrand.f(a + i * dx)
    return s * dx