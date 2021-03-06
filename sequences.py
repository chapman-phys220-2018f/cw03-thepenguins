#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Name: Jack Savage Student ID: 2295072 Email: jsavage@chapman.edu Course: 
# PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###

"""This module reads the input of a number and returns an array of the first n 
Fibonacci numbers in a list """

# return a list containing the fibonacci series up to n.
def fibonacci(n):
    '''Fibonacci function
    Args:
        n: number of fibonacci numbers to calculate
    Returns:
        List containing first n fibonacci numbers
    Raises:
        Custom Exception 'Exception':
            Thrown if n < 1
            Instructs user to enter value larger than 0
        TypeError:
            Thrown by non-integer value of n
    '''
    if n < 1:
        raise Exception('Please enter a value larger than 0')
    
    result = []
    x = 0
    y = 1
    z = 1
    
    #try:
    for i in range(n):
        z = x + y
        result.append(z)
        y = x
        x = z
    return result 

