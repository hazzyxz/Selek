import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Act 5")
root.geometry("600x575")

def Calculation():
    kj = int(kjentry.get())
    i1 = int(i1entry.get())
    i2 = int(i2entry.get())

    abb = int(abbentry.get())
    bk = int(bkentry.get())

    abt = int(abtentry.get())
    jk = int(jkentry.get())


    kpgi = (365 * (((i1 + i2) / 2) / kj))
    tk.Label(root, text=f"{kpgi}", font="arial 13 bold").place(x=450, y=140)

    tbh1 = ((abb / bk) * 365)
    tk.Label(root, text=f"{tbh1}", font="arial 13 bold").place(x=450, y=270)

    tkh1 = ((abt / jk) * 365)
    tk.Label(root, text=f"{tkh1}", font="arial 13 bold").place(x=450, y=390)

pn = tk.Label(root, text="Inventory change", font="arial 10 bold")
kj = tk.Label(root, text="Selling cost", font="arial 10")
i1 = tk.Label(root, text="Initial inventory", font="arial 10")
i2 = tk.Label(root, text="End inventory", font="arial 10")
kpgi0 = tk.Label(root, text="Time it takes for establishment to change inventory in days", font="arial 10")

tbh = tk.Label(root, text="Debt period for accounts payable", font="arial 10 bold")
abb = tk.Label(root, text="Accounts payable", font="arial 10")
bk = tk.Label(root, text="Credit purchases", font="arial 10")
tbh0= tk.Label(root, text="Time it takes for establishment to pay debt in days", font="arial 10")

tkh = tk.Label(root, text="Debt period for accounts receivable", font="arial 10 bold")
abt = tk.Label(root, text="Accounts receivable", font="arial 10")
jk = tk.Label(root, text="Credit sales", font="arial 10")
tkh0 = tk.Label(root, text="Time it takes for establishment to receive debt in days", font="arial 10")

pn.place(x=50, y=20)
kj.place(x=50, y=50)
i1.place(x=50, y=80)
i2.place(x=50, y=110)
kpgi0.place(x=50, y=140)

tbh.place(x=50, y=180)
abb.place(x=50, y=210)
bk.place(x=50, y=240)
tbh0.place(x=50, y=270)

tkh.place(x=50, y=300)
abt.place(x=50, y=330)
jk.place(x=50, y=360)
tkh0.place(x=50, y=390)


kjvalue = StringVar()
i1value = StringVar()
i2value = StringVar()

abbvalue = StringVar()
bkvalue = StringVar()

abtvalue = StringVar()
jkvalue = StringVar()

kjentry = Entry(root, textvariable=kjvalue, font="arial 13", width=8)
i1entry = Entry(root, textvariable=i1value, font="arial 13", width=8)
i2entry = Entry(root, textvariable=i2value, font="arial 13", width=8)

abbentry = Entry(root, textvariable=abbvalue, font="arial 13", width=8)
bkentry = Entry(root, textvariable=bkvalue, font="arial 13", width=8)

abtentry = Entry(root, textvariable=abtvalue, font="arial 13", width=8)
jkentry = Entry(root, textvariable=jkvalue, font="arial 13", width=8)

kjentry.place(x=450, y=50)
i1entry.place(x=450, y=80)
i2entry.place(x=450, y=110)

abbentry.place(x=450, y=210)
bkentry.place(x=450, y=240)

abtentry.place(x=450, y=330)
jkentry.place(x=450, y=360)

Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=475)
Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.quit).place(x=350, y=475)

root.mainloop()
