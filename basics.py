#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:13:09 2024

@author: nishi
"""
import multiprocessing 

from multiprocessing import Process
import time 
import math

print("Number of cpu : ", multiprocessing.cpu_count())

# learning to working parallel 
results_a = []
results_b = []
results_c = []

def make_calc1(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))

def make_calc2(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 4))

def make_calc3(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 5))

# since its a same list do it at the same time 

# entry point 
if __name__ == '__main__':
    
    number_list = list(range(5000000))
    
    # define a process 
    p1 = multiprocessing.Process(target=make_calc1, args=(number_list,))
    p2 = multiprocessing.Process(target=make_calc2, args=(number_list,))
    p3 = multiprocessing.Process(target=make_calc3, args=(number_list,))
    
    start0 = time.time()
    
    p1.start()   
    p2.start()
    p3.start()
    
    end0 = time.time()
    
    start = time.time()
    
    # make_calc1(number_list)
    # make_calc2(number_list)
    # make_calc3(number_list)
    
    end = time.time()
    
    print("time taken: ", end - start, ' secs')
    print("time taken for Multi: ", end0 - start0, ' secs')
    
