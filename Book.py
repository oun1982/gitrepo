__author__ = 'oun1982'
class Book:
    bookCount = 0
    def __init__(self):
        Book.bookCount += 1

    def setBookName(self,name):
        self.name = name

    def getBookName(self):
        print("Book Name : ",self.name)
class OtherBook(Book):
    def showYear(self):
        print("This Year 2016")
class Apple:
    def printApple(self):
        print("Apple")

obj = OtherBook()
obj.setBookName("Asterisk")
obj.getBookName()
obj.showYear()

if issubclass(OtherBook,Book):
    print("True")
else:
    print("False")

if isinstance(obj,OtherBook):
    print("True")
else:
    print("False")

if isinstance(obj,Book):
    print("true")
else:
    print("False")

if isinstance(obj,Apple):
    print("True")
else:
    print("False")