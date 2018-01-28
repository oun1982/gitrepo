__author__ = 'oun1982'
class Car:
    color = "No brand yet"
    brand = "No brand yet"
    number_of_seats = 4
    number_of_wheels = 4
    maxSpeed = 0
    registration_number = 0

    def __init__(self, color, brand, number_of_seats, number_of_wheels, maxSpeed):
        self.color = color
        self.brand = brand
        self.number_of_seats = number_of_seats
        self.number_of_wheels = number_of_wheels
        self.maxSpeed = maxSpeed
        self.registration_number += 1

   def setColor(self, x):
       self.color = x

   def setBrand(self, x):
       self.color = x


