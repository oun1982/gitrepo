import pyautogui as pg
import webbrowser as web
import time

''''
url = 'http://192.168.1.205/dcallcenter'
web.open(url)
time.sleep(1)
#pg.typewrite('oun1982', interval=0.25)
#pg.press('tab')
#pg.typewrite('Cisco@1982', interval=0.25)_
#pg.press('enter')
pg.press(['tab', 'tab', 'tab'])
time.sleep(3)
pg.typewrite('osdadmin', interval=0.25)
pg.press('tab')
pg.typewrite('osd_SIP4321!', interval=0.25)
pg.press('enter')
time.sleep(2)
pg.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab'])
pg.press('enter')       
'''
#print(pg.position())
#pg.moveTo(735,390)
#pg.click()
#time.sleep(2)
#pg.press(['tab', 'tab'])
#time.sleep(2)
#pg.moveTo(735,367)

with open("D:\Oun1982\OSD_Work\CUSTOMER\CENTER AUTO LEASE\POC E1 Cisco\mobile.txt","r") as file:
    data = file.read()
    num = data.split("\n")
    x = 368
    y = 0
    z = 620
    sc = -50
    for i in num:
        print(x,y,z,sc)

        if y > 9:
            pg.scroll(sc)
            time.sleep(0.5)
            pg.moveTo(735, z)
            pg.click()
            time.sleep(1)
            pg.press(['tab', 'tab'])
            pg.typewrite(i, interval=0.05)
            pg.press('tab')
            pg.typewrite('1', interval=0.05)
            time.sleep(1)
            pg.moveTo(736, 322)
            pg.click()
            z = z + 3
            sc = sc - 50
            time.sleep(2)
        pg.moveTo(735, x)
        pg.click()
        time.sleep(1)
        pg.press(['tab', 'tab'])
        pg.typewrite(i, interval=0.1)
        pg.press('tab')
        pg.typewrite('1', interval=0.1)
        time.sleep(1)
        pg.moveTo(736, 322)
        pg.click()
        x = x + 30
        y = y + 1
        time.sleep(1)

#for num in range(len(file.readlines())):7
#    print(file[0])