'''
TAO YICHEN
ytao15@binghamton.edu
Assignment11
Lab section: B56
CA name: Paul Maino
Assignment #11 Part 1
Phone: 6079532749
'''

from patron import *
'''
This class represents a book with a title, author, status,
a patron to whom the book is checked out, and a list
of patrons waiting for it
'''
#This one is just for my own use.
#I'm so confused as for what methods I have.
#I have this as an reminder for myself
all_attributes = ["Book",
           "is_checked_out", "is_reserved", "has_book","is_in_waitlist",
           "__needs_two_part_status",
           "get_title", "get_author","get_patron", "get_waitlist_str", "get_transaction_status",
           "borrow_me","return_me",
           "__lend_book", "__reset_patron","__lend_to_next_patron", "__put_in_wait_list","__set_transaction_status"
           "__lt__", "__eq__", "__str__"]

class Book:

  # Class Constants ----------------------------------------------------------
  # "\n" will be used to separate different transactions
  # "*-**-*"will be used to sepaate different arguments within the same transaction
  ZERO = 0
  LINE_DIVIDER = '\n'
  ARGUMENT_DIVIDER = " "
##  ARGUMENT_DIVIDER = "*-**-*"
  # index when book is first created (int)
  #No transactions yet
  NONE = 0
  
  # index when book is loaned successfully (int)
  #Successfully checked out
  SUCCESSFUL = 1
  
  # index when patron is put on waiting list (int)
  #Has been put on waiting list for
  WAIT = 2
  
  # index when request for loan is unsuccessful (int)
  #Must return books before taking out
  UNSUCCESSFUL = 3
  
  # index when book is returned (int)
  #Has returned
  RETURNED = 4
  
  # index when request for loan is invalid (int)
  #Has recorded an invalid transaction re:
  INVALID = 5

  TRANS_STATUS = [" No transactions yet",
                  " successfully checked out ",
                  " has been put on waiting list for ",
                  " must return books before taking out ",
                  " has returned ",
                  " has recorded an invalid transaction re:  "]

  # Constructor --------------------------------------------------------------

  # Creates a new book with the given title and author
  # params:  title (str) and author (str) of book
  # initialize:  self.__title (str) and self.__author (str) to value of
  #                 value of incoming parameters
  #               self.__transaction_status (str) to no transactions yet,
  #               self.__patron (_patron) & self.__waitlist (list of Patrons)
  #                 to null/empty values
  def __init__(self, title, author):
    # your code here
    self.__title = title
    self.__author = author
    self.__transaction_status = self.TRANS_STATUS[self.NONE]
    self.__patron = None#Patron object
    #self.__patron = Patron("")
    self.__waitlist = []
  # Predicates ---------------------------------------------------------------

  # returns: True when book is already loaned out, False otherwise (bool)
  #**************Check if the Book is checked out**************
  def is_checked_out(self):
    # your code here
    #return self.__transaction_status == self.TRANS_STATUS[self.SUCCESSFUL]
    return self.__patron != None

  # invokes len()
  # returns: True if Patron(s) are waiting for book, False otherwise (bool)
  #***************Check  if there's anyone in the waitlist***************8
  def is_reserved(self):
    # your code here
    return len(self.__waitlist) > self.ZERO

  # params: patron - a particular patron (Patron)
  # returns: True when Patron has checked out book, False otherwise (bool)  
  def has_book(self, patron):
   # your code here
    return self.__patron == patron
    #return self.__patron == patron.get_name()

  # params: patron - a particular patron (Patron objects)
  # returns: True when given Patron is on waiting list, False otherwise (bool)
  # Pretending waitlist to be a list of objects -------*******-------*****----
  #*************Check if a Patron object is in the list of objects********
  def is_in_waitlist(self, patron):
    # your code here
    return patron in self.__waitlist
#**********************************************************Above lines are checked.****/////-------
  # Both return and lend
  # returns: True when previous transaction is "returned" and 
  #          current transaction is "lend", False otherwise (bool)
  #*************************Check if string of returned is in previous transaction and string of successfull lend is in latest transaction*************(checked)
  def __needs_two_part_status(self):
    # your code here
    return self.TRANS_STATUS[Book.RETURNED] in self.__transaction_status and self.LINE_DIVIDER not in self.__transaction_status
##    return (self.TRANS_STATUS[self.SUCCESSFUL] in self.__transaction_status.split(self.LINE_DIVIDER)[-1])\
##               and (self.TRANS_STATUS[self.RETURNED] in self.__transaction_status.split(self.LINE_DIVIDER)[-2])
    #print("Need Attention.")
    
  # Accessors ----------------------------------------------------------------

  # returns: title of book (str)
  #***********String of title of the book***********(checked)
  def get_title(self):
    # your code here
    return self.__title

  # returns: author of book (str)
  #***********String of author of book************************(checked)
  def get_author(self):
   # your code here
    return self.__author

  # returns: Patron who has checked out book (str)
  #************************String of patron's name who checked out book*****(checked)
  def get_patron(self):
    # your code here
    return self.__patron.get_name() if self.__patron else None

  # invokes: str()
  # returns: str representation of waiting list for book (str)
  #**********************List of string representation of Patron objects who are in the waitlist of a Book object***********(checked by tester)
  def get_waitlist_str(self):
    # your code here
    return str([str(obj) for obj in self.__waitlist])
    ##    get_list4 = []
    ##    for obj in self.waitlist:
    ##      checker5 = obj.get_name()
    ##      get_list4.append(checker5)
    ##    return get_list4
    ##out_list = [str(obj.get_name()) for obj in self.waitlist]
    ##return str(out_list)
    ##    return "Wait list:\n%s\n"%str(self.waitlist)
    #return "Wait list:\n%s\n"%str(self.__waitlist)

  # returns: record of latest book transaction (str)
  #***********String of current transaction status********************(checked)
  def get_transaction_status(self):
    # your code here
    #print("Need attention.")
    #return self.__transaction_status.split(self.LINE_DIVIDER)[-1]
    return self.__transaction_status

# **********************************************************Above lines are checked.****/////-------
 # Mutators ------------------------------------------------------------------

  # This method delegates all responsibilities to private methods of class
  # invokes: has_book(), is_in_waitlist(), can_check_out_books(), is_checked_out(),
  #          __lend_book(), __put_in_wait_list(), and __set_transaction_status()
  # params:  patron - patron trying to borrow book (Patron)
  def borrow_me(self, patron):
    if (not patron.can_check_out_books()):
      self.__set_transaction_status(patron.get_name(),self.UNSUCCESSFUL)
    elif self.has_book(patron):
      self.__set_transaction_status(patron.get_name(),self.INVALID)
    elif self.is_checked_out():
      if self.is_in_waitlist(patron):
        self.__set_transaction_status(patron.get_name(),self.INVALID)
      else:
        self.__put_in_wait_list(patron)
        self.__set_transaction_status(patron.get_name(),self.WAIT)
    elif ((self.is_in_waitlist(patron) and self.__waitlist.index(patron) == self.ZERO))\
         or (not self.is_reserved()):
      self.__lend_book(patron)
      self.__set_transaction_status(patron.get_name(),self.SUCCESSFUL)
    else:
      self.__set_transaction_status(patron.get_name(),self.INVALID)
    # your code here
##    if patron:
##      if self.has_book(self.__patron) or self.is_in_waitlist(self.__patron):
##        self.__set_transaction_status(self.__patron.get_name()if bool(self.__patron) else "Unknown" , self.INVALID)
##      elif (not (patron.can_check_out_books())):
##        self.__set_transaction_status(patron.get_name() if bool(patron) else "Unknown", self.UNSUCCESSFUL)
##      elif (self.is_checked_out()):
##        self.__put_in_wait_list(self.__patron)
##        self.__set_transaction_status(self.__patron.get_name() if bool(self.__patron) else "Unknown", self.WAIT)
##      else:
##        self.__lend_book(patron)
##        self.__patron = patron
##        self.__set_transaction_status(self.__patron.get_name() if bool(self.__patron) else "Unknown", self.SUCCESSFUL)
##    else:
##      self.__set_transaction_status(self.__patron.get_name()if self.__patron else "Unknown", self.INVALID)
##
##    if self.is_checked_out() and (not self.is_in_waitlist(patron)) and (not self.has_book(patron)) and (patron.can_check_out_books()):
##      self.__put_in_wait_list(patron)
##
##    elif self.is_checked_out() and self.has_book(patron):
##      self.__lend_book()
##      self.__set_transaction_status(patron.get_name(),self.SUCCESSFUL)
##    else:
##      self.__set_transaction_status(self.__patron.get_name()if self.__patron else "Unknown", self.INVALID)

  # Return book: release current patron, try to lend to waiting patron  
  # This method delegates all responsibilities to private methods of class
  # invokes: is_checked_out(), is_reserved(), get_name(),
  #          __reset_patron,(), __lend_to_next_patron(), and
  #          __set_transaction_status()
  def return_me(self):
    if self.is_checked_out():
##      if self.has_book(self, patron):
      self.__set_transaction_status(self.__patron.get_name(), self.RETURNED)
      self.__reset_patron()
      if self.is_reserved():
        self.__lend_to_next_patron()
##    else:
##      self.__set_transaction_status(self.__patron.get_name()if self.__patron else "Unknown", self.INVALID)
##    if self.is_checked_out():
##      name = self.__patron.get_name()
##
##      self.__reset_patron()
##      self.__set_transaction_status(name,self.__RETURNED)
##      if self.isreserved():
##        self.__lend_to_next_patron()
##    else:
##      self.__set_transaction_status('Unknown',self.INVALID)
##    # your code here
##    if self.is_checked_out():
##      self.__reset_patron()
##      if self.is_reserved():
##        self.__lend_to_next_patron()
##        self.__set_transaction_status(patron.get_name(),self.SUCCESSFUL)


  # invokes: increment() (Patron class)
  # params: patron - Patron borrowing book (Patron)
  #***********Increase number of books a patron borrowed*******************(checked)

  def __lend_book(self, patron): 
   # your code here
    self.__patron = patron
    patron.increment()

  # invokes: decrement() (Patron class)
  #************Decrease number of books a patron borrowed*******************(checked)
  def __reset_patron(self): #patron mutator
    # your code here
    self.__patron.decrement()
    self.__patron = None
##    self.__patron.decrement()
    
  # Lend book to waiting patron if eligible; if not, remove from wait List
  # invokes: is_checked_out(), is_reserved(),
  #          pop() (from list), borrow_me()
  def __lend_to_next_patron(self): # waitlist mutator
    # your code here
    if (not self.is_checked_out()) and self.is_reserved():
      self.borrow_me(self.__waitlist[0])
      self.__waitlist.pop(0)
##      self.__patron_attempt = self.__waitlist.pop()
##      self.borrow_me(self.__patron_attempt)

  # params:  patron - Patron to put in waiting list (Patron)
  # invokes: append() (to list)
  #******************Add patron object into waitlist of Book object**************(checked)
  def __put_in_wait_list(self, patron): # waitlist mutator
    # add patron to wait list
    # your code here
    self.__waitlist.append(patron)

  # Creates string describing latest transaction
  # Combines name of patron participation in transaction with
  #   status of most recent transaction and title of this book 
  # params: name - name of Patron participating in transaction (str)
  #         index - index of transaction in TRANS_STATUS (int)
  # invokes: __needs_two_part_status()
  # I have no idea as for what the above description is talking about
  # So I am unable to adhere to the above requirements
  # Assuming transaction status of Book object is used to store all the transaction history
  # "\n" will be used to separate different transactions
  # "*-**-*"will be used to sepaate different arguments within the same transaction
  def __set_transaction_status(self, name, index):# trans_status mutator
   # your code here
   if self.__needs_two_part_status():
     self.__transaction_status+=(self.LINE_DIVIDER + name + self.ARGUMENT_DIVIDER + self.TRANS_STATUS[index]+ self.ARGUMENT_DIVIDER + self.get_title())
   else:
     self.__transaction_status=(name + self.ARGUMENT_DIVIDER + self.TRANS_STATUS[index]+ self.ARGUMENT_DIVIDER + self.get_title())
##   if self.__needs_two_part_status and index == self.WAIT:
##     self.__transaction_status+=(self.LINE_DIVIDER + name + self.ARGUMENT_DIVIDER + self.TRANS_STATUS[index]+ self.ARGUMENT_DIVIDER + self.get_title())
##   elif index == self.INVALID:
##     self.__transaction_status+=(self.LINE_DIVIDER + name + self.ARGUMENT_DIVIDER + self.TRANS_STATUS[index]+ self.ARGUMENT_DIVIDER + self.get_title())
##   else:
##     self.__transaction_status+=(self.LINE_DIVIDER + name + self.ARGUMENT_DIVIDER + self.TRANS_STATUS[index]+ self.ARGUMENT_DIVIDER + self.get_title())
##   self.__transaction_status_attempt = self.TRANS_STATUS[index]
##   if self.__needs_two_part_status():
##     print("------------------------********YIUY")
##     self.__transaction_status = self.__transaction_status_attempt
##   elif self.is_checked_out() and self.has_book(patron):
##     self.__transaction_status = self.TRANS_STATUS[self.UNSUCCESSFUL]
##   elif self.is_checked_out() and (not(self.__patron ==patron.get_name())):
##     self.__transaction_status = self.TRANS_STATUS[self.WAIT]
##   else:
##     self.__transaction_status = self.TRANS_STATUS[self.INVALID]

   #print("Need attention")


  # Comparators --------------------------------------------------------------

  # Already written for you:
  # Include these in order to sort Book objects


  # Shows how two Books can be compared with respect to the < relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when they are not same Book and other is Book object and
  #            title of this Book is lexicographically lower than title of
  #            other Book, False otherwise (bool)   
  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__title < other.__title

  # Shows how two Books can be compared with respect to the == relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when both are same Book or both are Book objects and
  #            title and author are equal, False otherwise (bool)
  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and self.__title == other.__title)
      


  # Convert to Str -----------------------------------------------------------

  # invokes:  str(), get_waitlist_str()
  # returns:  str representation of Book object (str)
  def __str__(self):
    # your code here
    return"\nTitle: %s\nAuthor: %s\n%s\nWait list: %s\n"%(self.__title,self.__author,"Checked out: "+self.__patron if bool(self.__patron) else "Not checked out",self.get_waitlist_str())
