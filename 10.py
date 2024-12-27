#Write a program to define a class Point with coordinates x and y as attributes. Create
#relevant methods and print the objects. Also define a method distance to calculate the distance
#between any two point objects. 

class Point():
  
  def __init__(self, x, y):
    self.x=x
    self.y=y
  def print_x(self):
    print(f"X coordinate of point 1 is:{self.x}")
  def print_y(self):
    print(f"X coordinate of point 1 is:{self.y}")
    
object_pointer=Point(2,3)
object_pointer2=Point(5,4)
object_pointer.print_x()
object_pointer.print_y()
def distance():
  x1=object_pointer.x
  x2=object_pointer2.x
  y1=object_pointer.y
  y2=object_pointer2.y
  x_dist=(x2-x1)**2
  y_dist=(y2-y1)**2
  dist=(x_dist-y_dist)**0.5
  print("Distance between two points is:",dist)  
distance()
