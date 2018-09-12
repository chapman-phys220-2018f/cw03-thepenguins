#!/usr/bin/env python3 
#-*- coding: utf-8 -*-
###
# Name: Jack Savage Student ID: 2295072 Email: jsavage@chapman.edu Course: 
# PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###
def main(local_argv):
    print("This program imports the sequences module, reads a command line"+
          " argument 'n', and returns the 'n'th fibonacci number")

    # storing first value in list of command line arguments for use in sequence
    n = int(local_argv[1])

    print(sequences.fibonacci(n).pop())

# Below is the python convention for defining an executable main section
if __name__ == "__main__":
    import sequences # contains fibonacci function
    import sys
    main(sys.argv)
