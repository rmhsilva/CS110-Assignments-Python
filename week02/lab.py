import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
wn.setworldcoordinates(0,-1,360,1)

#your code here
for angle in range(0,361,1):
    sine_value = math.sin(math.radians(angle))
    fred.goto(angle, sine_value)
wn.exitonclick()
