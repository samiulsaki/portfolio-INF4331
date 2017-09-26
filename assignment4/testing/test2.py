import numpy as np


class integrate():
    def integrate1(f, a, b, N):
        x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
        fx=f(x)
        area = np.sum(fx)*(b-a)/N
        return area

    def integrate2(f, a, b, N):
        x = np.linspace(a, b, N)
        fx = f(x)
        area = np.sum(fx)* (b-a)/N
        return area

    def trapezoidal(f, a, b, n):
        h = float(b - a) / n
        s = 0.0
        s += f(a)/2.0
        for i in range(1, n):
            s += f(a + i*h)
        s += f(b)/2.0
        return s * h

import scipy.integrate as integrate 
import numpy as np
f = lambda x : x**2
I,e = integrate.quad(f, 0, 1)
print(I)
float_formatter = lambda x: "%.20f" % x
print(float_formatter(e))

#print(integrate.integrate1(np.sin, 0, 1, 0.00000000001))
#print(integrate.integrate2(np.sin, 0, np.pi/2, 100))
#print(integrate.trapezoidal(lambda x:x**2, 0, 1, 100))
