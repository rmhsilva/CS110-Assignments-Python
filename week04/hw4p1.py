'''
TAO YICHEN
ytao15@binghamton.edu
Assignment4
Lab section: B56
CA name: Paul Maino
Assignment #4 Part 1
Phone: 6079532749
'''
'''
RESTATEMENT:
  Display tax for single and married filers given set of incomes

OUTPUT to monitor:
  marital_status[status] (str)
  total_income[status][income] (float)
  tax (float)

GIVEN:
  marital_status (str) - ['single', 'married']
  total_income[status][income] (float):
    [[0,9075, 9076, 36900, 36901, 89350, 89351,
      186350, 186351, 405100, 405101, 406750, 406751],
     [0, 18150, 18151, 73800, 73801, 148850, 148851,
      226850, 226851,  405100, 405101, 457600, 457601]]
  Define constants below

FORMULA:
  tax = base tax amount for bracket
          + (tax rate for bracket * (total_income[status][income]
          - base total_income[status][income] level for bracket))
'''

# No MAGIC numbers!
# CONSTANTS

# base total_income[status][income] levels
# for single and married tax brackets
SINGLE_BRACKET0 = 0
SINGLE_BRACKET1 = 9075
SINGLE_BRACKET2 = 36900
SINGLE_BRACKET3 = 89350
SINGLE_BRACKET4 = 186350
SINGLE_BRACKET5 = 405100
SINGLE_BRACKET6 = 406750

MARRIED_BRACKET0 = 0
MARRIED_BRACKET1 = 18150
MARRIED_BRACKET2 = 73800
MARRIED_BRACKET3 = 148850 
MARRIED_BRACKET4 = 226850
MARRIED_BRACKET5 = 405100
MARRIED_BRACKET6 = 457600

# Define base tax amounts for single and married tax brackets
SINGLE_BASE_TAX0 = 0
SINGLE_BASE_TAX1 = 907.50
SINGLE_BASE_TAX2 = 5081.25
SINGLE_BASE_TAX3 = 18193.75
SINGLE_BASE_TAX4 = 45353.75
SINGLE_BASE_TAX5 = 117541.25
SINGLE_BASE_TAX6 = 118118.75

MARRIED_BASE_TAX0 = 0
MARRIED_BASE_TAX1 = 1815.0
MARRIED_BASE_TAX2 = 10162.5
MARRIED_BASE_TAX3 = 28925.0
MARRIED_BASE_TAX4 = 50765.0
MARRIED_BASE_TAX5 = 109587.5
MARRIED_BASE_TAX6 = 127962.5

# Define tax rate applied to total_income[status][income] over
# base total_income[status][income] of given tax bracket
TAX_RATE0 = 0.1
TAX_RATE1 = 0.15
TAX_RATE2 = 0.25
TAX_RATE3 = 0.28
TAX_RATE4 = 0.33
TAX_RATE5 = 0.35
TAX_RATE6 = 0.396

# This progam displays the simple tax for single and married
# filers given a set of incomes
def main():
  # Explain what program does
  print(
    "This program computes a simple tax table for single and married filers")

  # Define marital status and income data
  marital_status = ['single', 'married']
  total_income = [[SINGLE_BRACKET0,SINGLE_BRACKET1, SINGLE_BRACKET1 + 1,
                   SINGLE_BRACKET2, SINGLE_BRACKET2 + 1,
                   SINGLE_BRACKET3, SINGLE_BRACKET3 + 1,
                   SINGLE_BRACKET4, SINGLE_BRACKET4 + 1,
                   SINGLE_BRACKET5, SINGLE_BRACKET5 + 1,
                   SINGLE_BRACKET6, SINGLE_BRACKET6 + 1],
                  [MARRIED_BRACKET0, MARRIED_BRACKET1, MARRIED_BRACKET1 + 1,
                   MARRIED_BRACKET2, MARRIED_BRACKET2 + 1,
                   MARRIED_BRACKET3, MARRIED_BRACKET3 + 1,
                   MARRIED_BRACKET4, MARRIED_BRACKET4 + 1,
                   MARRIED_BRACKET5, MARRIED_BRACKET5 + 1,
                   MARRIED_BRACKET6, MARRIED_BRACKET6 + 1]]


  # loop through single, then married categories
  for i in range(len(marital_status)):
    status = marital_status[i]
    # loop thru income brackets - will go through single first, then married
    for j in range(len(total_income[0])):
      income = total_income[i][j]
      #print(i,'-------',j)#test

      # Use nested and chained conditionals to compute tax
      ### YOUR CODE HERE ###
      if status =='single':
        if income >= SINGLE_BRACKET6:
          tax = SINGLE_BASE_TAX6 + TAX_RATE6 * (income - SINGLE_BRACKET6)
        elif income >= SINGLE_BRACKET5:
          tax = SINGLE_BASE_TAX5 + TAX_RATE5* (income - SINGLE_BRACKET5)
        elif income >= SINGLE_BRACKET4:
          tax = SINGLE_BASE_TAX4 + TAX_RATE4 * (income - SINGLE_BRACKET4)
        elif income >= SINGLE_BRACKET3:
          tax = SINGLE_BASE_TAX3 + TAX_RATE3 * (income - SINGLE_BRACKET3)
        elif income >= SINGLE_BRACKET2:
          tax = SINGLE_BASE_TAX2 + TAX_RATE2 * (income - SINGLE_BRACKET2)
        elif income >= SINGLE_BRACKET1:
          tax = SINGLE_BASE_TAX1 + TAX_RATE1 * (income - SINGLE_BRACKET1)
        elif income >= SINGLE_BRACKET0:
          tax = SINGLE_BASE_TAX0 + TAX_RATE0 * (income - SINGLE_BRACKET0)
      
      elif status =='married':
        if income >= MARRIED_BRACKET6:
          tax = MARRIED_BASE_TAX6 + TAX_RATE6 * (income - MARRIED_BRACKET6)
        elif income >= MARRIED_BRACKET5:
          tax = MARRIED_BASE_TAX5 + TAX_RATE5 * (income -MARRIED_BRACKET5)
        elif income >= MARRIED_BRACKET4:
          tax = MARRIED_BASE_TAX4 + TAX_RATE4 * (income -MARRIED_BRACKET4)
        elif income >= MARRIED_BRACKET3:
          tax = MARRIED_BASE_TAX3 + TAX_RATE3 * (income -MARRIED_BRACKET3)
        elif income >= MARRIED_BRACKET2:
          tax = MARRIED_BASE_TAX2 + TAX_RATE2 * (income -MARRIED_BRACKET2)
        elif income >= MARRIED_BRACKET1:
          tax = MARRIED_BASE_TAX1 + TAX_RATE1 * (income -MARRIED_BRACKET1)
        elif income >= MARRIED_BRACKET0:
          tax = MARRIED_BASE_TAX0 + TAX_RATE0 * (income -MARRIED_BRACKET0)
      
      else:
        print('Wrong input')

      print("Tax for %7s filer, with income $%9.2f = $%9.2f" %
            (status, income, tax))
            
main()
