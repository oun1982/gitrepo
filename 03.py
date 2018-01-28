__author__ = 'oun1982'
score = float(input("Enter your score : "))
msg = "Your score is : "
if score >= 80:
    print(msg + "A")
elif score >= 75:
    print(msg + "B+")
elif score >= 70:
    print(msg + "B" )
elif score >= 60:
    print(msg + "C+")
elif score >= 55:
    print(msg + "C" )
elif score >= 50:
    print(msg + "D+")
else:
    print(msg + "F")
print("GoodBye")

count = 0
while (count <= 9):
    print("The count is : ",count)
    count += 1
print("Good Luck")

for i in range(5,10):
    print("i = ",i)

for i in range(100):
    print("i = ",i)

for k in range(20):
    print("k =",k,end = ' ')
