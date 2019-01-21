'''
This program finds the population of a city via database query
Output:
  query result (str)
Input:
  city (str)
Classes Used:
  BadArgument
  QueryWorldBD
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Missing Argument'
    self.__message = 'Population is not valid'


#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def get_title(self):
    return self.__title

    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDB:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, db_name):
    conn = sqlite3.connect(db_name)
    self.__cursor = conn.cursor()
    # Must make city instance variable so that it is accessible to all methods
    #self.__current_city = "" 
    self.__min_pop = ""
    self.__max_pop = ""
    self.__answer = None

# -- Predicate ---------------------------------------------------------------
  def __is_valid_range(self):
    return self.__min_pop.isdigit() and self.__max_pop.isdigit() and \
           int(self.__min_pop) <= int(self.__max_pop)

# -- Accessor ----------------------------------------------------------------
  def get_answer(self):
    return self.__answer

# -- Mutators ----------------------------------------------------------------

  # 
  # param city_name (str)
##  def set_city(self, city_name):
##    self.__current_city = city_name

  def set_min_pop(self,min_pop):
    self.__min_pop = min_pop
  def set_max_pop(self,max_pop):
    self.__max_pop = max_pop
  def set_answer(self):
    self.__answer = self.__cursor.fetchall()
##    print(self.__answer)
    
  # raises BadArgument Exception if city is blank or contains invalid chars
  def pop_query(self):
    if self.__is_valid_range():
##      self.__cursor.execute('select name, population from city where population > 0')
      self.__cursor.execute('select name, population from city where population \
          >= ? and population <= ? order by population',\
                          (self.__min_pop,self.__max_pop))
      
    else:
      raise BadArgument()


  # Close connection to db
  def close_connection(self):
    self.__cursor.close()

# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    # Note that if city isn't in database, then answer will be None
    # If city is in database, answer will be a tuple object
    # Will have to get element[0] of tuple in order to use it
    ##answer = self.__cursor.fetchone()

    # Note that 4th format specifier denotes a string rather than an int in 
    # order to accommodate possibility that answer is None
    ##return '%s %s %s %s\n' % (
      #('The population of' if answer else 'There is no city named'),
      #self.__current_city,
      #('is' if answer else 'in the database'),
      #('' if answer == None else str(answer[0])) )
##    self.__list_of_cities = self.__cursor.fetchall()
    string = ""
    ##print("1")
##    self.set_answer()
    for city_name, city_population in self.__answer:
      string += city_name +" has a Population of : "\
                            +str(city_population) +"\n"
    return string
  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
def main():
  # set up connection and create cursor
##  connection = sqlite3.connect("/Users/wangxuening/Desktop/worldDB")
##  query = connection.cursor()
##  print(query)
  query = QueryWorldDB('worldDB')
##  query = QueryWorldDB('world.db')

  # get input from user (priming read)
  min_pop = input("Input the minimun population you want to set or press" \
                  " <ENTER> to quit: ")
  while min_pop:
    try:
      max_pop = input("Input the maximum population you want to set or press"\
                      " <ENTER> to quit: ")
      query.set_min_pop(min_pop)
      query.set_max_pop(max_pop)
      query.pop_query()

      query.set_answer()
      print(str(query))
    except BadArgument as err:
      print('\n%s: %s\n' % (err.get_title(), str(err) ))
  
  # let user get as many results as desired
  ##while city:
    ##try:
      # set up and issue query
      #cursor.set_city(city.strip())
      #connection.pop_query()
      # show results
      #print(query)
    #except BadArgument as err:
      # city input empty or malformed
      #print('\n%s: %s\n' % (err.get_title(), str(err) ))
       
    # let user enter another city (continuation read)
    #city = input("Find the population of a city\nEnter the city name, " + \
                # "separate multi-word cities by '_'\n" + \
                 #"(Press <Enter> to quit):  ")
  
  #print("Find the city by population \n")


  # close connection to db
    min_pop = input("Input the minimun population you want to set or press" \
                              " <ENTER> to quit: ")
  query.close_connection()

main()
                            
                            
                    
