'''

Yichen Tao
ytao15@binghamton.edu
Lab Section B 56
Lab#3, Part 1

'''
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
wn.setworldcoordinates(0,-1,360,1)
def sinegraph():
  for angle in range(0,361,1):
    sine_value = math.sin(math.radians(angle))
    fred.goto(angle, sine_value)
      
def cosgraph():
  fred.up()
  fred.goto(1,math.cos(math.radians(1)))
  fred.down()
  for angle in range(0,361,1):
    cos_value = math.cos(math.radians(angle))
    fred.goto(angle,cos_value)

answer = input("Do you want graph of sine or cosine function? (COS or SINE)\n")
if answer == 'COS':
  cosgraph()
elif answer == 'SINE':
  sinegraph()
wn.exitonclick()
