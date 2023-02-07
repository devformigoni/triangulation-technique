### Program developed by Prof. MSc. Paulo O. Formigoni, PhD ###
### profpauloformigoni@gmail.com ###

### This is a python code that implements the triangulation technique to determine the location of a
### signal source. The code defines a function distance that calculates the Euclidean distance between
### two points, and a function triangulate that calculates the location of the signal source based on the
### distances between it and three reference points. The code also provides a graphical representation of
### the triangulation result using matplotlib library. The user inputs the coordinates and distances of the
### three reference points and the code outputs the calculated location of the signal source.

import math
import matplotlib.pyplot as plt

def distance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangulate(x1, y1, x2, y2, x3, y3, d1, d2, d3):
  A = 2 * (x2 - x1)
  B = 2 * (y2 - y1)
  C = d1**2 - d2**2 - x1**2 - y1**2 + x2**2 + y2**2
  D = 2 * (x3 - x2)
  E = 2 * (y3 - y2)
  F = d2**2 - d3**2 - x2**2 - y2**2 + x3**2 + y3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x, y

x1 = float(input("Enter the X coordinate of the first reference point: "))
y1 = float(input("Enter the Y coordinate of the first reference point: "))
x2 = float(input("Enter the X coordinate of the second reference point: "))
y2 = float(input("Enter the Y coordinate of the second reference point: "))
x3 = float(input("Enter the X coordinate of the third reference point: "))
y3 = float(input("Enter the Y coordinate of the third reference point: "))
d1 = float(input("Enter the distance to the first reference point: "))
d2 = float(input("Enter the distance to the second reference point: "))
d3 = float(input("Enter the distance to the third reference point: "))
x, y = triangulate(x1, y1, x2, y2, x3, y3, d1, d2, d3)
print("The location of the signal is approximately at (%.2f, %.2f)" % (x, y))

plt.scatter([x1], [y1], c='blue')
plt.scatter([x2], [y2], c='red')
plt.scatter([x3], [y3], c='green')
plt.scatter([x], [y], c='black')
plt.annotate("Point 1", (x1, y1), color='blue')
plt.annotate("Point 2", (x2, y2), color='red')
plt.annotate("Point 3", (x3, y3), color='green')
plt.annotate("Signal Source", (x, y), color='black')
plt.title("Triangulation Localization")
plt.xlabel("distance (km)")
plt.ylabel("distance (km)")
plt.legend(["Reference Point 1", "Reference Point 2", "Reference Point 3", "Signal Source"])
plt.show()