__author__ = 'oun1982'
class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee = %d" %Employee.empCount)

    def displayEmployee(self):
        print("Name :",self.name,",salary:",self.salary)

emp1 = Employee("Oun1982",30000)
emp2 = Employee("Jang",40000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print(emp1.name)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__doc__:",Employee.__doc__)
print("Employee.__dict__:",Employee.__dict__)

