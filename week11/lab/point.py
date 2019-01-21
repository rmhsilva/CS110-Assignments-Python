import math

# Point class for representing and manipulating
# x,y coordinates. 
class Point:
  # --------------------------------------------------------------------------
  # Constructor

  # param init_x (int)
  # param init_y (int)
  def __init__(self, init_x = 0, init_y = 0):
    self.__x = init_x
    self.__y = init_y

  # --------------------------------------------------------------------------
  # Accessors

  # return value of x (int)
  def get_x(self):
    return self.__x

  # return value of y (int)
  def get_y(self):
    return self.__y

  # param other_point (Point)
  # return distance from other point (float)
  def compute_distance_from_point(self, other_point):
    dx = (other_point.get_x() - self.__x)
    dy = (other_point.get_y() - self.__y)
    return math.sqrt(dy**2 + dx**2)

  # return distance from origin (float)
  def compute_distance_from_origin(self):
    dx = 0 - self.__x
    dy = 0 - self.__y
    #return math.sqrt(dy**2 + dx**2)
    return self.compute_distance_from_point(Point(0, 0))

  # return x reflection (Point)
  def create_x_reflection(self):
    return Point(self.__x, self.__y * -1)

  # param other_point (Point)
  # return slope to point (float)
  # Note exception handling!
  def compute_slope_from_point(self, other_point):
    try:
      slope = (self.__y - other_point.get_y()) / (self.__x - other_point.get_x())
    except ZeroDivisionError:
      slope = None  
    return slope

  # return slope from origin (float)
  def compute_slope_from_origin(self):    
    return self.compute_slope_from_point(Point(0, 0))

  # param other_point (Point)
  # return y-intercept of line (float)
  def compute_y_intercept_of_line_to(self, other_point): 
    return self.__y - (self.compute_slope_from_point(other_point) * self.__x)

  # param other_point (Point)
  # return coefficients of line (tuple)
  def getLineTo(self, other_point):
    slope = self.compute_slope_from_point(other_point)
    intercept = self.compute_y_intercept_of_line_to(other_point)
    return (slope, intercept)

  # --------------------------------------------------------------------------
  # Mutators 
   
  # param dx (int)
  # param dy (int)
  def move(self, dx, dy):
    self.__x += dx
    self.__y += dy
    
  # --------------------------------------------------------------------------
  # to_string

  # return string representation of Point object (str)
  def __str__(self):
    return "(%d, %d)" % (self.__x, self.__y)

# ----------------------------------------------------------------------------  

# Create point objects and exercise methods
def main():
  p1 = Point()
  p2 = Point(3, 4)
  p3 = Point(6, 8)
  print("Test to_string() on p1, p2 and p3:")
  print(p1)
  print(p2)
  print(p3)
  print("Test get_x() and get_y() on p2:")
  print(p2.get_x())
  print(p2.get_y())
  print("Test compute_distance_from_origin() on p2:")
  print(p2.compute_distance_from_origin())
  print("Test compute_distance_from_point() on p3 from p2:")
  print(p3.compute_distance_from_point(p2))
  print("Test create_x_reflection()")
  print(p2.create_x_reflection())
  print("Test compute_slope_from_origin() on p2:")
  print(p2.compute_slope_from_origin())
  print("Test compute_slope_from_point() on p3 from p2:")
  print(p3.compute_slope_from_point(p2))
  print("Test compute_y_intercept_of_line_to() on p2 to p3:")
  print(p2.compute_y_intercept_of_line_to(p3))
  print("Test get_line_to() on p2 to p3:")
  print(p2.getLineTo(p3))
  print("Test move() on p2:")
  p2.move(2, 4)
  print(p2)
    
main()

