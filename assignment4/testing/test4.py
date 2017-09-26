import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
def f(x):
    return x**2
x_vals = np.arange(-20, 21, 1)
y_vals = si.odeint(lambda y,x: f(x), 0, x_vals)

plt.plot(x_vals, y_vals,'-', color = 'r')

plt.show()