'''
TAO YICHEN
ytao15@binghamton.edu
Lab section: B56
CA name: Paul Maino
Lab#5 Part 1
Phone: 6079532749
'''
import turtle
import math
import random
#Since resource usage is related to number of darts
#and drawing speed
numdarts_str = \
             input(\
               "Number of dots:(Less than 10000 \is recommended\n  due to resource usage):")
while not numdarts_str.isdigit():
  numdarts_str=(input("Wrong entry\n Only numbers PLEASE:"))
numdarts = int(numdarts_str)
drawing_speed_str = \
              input(\
                "Drawing speed:(Less than 1000 \is recommended\n  due to resource usage):")
while not drawing_speed_str.isdigit():
  drawing_speed_str=(input("Wrong entry\n Only numbers PLEASE:"))
drawing_speed = int(numdarts_str)
def main():
  COLOR_INSIDE = 'red'
  COLOR_OUTSIDE = 'blue'
  DOT_SIZE = 5
  multiples =(-1,1)
  fred = turtle.Turtle()
  #fred.hideturtle()
  insideCount = 0
  outsideCount = 0
  #fred.shape('turtle')
  wn = turtle.Screen()
  wn.setworldcoordinates(-1,-1,1,1)
  #numdarts = 10**4#10**13
  wn.tracer(drawing_speed)#The tested speed which is good for me is 1000
  #fred.hideturtle()
  fred.up()
  #fred.dot(200)#a test for dot size
  #numdarts = 10**13
  for i in range(numdarts):
    #randx = random.random()*random.choice(-1,1)
    #randy = random.random()*random.choice(-1,1)
    x =random.random()*random.choice(multiples)
    y =random.random()*random.choice(multiples)
    fred.goto(x,y)
    distance = fred.distance(0,0)
    if distance<=1:
      #fred.color(COLOR_INSIDE)
      #fred.stamp()
      #fred.down()
      fred.dot(DOT_SIZE,COLOR_INSIDE)
      #fred.up()
      insideCount+=1
    else:
      #fred.color(COLOR_OUTSIDE)
      #fred.stamp()
      fred.dot(DOT_SIZE,COLOR_OUTSIDE)
      outsideCount +=1
  calc_pi = insideCount/numdarts*4
  #print(insideCount)#For manual calculation and
  #print(outsideCount+insideCount)#validation
  print("The pi value we calculated is:",calc_pi)
  wn.exitonclick()
main()
