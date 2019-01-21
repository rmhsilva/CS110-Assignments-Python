
'''

The Counter class models a simple up/down counter that maintains a single value

It can be imported and used in text-base OR GUI programs

In a GUI, an instance of this class can serve as the Model (MVC Meta-Pattern)

'''

class CounterWP:

  

  # --------------------------------------------------------------------------

  # Constructor

  

  def __init__(self):

    self.__value = 0


  # ---------------------------------------------------------------------------

  # Predicates

  

  def is_positive(self):

    return self.__value > 0


  # ---------------------------------------------------------------------------

  # Accessors


  # returns value (int)

  def get_value(self):

    return self.__value

  

  # ---------------------------------------------------------------------------

  # Mutators

  

  def increment(self):

    self.__value += 1


  # Does NOT stop at 0

  def decrement(self):

    self.__value -= 1


  def reset(self):

    self.__value = 0


  # param value (int)

  def set(self, value):

    self.__value = value


  # --------------------------------------------------------------------------

  # to_string()


  def __str__(self):

    return "Current value of counter is %d" % self.__value

