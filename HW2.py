# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:16:58 2018

@author: Rabbit/Joshua Crisp
"""


def trap(f, lower, upper, numberOfPoly):
    """code (upper and lower)
    and (n) number of polygons
    Trapaziod Rule calculations
    return approx area and error
    
    inputs upper-bound, lower-bound,
    number of polygons
    
    find number of polygons gives error less than
    1e-5 (round n to nearest polygon)"""
    def f(x):
        return 3*(x**2)
    
    h = (upper-lower)/numberOfPoly
    print(h)
    result = (0.5*(f(lower))) + (0.5*(f(upper)))
    print(result)
    for i in range (1, int(numberOfPoly)):
        result += f(lower + i*h)
        
    result *= h
    print('result = %f' % result)
    return result

def exact():
    from math import exp
    def f(x):
        return 3*(x**2)
    var = lambda t: f(t) * exp(t**3)
    n = float(input('Please enter the number of Polygons: '))
    upper = float(input('Please enter upper: '))
    lower = float(input('Please enter lower: '))
    #upper = 5.0
    #lower = 1.0
    """h = float(upper-lower)/n
    result = 0.5*(var(lower) + var(upper))
    for i in range (1, int(n)):
        result += var(lower + i*h)
    result2 = h * result
    print('result = %f' % result2)"""
    num = trap(var, lower, upper, n)
    print('num: %f' % num)
    Va = lambda v: exp(v**3)
    
    exact = trap(Va, lower, upper, n)
    
    error = exact - num
    print(var)
    print('exact = %f' % (exact))
    
    print ('n=%d: %.16f, error: %g' % (n, num, error)) 
    return error

#trap(1.0, 5.0, 23500000)
exact()
"""for i in range(23400000, 23500000):
    n = i
    error = exact(n)
    if error == 0.00001:
        print ('Number: %s'% (n))
        
    else:
        ++i
        """
        
"""Found the error gets closer to .00001 around 23.5 to
    24 million poly""" 