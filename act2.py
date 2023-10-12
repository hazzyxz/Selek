import tkinter
from tkinter import *

root=Tk()
root.title("Act 2")
root.geometry("500x500")

def Calculation():
    ia=int(iaentry.get())
    il=int(ilentry.get())
    am = int(amentry.get())
    fa=int(faentry.get())
    fl=int(flentry.get())
    mt= int(mtentry.get())

    ic=(ia-il+mt)
    Label(text=f"{ic}", font="arial 15 bold").place(x=250, y=140)

    fc=(fa-fl+am)
    Label(text=f"{fc}", font="arial 15 bold").place(x=250, y=310)

    pol=int(fc-ic)
    Label(text=f"{pol}", font="arial 15 bold").place(x=250, y=360)


ia=Label(root, text="Initial assets", font="arial 10")
il=Label(root, text="Initial liabilities", font="arial 10")
am=Label(root, text="Money taken (if any)", font="arial 10")
ic=Label(root, text="Initial capital", font="arial 10")
fa=Label(root, text="Final asset", font="arial 10")
fl=Label(root, text="Final liability", font="arial 10")
mt=Label(root, text="Captal added (if any)", font="arial 10")
fc=Label(root, text="Final capital", font="arial 10")
pol=Label(root, text="Profit / Loss", font="arial 10")

ia.place(x=50, y=20)
il.place(x=50, y=60)
am.place(x=50, y=100)
ic.place(x=50, y=140)
fa.place(x=50, y=190)
fl.place(x=50, y=230)
mt.place(x=50, y=270)
fc.place(x=50, y=310)
pol.place(x=50, y=360)

iavalue=StringVar()
ilvalue=StringVar()
amvalue=StringVar()
favalue=StringVar()
flvalue=StringVar()
mtvalue=StringVar()

iaentry=Entry(root, textvariable=iavalue, font="arial 15", width=15)
ilentry=Entry(root, textvariable=ilvalue, font="arial 15", width=15)
amentry=Entry(root, textvariable=amvalue, font="arial 15", width=15)
faentry=Entry(root, textvariable=favalue, font="arial 15", width=15)
flentry=Entry(root, textvariable=flvalue, font="arial 15", width=15)
mtentry=Entry(root, textvariable=mtvalue, font="arial 15", width=15)

iaentry.place(x=250, y=20)
ilentry.place(x=250, y=60)
amentry.place(x=250, y=100)
faentry.place(x=250, y=190)
flentry.place(x=250, y=230)
mtentry.place(x=250, y=270)

Button(text="Calculate", font="arial 15", bg="white",bd=10, command=Calculation).place(x=50, y=400)
Button(text="Exit", font="arial 15", bg="white",bd=10, width=8, command=lambda:exit()).place(x=350, y=400)


root.mainloop()