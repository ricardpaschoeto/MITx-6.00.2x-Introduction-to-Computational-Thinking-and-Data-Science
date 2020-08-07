# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:38:21 2020

@author: paschoeto
"""

def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    
    if(s == 0):
        return [0,0,0,0]
    
    if(s >= 1 and s < 5):
        return [0,0,0,s]
    
    elif(s >= 5 and  s < 10):
        x3 = int(s/5)
        x4 = s%5
    elif(s >= 10 and s < 25):
        x2 = int(s/10);
        temp = s%10
        if(temp < 5):
            x3 = 0;
        else:
            x3 = int(temp/5)
            temp = temp%5
        x4 = temp
    elif(s >= 25):
        x1 = int(s/25)
        temp = s%25
        if(temp < 10):
            x2 = 0
        else:
            x2 = int(temp/10)
            temp = temp%10
            
        if(temp < 5):
            x3 = 0
        else:
            x3 = int(temp/5)
            temp = temp%5            
        x4 = temp
        
    return [x1,x2,x3,x4]

print(solve(100))
            
    