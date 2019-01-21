'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #6 Part 1
Phone: 6079532749
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
def is_positive(year_str):
  '''To check if a year is whole number bigger than 0'''
  #takes in a string representing a year, and checks to see 
  #that it only contains digits and is not <=0
  return (year_str.isdigit() and int(year_str)>0)

#def leap_year_checker(year):#Unused since name is specified
def is_leap_year(year):
  '''To check if a year is leap year'''
  #takes in a year as an integer, returns True 
  #if it is a leap year, and False otherwise
  return (0==year%LEAP_YEAR_ONE and year%LEAP_YEAR_TWO != 0) or \
         (year%(LEAP_YEAR_ONE*LEAP_YEAR_TWO)==0)

def main():
  print("This program outputs if a year is a leap year.")
  #Priming read
  year_str = input(\
    "What year do you want to compute?\nPress <Enter> to quit.\n")
  #Check if there is any input
  while year_str:
    while not is_positive(year_str):
      print("Wrong input!\nOnly whole numbers bigger than zero!")
      year_str = input(\
        "What year do you want to compute?\n")
    year = int(year_str)
    print("%d %s a leap year\n"%\
      (year, 'is' if is_leap_year(year) else 'is not '))
    #Ensure the loop is not infinite
    print("This program outputs if a year is a leap year.")
    year_str = input(\
      "What year do you want to compute?\nPress <Enter> to quit.\n")

main()

"""
---------------------------------------------------------
Below is the older version of my program which is totally rewritten to meet
With requirments
---------------------------------------------------------
#def main(year):#This will only apply with the for loop below(Rewritten)
#def main():#This is normal program without for loop
  #Obtain Input
  #year = int(input("Which year are you asking about? \n"))#since there is a for loop, no input is needed
    
  #Obtain output from input
  leap_year = is_leap_year(year)
  '''#Changed into a single boolean expression as required
  if LEAP_YEAR is True:
    answer = 'is'
  elif LEAP_YEAR is False:
    answer = 'is not'
  #else:
    #answer = ''
    '''
  #Output on screen
  print(" %d %s a leap year\n"%(year, 'is' if leap_year is True else 'is not '))
#main()# since for loop called the function, no need to manually invoke
year = int(input("Enter a year:\n"))
main(year)
for year in range(1800,2101,10):
  main(year)
TEST_EDGE_DATA_LIST = [1599,1600,1601,1602,1603,1604,1605, 1799,1800,1801,1802,1803,1804,1805]
print('------------------------------')#To mark additional parts
for year in TEST_EDGE_DATA_LIST:
  main(year)
  
"""
2 of 3



