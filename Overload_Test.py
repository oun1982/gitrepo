__author__ = 'oun1982'
class Car:
    def __init__(self,*args):
        if(len(args) == 0):
            print("No parameter No Overloading")
        else:
            print("There are %d argument overloading : "%(len(args)))
            lists = []
            for i in args:
                lists.append(i)
            print("Constructor overloading argument:",lists)

    def printX(*args):
        if (len(args) == 0):
            print("No Overloading")
        else:
            print("There are %d argument overloading"%(len(args)-1))
            lists = []
            for i in args:
                lists.append(i)
            print("Constructor overloading argument:",lists[1:])
car1 = Car()
print("-------------------------")
#car2 = Car("Toyota")
#car3 = Car("Toyota","Honda","BMW","BENZ")
car1.printX()
print("---------car1-1-------------")
car1.printX(5)
print("---------car1-2-------------")
car1.printX(5,6.5,-5,"Overloading")
print("---------car1-3-------------")
