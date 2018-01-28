__author__ = 'oun1982'

from CalArea import CalAreaRectangle


def printMe(str):
    "This prints a passed string into this function"
    print (str)
    return
print ('----------------------')
printMe("My Name is pongsakon")
print ('----------------------')

def areaShow(width,heigth):
    return width * heigth
print ('----------------------')
print (areaShow(12,10))
print ('----------------------')

print ("Area of Rectangle :", CalAreaRectangle.rectangle(20,6))
