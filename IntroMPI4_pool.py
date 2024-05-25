#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 01:47:32 2024

@author: nishi
"""
from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == "__main__":
    
    arr = [1,2,3,4,5]
    
    p = Pool()   # p object of Pool() class
    
    result = p.map(f,arr)
    
    p.close()
    p.join()
    
    print(result)

    