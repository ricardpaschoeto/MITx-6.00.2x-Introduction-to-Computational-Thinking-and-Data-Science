# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:20:50 2020

@author: paschoeto
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    delta = 1
    while(not test(x)):
        x = x + delta
        if(x > 10000000):
            return False
    
    return int(x) 
        

    
def f(x):
    return (x+15)**0.5 + x**0.5 == 15

print(f(49))