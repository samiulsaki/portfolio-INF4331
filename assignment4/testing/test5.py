
import matplotlib.pyplot as plt
def func(x): return x**2

def integrate(f, a, b, N):
    width = (float(b) - float(a)) / N
    sum = 0
    for i in range(N):
        height = f(a + i*width)
        area = height * width
        sum += area
        #print(sum)
    return sum


print(integrate(func, 0,1,1000))
#plt.plot(integrate(func, 0,1,10), 1)
#plt.show()
