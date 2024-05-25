#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:56:38 2024

@author: nishi
"""
import time 
import os 
from multiprocessing import Pool, Process, current_process

def sum_square(number):
    
    s = 0
    
    for i in range(number):
        s += i * i 
    return s 

if __name__ == '__main__':
    
    numbers = range(5)
    print('numbers: ', numbers)
    
    # pool can take arguments of how many processors we want to distribute for this pool = processors on the machine
    # by default its the maximum available on the machine 
    print("cores:", os.cpu_count())
    p = Pool()
    
    
    result = p.map(sum_square, numbers)
    print(result)
    
    p.close()
    p.join()








        

    

