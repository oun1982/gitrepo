__author__ = 'oun1982'
'''
try:
    print("ไม่สามารถเปิดแฟ้มได้ :",err.args)
else:
    print("ปิดแฟ้มเรียบร้อยแล้ว")
    f.closed
'''
filePath = "install Zabbix.txt"
try:
    f = open(filePath)
    print("-------------------- STEP 1 -------------------")
    str = f.read()
    print("-------------------- STEP 1 -------------------")
    print(str)
    print("-------------------- STEP 2 -------------------")
    str2 = f.readline(15)
    print("-------------------- STEP 2 -------------------")
    print (str2)
    print("-------------------- STEP 2 -------------------")

    #Test Readline method
    print("-------------------- STEP 3 -------------------")
    f = open(filePath)
    while 1:
        line = f.readline()
        if len(line):
            print(line)
        else:break
except IOError as err:
    print("Cannot open file")
else:
    print("This file close")
    print("-------------------- STEP 3 -------------------")
    f.close()

