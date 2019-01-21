'''
TAO YICHEN
ytao15@binghamton.edu
Assignment11
Lab section: B56
CA name: Paul Maino
Assignment #11 Part 1
Phone: 6079532749
'''

'''
This class represents a patron
A Patron has a name, a status and
zero or more books checked out
'''
#This one is just for my own use.
#I'm so confused as for what methods I have.
#I have this as an reminder for myself
all_attributes = ["Patron",
           "can_check_out_books", "has_checked_out_books",
           "get_name", "get_status","get_num_books_out",
           "__update_status","increment", "decrement",
           "__lt__","__eq__", "__str__"]

class Patron:

  # Class Constants ----------------------------------------------------------

  # Maximum number of books Patron can take out (int)
  MAX_BOOKS_OUT = 3

  # Current status of this Patron (str)
  # Will be combined with name of Patron
  STATUS = [" can borrow up to 3 books", " can borrow two more books", \
            " can borrow one more book", " must return book(s)"]

  # Constructor --------------------------------------------------------------
  zero = 0
  # params:  name - name of Patron(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__num_books_out (int) to 0, and self.__status() (str)
  #              to STATUS with respect to number books out
  def __init__(self, name):
    # your code here
    self.__name = name
    self.__num_books_out = self.zero
    self.__status = self.STATUS[self.__num_books_out]
  # Predicates ---------------------------------------------------------------

  # returns: True if less then max books checked out, False otherwise (bool)
  def can_check_out_books(self):
    # your code here
    return self.__num_books_out < self.MAX_BOOKS_OUT
  # returns: True if books checked out, False otherwise (bool)
  def has_checked_out_books(self):
     # your code here
    return self.__num_books_out > 0
  # Accessors ----------------------------------------------------------------    

  # returns: name (str)
  def get_name(self):
    # your code here
    return str(self.__name)
  # returns: status (str)
  def get_status(self):
    # your code here
    return str(self.__status)
  # returns: number of books out (int)
  def get_num_books_out(self):
    # your code here
    return int(self.__num_books_out)
  # Mutators -----------------------------------------------------------------

  # set to STATUS indexed by number of books out
  def __update_status(self):
    # your code here
    self.__status = self.STATUS[self.__num_books_out]
  # Increases number of books out by one
  # invokes: update_status()
  def increment(self):
    # your code here
    self.__num_books_out+=1
    self.__update_status()
  # Decereases number of books out by one
  # invokes update_status()
  def decrement(self):
    # your code here
    self.__num_books_out -= 1
    self.__update_status()
  # Comparators --------------------------------------------------------------

  # Already written for you:
  # You will need to include these in order to sort Patron objects
  
  # Shows how two Patrons can be compared with respect to the < relationship
  # params:  other - another Patron object
  # invokes: type()
  # returns: True when they are not the same Patron and other is a Patron
  #          object and name of this Patron is lexicographically less than 
  #          name of other Patron, False otherwise (bool)
  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__name < other.__name

  # Shows how two Patrons can be compared with respect to the == relationship
  # params:  other - another Patron object
  # invokes: type()
  # returns: True when both are same Patron OR both are Patron objects AND
  #          all attributes are equal, False otherwise (bool)
  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and \
            self.__name == other.__name and \
            self.__status == other.__status and \
            self.__num_books_out == other.__num_books_out)

  # Convert to Str -----------------------------------------------------

  # invokes:  str()
  # returns:  str representation of Patron object (str)
  def __str__(self):
    # your code here
    return "%s %s, %s book(s) out.\n"%(self.__name,self.__status, self.__num_books_out)
