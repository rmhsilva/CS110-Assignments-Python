'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #1 Part 2
Phone: 6079532749
'''
## Do not write anything past column 78
## Go to next line instead (no wrapping!)
## USE MEANINGFUL NAMES!
## variables will use lower_snake_case
## constants will use UPPER_SNAKE_CASE

'''
ANALYSIS
  Output total value  of coins. Provided number of different coins


OUTPUT to monitor:
  tol_money_flt - total money (float)

INPUT from keyboard:
  no_quarter_int - number of quarters
  no_dime_int - number of dimes
  no_nickel_int - number of nickels
  no_penny_int - number of pennies


GIVENS (i.e., program constants):
  QUARTER (int) - 25
  DIME (int) - 10
  NICKEL (int) - 5
  PENNY (int) - 1
  
  # Your code here:
  QUARTER_VALUE (int) => 25
  DIME_VALUE (int) => 10
  NICKEL_VALUE (int) => 5
  PENNY_VALUE (int) => 1
  TO_DOLLAR (int) => 100

PROCESSING:
  Get input, Convert str input to int values
    Find total value of each type of coin:  QUARTER * 25 + DIME * 10 + NICKEL*5 + PENNY
  Find total value of each type of coin:  coin_type_value * coin_type_count
  Convert int value to dollar value (will be float):  total_value / TO_DOLLAR
  Display output

  
'''

# CONSTANTS 
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1
TO_DOLLAR = 100

## BRIEF description of overall program:
# This program outputs the total amount of change that a user has in dollars
# given the count of each type of coin

def main():

  # Explain purpose of program to user
  print("This program will print out the total amount of change " +
        "you have in dollars when you provide a count of each type of coin")

  # Ask user for number of coins they have
  ## Start with quarters, end with pennies
  # Note constraints: no dollar, half-dollar coins
  #quarter_count_str = input("Please enter the number of quarters you have:  ")
  ## Input the rest here 
  no_quarter_int = int(input("Please provide number of quarters: "))  
  no_dime_int = int(input("Please provide number of dimes: "))  
  no_nickel_int = int(input("Please provide number of nickels: "))  
  no_penny_int = int(input("Please provide number of pennies: "))  

  # Convert str data to int (no need)
  #quarter_count = int(quarter_count_str)
  ## Convert the rest here

  # Multiply the value of each type of coin by it's count and sum each result
  total_cents = (QUARTER * no_quarter_int) + (no_dime_int * DIME) + (no_nickel_int * NICKEL) + no_penny_int

  #Pretty sure everything before this is right
  # Convert to dollars (float)
  #tol_money_flt = float(total_cents / TO_DOLLAR)
  
  total_cents = float(total_cents)#I don't know what's wrong, but things won't work until I add this line.
  tol_money_flt = total_cents / TO_DOLLAR

  #print(total_cents)
  #print(tol_money_flt)
  # Display labeled and formatted amount in dollars
  print("The total amount of change you have in dollars is $%.2f" %
        tol_money_flt)
  

main()

# Actually I have implemented something similar in c
#I will attach it under this line
'''
#include <stdio.h>
#include <cs50.h>
/*cs50.h is a customized file that sometimes doesn't matter. */
#define quarter 250
#define dime 100
#define nickel 50
#define penny 10
/*Somenumbers are enlarged purposefully*/
/*No notes since I learnt by myself
int main(void)
{
    float change;
    
    int n_quarter=0;
    int n_dime=0;
    int n_nickel=0;
    int n_penny=0;
    int sum=0;
    int changeA;
    do
    {
        printf("o hai! How much change is owed?\n");
        change=get_float();
    }
    
    while(change<0);
    changeA=1000*change;
    n_quarter=changeA/quarter;
    changeA=changeA-n_quarter*quarter;
    n_dime=changeA/dime;
    changeA=changeA-n_dime*dime;
    n_nickel=changeA/nickel;
    changeA=changeA-n_nickel*nickel;
    n_penny=changeA/penny;
    sum=n_quarter+n_dime+n_nickel+n_penny;

    printf("%d\n",sum);
    
}

'''
