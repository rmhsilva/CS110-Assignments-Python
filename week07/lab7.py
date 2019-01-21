'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Phone: 6079532749
'''
# Complete this program as indicated
# Note that some of the code has already been written
# Use the variable names given


# Demonstration function for nested loops
# param i (int) - times through outer loop body
# param j (int) - times through middle loop body
# param k (int) - times through inner loop body
# return list of results (list of ints) -
# running sum of control variables computed in body of inner,
#   execution count for outer loop body, middle loop body, and inner loop body
def demonstration(i,j,k):
  

  # Initialization of accumulators (lines 2-5)
  sum_of_control_variable_values = 0
  count_outer = 0
  count_middle = 0
  count_inner = 0

  # Nested loops
  # Outer (lines 6-7)
  for outer_loop in range(i):
    # increment outer count
    count_outer +=1
    
    # Middle (lines 8-9)
    for middle_loop in range(j):
      # increment middle count
      count_middle +=1
      
      # Inner (lines 10-11)
      for inner_loop in range(k):
        # increment inner count
        count_inner +=1
        
        # Add up and accumulate current value of control variables (line 12)
        sum_of_control_variable_values += outer_loop + middle_loop + inner_loop
        
  # return results (wrapped in a list) (line 13)
  return [sum_of_control_variable_values, count_outer, count_middle, count_inner]


# Predicate function for validation (lines 14-15)
# param limit_value (int) 
def is_whole_and_positive(limit_value):
  return limit_value.isdigit() and int(limit_value) > 0


# For illustration and exam preparation
def main():  #(line 16)
  # Purpose
  print("Let's experiment with functions and loops!") # line 17
  
  # Get outer loop limit (priming read) (line 18+)
  outer_str = input("How many times do you want to execute the outer loop body?\n"\
                +"Press <Enter> to quit.\n")
  
  # Continuation loop (line 19)
  while outer_str:
  
    # validate and convert
    # validation loop (lines 20-21+)
    while not is_whole_and_positive(outer_str):
      outer_str = input("wrong Entry!\nTry again:\n")
    
    # convert (line 22)
    outer = int(outer_str)

    
    # print info (line 23)
    print("The outer loop body will execute %d times" % outer)

    # Get middle loop limit, validate, convert and print info (lines 24-27+)
    middle_str = input("How many times do you want to execute the middle loop body?\n")
    while not is_whole_and_positive(middle_str):
      middle_str = input("wrong Entry!\nTry again:\n")
    middle = int(middle_str)


    
    print("Every time the outer loop body executes once, " +\
          "the middle loop body will execute %d times " % middle) #(line 28+)

    # Get inner loop limit, validate, convert and print info (lines 29-32+)
    inner_str = input("How many times do you want to execute the inner loop body?\n")
    while not is_whole_and_positive(inner_str):
      inner_str = input("wrong Entry!\nTry again:\n")
    inner = int(inner_str)


    

    print("Every time the middle loop body executes once " +\
          "the inner loop body will execute %d times  " % inner) # (line 33+)


    # Info about (line 34+)
    print("This function will sum and accumulate each of the control " +\
          "variables values every time its reaches the inner loop body")

    # Invoke function and store results in variable result_list (line 35)
    result_list = demonstration(outer,middle,inner)
    
    # Recover individual elements from result_list (lines 36-39)
    total = result_list.pop(0)
    outer_count = result_list.pop(0)
    middle_count = result_list.pop(0)
    inner_count = result_list.pop(0)

    # Print results (lines 38-41)  
    print("The body of the outer loop executed %d times" % outer_count)
    print("The body of the middle loop executed %d times" % middle_count)
    print("The body of the inner loop executed %d times" % inner_count)
    print("The sum of the control variables is %d" % total)

    # Get outer loop limit (continuation read) (line 44)
    outer_str = input("How many times do you want to execute the outer loop body?\n"\
                    +"Press <Enter> to quit.\n")

# Invoke main  (line 45)      
main()
