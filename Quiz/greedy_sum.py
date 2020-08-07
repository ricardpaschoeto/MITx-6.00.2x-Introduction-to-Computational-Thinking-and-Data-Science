# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:41:35 2020

@author: paschoeto
"""

def greedySum(L, s):
    if(s == 0):
        return 0
    
    if (len(L) == 0):
        return 'no solution'
    L = sorted(L)
    m = 0;
    temp = 0
    ii = len(L)-1
    temp = s
    res = 0
    m_sum = 0
    while(ii >= 0):
        
        if(L[ii] <= temp):
            m = int(temp/L[ii])
            temp = temp % L[ii]
        else:
            m = 0;
        
        m_sum = m_sum + m
        res = res + L[ii]*m
        
        if(res == s):
            return m_sum
            
        ii = ii - 1
    
    return 'no solution'

print(greedySum([10, 7, 6, 3], 19))