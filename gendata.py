
"""
Aum Desai
Sept 20, 2022
CS152 B
Project 01
This is a program for the first CS 152 Project.

It will implement the equations of motion for a ballistic trajectory,
and output the horizontal and vertical postions of an object over a period of time.
To run this file from terminal, make sure the directory is in Project 01 
and type: python3 gendata.py into the terminal
"""


initial_position = 1
initial_velocity = 11
acceleration = -10

def ballistic1(time):

    ''' Takes the int parameter called time, 
    and returns a float called final_position. 
    Calculates Final Position.'''

    final_positon = initial_position + (initial_velocity * time) + (0.5 * (acceleration) * (time**2))

    return final_positon

#print(ballistic1(0.5))

y = ballistic1(1.0)
#print("f(1.0) is", y)



def ballistic2(initial_position, initial_velocity, acceleration, time):

    ''' Takes 4 int parameters and calculates the final position 
    of an equation of motion. Output is given as a float'''

    final_positon = initial_position + (initial_velocity * time) + (0.5 * (acceleration) * (time**2))

    return final_positon

#print(ballistic2(2,11,-10,0.5))



def ComputeAndOutput(initial_position, initial_velocity, acceleration, time):

    '''Takes 4 into parameters. Calls on the ballistic2 function and outputs the time and final position value. Outputs are given as a float.
    Also, everytime the function is called, it appends a spreadsheet named data.csv with the relative output.
    '''

    y_var = ballistic2(initial_position, initial_velocity, acceleration, time)    # y_var represents y variable and stores the final position value of the ballistic function.
    
    print(time, ",", y_var)

    fp = open('data.csv','a')                            #the following lines of code are to
    fp.write( str(time) + "," + str(y_var) + "\n")
    fp.close()

    return (time, ",", y_var)

#ComputeAndOutput(2,11,-10,0.5)

def clearfile():

    '''This function opens the data.csv file and clears all existing data'''

    fp = open('data.csv','w')
    fp.close()



def trajectory10(initial_position, initial_velocity, acceleration, time):

    '''Takes 4 int parameters and calls the ComputeAndOutput function 10 times
    as time goes up by 0.1. Outputs are given as floats.'''
    
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 0 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 1 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 2 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 3 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 4 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 5 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 6 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 7 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 8 * (0.1))
    ComputeAndOutput(initial_position, initial_velocity, acceleration, time + 9 * (0.1))

#trajectory10(1,11,-10,0)
#trajectory10(1,11,-10,1)



def trajectory100(initial_position, initial_velocity, acceleration, time):

    '''Takes 4 int parameters and calls the trajectory10 function 10 times, 
    outputs are given as floats'''

    trajectory10(initial_position, initial_velocity, acceleration, time + 0 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 1 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 2 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 3 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 4 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 5 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 6 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 7 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 8 * (1))
    trajectory10(initial_position, initial_velocity, acceleration, time + 9 * (1))



clearfile()

trajectory100(1,50,-10,0)   #Earth Acceleration
#trajectory100(1,50,-23.6,0) #Jupiter Acceleration
#trajectory100(1,50,-1.66,0) #Moon Acceleration

