# -*- coding: utf-8 -*-
import math
# homework
print(format(57.4, ">9.2f"))

# geometry of a pentagon

#r = float(input("Radius "))
#s = 2*r*math.sin(math.pi/5)
#area = (5*(s ** 2)) / (4 * math.tan(math.pi/5))
#print(area)

#robust slope line formula
y1 = float(input("Enter first y point: "))
y2 = float(input("Enter second y point: "))
x1 = float(input("Enter first x point: "))
x2 = float(input("Enter second x point: "))

m = (y2 - y1) / (x2 - x1)

b = y1 - (m * x1)

if m == 1 and b == 0:
    print("y = x")
elif m == 1.0 and b > 0.0:
    print(f"y = x +({b})")
elif m > 1 and b > 0:
    print(f"y = {m}x +({b})")
else:
    print(f"Something's wrong with your slope input, m = {m}, and b = {b},\
          y1 = {y1}, y2 = {y2}, x1 = {x1}, x2 = {x2}")
          