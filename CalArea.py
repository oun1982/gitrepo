__author__ = 'oun1982'
'''
import CalAreaRectangle
print("Area of Recangle : ", CalAreaRectangle.rectangle(3, 4))
print("Area of Squre :", CalAreaRectangle.squre(10, 10))
print("Area of Parallelogram :", CalAreaRectangle.parallelogram(1.5, 4.5))
print("Area of Trapzoid :",CalAreaRectangle.trapezoid(5, 2.5))
'''
import sys

from CalArea import CalAreaRectangle
from CalArea.CalAreaRectangle import *

print("Area of Recangle : ", rectangle(3, 4))
print("Area of Squre :", squre(10, 10))
print("Area of Parallelogram :", parallelogram(1.5, 4.5))
print("Area of Trapzoid :", trapezoid(5, 2.5))
print (dir(CalAreaRectangle))

print(sys.path)