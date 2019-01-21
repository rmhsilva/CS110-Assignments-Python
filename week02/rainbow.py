import turtle

from turtle import *
wn = turtle.Screen()
def HSB2RGB(hues):
  hues = hues * 3.59 #100转成359范围
  rgb=[0.0,0.0,0.0]
  i = int(hues/60)%6
  f = hues/60 -i
  if i == 0:
    rgb[0] = 1; rgb[1] = f; rgb[2] = 0
  elif i == 1:
    rgb[0] = 1-f; rgb[1] = 1; rgb[2] = 0
  elif i == 2:
    rgb[0] = 0; rgb[1] = 1; rgb[2] = f
  elif i == 3:
    rgb[0] = 0; rgb[1] = 1-f; rgb[2] = 1
  elif i == 4:
    rgb[0] = f; rgb[1] = 0; rgb[2] = 1
  elif i == 5:
    rgb[0] = 1; rgb[1] = 0; rgb[2] = 1-f
  return rgb
def rainbow():
  hues = 0.0
  color(1,0,0) #绘制彩虹
  hideturtle() #隐藏乌龟
  speed(5)
  pensize(3)
  penup()
  goto(-650,-150)
  pendown()
  right(110)
  for i in range (100):
    circle(600) #圆的半径600
    right(0.23)
    hues = hues + 1
    rgb = HSB2RGB(hues)
    color(rgb[0],rgb[1],rgb[2])
    penup()

def main():
  setup(1200, 800, 0, 0)
  bgcolor((64/255, 64/255, 1))
  tracer(False)
  rainbow() #输出文字
  tracer(False)
  goto(0,0)
  pendown()
  color('yellow')
  write("彩虹",align="center", font=("Script MT Bold", 80, "bold"))
  tracer(True)

  mainloop()
  if __name__ == "__main__":
    main() 
