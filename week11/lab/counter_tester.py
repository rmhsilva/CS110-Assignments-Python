'''
Tester for Counter class:  exercises all the methods in the Counter class
'''
import counter

def main():
  # The following causes the constructor to be invoked:  __init__()
  score_counter = counter.Counter()  # Create a counter object
  print(score_counter.get_count())   # Display the current value of counter
  for points in range(10):           # Increment the counter 10 times
    score_counter.increment()
  print(score_counter.get_count())   # Display the current value of counter
  for points in range(5):            # Decrement the counter 5 times
    score_counter.decrement()
  print(score_counter.get_count())   # Display the current value of counter
  score_counter.reset()              # Reset the counter
  print(score_counter.get_count())   # Display the current value of counter
  # The following causes the 'to string' method to be invoked:  __str__()
  print(score_counter)               # Displays str representation of counter
  score_counter.set_count(100)       # Set counter to 100
  print(score_counter)               # Displays str representation of counter

main()
