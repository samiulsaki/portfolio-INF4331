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
def integrate(f, a, b, N):
    height = (b-a)/N
    sum = 0
    for i in range(N):
        sum += f( a + i*height)
    return sum * height


''' N=10000
a=0
b=1
print(integrate(f,a,b,N)) '''
''' def main_func():
    f = lambda x: x**2
    N = 500
    print(integrate(f, 0, 1, N))
 '''

#main()
''' if __name__ == '__main__':
    import timeit
    for i in range(4):
        print("Naive: {:.5f} sec".format(timeit.timeit("main()", number=1))) '''
