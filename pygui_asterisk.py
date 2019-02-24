import pyautogui as pg
import webbrowser as web
import time

with open("D:\Oun1982\OSD_Work\CUSTOMER\CENTER AUTO LEASE\POC E1 Cisco\mobile.txt","r") as file:
    data = file.read()
    num = data.split("\n")
    x = 4
    for i in num:
        print(x)
        pg.moveTo(326, 205)
        pg.click()
        time.sleep(1)
        for y in range(x):
            pg.press('tab')
            time.sleep(0.025)

        pg.press('enter')
        time.sleep(1)
        pg.press(['tab', 'tab'])
        pg.typewrite(i, interval=0.01)
        pg.press('tab')
        pg.typewrite('1', interval=0.01)
        time.sleep(1)
        pg.press('tab')
        pg.press('enter')
        if x > 18:
            x = 19
        else:
            x = x + 1


#for num in range(len(file.readlines())):7
#    print(file[0])