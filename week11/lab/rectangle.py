import point

class Rectangle:
  """Rectangle class using Point, width and height"""

  def __init__(self, initP, initW, initH):
    self.__location = initP
    self.__width = initW
    self.__height = initH

  def getWidth(self):
    return self.__width
  def getHeight(self):
    return self.__height

  def __str__(self):
    #pass
    return "%s %d %d"%(self.__location,self.__width,self.__height)

  def area(self):
    return self.__width * self.__height

  def perimeter(self):
    return 2*(self.__width + self.__height)
test = point.Point(2,3)
print(test)
r = Rectangle(point.Point(4, 5), 6, 5)
print(r)
