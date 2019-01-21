'''
TAO YICHEN
ytao15@binghamton.edu
Assignment11
Lab section: B56
CA name: Paul Maino
Assignment #11 Part 1
Phone: 6079532749
'''

from librarymodule import StringGeneratorForDictionaries
from book import *

'''
This class represents a library with books and patrons.
'''

class Library(object):

#-- Class Variables ----------------------------------------------------
  ZERO = 0
  # index when book not in library
  NOT_IN_LIBRARY = 0

  # index when book added to library
  ADD = 1

  # index when book removed from library
  REMOVE = 2

  # index when patron not a member of library
  NOT_A_MEMBER = 3

  # index when patron becomes member of library
  JOIN = 4

  # index when patron ends membership in library
  LEAVE = 5

  # index when book information is accessed
  ACCESS = 6

  # index when patron information is accessed
  LOOK_UP = 7

  # most reacent transaction with respect to either a book or a patron
  TRANS_STATUS = [" is not in library",
                  " has been added to the library",
                  " has been removed from the library ",
                  " is not a library member ",
                  " has been added as a library member",
                  " has been removed as a library member",
                  " has been accessed", 
                  " member files have been accessed"]
  
#-- Constructor --------------------------------------------------------

  # params:  name - name of Library(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__books (dict of Book)  and
  #              self.__patrons() (dict of Patron) to empty dictionaries,
  #              self.__transaction_status (str) to TRANS_STATUS with respect to
  #                book participating in transaction or
  #                patron participating in transaction
  def __init__(self, name):##checked
    # your code here
    self.__name = None #String-Library name
    self.__books = {}#Dictionary of Book objects
    self.__patrons = {}#Dictionary of Patron objects
    self.__transaction_status  = self.TRANS_STATUS[self.NOT_IN_LIBRARY]#String -status of Book object or Patron object

#-- Accessors ----------------------------------------------------------

  def get_name(self):##checked
   # your code here
   return self.__name
  def set_name(self,new_name):
    self.__name = new_name

  # returns:  record of latest transaction (str)
  def get_transaction_status(self):##checked
    # your code here
    return self.__transaction_status

  # params:  title of Book (str)
  # invokes:  in_library(), __set_transaction_status()
  # returns:  Book stored in library (Book) or None
  def get_book(self, title):#Finished, unchecked
    # your code here
    if self.in_library(title):
      self.__set_transaction_status(title = title, index = self.ACCESS)
    else:
      self.__set_transaction_status(title = title, index = self.NOT_IN_LIBRARY)
    return self.__books[title] if self.in_library(title) else None

  # params: name of Patron who is member of library (str)
  # invokes:  is_member(),  __set_transaction_status()
  # returns:  name of Patron (Patron) or None
  def get_patron(self, name):#Finished, unchecked
    # your code here
    if self.is_member(name):
      self.__set_transaction_status(name = name, index = self.LOOK_UP)
    else:
      self.__set_transaction_status(name = name, index = self.NOT_A_MEMBER)
    return self.__patrons[name] if self.is_member(name) else None

#-- Predicates ---------------------------------------------------------


  # params: title - title of Book to search for in library (str)
  # returns:  True if in library, False otherwise (bool)
  def in_library(self, title):#checked
    # your code here
    return title in self.__books

  # params: name - name of Patron to search for in library (str)
  # returns:  True if member of library, False otherwise (bool)
  def is_member(self, patron_name):#checked
    # your code here
    return patron_name in self.__patrons

  # invokes:  len()
  # returns:  True if library has any books, False otherwise (bool)
  def has_books(self):#checked
    # your code here
    return len(self.__books) > self.ZERO
  
  # invokes:  len()
  # returns:  True if library has any members, False otherwise (bool)
  def has_members(self):#checked
    # your code here
    return len(self.__patrons) > self.ZERO

#-- Mutators -----------------------------------------------------------
    
  # params:  title - title of Book participating in transaction (str)
  #          name = name of Patron participating in transaction (str)
  #          Note:  one of the above should be an empty string
  #          index into TRANS_STATUS (int)
  def __set_transaction_status(self, title = "", name = "", index = None):#checked
    # your code here
    if title:       
      self.__transaction_status = title + self.TRANS_STATUS[index]
    elif name:
      self.__transaction_status = name + self.TRANS_STATUS[index]

  # params:  book - new Book to be added to library (Book)
  # invokes:  get_title() (_book), __set_transaction_status()
  def add_book(self, book):#Finished, not checked
    # your code here
    self.__books[book.get_title()] = book
    self.__set_transaction_status(title = book.get_title(),index = self.ADD)

  # params:  title - title of Book to remove from library (str)
  # invokes:  pop() (list),
  #           is_checked_out() (_book), get_patron (Book)
  #           decrement () (Patron)
  #           in_library(), __set_transaction_status()
  def remove_book(self, title):
     # your code here
     if self.in_library(title) and not self.__books[title].is_checked_out():
       #book_patron = self.__books[title].get_patron()
       if bool(self.__books[title].get_patron()):
         book_patron.decrement# if bool(book_patron)
       self.__books.pop(title)
       self.__set_transaction_status(title = title, index = self.REMOVE)

  # params:  patron - new Patron to add to library (Patron)
  # invokes:  get_name (Patron), __set_transaction_status()
  def add_patron(self, patron):#Finished, not checked
   # your code here
   self.__patrons[patron.get_name()] = patron
   self.__set_transaction_status(name = patron.get_name(),index = self.JOIN)

  # params:  name - name of Patron to remove from library (str)  
  # invokes:  pop() (list),
  #           has_checked_out_books() (Patron) 
  #           get_patron (Book), return_me (Book)
  #           is_member(), __set_transaction_status()
  def remove_patron(self, name):
    # your code here
    if self.is_member(name):
      #Have no idea about how to link patron to books the borrowed
##      if self.__patrons[name].has_checked_out_books():
##        Book.return_me(Book)
      if self.__patrons[name].has_checked_out_books():
        for BookObject in self.__books.values():
          if BookObject.has_book(self.__patrons[name]):
            BookObject.return_me()
      self.__patrons.pop(name)
      self.__set_transaction_status(name = name, index = self.LEAVE)

#-- Convert to Str -----------------------------------------------------

 # creates:  StringGeneratorForDictionaries objects
  # invokes:  str(), get_name(), has_books(), has_members(),
  #           get_dict_string() (StringGeneratorForDictionaries)
  # returns:  str representation of Library object (str)  
  def __str__(self):
    # your code here
    book_out = StringGeneratorForDictionaries(self.__books,"Books")
    patron_out = StringGeneratorForDictionaries(self.__patrons, "Patrons")
    return book_out.get_dict_string() + patron_out.get_dict_string()
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
