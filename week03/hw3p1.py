'''

Yichen Tao
ytao15@binghamton.edu
Lab Section B 56
Ca : Paul Maino
Assignment #3, Part 1

'''
#There will be a lot of comments down there. I know it looks horrible, but I don't have enough time to
#clean up comments and duplicated codes and not-working functions given the due date
#I basiclly used comments where I should delete since I'am afraid of deleting things accidentally
'''
Determine how to plot a log (base2) curve
NOTE:  you will probably want to allow your max x value to be much larger than your max y value!
Modify your input prompt to ask the user if they want to plot a sine, cosine, or log curve
Use a multiway decision statement to execute the appropriate code (if/elif/else)
Print out an error message if they ask for something other then sine, cosine, or log - use your else:  clause for this!
You must draw a properly scaled x-axis at a minimum
You can receive extra points if you:
Draw a properly scaled y-axis (1 pt for each)
Label your axes (1 pt for each axis)
Remember to hide any extraneous turtle movements
'''

import math
import turtle
import decimal

#This makes graphs look better, some part of this comes from:
#https://stackoverflow.com/questions/7267226/range-for-floats/7267806
def frange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)
  while x > y:#I was testing around to see what went wrong until I realized the backward funcion was missing
    yield float(x)
    x -= decimal.Decimal(jump)
#print(list(frange(2,3,0.1)))#test of frange
'''Start of data block-----------------------------------------------------------'''
little_numbers = (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9)
cos_answer = ('COS','cos','Cos','COSINE','cosine','Cosine')
sin_answer = ('SIN','sin','Sin','SINE','sine','Sine')
log_answer = ('LOG','log','Log' ''','COSINE','cosine','Cosine''')
log_position = (0,-3.5,15,4)#Position data for log in range 0 to 15
trig_position = (0,-1,360,1)#Position data for trig functions in range 0 to 360
'''End of data block-------------------------------------------------------------'''
#The position data is (lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
'''
def use_log_position():
  lower_bound_x = log_position[0]
  lower_bound_y = log_position[1]
  upper_bound_x = log_position[2]
  upper_bound_y = log_position[3]
  return lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y
def use_trig_position():
  lower_bound_x = trig_position[0]
  lower_bound_y = trig_position[1]
  upper_bound_x = trig_position[2]
  upper_bound_y = trig_position[3]
'''
#def set_up_painter(answer):#I would never do this again. This caused so many problems.
#Need more time if I were to complete the set up function
#wn = turtle.Screen()
#wn.bgcolor('lightblue')
'''
------------------Don't have enought time to see what went wrong. Maybe with a later due date the functions
------------------Will look better
  if (answer in cos_answer) or (answer in sin_answer):
    lower_bound_x = trig_position[0]
    lower_bound_y = trig_position[1]
    upper_bound_x = trig_position[2]
    upper_bound_y = trig_position[3]
  elif answer in log_answer:
    lower_bound_x = log_position[0]
    lower_bound_y = log_position[1]
    upper_bound_x = log_position[2]
    upper_bound_y = log_position[3]

  #wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
  pag = turtle.Turtle()
  #fred = turtle.Turtle()
  pag.speed(20000)
  pag.goto(0,20)
  pag.write('x')
  pag.goto(0,0)
  pag.goto(20,0)
  pag.write('x')
  '''
wn = turtle.Screen()
wn.bgcolor('lightblue')
fred = turtle.Turtle()#From all the failed attempts, I believe this one could only be outside of any function
pag = turtle.Turtle()

def axis_drawer(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y):
  pag.speed(200000)
  pag.hideturtle()
  pag.up()
  pag.goto(lower_bound_x,0)
  pag.down()
  pag.goto(upper_bound_x,0)
  #pag.left(90)
  pag.stamp()
  pag.up()
  pag.goto(((upper_bound_x-lower_bound_x)/7*6),0.05)
  pag.write ('X', font = ('Times New Roman', 25, 'bold'))
  #pag.up()
  pag.goto(0,lower_bound_y)
  pag.down()
  pag.goto(0,upper_bound_y)
  pag.left(90)
  pag.stamp()
  pag.up()
  pag.goto(0.5,((upper_bound_y-lower_bound_y)/2/7*6))
  #pag.stamp()
  pag.write ('Y', font = ('Times New Roman', 25, 'bold'))
  

def loggraph(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y):
  #wn.setworldcoordinates(0,-3.5,15,4)#Yeah, these numbers looks best
  #wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
  #fred.color("red")
  #for x in frange(1,0,0.1):#Decided to discard this since it looks weird to draw backward
  fred.up()
  fred.goto(0.1,math.log2(0.1))
  fred.down()
  fred.color("red")
  for x in little_numbers:
     log_value = math.log2(x)
     fred.goto(x,log_value)
     #print(log_value)
  for x in frange(1,15,0.1):
    log_value = math.log2(x)
    fred.goto(x,log_value)
    #print(x)
    #print(log_value)
  #print('KKKKKKKKKkkkk')#initial test for what went wrong

def sinegraph(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y):
  #wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
  #fred.speed(1000000)
  fred.up()
  fred.goto(0,math.sin(math.radians(0)))
  fred.down()
  fred.color("red")
  for x in frange(0,360,0.5):
    sine_value = math.sin(math.radians(x))
    fred.goto(x, sine_value)
  #fred.write ('Hello World!', font = ('Times New Roman', 13, 'bold'))
      
def cosgraph(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y):
  #wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
  fred.up()
  fred.goto(0,math.cos(math.radians(0)))
  fred.down()
  fred.color("red")
  for x in frange(0,360,1):
    cos_value = math.cos(math.radians(x))
    fred.goto(x,cos_value)

def main():
  answer = input("Do you want graph of sine or cosine or log function? \n")#First prompt for answer, then we draw!
  #wn = turtle.Screen()
  #wn.bgcolor('lightblue')
  fred = turtle.Turtle()
  #fred.color("red") #Since this will be reset, this line doesn't work
  #answer = input("Do you want graph of sine or cosine or log function? (COS or SINE or LOG)\n")
  if answer in cos_answer: #== 'COS' or answer == 'cos' or answer == 'Cos':
    #use_trig_position()
    #set_up_painter(answer)
    lower_bound_x = trig_position[0]#I'm trying to reduce the repeating code. But I don't have enough time to try everything
    lower_bound_y = trig_position[1]#And the ways I tried previously failed.
    upper_bound_x = trig_position[2]
    upper_bound_y = trig_position[3]
    wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    axis_drawer(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    #fred.color("red")
    cosgraph(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
  elif answer in sin_answer: #== 'SINE' or answer == 'sine':
    #use_trig_position()
    #set_up_painter(answer)
    lower_bound_x = trig_position[0]
    lower_bound_y = trig_position[1]
    upper_bound_x = trig_position[2]
    upper_bound_y = trig_position[3]
    wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    axis_drawer(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    #fred.color("red")
    sinegraph(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
  elif answer in log_answer: #=='LOG':
    #use_log_position()
    #wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    #lower_bound_x = trig_position[0]
    #lower_bound_y = trig_position[1]
    #upper_bound_x = trig_position[2]
    #upper_bound_y = trig_position[3]
    lower_bound_x = log_position[0]
    lower_bound_y = log_position[1]
    upper_bound_x = log_position[2]
    upper_bound_y = log_position[3]
    wn.setworldcoordinates(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    axis_drawer(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)
    #fred.color("red")
    #set_up_painter(answer)
    loggraph(lower_bound_x,lower_bound_y,upper_bound_x,upper_bound_y)

  #turtle.write("aka", move=False, align="left", font=("Arial", 8, "normal")
  #def _write(self, pos, txt, align, font, pencolor):
  #fred.write ('Hello World!', font = ('Times New Roman', 13, 'bold'))
  #turtle.write(pos =(1,1),txt='xrayecho',font = ('Times New Roman', 36, 'bold'))
  wn.exitonclick()

main()
