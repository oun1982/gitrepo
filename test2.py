__author__ = 'oun1982'
'''
import time
start_time = time.time()
number = int(input("enter your number : "))
for i in range(1,1000001):
    print("%d * %d = %d" %(number,i,(number * i)))
print("---%s seconds ---"%(time.time() - start_time))

tup1 = (12,13,14,15.6)
tup2 = ('Asterisk','linux',1982)
print (tup1)
print (tup2)

dict1={'oun1982':'1','pongsakon':'2'}
print (dict1)
'''

'''
var = 100
if var < 200:
    print ("Expression value is less than 200" )
    if var == 150:
        print ("which is 150")
    elif var == 100:
        print ("which is 100")
    elif var == 50:
        print ("which is 50")
elif var < 50:
    print ("Expression value is less than  less than 50" )
else:
    print ("Could not find true expression")
print ('Good Bye')

strr = 'Pongsakon Tongsook'
for name in strr:
    print (name)

for row in range(1,10):
    for col in range(1,10):
        prod = row * col
        if prod < 10:
            print (' ',end = '')
        print(row * col,' ',end =' ')
    print()
'''

combs = []
for x in [1,2,3]:
    for y in [7,8,9]:
        if x != y:
            combs.append((x,y))
print(combs)
