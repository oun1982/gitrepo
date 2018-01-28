__author__ = 'oun1982'
name = input("Enter goods name : ")
price = float(input("Enter price of %s : "%name))
print(price)
if price >= 500:
    temp = price * 0.03
    price = price - temp
else:
    VAT = price * 0.07
    price = price + VAT
print("The price of %s (inc VAT 7%%) is %.2f %s :"%(name,price,"Bath."))

num = int(input("Put your number : "))
if  num % 2 != 0:
    print(num,"is Odd.")
else:
    print(num,"is Even")
print("Good Bye!")