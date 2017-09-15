''' 
The Test Polynomials Script

The script imports all the function from pynomials.py script. The test function
will test all the expected results by given value and if the test fails i.e., the 
expected results do not match it will raise an assertion error. If the functions 
are implemented correctly it will pass the tests.

Run the test script with the following command:

py.test test_polynomials.py -v

The corresponding comments are given to describe the test functions.

'''

from polynomials import *

p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
r = Polynomial([10, 7, 1, 6])
x = [51, 15, 26]
x1 = [10, 20, 0, 0, 50]
x2 = [10, 50, 0, 0]
y = [20, 31, 73]
z = [18, 28, 44]
k = Polynomial([22,33,0,55,66,77,88])


def test():
  assert str(p) == "x^2 + 2x + 1" # Test: Nice representation of string
  assert str(q) == "6x^3 + 5x + 9"
  assert str(r) == "6x^3 + x^2 + 7x + 10"
  assert str(Polynomial([5,-10,-15,20])) == "20x^3 - 15x^2 - 10x + 5" # Test: Can take negative signs
  assert p(7) == 64 # Test: The value at 7
  assert str(p+q) == "6x^3 + x^2 + 7x + 10" # Test: Pynomials addition
  assert str(p-q) == "-6x^3 + x^2 - 3x - 8" # Test: Pynomilas substration
  assert str(p+q) == str(r) # Test: Compare equality
  assert str(p*q) == "6x^5 + 12x^4 + 11x^3 + 19x^2 + 23x + 9" # Test: Two Pynomials multiplication 
  assert str(p*-2) == "-2x^2 - 4x - 2" # Test: Pynomial multiply by integer
  assert str(k) == "88x^6 + 77x^5 + 66x^4 + 55x^3 + 33x + 22" # Test: Check how zeros are handled
  assert str(Polynomial(x) * Polynomial(y) * Polynomial(z)) == "83512x^6 + 136788x^5 + 294544x^4 + 248806x^3 + 182292x^2 + 62418x + 18360" # Test: Multiply three Pynomials  
  assert string(add(x,y)) == "99x^2 + 46x + 71" # Test: Addition function
  assert string(sub(x,y)) == "-47x^2 - 16x + 31" # Test: Substraction function
  assert string(multiply(x , y)) == "1898x^4 + 1901x^3 + 4708x^2 + 1881x + 1020" # Test: Multiply function
  assert degree(x) == "2" # Test: Check highest (power of x) degree of leading polynomial coefficients (not the best function)
  assert degree(x1) == "4" # Test: Another degree test with some coefficients are zeros
  assert degree(x2) == "1" # Test: In this test the highest (power of x) degrees are zeros
  assert str(string(power([1,1,12],3))) == "1728x^2 + x + 1" # Test: Power
  