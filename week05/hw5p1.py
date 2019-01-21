import package_test
from package_test import hw5p2
#import package_test.hw5p2
#package_test.hw5p2.main()
hw5p2.main()
"""
'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #5 Part 1
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

single_answer = ("single","Single","SINGLE")
married_answer = ("married","Married","MARRIED")

def main(status,income):
  
  if status in single_answer:
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
      
  elif status in married_answer:
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
  print("Tax for %7s filer, with income $%9.2f = $%9.2f" %
          (status, income, tax))
          
status = input("What is your marital status? Press <Enter> to quite.\n")
while status:
  
  while not ((status in single_answer) or (status in married_answer)):
    status = input("Wrong entry!\nWhat is your status?\n")
  income_str = input("What is your income? (Round to whole numbers please)\n")
  while not income_str.isdigit and int(income_str)>0:
    income_str = input("Wrong entry!\nWhat is your inocme?\n")
    
  while not int(income_str)>0:
    income_str = input("Wrong entry!\nWhat is your inocme?\n")
    while not income_str.isdigit:
    
      income_str = input("Wrong entry!\nWhat is your inocme?\n")
    
      
  
      
  income = int(income_str)
  main(status,income)
  status = input("What is your marital status? Press <Enter> to quite.\n")
  """
