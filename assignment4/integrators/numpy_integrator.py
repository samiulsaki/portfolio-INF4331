#!/usr/bin/env python3

import os, sys
from math import exp
from numpy import linspace, sum

def f(x):
    return x**2

def numpy_integrate(f, a, b, N):
    height = float(b-a) / N
    x = linspace(a, b, N)
    #fx = f(x)
    area = sum(f(x))*height
    return area

