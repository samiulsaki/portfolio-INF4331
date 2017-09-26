import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
#%matplotlib inline

def f(x):
    if (np.abs(x)<1e-06):
        res = x
    else:
        res = x*np.sin(1.0/x)
    return res

X = np.arange(-0.5,0.5,0.001)

#plot(X,f(X))

def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = integrate.quad(f,0,val)
        res[i]=y
    return res

plt.plot(X,F(X))