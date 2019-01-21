import random

'''
Simulates a coin that can be flipped
'''

class Coin:
#------------------------------------------------------------------------------
# Constructor
  
  # Initializes side_up (str) to "Heads"
  # Stores list of outcomes since they are strings
  def __init__(self):
    self.__VALUE_LIST = ['Tails', 'Heads']
    self.__side_up = self.__VALUE_LIST[1]

#------------------------------------------------------------------------------
# Accessors

  # returns value of side_up (str)
  def get_side_up(self):
    return self.__side_up

#------------------------------------------------------------------------------
# Mutators

  # Randomly generated 0 = "Tails"
  # Randomly generated 1 = "Heads"
  def toss(self):
    self.__side_up = self.__VALUE_LIST[random.randint(0,1)]

#------------------------------------------------------------------------------
# "to_string"

  def __str__(self):
    return "Coin is %s-up" % (self.__side_up)

  


