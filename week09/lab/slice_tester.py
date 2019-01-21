'''
TAO YICHEN
ytao15@binghamton.edu
Lab9
Lab section: B56
CA: Paul Maino
Lab9,Part2
Phone: 6079532749
'''

'''
Tester for 'home grown' slice operator
Output to monitor:
  slice of list (list)
Input from keyboard:
  slice_start (int)
  slice_limit (int)
Tasks allocated to functions:
  my_slice()
  isInteger()
  are_valid_indices()(outside)
  and others found in listFunctions.py module
'''

from listfunctions import *

#Return: a sublist (list)
#Parameters: list (list)
#Parameters: a starting index (int)
#Parameters: a limiting index up-to-but-not-including (int)
def my_slice(new_list,slice_start, slice_limit):
  my_list = []
  for index in range(slice_start, slice_limit):
    my_list[len(my_list):] =[new_list[index]]
  return my_list
  pass

# Test my_slice() function
def main():
  new_list = create_random_ints(20, 0, 100) # Generate random list of numbers
  print('The list is: ', new_list, 'and its length is', len(new_list))
  slice_start_str = input("\nEnter the starting index for the slice \n" + \
                  "OR press <Enter> to quit:  ")
  while slice_start_str:      
    slice_limit_str = input("Enter the limiting index for the slice:  ")
    while not are_valid_indices(slice_start_str, slice_limit_str, len(new_list)):
      print("One or both of your indices were invalid")
      slice_start_str = input("\nEnter the starting index for the slice ")
      slice_limit_str = input("Enter the limiting index for the slice:  ")
        
    slice_start = int(slice_start_str)
    slice_limit = int(slice_limit_str)
      
    slice1 = my_slice(new_list,slice_start, slice_limit)
    slice2 = new_list[slice_start:slice_limit]
    
    print('My slice is: ', slice1)
    print("Python's slice is: ", slice2)
    if is_equal(slice1, slice2):
      print("Success:  slices are equal")
    else:
      print("Back to the drawing board :~(")
        
    slice_start_str = input("\nEnter the starting index for another slice \n" + \
                  "OR press <Enter> to quit:  ")
        
main()


      
