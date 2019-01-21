'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #5 Part 3
Phone: 6079532749
'''
'''
Write a complete program that iteratively computes the amount of money a person would earn over a period of time if his or 
her salary is one penny the first day, two pennies the second day, and continues to double each day. 

For input, the program should ask the user for the number of days
validate the player input
For output, the program should display a table showing
both the day and what the salary was for that day, and then show the total pay at the end of the period as a dollar amount
Hint:  treat day 1 as a special case (i.e., you should initialize the day 1 values, then start your loop at 2)
Let the user repeat this as many times as they like
'''

'''
ANALYSIS
  Output table of day number and payment.
  Output total payment
  Provided number of days.


OUTPUT to monitor:
  day_no - number of days (integer)
  day - count of days (integer)
  money - money received at a given day (integer)
  money_total_dollar - money received after given days (float)

INPUT from keyboard:
  day_no_str - number of days(string)

GIVENS:
  CALC_BASE - the base for power equation
  CHANGE_RATE - change rate between dollar and penny

  Code:
  CALC_BASE = 2
  CHANGE_RATE = 100


PROCESSING:
  Get input
  Validate
  Convert str input to int values( in one step)
  Use the equation that money gained equal to CALC_BASE to the power of days

'''

# CONSTANTS
CALC_BASE = 2
CHANGE_RATE = 100

#Design


def main():
  day_no_str = input("What is the number of days of salary to be calculated?\nPress <Enter> to quit\n")
  while day_no_str:
    while not day_no_str.isdigit():
      day_no_str = input("wrong Entry!\nWhat is the number o fdays of salary to be calculated?\n")
    while not int(day_no_str)>0:
      day_no_str = input("wrong Entry!\nWhat is the number o fdays of salary to be calculated?\n")
      while not day_no_str.isdigit():
        day_no_str = input("wrong Entry!\nWhat is the number o fdays of salary to be calculated?\n")
    day_no = int(day_no_str)
    money = 0
    money_total = 0
    start_power = 0
    while start_power < day_no:
      money = CALC_BASE**start_power
      day = start_power+1
      money_total +=money
      money_total_dollar = money_total / CHANGE_RATE
      print("Day                    Pay")
      print("%d                     %d"%(day, money))
      start_power+=1
    print("In %d %s a penny grows to $%2.2f"%(day,"day" if day == 1 else "days", money_total_dollar))
    day_no_str = input("What is the number ofdays of salary to be calculated?\nPress <Enter> to quit\n")
main()
