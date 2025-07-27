
"""
Aum Desai
Sept 19, 2022
CS152 B
Project 01
This is a practice program about executing a simple action of adding or averaging numbers 
more efficiently through increasingly sophisticated.

To run this file from terminal, make sure the directory is in Project 01
 and type: python3 addthree.py into the terminal
"""

#VERSION 1

print('version 1')                
print('sum', 42 + 21 + 5)
print('avg', (42 + 21 + 5) / 3)

def myfunction(a, b, c):

    """Takes 3 int parameters, then calculates their sum. 
    Sum is given as an int."""

    print('sum', a + b + c)

myfunction(4, 5, 6)
myfunction(9, 18, 81)



#VERSION 2

print('version 2')              
print('sum', 42 + 21 + 5)
print('avg', (42 + 21 + 5) // 3)    # // prints out an int instead of a float due to integer division



#VERSION 3

print('version 3')             
print('sum', 42 + 21 + 5.0)
print('avg', (42 + 21 + 5) // 3.0)



#VERSION 4

print('version 4')  

a = 42
b = 21
c = 5

print('sum', a + b + c)
print('avg', (a + b + c) / 3.0)



#VERSION 5

print('version 5')  

a = int(input("Enter first number :"))   #int function converts the input which is a string into the class int so further arithmitic can be done
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

print('sum', a + b + c)
print('avg', (a + b + c) / 3.0)



#VERSION 6

print('version 6')    

def stats( a, b, c ):

    """Takes 3 int parameters, then calculates their sum and average.
     Sum is given as an int, average is given as a float."""
    
    print('sum', a + b + c)
    print('avg', (a + b + c) / 3.0)
    
stats( 42, 21, 5 )
stats(9, 18, 81)

