
"""
Aum Desai
Sept 14, 2022
CS152 B
Lab 01
This is a practice program for the first CS 152 Lab. It adds and averages 3 numbers.
To run this file from terminal, make sure the directory is in Lab 01 and type: python3 addthree.py into the terminal
"""

#VERSION 1

print('version 1')          
print('sum', 42 + 21 + 5)        #prints an int
print('avg', (42 + 21 + 5) / 3)  #prints a float

def myfunction(a, b, c):

    """Takes 3 int parameters, then calculates their sum. Sum is given as an int."""
    
    print('sum', a + b +c)

myfunction(4, 5, 6)
myfunction(9, 18, 81)


