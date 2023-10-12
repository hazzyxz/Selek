import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Act 1")
root.geometry("500x650")

def Calculation():
    abs1 = int(abs1entry.get())

    aas1 = int(aas1entry.get())
    aas2 = int(aas2entry.get())
    aas3 = int(aas3entry.get())
    aas4 = int(aas4entry.get())
    aas5 = int(aas5entry.get())

    ls1 = int(ls1entry.get())
    ls2 = int(ls2entry.get())

    ep1 = int(ep1entry.get())
    ep2 = int(ep2entry.get())
    ep3 = int(ep3entry.get())
    ep4 = int(ep4entry.get())

    mk = (abs1 + aas1 + aas2 + aas3 + aas4 + aas5 - ls1 - ls2)
    mk_label.config(text=f"{mk}")

    t1 = (aas1 + aas2 + aas3 + aas4 + aas5 )
    t1_label.config(text=f"{t1}")

    t2 = (aas1 + aas2 + aas3 + aas4 + aas5)
    t2_label.config(text=f"{t2}")

    ep5 = (ep1 + ep2 + ep3 + ep4)
    ep5_label.config(text=f"{ep5}")

abs_label = tk.Label(root, text="Illiquified Assets", font="arial 10 bold")
abs1_label = tk.Label(root, text="Equipment", font="arial 10")

aas_label = tk.Label(root, text="Liquified Assets", font="arial 10 bold")
aas1_label = tk.Label(root, text="Final inventory", font="arial 10")
aas2_label = tk.Label(root, text="Receivable accounts", font="arial 10")
aas3_label = tk.Label(root, text="Bank", font="arial 10")
aas4_label = tk.Label(root, text="Cash", font="arial 10")
aas5_label = tk.Label(root, text="Others", font="arial 10")

ls_label = tk.Label(root, text="Liabilities", font="arial 10 bold")
ls1_label = tk.Label(root, text="Accounts payable", font="arial 10")
ls2_label = tk.Label(root, text="Others", font="arial 10")
mk_label = tk.Label(root, text="Working Capital", font="arial 10 bold")

ep_label = tk.Label(root, text="Owner's Equity", font="arial 10 bold")
ep1_label = tk.Label(root, text="Initial capital", font="arial 10")
ep2_label = tk.Label(root, text="Additional capital", font="arial 10")
ep3_label = tk.Label(root, text="Profit / Loss", font="arial 10")
ep4_label = tk.Label(root, text="Amount you took", font="arial 10")
ep5_label = tk.Label(root, text="End capital", font="arial 10")

abs_label.place(x=50, y=20)
abs1_label.place(x=50, y=50)

aas_label.place(x=50, y=90)
aas1_label.place(x=50, y=120)
aas2_label.place(x=50, y=150)
aas3_label.place(x=50, y=180)
aas4_label.place(x=50, y=210)
aas5_label.place(x=50, y=240)

ls_label.place(x=50, y=280)
ls1_label.place(x=50, y=310)
ls2_label.place(x=50, y=340)
mk_label.place(x=50, y=370)

ep1_label.place(x=50, y=410)
ep2_label.place(x=50, y=440)
ep3_label.place(x=50, y=470)
ep4_label.place(x=50, y=500)
ep5_label.place(x=50, y=530)

abs1_value = StringVar()

aas1_value = StringVar()
aas2_value = StringVar()
aas3_value = StringVar()
aas4_value = StringVar()
aas5_value = StringVar()

ls1_value = StringVar()
ls2_value = StringVar()

ep1_value = StringVar()
ep2_value = StringVar()
ep3_value = StringVar()
ep4_value = StringVar()

abs1entry = Entry(root, textvariable=abs1_value, font="arial 13", width=8)

aas1entry = Entry(root, textvariable=aas1_value, font="arial 13", width=8)
aas2entry = Entry(root, textvariable=aas2_value, font="arial 13", width=8)
aas3entry = Entry(root, textvariable=aas3_value, font="arial 13", width=8)
aas4entry = Entry(root, textvariable=aas4_value, font="arial 13", width=8)
aas5entry = Entry(root, textvariable=aas5_value, font="arial 13", width=8)

ls1entry = Entry(root, textvariable=ls1_value, font="arial 13", width=8)
ls2entry = Entry(root, textvariable=ls2_value, font="arial 13", width=8)

ep1entry = Entry(root, textvariable=ep1_value, font="arial 13", width=8)
ep2entry = Entry(root, textvariable=ep2_value, font="arial 13", width=8)
ep3entry = Entry(root, textvariable=ep3_value, font="arial 13", width=8)
ep4entry = Entry(root, textvariable=ep4_value, font="arial 13", width=8)


abs1entry.place(x=350, y=50)

aas1entry.place(x=250, y=120)
aas2entry.place(x=250, y=150)
aas3entry.place(x=250, y=180)
aas4entry.place(x=250, y=210)
aas5entry.place(x=250, y=240)

ls1entry.place(x=250, y=310)
ls2entry.place(x=250, y=340)

ep1entry.place(x=350, y=410)
ep2entry.place(x=350, y=440)
ep3entry.place(x=350, y=470)
ep4entry.place(x=350, y=500)

mk_label = Label(root, text="", font="arial 13 bold")
mk_label.place(x=350, y=370)

t1_label = Label(root, text="", font="arial 13 bold")
t1_label.place(x=350, y=240)

t2_label = Label(root, text="", font="arial 13 bold")
t2_label.place(x=350, y=340)

ep5_label = Label(root, text="", font="arial 13 bold")
ep5_label.place(x=350, y=530)

Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=575)
Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.quit).place(x=350, y=575)

root.mainloop()
