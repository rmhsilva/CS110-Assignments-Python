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
This module contains a collection of functions which are useful for 
list manipulation
'''

import random

contain_function = {"create_random_ints",\
                    "compute_sum",\
                    "compute_average",\
                    "find_min_value",\
                    "find_max_value",\
                    "is_equal",\
                    "are_valid_indices"}
if __name__ == "__main__":
  print(contain_function)

# Generate random list of numbers
# param how_many (int)
# param lowest (int)
# param highest (int)
def create_random_ints(how_many, lowest, highest):
  random_list = []
  for count in range(how_many):
    random_list.append(random.randint(lowest, highest))
  return random_list

# Compute sum of list members
# param int_list (list)
# return total (int)
def compute_sum(int_list):
  total = 0
  for item in int_list:
    total += item
  return total

# Computes average value of list members
# param int_list (list)
# return average (float)
def compute_average(int_list):
  total = 0
  for item in int_list:
    total += item
  return total/len(int_list)

# Finds smallest value in list
# param int_list (list)
# return min_value (int)
def find_min_value(int_list, highest):
  min_value = highest + 1
  for item in int_list:
    if item < min_value:
      min_value = item
  return min_value

# Finds largest value in list
# param int_list (list)
# return max_value (int)
def find_max_value(int_list, lowest):
  max_value = lowest - 1
  for item in int_list:
    if item > max_value:
      max_value = item
  return max_value

#Compare for equality
# param first (NA)
# parma second (NA)
# return True if equal, False if not
def is_equal(first, second):
  return first == second

# Validates that indices are unsigned integers, start index < limit index,
#   start index < length of list, limit index <= length of list
# param slice_start_str (str)
# param slice_limit_str (str)
# param length (int)
# returns True if valid, False if not (bool)
def are_valid_indices(slice_start_str, slice_limit_str, length):
  return slice_start_str.isdigit() and slice_limit_str.isdigit() and \
         int(slice_start_str) < int(slice_limit_str) and \
         int(slice_start_str) < length and int(slice_limit_str) <= length 
  



