#1/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###

"""This module simple returns a fibonacci sequence
   all the way to the "n"th term. N is defined by the user
"""
def fibonacci(n):
    """fibonacci function
    
    Args:
        n - The final amount of fibonacci numbers calculated.
    Returns:
        returns a array called "result" which holds the fibonacci sequence to the nth term.
    
    Raises:
        Custom exception "Exception"
            Is thrown when the user inputs an integer < 1.
            Instructs user to enter another integer greater than 0.
        typer error: If user does not input an integer, this error is thrown.
    """
    if n < 1:
        raise Exception("Error. Enter a proper int greater than 0")

    result = []
    a = 0
    b = 1
    c = 1
    for i in range(n):
        c = a+b
        result.append(c)
        b = a
        a = c

    return result