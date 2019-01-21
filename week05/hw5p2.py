'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #5 Part 2
Phone: 6079532749
'''
'''
Write a complete program based on the game of lucky sevens:

Game Rules:
A player inputs the amount of money he or she is willing to bet, that amount goes into the pot
The program simulates rolling a pair of dice for each turn
If the sum of the dice equals 7, the player wins $4; otherwise, the player loses $1:  these amounts are added to/subtracted from the pot
A single game continues until the pot is empty
Program Requirements
Allow playing multiple games until the player wants to quit
Validate the player input:  they should only input positive whole number amounts
Make sure that you follow the same patterns we discussed in class
For each game:
output a table showing the roll number and amount left in the pot after each roll
output the highest amount that was in the pot, the roll number when the amount was the highest, and the number of rolls it took for the player to go bankrupt
'''


'''
ANALYSIS
  Output a table of roll numbers, roll value and money left.
  Output highest amount, roll number of that roll and rolls to go bankrupt.
  Provided amount of money user put in.


OUTPUT to monitor:
  roll_no - number of rolls (integer)
  roll_val - value of rolls (integer)
  money - the amount of money user put in (integer)
  max_money - the maximum amount of money gained (integer)
  max_roll - the roll number which maximum money is gained (integer)

INPUT from keyboard:
  money - the amount of money user put into the pot (integer)

GIVENS:
  LUCK_VAL - the roll value which user wins money
  MONEY_WIN - money gained after user won
  MONEY_LOSE - the money lost after use lose
  
  Code:
  LUCK_VAL = 7
  MONEY_WIN = 4
  MONEY_LOSE = 1

PROCESSING:
  Get input
  Validate input
  Convert input to integer
  Use money in the pot equal to total money add money gained minus money lost

'''
import random
# CONSTANTS
LUCK_VAL = 7
MONEY_WIN = 4
MONEY_LOSE = 1

#Design
def main():
  money_str = input("How much money do you want to put in? Press <Enter> to quit.\n")
  while money_str:#Using multiple validation to ensure correct input
    while not money_str.isdigit()>0:
      money_str = input("wrong Entry!\nHow much money do you want to put in?\n")
      
    while not int(money_str)>0:
      money_str = input("wrong Entry!\nHow much money do you want to put in?\n")
      while not money_str.isdigit():
        money_str = input("wrong Entry!\nHow much money do you want to put in?\n")
    
    money = int(money_str)
    max_money = money
    roll_no_count = 1
    max_roll = roll_no_count
    print("Roll Value Dollars")
    while money !=0:
      
      dice_one = random.randrange(7)
      dice_two = random.randrange(7)
      roll_val = dice_one + dice_two
      if roll_val == LUCK_VAL:
        money += MONEY_WIN
      else:
        money -= MONEY_LOSE
      if money>max_money:
        max_money = money
        max_roll = roll_no_count
      print(' ',roll_no_count,'   ',roll_val,'   ',money)
      roll_no = roll_no_count
      roll_no_count+=1
    print("You became broke after %d rolls."%roll_no)
    print("You should have quit after %d %s when you had $%d"%(max_roll, "roll" if max_roll == 1 else "rolls",max_money))
    money_str = input("How much money do you want to put in? Press <Enter> to quit.\n")

main()

