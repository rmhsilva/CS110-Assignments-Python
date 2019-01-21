'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Assignment #1 Part 1
Phone: 6079532749
'''

# Analysis

#Obtain number of communication lines, Provided number of people

#Output
#no_comm - number communication lines (int)

#Input
#no_people -number of people (int)

#Process
#Use the formula : total == (n*(n-1))/2

#Design



def main():
  #Obtain Input
  no_people = int(input("What is number of people? "))
    
  #Obtain output from input use the formula
  no_comm = (no_people*(no_people-1))/2
    
  #Output on screen
  print("Lines of communication for", no_people,"people is : ", no_comm)
main()
