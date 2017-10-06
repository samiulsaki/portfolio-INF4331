#!/usr/bin/env python3

import os, sys
import timeit
from integrators.integrator import integrate
from integrators.numpy_integrator import numpy_integrate
os.system("clear")

def test_integral_of_constant_function():
    f = lambda x: 2
    F = lambda x: 2*x
    expected_answer = F(1) - F(0)
    tol = 1E-20
    for N in 2000, 4000, 8000, 16000:
        computed_answer = integrate(f, 0, 1, N) # a=0, b=1
        error = abs(expected_answer - computed_answer)
        assert error < tol

def test_integral_of_linear_function():
    f = lambda x: 2*x
    F = lambda x: x**2
    expected_answer = F(1) - F(0)
    tol = 1E-03
    for N in 2000, 4000, 8000, 16000:
        computed_answer = integrate(f, 0, 1, N) # a=0, b=1
        error = abs(expected_answer - computed_answer)
        assert error < (1/N+1) # N+1 simply because exact N is not always greater than error

def test_numpy_integral():
    f = lambda x: x**2
    F = lambda x: (x**3)/3
    expected_answer = F(1) - F(0)
    tol = 1E-05
    for N in 20000, 40000, 80000, 160000, 320000:
        computed_answer = numpy_integrate(f, 0, 1, N) # a=0, b=1
        error = abs(expected_answer - computed_answer)
        assert error < tol
