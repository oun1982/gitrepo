__author__ = 'oun1982'

import tkinter
from tkinter import *
root = tkinter.Tk()
'''
for r in range(5):
    for c in range(5):
        tkinter.Label(root,text='Row[%s]/Col[%s]'%(r,c),borderwidth = 5)\

        .grid(row=r,column=c)
'''
CheckVar1 = StringVar()
CheckVar2 = IntVar()

def checkCallBack():
    C1.select()
    C2.toggle()
    print(CheckVar1.get())
    print(CheckVar2.get())

C1 = Checkbutton(root,text = "Music",variable = CheckVar1,onvalue = "on",offvalue = "off",height = 5,width = 20,command = checkCallBack)
C2 = Checkbutton(root,text = "Video",variable = CheckVar2,onvalue = 1,offvalue = 0,height = 5,width = 20,command = checkCallBack)
C1.pack()
C2.pack()
root.mainloop()



