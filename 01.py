__author__ = 'oun1982'

lst1 = [0,1,2,3,4]
lst2 = [5,6,7,8,9]
str1 = "Python language"
print("Hello %s "%str1)
print("%0.6s"%str1)
print("str1[0:6] =",str1[0:6])
print(lst1[3])
print(lst1[-2])
print(type(lst1))
print(type(str1))
print(len(lst1))
print(lst1+lst2)
print(lst1*3)
print(3 in lst1)
for x in lst1:
    print(x)

setCar = {"toyota","honda","mazda","benz"}
print(setCar)
print('toyota' in setCar)
print(10**5)

var1 = 100
if var1:
    print("1 - Got a true expression value ")
    print(var1)
var2 = 0
if var2:
    print("1 - Got a true expression value ")
    print(var2)
    pass
print("Good Bye")

