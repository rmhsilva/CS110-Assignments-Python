import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
startpoint = turtle.Turtle()
endpoint = turtle.Turtle()
startpoint.hideturtle()
endpoint.hideturtle()
startpoint.up()
startpoint.speed(20000)
startpoint.pensize(10)
startpoint.goto(-100,-40)
startpoint.left(90)
startpoint.down()
startpoint.forward(100)
endpoint.up()
endpoint.speed(20000)
endpoint.pensize(3)

lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)
andy.stamp()
lance.stamp()
# your code goes here, I've changed lines above as well


def speed_andy():
  andy_speed=random.randrange(1,5)
  return andy_speed
'''andy.speed = speed_andy()
andy.forward(500)'''

def speed_lance():
  lance_speed=random.randrange(1,5)
  return lance_speed
'''lance.speed = speed_lance()
andy.shape("turtle")
andy.stamp()'''
#Let the turtles go directly without loops make them strange
'''
andy.speed = speed_andy()
andy.forward(500)
lance.forward(500)
'''
andy_total_range = 0
lance_total_range = 0
#I've done tests on windows for many times and adjusted my code that I think the turtles looks good now
for iterations in range(200):
  andy.speed = speed_andy()
  lance.speed = speed_lance()
  andy_range = random.randrange(0,4)#The real strange thing is that lance never wins when range is set up to 5
  lance_range = random.randrange(0,4)
  andy.forward(andy_range)
  lance.forward(lance_range)
  andy_total_range = andy_total_range + andy_range
  lance_total_range = lance_total_range + lance_range
#print out for tests
#print(andy_total_range)
#print(lance_total_range)
winner = 0#the winner would be indicated by a line
if andy_total_range > lance_total_range:
  winner = andy_total_range
else:
  winner = lance_total_range
position_endpoint = -100+winner
endpoint.goto(position_endpoint,-40)
endpoint.down()
endpoint.left(90)
endpoint.forward(100)
wn.exitonclick()
