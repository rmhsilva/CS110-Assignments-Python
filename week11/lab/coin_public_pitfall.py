import random

'''
Simulates a coin that can be flipped
'''

class Coin:
  
  # Initializes side_up (str) to "Heads"
  # Stores list of outcomes since they are strings  
  def __init__(self):
    self.value_list = ['Tails', 'Heads']
    self.side_up = self.value_list[1]

#------------------------------------------------------------------------------
# Accessors

  # returns value of side_up (str)
  def get_side_up(self):
    return self.side_up

#------------------------------------------------------------------------------
# Mutators

  # Randomly generated 0 = "Tails"
  # Randomly generated 1 = "Heads"
  def toss(self):
    self.side_up = self.value_list[random.randint(0,1)]

  

'''
Shows that encapsulation (i.e., data hiding)can be violated by carelessly
  naming instance data
Note:  neglecting to make data private (self.__ . . .) allows instance data
  to be accessed directly, instead of through accessors
Output:
  state of Coin object (str)
  value of Coin side_up (str)
Input:
  none (values generated randomly)
Uses:
  Coin class
'''

# Create Coin object and show how it is used
# Note that improper use can't be prevented since
#   data isn't private
def main():
  # Create an object from the Coin class.
  my_coin = Coin()

  ok_str = "OK"
  while ok_str:
    # Display the side of the coin that is facing up.
    print("START RUN")
    print()
    print ('This side is up to start: ', my_coin.get_side_up())
    print()
    
    # Toss the coin.
    print ('I am tossing the coin...')
    my_coin.toss()

    print()
    print("After tossing, display the side of the coin " + \
          "that is facing up.")
    print ('This side is up: ', my_coin.get_side_up())

    print()
    print("But now I'm going to cheat! \n" + \
          "I'm going to directly change \nthe value " + \
          "of the object's side_up attribute to 'Heads'.")
    my_coin.side_up = 'Heads'

    # Display the side of the coin that is facing up.
    print()
    print ('Now, this side is up no matter what: ',
           my_coin.get_side_up())

    print()
    print("I'm going to cheat again! \n" + \
          "Now I'm going to directly change \nthe value " + \
          "of the object's side_up attribute to 'Tails'.")
    my_coin.side_up = 'Tails'
    
    # Display the side of the coin that is facing up.
    print()
    print ('Now, this side is up no matter what: ',
           my_coin.get_side_up())

    print()
    ok_str = input("Press any key to continue, \n" + \
                  "press <Enter> to quit:  ")

# Call the main function.
main()
