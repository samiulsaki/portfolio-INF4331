import os, sys
from math import exp
#os.system("clear")

def f(x):
    return x**2

''' def integrate(f, a, b, N):
    width = (float(b) - float(a)) / N
    sum = 0
    for i in range(N):
        height = f(a + i*width)
        area = height * width
        sum += area
        #print(sum)
    return sum '''

''' def integrate(f, a, b, N):
    height = float(b-a)/N
    sum = 0.5*f(a) + 0.5*f(b)
    for i in range(N):
        sum += f(a + i*height)        
    sum *= height    
    return sum '''

''' def integrate(f, a, b, N):
    height = float(b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*height)
    return sum * height
 '''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def f(x):
    return x**2

def integrate(f, a, b, N):
    height = float(b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*height)
    return sum * height



# Numpy is only used for integral_plot() function

def integral_plot():
    a, b = 0, 1  # integral limits
    N=1000
    height = float(b-a) / N
    #x=0
    for i in range(N):
        x = (a + i*height)

    #x = np.linspace(0, 1.3)
    y = f(x) 
    fig, ax = plt.subplots()
    plt.plot(x, y, 'r', linewidth=2)
    plt.ylim(ymin=0)

    # Make the shaded region
    ix = np.linspace(a, b)
    iy = f(ix)
    verticals = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]

    poly = Polygon(verticals, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)
    plt.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20)
    plt.figtext(0.9, 0.05, '$x$')
    plt.figtext(0.1, 0.9, '$y$')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks((a, b))
    ax.set_xticklabels(('$a$', '$b$'))
    ax.set_yticks([])
    plt.show()

integral_plot()

