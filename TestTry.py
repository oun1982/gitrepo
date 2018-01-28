__author__ = 'oun1982'
import sys
try:
    f = open('num.txt')
    s = f.read()
    i = int(s.strip())
    print(i)
except IOError:
    print("IO Error")
except ValueError:
    print("N0 valid interger")
except:
    print("Unexcepted error")
#try:
#    fh = open("test","w")


