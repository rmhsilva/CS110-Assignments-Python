'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA: Paul Maino
Assignment9
Phone: 6079532749
'''
'''
Write a complete program that, given a literal list of tuples consisting of (name, list of grades) pairs
(i.e., the first line of your main should simply be:   gradeList = )
prints out a table showing the number of scores and score average for each person, generated in two different ways
'''

'''
ANALYSIS
  Output a table showing the number of scores and
                          score average for each person
  Provided a list of tuples consisting
                          name and
                          list of grades

OUTPUT to monitor:
  student_name - name (string)
  grade_count - nunmber of scores (integer)
  grade_list_average - average score (float with 2 decimal places)

INPUT from keyboard:
  N/A

GIVENS:
 Nested list of student scores
  
  Code:
    N/A

PROCESSING:
  Part 1:
    Create a dictionary and populate it with the information from the tuples
    Create a list of dictionary keys and sort them
    Iterate over the sorted keys
    Compute the average of the list of grades for each person
    Display each name and average in a table
  Part 2:
    Create a list of tuples from the dictionary using the items() method
    Sort the list
    Iterate over this list
    For each item in the list
    Display the name portion of the item, along with the average of the values as above

'''

# CONSTANTS
student_grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]), ('Slartibartfast',[]),

      ('Trillian', [98, 88]), ('Trillian', [97, 77]), ('Slartibartfast', []),

      ('Marvin', [2000, 500]) , ('Arthur', [42, 20]), ('Arthur', [64]),

      ('Trillian', [99]), ('Marvin', [450]), ('Marvin', [550]),

      ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),

      ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]

#Design

#----------tupleListToDict---------------------
#parameter: old_list - list of tuples consisting of (name, list of grades) pairs (list)
#return: new_dict (dictionary)
#Write a function named tupleListToDict() to
#create a dictionary and populate it with the information from the tuples
#Use each unique name as a dictionary key
#If a person's name is not in the dictionary yet and they do not
#have any grades yet, make their name a key, but set the value for that key to an empty list
def tupleListToDict(old_list):
  new_dict = {}
  for old_list_index in range(len(old_list)):
    student_name = student_grade_list[old_list_index][0]
    grade_list = student_grade_list[old_list_index][1]
    if student_name not in new_dict:
      new_dict[student_name] = []
    #print(new_dict[student_name])
    (new_dict[student_name]).extend(grade_list)
    #new_dict[student_name]=(new_dict[student_name]).append(grade_list)
  #print(new_dict)
  return new_dict

#-----------getSortedKeyList----------------
#parameter: old_dict(dictionary)
#return: new_keys_list (list)
#Write a function named getSortedKeyList() to
#create a list of dictionary keys and sort them
def getSortedKeyList(old_dict):
  new_keys_list = list(old_dict.keys())
  #print(new_keys_list)
  new_keys_list.sort()
  #print(new_keys_list)
  return new_keys_list

#-------------computeAverage----------------
#parameter: old_list - a list of numeric values (list)
#return: average of values in the list(float)
#Write a function named computeAverage() to
#compute the average of the list of grades for each person
def computeAverage(old_list):
  return (sum(old_list)/len(old_list)) if (len(old_list) != 0) else 0
  #return new_average

#------------getSortedListOfTuples------------
#parameters: old_list - list of tuples (list)
#return: old_list - list of sorted tuples (list)
#Write a function named getSortedListOfTuples() to
#sort the list of tuples
def getSortedListOfTuples(old_list):
  old_list.sort()
  #print(old_list)
  return old_list

#----------------------main-------------------
#Main flow of the program
def main():

  #--------------------Part 1----------------------------
  #Create a dictionary and populate it with the information from the tuples
  student_grade_dict = tupleListToDict(student_grade_list)
  #Create a list of dictionary keys and sort them
  student_grade_keys_list = getSortedKeyList(student_grade_dict)
  #Print the frame
  print("               Grade         ")
  print("          Name Count  Average")
  print("------------------------------")
  #Iterate over the sorted keys
  for student_name in student_grade_keys_list:
    #Display each name and average in a table
    grades_list = student_grade_dict[student_name]
    grade_list_average = computeAverage(grades_list)#Get average score
    grade_count = len(grades_list)
    print("%14s%6d%9.2f"%(student_name,grade_count,grade_list_average))
  print()

  #---------------------Part 2------------------------------
  #Create a list of tuples from the dictionary using the items() method
  student_grade_tuple_list = list(student_grade_dict.items())
  #Sort the list
  student_grade_tuple_sorted_list = getSortedListOfTuples(student_grade_tuple_list)
  #Print the frame
  print("               Grade         ")
  print("          Name Count  Average")
  print("------------------------------")
  for index in range(len(student_grade_tuple_sorted_list)):
    student_name = student_grade_tuple_sorted_list[index][0]
    grades_list = student_grade_tuple_sorted_list[index][1]
    grade_list_average = computeAverage(grades_list)#Get average score
    grade_count = len(grades_list)#count
    print("%14s%6d%9.2f"%(student_name,grade_count,grade_list_average))
  print()

main()
