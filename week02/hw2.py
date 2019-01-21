'''

Yichen Tao
ytao15@binghamton.edu
Lab Section B 56
Assignment #2, Part 2

'''


'''
ANALYSIS
  Output number of diagonals inside the polygon. Provided number of sides in a polygon


OUTPUT to monitor:
  tol_diagonals_int - total number of diagnoals (integer)

INPUT from keyboard:
  no_sides - number of sides of a polygon

GIVENS:
  N/A
  
  Code:
  N/A

PROCESSING:
  Get input, Convert str input to int values
  Use formula:
    total number of diagonals = 0.5(number of sides*(number of sides -1))-number of sides
    
'''

# CONSTANTS 
#N/A
#Design
def main():
  #Obtain Input
  no_sides = int(input("What is number of sides? "))
    
  #Obtain output from input use the formula
  tol_diagonals_int = (no_sides*(no_sides-1))/2 - no_sides
    
  #Output on screen
  print("Total number of diagnoals for a %d sized polygon is %d"%(no_sides,tol_diagonals_int))
main()


