import tkinter
from tkinter import *

root=Tk()
root.title("Act 3")
root.geometry("500x400")

def Calculation():
    kt=int(ktentry.get())
    hj=int(hjentry.get())
    kbs=int(kbsentry.get())

    mcs=(hj-kbs)
    Label(text=f"{mcs}", font="arial 15 bold").place(x=270, y=170)

    mcs2=(kt/(hj-kbs))
    Label(text=f"{mcs2}", font="arial 15 bold").place(x=270, y=210)

    mcs1=int(mcs*hj)
    Label(text=f"{mcs1}", font="arial 15 bold").place(x=270, y=250)


kt=Label(root, text="Fixed cost", font="arial 10")
hj=Label(root, text="Selling price per unit", font="arial 10")
kbs=Label(root, text="Current variable cost", font="arial 10")
mcs=Label(root, text="Contribution margin per unit", font="arial 10")
mcs2=Label(root, text="Capital return point per unit in units ", font="arial 10")
mcs1=Label(root, text="Capital return point per unit in RM", font="arial 10")

kt.place(x=50, y=20)
hj.place(x=50, y=70)
kbs.place(x=50, y=120)
mcs.place(x=50, y=170)
mcs2.place(x=50, y=210)
mcs1.place(x=50, y=250)

ktvalue=StringVar()
hjvalue=StringVar()
kbsvalue=StringVar()

ktentry=Entry(root, textvariable=ktvalue, font="arial 15", width=15)
kbsentry=Entry(root, textvariable=kbsvalue, font="arial 15", width=15)
hjentry=Entry(root, textvariable=hjvalue, font="arial 15", width=15)


ktentry.place(x=250, y=20)
kbsentry.place(x=250, y=120)
hjentry.place(x=250, y=70)

Button(text="Calculate", font="arial 15", bg="white",bd=10, command=Calculation).place(x=50, y=300)
Button(text="Exit", font="arial 15", bg="white",bd=10, width=8, command=lambda:exit()).place(x=350, y=300)


root.mainloop()