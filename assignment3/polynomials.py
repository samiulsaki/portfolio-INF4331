#!/usr/bin/env python3

''' 
The Polynomials Script

The script does most of the task required to fulfill this assignment 3. But it is not perfect. 
For example, the degree or coeeficiency of the Polynomials cannot take an expression in the form 
of Polynomials instead the it is counted by the number of elements in the list. This is not 
expected and not the task goal. Degree function is set here just to make the programme complete.
it can be easily removed by commenting out the degree function.

Other than that all other functions are running perfectly as it was required for this script.

'''

import os, sys, re
from scipy import *
os.system("clear")

class Polynomial:
    def __init__(self,val):
        if type(val) == type([]):
            self.plist = val
        elif type(val) == type(''):
            self.plist = parse_string(val)
        else:
            raise "Wrong arguments : %s" % val
        return
    def __add__(self,p):return Polynomial(add(self.plist,plist(p)))
    def __radd__(self,p): return Polynomial(add(self.plist,plist(p)))
    def __sub__(self,p):  return Polynomial(sub(self.plist,plist(p)))
    def __mul__(self,p): return Polynomial(multiply(self.plist,plist(p)))
    def __rmul__(self,p): return Polynomial(multiply(self.plist,plist(p)))
    def __deg__(self): return Polynomial(degree(self.plist))
    def __repr__(self): return string(self.plist)
    def __call__(self,x1,x2=None): return peval(self.plist,x1,x2)
    def __eq__(self, p): return not (self - p)
   
def degree(self):
	return len(self) - 1 

def plist(term):
    try:
        pl = term.plist
        return pl
    except:
        pass
    if type(term) == type(1.0) or type(term) == type(1):
        return [term]
    elif type(term) == type(''):
        return parse_string(term)
    else:
        raise "Can't be set : %s" % term
    return None

def peval(plist,x,x2=None):
    val = 0
    if x2:
        for i in range(len(plist)): val += plist[i]*(pow(x2,i)-pow(x,i))
    else:
        for i in range(len(plist)): val += plist[i]*pow(x,i)
    return val

def add(p1,p2):
    if len(p1) > len(p2):
        new = [i for i in p1]
        for i in range(len(p2)): new[i] += p2[i]
    else:
        new = [i for i in p2]
        for i in range(len(p1)): new[i] += p1[i]
    return new

def sub(p1,p2): 
  return add(p1,multiple(p2,-1))

def multiple(p,c):
    return [c*pi for pi in p]

def multiply(p1,p2):
    if len(p1) > len(p2): short,long = p2,p1
    else: short,long = p1,p2
    new = []
    for i in range(len(short)): new = add(new,multiply_w_single(long,short[i],i))
    return new

def multiply_w_single(p,c,i):
    new = [0]*i 
    for pi in p: new.append(pi*c)
    return new

def strip_zero(p):
    for i in range(len(p)-1,-1,-1):
        if p[i]: break
    return p[:i+1]

def string(p):
    p = strip_zero(p)
    str = []
    for i in range(len(p)-1,-1,-1):
        if p[i]:
            if i < len(p)-1:
                if p[i] >= 0: str.append('+')
                else: str.append('-')
                str.append(string_convert(abs(p[i]),i))
            else:
                str.append(string_convert(p[i],i))
    return ' '.join(str)

def string_convert(c,i):
    if i == 1:
        if c == 1: return 'x'
        elif c == -1: return '-x'
        return "%sx" % c
    elif i: 
        if c == 1: return "x^%d" % i
        elif c == -1: return "-x^%d" % i
        return "%sx^%d" % (c,i)
    return "%s" % c

def test():
    print("\nTesting......")
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    print("\n\tThe value of {} at {} is {}".format(p, 7, p(7)))
    print("\n\tMultiplication of {} and {} yields {}".format(p , q, p * q))
    print("\n\tMultiplication of {} and an integer {} yields {}".format(p , 2, p * 2))
    p, q, r = map(Polynomial, [[1, 0, 1], [0, 2, 0], [1, 2, 1]])
    print("\n\tWill adding {} and {} be the same as {}? Answer: {}".format(p, q, r, str(p+q) == str(r)))
    print("\n\tIs {} - {} the same as {}? Answer: {}".format(p, q, r, str(p-q) == str(r)))  
    
    print("\nAdditional Testing.....")
    x = [51, 15, 26]
    y = [20, 31, 73]
    z = [18, 28, 44]
    print("\n\tAddition of {} and {} yields {} ".format(x , y, string(add(x,y))))
    print("\n\tThe degree of coefficients of {} is {}".format(x, degree(x))) # Not the right function
    print("\n\tSubstruction of {} and {} yields {}".format(Polynomial([1,2,3]), Polynomial([1,2]), Polynomial([1,2,3]) - Polynomial([1,2])))
    print("\n\tAdding {} and {} yields {}".format(p, q, p+q))
    print("\n\tMultiplication of {} with {} yields {}".format(-1, Polynomial([1,2,3]), (-1*Polynomial([1,2,3]))))
    print("\n\tAddition of {} with {} yields {}".format(1, Polynomial([1,2,3]), (1+Polynomial([1,2,3]))))
    print("\n\tPolynomial of {} yields {}".format(x, Polynomial(x)))
    print("\n\tTesting leading zero stripping of {} yields {}".format([0,1,2,0], string([0,1,2,0])))
    print("\n\tAnd the second similar test of {} yields {}".format([0,1], string([0,1])))
    print("\n\tTesting power {} of {} yields {}".format([1,1,12], 3, string(power([1,1,12],3))))
    print("\n\tTesting if can handle signs in {} : {}".format([0,1,-2,0], string([0,1,-2,0])))
    print("\n\tTesting if can add three polynomials {} , {} , {} : {}".format(p,q,r,p+q+r))
    print("\n\tTesting if can multiply three polynomials {} , {} , {} : {}".format(p,q,r,p*q*r))
    print("\n\t(Similar to above) Testing if can multiply three sets {}, {}, {} : {}".format(x,y,z, Polynomial(x)*Polynomial(y)*Polynomial(z)))
 
if __name__ == '__main__':
    test()