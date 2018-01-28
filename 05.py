__author__ = 'oun1982'
'''
f = open("myfile.txt","r+")

print("nmae of file :",f.name)
print("Close or not :",f.closed)
print("Opening mode :",f.mode)
print(f.readlines())
'''
import os
import linecache
fPath = "myfile.txt"
for line in range(5):
    print(linecache.getline(fPath, line))
linecache.clearcache()

wordTemp = []
wordCount = 0
file = open("myfile.txt", 'r+')
for line in file:
    for word in line.split():
        wordTemp.append(word)
        wordCount = wordCount + 1
print(wordTemp)
print(wordCount)

print(os.getcwd())

