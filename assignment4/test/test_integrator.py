from integrator import integrate
from numpy_integrator import numpy_integrate
from math import exp

def test_integral_of_constant_function():
    f = lambda x: 2
    F = lambda x: 2*x
    expected_answer = F(1) - F(0)
    tol = 1E-03
    for N in 2000, 4000, 8000, 16000:
        computed_answer = integrate(f, 0, 1, N) # a=0, b=1
        error = abs(expected_answer - computed_answer)
        #print(error)
        #float_formatter = lambda x: "%.20f" % x
        #print(float_formatter(tol))
        #print(error<tol)
        assert error < tol

def test_integral_of_linear_function():
    f = lambda x: 2*x
    F = lambda x: x**2
    expected_answer = F(1) - F(0)
    tol = 1E-15
    for N in 2000, 4000, 8000, 16000:
        computed_answer = integrate(f, 0, 1, N) # a=0, b=1
        error = abs(expected_answer - computed_answer)
        #print(error)
        #float_formatter = lambda x: "%.20f" % x
        #print(float_formatter(tol))
        #print(error<tol)
        assert error < tol

def test_numpy_integral():
    f = lambda x: x**2
    F = lambda x: (x**3)/3
    expected_answer = F(1) - F(0)
    tol = 1E-05
    for N in 200, 400, 800, 1600, 3200:
        computed_answer = numpy_integrate(f, 0, 1, N) # a=0, b=1
        error = abs(expected_answer - computed_answer)
        print(error)
        float_formatter = lambda x: "%.20f" % x
        print(float_formatter(tol))
        print(error<tol)
        #assert error < tol

#test_integral_of_constant_function()
#test_integral_of_linear_function()
test_numpy_integral()