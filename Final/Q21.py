# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:51:56 2020

@author: paschoeto
"""
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    res = np.zeros(len(choices)) 
    if(choices.count(total) > 0):
        index = choices.index(total)
        res[index] = 1
        return res
    
    strBin = bin(total)
        
    binArray = np.array(list(strBin))
    binArray[1] = '0'
    binArray = np.flipud(binArray.astype(int))   
    
    indexes  = np.array(np.where(binArray == 1))[0]
    temp = 0
    res = np.zeros(len(choices))
    it = np.array(choices)
    for ii in indexes:
        if ii == 0:        
            if np.count_nonzero(it == 1) > 0:
                temp += 1
                res[it.where(it == 1)] = 1
        else:
            if np.count_nonzero(it == 2**ii) == 1:
                temp += 2**ii
                res[it.where(it == 2**ii)] = 1
            elif np.count_nonzero(it == 2) == ii:
                temp += 2
                res[it == 2] = 1
    

    ii = len(choices)-1
    tchoices = sorted(choices,reverse = False)
    while(temp < total):
        if tchoices[ii] + temp <= total:
            temp += tchoices[ii]
            res[choices.index(tchoices[ii])] = 1
        ii -= 1                        

    return res.astype(int)
    
print(find_combination([1,2,2,3], 4))