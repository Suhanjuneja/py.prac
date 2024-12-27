import math
def roots():
  print("a is coeff of x^2, b is coeff of x and c is const")
  a=int(input("Enter a"))
  b=int(input("Enter b"))
  c=int(input("Enter c"))
  D=b*b-4*a*c
  rootd=math.sqrt(abs(D))
  if D>0:
    print("real and different roots")
    print((-b+rootd)/(2*a))
    print((-b-rootd)/(2*a))
  elif D == 0:
    print(-b/(2*a))
  else:
    print("No real roots")
roots()
