__author__ = 'oun1982'
class Car:
    #Attricutes
    color = "No brand yet"
    brand = "No brand yet"
    number_of_seats = 4
    number_of_wheels = 4
    maxSpeed = 0
    regis_number = 0

    def __init__(self,color,brand,number_of_seats,number_of_wheels,maxSpeed):
        self.color = color
        self.brand = brand
        self.number_of_seats = number_of_seats
        self.number_of_wheels = number_of_wheels
        self.maxSpeed = maxSpeed
        #self.regis_number +=1
        Car.regis_number +=1
    def serColor(self,x):
        self.color = x

    def setBrand(self,x):
        self.brand = x

    def setNumberOfSeates(self,x):
        self.number_of_seats = x

    def setNumberOfWheels(self,x):
        self.number_of_wheels = x

    def setMaxSpeed(self,x):
        self.maxSpeed = x

    def printData(self):
        print("The color of car is : ",self.color)
        print("The car brand : ",self.brand)
        print("The number of seats :",self.number_of_seats)
        print("The number of Wheels :",self.number_of_wheels)
        print("The maximum speed is :",self.maxSpeed,"km/h")
        print("Register number : ",self.regis_number)
car1 = Car('blue','ToYoTa',4,4,150)
car1.printData()
car2 = Car('green','Honda',4,4,120)
car2.printData()
