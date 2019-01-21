'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #6 Part 2
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

status_answer = 's','m'

#Would be better if allowing flexible answers
#Changed to meet requirments
#single_answer = ("single","Single","SINGLE")
#married_answer = ("married","Married","MARRIED")

def is_positive(income_str):
  '''To check if a year is whole number bigger than 0'''
  #takes in a string representing a year, and checks to see 
  #that it only contains digits and is not <=0
  return (income_str.isdigit() and int(income_str)>0)

def is_valid_status(status):
  '''To check if answer is 's' or 'm' '''
  #a predicate functions that takes in a string representing 
  #marital status and checks to see that 
  #it only contains 's' or 'm'
  return status in status_answer

def compute_tax_for_bracket(income,base_tax,tax_rate,bottom_value):
  #a function that takes in => 
  #{an income, the base tax amount for the given bracket,
  #the tax rate for that bracket,
  #and the bottom value of the income range for that bracket},
  #and returns the correct tax
  return (base_tax+tax_rate*(income-bottom_value))
  #pass

def compute_tax(status,income):
  #a function that takes in status and
  #income,
  #determines which bracket it falls under,
  #and invokes compute_tax_for_bracket(),
  #sending it the income and the proper values for the given bracket
  #if status in single_answer:
  if status == status_answer[0]:
    if income >= SINGLE_BRACKET6:
      base_tax = SINGLE_BASE_TAX6
      tax_rate = TAX_RATE6
      bottom_value = SINGLE_BRACKET6
      #tax = SINGLE_BASE_TAX6 + TAX_RATE6 * (income - SINGLE_BRACKET6)
    elif income >= SINGLE_BRACKET5:
      base_tax = SINGLE_BASE_TAX5
      tax_rate = TAX_RATE5
      bottom_value = SINGLE_BRACKET5
      #tax = SINGLE_BASE_TAX5 + TAX_RATE5* (income - SINGLE_BRACKET5)
    elif income >= SINGLE_BRACKET4:
      base_tax = SINGLE_BASE_TAX4
      tax_rate = TAX_RATE4
      bottom_value = SINGLE_BRACKET4
      #tax = SINGLE_BASE_TAX4 + TAX_RATE4 * (income - SINGLE_BRACKET4)
    elif income >= SINGLE_BRACKET3:
      base_tax = SINGLE_BASE_TAX3
      tax_rate = TAX_RATE3
      bottom_value = SINGLE_BRACKET3
      #tax = SINGLE_BASE_TAX3 + TAX_RATE3 * (income - SINGLE_BRACKET3)
    elif income >= SINGLE_BRACKET2:
      base_tax = SINGLE_BASE_TAX2
      tax_rate = TAX_RATE2
      bottom_value = SINGLE_BRACKET2
      #tax = SINGLE_BASE_TAX2 + TAX_RATE2 * (income - SINGLE_BRACKET2)
    elif income >= SINGLE_BRACKET1:
      base_tax = SINGLE_BASE_TAX1
      tax_rate = TAX_RATE1
      bottom_value = SINGLE_BRACKET1
      #tax = SINGLE_BASE_TAX1 + TAX_RATE1 * (income - SINGLE_BRACKET1)
    elif income >= SINGLE_BRACKET0:
      base_tax = SINGLE_BASE_TAX0
      tax_rate = TAX_RATE0
      bottom_value = SINGLE_BRACKET0
      #tax = SINGLE_BASE_TAX0 + TAX_RATE0 * (income - SINGLE_BRACKET0)
  
      
  #elif status in married_answer:
  elif status == status_answer[1]:
    if income >= MARRIED_BRACKET6:
      base_tax = MARRIED_BASE_TAX6
      tax_rate = TAX_RATE6
      bottom_value = MARRIED_BRACKET6
      #tax = MARRIED_BASE_TAX6 + TAX_RATE6 * (income - MARRIED_BRACKET6)
    elif income >= MARRIED_BRACKET5:
      base_tax = MARRIED_BASE_TAX5
      tax_rate = TAX_RATE5
      bottom_value = MARRIED_BRACKET5
      #tax = MARRIED_BASE_TAX5 + TAX_RATE5 * (income -MARRIED_BRACKET5)
    elif income >= MARRIED_BRACKET4:
      base_tax = MARRIED_BASE_TAX4
      tax_rate = TAX_RATE4
      bottom_value = MARRIED_BRACKET4
      #tax = MARRIED_BASE_TAX4 + TAX_RATE4 * (income -MARRIED_BRACKET4)
    elif income >= MARRIED_BRACKET3:
      base_tax = MARRIED_BASE_TAX3
      tax_rate = TAX_RATE3
      bottom_value = MARRIED_BRACKET3
      #tax = MARRIED_BASE_TAX3 + TAX_RATE3 * (income -MARRIED_BRACKET3)
    elif income >= MARRIED_BRACKET2:
      base_tax = MARRIED_BASE_TAX2
      tax_rate = TAX_RATE2
      bottom_value = MARRIED_BRACKET2
      #tax = MARRIED_BASE_TAX2 + TAX_RATE2 * (income -MARRIED_BRACKET2)
    elif income >= MARRIED_BRACKET1:
      base_tax = MARRIED_BASE_TAX1
      tax_rate = TAX_RATE1
      bottom_value = MARRIED_BRACKET1
      #tax = MARRIED_BASE_TAX1 + TAX_RATE1 * (income -MARRIED_BRACKET1)
    elif income >= MARRIED_BRACKET0:
      base_tax = MARRIED_BASE_TAX0
      tax_rate = TAX_RATE0
      bottom_value = MARRIED_BRACKET0
      #tax = MARRIED_BASE_TAX0 + TAX_RATE0 * (income -MARRIED_BRACKET0)
  
  tax = compute_tax_for_bracket(income,base_tax,tax_rate,bottom_value)
  return tax
  #pass
def main():
  print("This program computes tax according to income and marital_status")
  status = input("What is your marital status?('s' or 'm')\nPress <Enter> to quite.\n")
  while status:
    while not is_valid_status(status):
      print("Wrong input!\nOnly 's' or 'm'")
      status = input("What is your marital status?\n")
    income_str = input("What is your income? (Round to whole numbers please)\n")
    while not is_positive(income_str):
      print("Wrong input!\nOnly whole numbers bigger than zero!\n")
      income_str = input("Wrong entry!\nWhat is your inocme?\n")
    income = int(income_str)
    
    print("Tax for %s filer, with income $%9.2f = $%9.2f\n" %
            ("single" if status == 's' else "married", income, compute_tax(status,income)))
    
    print("This program computes tax according to income and marital_statuss")
    status = input("What is your marital status?('s' or 'm')\nPress <Enter> to quite.\n")

main()
    
'''
def main(status,income):
  
  #if status in single_answer:
  if status == status_answer[0]:
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
      
  #elif status in married_answer:
  elif status == status_answer[1]:
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
    #The repeated loops are used to handle problems with python 2
      income_str = input("Wrong entry!\nWhat is your inocme?\n")
    
      
  
      
  income = int(income_str)
  main(status,income)
  status = input("What is your marital status? Press <Enter> to quite.\n")
'''
2 of 6


