'''

Yichen Tao
ytao15@binghamton.edu
Lab Section B 56
Ca : Paul Maino
Assignment #3, Part 2

'''
'''
Write a program that prompts the user to input a year, and prints out whether or not the year is a leap year

Make your determination using a single Boolean expression.
Make sure to eradicate any Magic Numbers - use named constants instead!
Include a for loop in your program that tests the following set of years to show that your program is working
'''

'''
ANALYSIS
  Output whether or not the year is a leap year. Provided which year is asked.


OUTPUT to monitor:
  leap_year_checker - whether or not this is a leap year
    True - The year is a leap year(boolean)
    False - The year is NOT a leap year (boolean)
  answer - The string output to the screen

INPUT from keyboard:
  year - the year that is asked

GIVENS:
  LEAP_YEAR_ONE - the number of leap years are 4
  LEAP_YEAR_TWO - 100 a essential number for calculating leap year
  
  Code:
  LEAP_YEAR_ONE = 4
  LEAP_YEAR_TWO = 100

PROCESSING:
  Get input, Convert str input to int values( in one step)
  Use the rule that year/LEAP_Year should be an integer  

'''

# CONSTANTS
LEAP_YEAR_ONE = 4
LEAP_YEAR_TWO = 100

#Design
#Compute whether or not leap year
def leap_year_checker(year):
  return (0==year%LEAP_YEAR_ONE and year%LEAP_YEAR_TWO != 0) or \
         (year%(LEAP_YEAR_ONE*LEAP_YEAR_TWO)==0)
def main(year):#This will only apply with the for loop below
#def main():#This is normal program without for loop
  #Obtain Input
  #year = int(input("Which year are you asking about? \n"))#since there is a for loop, no input is needed
    
  #Obtain output from input
  LEAP_YEAR = leap_year_checker(year)
  if LEAP_YEAR is True:
    answer = 'is'
  elif LEAP_YEAR is False:
    answer = 'is not'
  #else:
    #answer = ''
  #Output on screen
  print(" %d %s a leap year\n"%(year,answer))
#main()# since for loop called the function, no need to manually invoke

for year in range(1800,2101,10):
  main(year)

  
