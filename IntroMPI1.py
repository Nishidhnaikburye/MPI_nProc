#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:56:38 2024

@author: nishi
"""
import time 
import os 
from multiprocessing import Process, current_process

def square(number):
    # using OD module in python to print out the process ID 
    # assigned to the call of this function assigned by the operating system 
    
    process_ID = os.getpid()
    print(f'process ID: {process_ID}')
    print(" ")
    
    process_name = current_process().name
    print(f'process name: {process_name}')
    
    
    result = number * number
    print(f'The number is {number} squares to {result}')
    
    
if __name__ == '__main__':
    processes = []
    numbers = [1,2,3,4]
    
    # how to distribute across processors 
    
    # extentiate process and store processes in a list and start each processes 
    
    # start = time.time()
    
    for number in numbers:
        process = Process(target=square, args=(number,)) # process pbject
        processes.append(process)
        
        # processes are spawned by creating a Process object and 
        # then calling its start() method 
        process.start()
    
#     end = time.time()
    
# print("Time take: ", end - start)
        
