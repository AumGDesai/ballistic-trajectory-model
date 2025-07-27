
"""
Aum Desai
Sept 20, 2022
CS152 B
Project 01 Extension
This is a program for the first CS 152 Project Extension.

It will implement the equations of motion for a ballistic trajectory,
and output the horizontal and vertical postions of an object over a period of time.
However, to do so more efficiently it will use loops and calculate for larger time intervals.

To run this file from terminal, make sure the directory is in Project 01 
and type: python3 extension.py into the terminal
"""

def ballistic(initial_position, initial_velocity, acceleration, time):

    ''' Takes 4 int parameters and calculates the final position 
    of an equation of motion. Output is given as a float'''

    final_positon = initial_position + (initial_velocity * time) + (0.5 * (acceleration) * (time**2))

    return final_positon


def ComputeAndOutput(initial_position, initial_velocity, acceleration, time):

    '''Takes 4 into parameters. Calls on the ballistic2 function and outputs the time and final position value. Outputs are given as a float.
    Also, everytime the function is called, it appends a spreadsheet named extensiondata.csv with the relative output.
    '''

    y_var = ballistic(initial_position, initial_velocity, acceleration, time)      # y_var represents y variable and stores the final position value of the ballistic function.
    
    print(time, ",", y_var)

    fp = open('extensiondata.csv','a')
    fp.write( str(time) + "," + str(y_var) + "\n")
    fp.close()

    return (time, ",", y_var)

def clearfile():

    '''This function opens the extensiondata.csv file and clears all existing data'''

    fp = open('extensiondata.csv','w')
    fp.close()


def trajectory10(initial_position, initial_velocity, acceleration, time):
    
    '''Takes 4 int parameters and loops the ComputeAndOutput function 10 times
    as time goes up by 0.1. Outputs are given as floats.'''

    N = 0
    
    for i in range(10):

        ComputeAndOutput(initial_position, initial_velocity, acceleration, time + N)

        N += 0.1

def trajectory100(initial_position, initial_velocity, acceleration, time):
    
    '''Takes 4 int parameters and loops the ComputeAndOutput function 100 times
    as time goes up by 0.1. Outputs are given as floats.'''

    N = 0
    
    for i in range(100):
        ComputeAndOutput(initial_position, initial_velocity, acceleration, time + N)
        N += 0.1

def trajectory1000(initial_position, initial_velocity, acceleration, time):
    
    '''Takes 4 int parameters and loops the ComputeAndOutput function 1000 times
    as time goes up by 0.1. Outputs are given as floats.'''

    N = 0
    for i in range(1000):
        ComputeAndOutput(initial_position, initial_velocity, acceleration, time + N)
        N += 0.1



clearfile()
#trajectory10(1,50,-10,1)
#trajectory100(1,50,-10,1)
trajectory100(1,50,-10,1)





