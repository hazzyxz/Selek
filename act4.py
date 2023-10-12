import tkinter
from tkinter import *

root=Tk()
root.title("Act 4")
root.geometry("500x400")

def Calculation():
    kt=int(ktentry.get())
    kbs=int(kbsentry.get())
    hj=int(hjentry.get())
    us = int(usentry.get())

    mcs=(hj-kbs)
    Label(text=f"{mcs}", font="arial 15 bold").place(x=250, y=210)

    jp=int(kt+us/mcs)
    Label(text=f"{jp}", font="arial 15 bold").place(x=250, y=250)


kt=Label(root, text="Fixed cost", font="arial 10")
kbs=Label(root, text="Current variable cost", font="arial 10")
hj=Label(root, text="Selling price per unit", font="arial 10")
us=Label(root, text="Target profit", font="arial 10")
mcs=Label(root, text="Contribution margin per unit", font="arial 10")
jp=Label(root, text="Units need to be sold", font="arial 10")

kt.place(x=50, y=20)
kbs.place(x=50, y=70)
hj.place(x=50, y=120)
us.place(x=50, y=170)
mcs.place(x=50, y=210)
jp.place(x=50, y=250)

ktvalue=StringVar()
kbsvalue=StringVar()
hjvalue=StringVar()
usvalue=StringVar()

ktentry=Entry(root, textvariable=ktvalue, font="arial 15", width=15)
kbsentry=Entry(root, textvariable=kbsvalue, font="arial 15", width=15)
hjentry=Entry(root, textvariable=hjvalue, font="arial 15", width=15)
usentry=Entry(root, textvariable=usvalue, font="arial 15", width=15)

ktentry.place(x=250, y=20)
kbsentry.place(x=250, y=70)
hjentry.place(x=250, y=120)
usentry.place(x=250, y=170)

Button(text="Calculate", font="arial 15", bg="white",bd=10, command=Calculation).place(x=50, y=300)
Button(text="Exit", font="arial 15", bg="white",bd=10, width=8, command=lambda:exit()).place(x=350, y=300)


root.mainloop()