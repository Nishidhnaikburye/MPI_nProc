#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:56:38 2024

@author: nishi
"""
import time 
import os 
from multiprocessing import Process, current_process

def square(numbers):
    
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        print(f'The number is {number} squares to {result}')

if __name__ == '__main__':
    
    processes = []
    numbers = range(100)
    
    for i in range(50):
        process = Process(target=square, args=(numbers,)) # process pbject
        processes.append(process)
        
        # processes are spawned by creating a Process object and 
        # then calling its start() method 
        process.start()
    
    for process in processes:
        process.join()
    
    print("multiprocessing complete!")
        

    

