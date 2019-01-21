#function that performs + operation
def add_them (num1, num2):
  return num1+ num2

def main():
  first_str = input ("Please enter a whole number: ")
  second_str = input("Please enter another whole number: ")
  first = int(first_str)
  second = int(second_str)
  total = add_them(first, second)
  print("The sum of your numbers is", total)
  print("The sum of your numbers is", add_them(first, second))

main()

#------------------------------------------------------------------------


