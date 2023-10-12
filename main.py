import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def actt1():

    root = tk.Toplevel()
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
        tk.Label(root,text=f"{mk}", font="arial 13 bold").place(x=350, y=370)

        t1 = (aas1 + aas2 + aas3 + aas4 + aas5)
        tk.Label(root,text=f"{t1}", font="arial 13 bold").place(x=350, y=240)

        t2 = (aas1 + aas2 + aas3 + aas4 + aas5)
        tk.Label(root,text=f"{t2}", font="arial 13 bold").place(x=350, y=340)

        ep5 = (ep1 + ep2 + ep3 + ep4)
        tk.Label(root,text=f"{ep5}", font="arial 13 bold").place(x=350, y=530)

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

    ep_label.place(x=50, y=410)
    ep1_label.place(x=50, y=440)
    ep2_label.place(x=50, y=470)
    ep3_label.place(x=50, y=500)
    ep4_label.place(x=50, y=530)
    ep5_label.place(x=50, y=560)

    abs1_value = tk.StringVar()

    aas1_value = tk.StringVar()
    aas2_value = tk.StringVar()
    aas3_value = tk.StringVar()
    aas4_value = tk.StringVar()
    aas5_value = tk.StringVar()

    ls1_value = tk.StringVar()
    ls2_value = tk.StringVar()

    ep1_value = tk.StringVar()
    ep2_value = tk.StringVar()
    ep3_value = tk.StringVar()
    ep4_value = tk.StringVar()

    abs1entry = tk.Entry(root, textvariable=abs1_value, font="arial 13", width=8)

    aas1entry = tk.Entry(root, textvariable=aas1_value, font="arial 13", width=8)
    aas2entry = tk.Entry(root, textvariable=aas2_value, font="arial 13", width=8)
    aas3entry = tk.Entry(root, textvariable=aas3_value, font="arial 13", width=8)
    aas4entry = tk.Entry(root, textvariable=aas4_value, font="arial 13", width=8)
    aas5entry = tk.Entry(root, textvariable=aas5_value, font="arial 13", width=8)

    ls1entry = tk.Entry(root, textvariable=ls1_value, font="arial 13", width=8)
    ls2entry = tk.Entry(root, textvariable=ls2_value, font="arial 13", width=8)

    ep1entry = tk.Entry(root, textvariable=ep1_value, font="arial 13", width=8)
    ep2entry = tk.Entry(root, textvariable=ep2_value, font="arial 13", width=8)
    ep3entry = tk.Entry(root, textvariable=ep3_value, font="arial 13", width=8)
    ep4entry = tk.Entry(root, textvariable=ep4_value, font="arial 13", width=8)

    abs1entry.place(x=350, y=50)

    aas1entry.place(x=250, y=120)
    aas2entry.place(x=250, y=150)
    aas3entry.place(x=250, y=180)
    aas4entry.place(x=250, y=210)
    aas5entry.place(x=250, y=240)

    ls1entry.place(x=250, y=310)
    ls2entry.place(x=250, y=340)

    ep1entry.place(x=350, y=440)
    ep2entry.place(x=350, y=470)
    ep3entry.place(x=350, y=500)
    ep4entry.place(x=350, y=530)

    tk.Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=590)
    tk.Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=350, y=590)

    root.mainloop()


####################_____________________

def actt2():
    root = tk.Toplevel()
    root.title("Act 2")
    root.geometry("500x500")

    def Calculation():
        ia = int(iaentry.get())
        il = int(ilentry.get())
        am = int(amentry.get())
        fa = int(faentry.get())
        fl = int(flentry.get())
        mt = int(mtentry.get())

        ic = (ia - il + mt)
        tk.Label(text=f"{ic}", font="arial 15 bold").place(x=250, y=140)

        fc = (fa - fl + am)
        tk.Label(text=f"{fc}", font="arial 15 bold").place(x=250, y=310)

        pol = int(fc - ic)
        tk.Label(text=f"{pol}", font="arial 15 bold").place(x=250, y=360)

    ia = tk.Label(root, text="Initial assets", font="arial 10")
    il = tk.Label(root, text="Initial liabilities", font="arial 10")
    am = tk.Label(root, text="Money taken (if any)", font="arial 10")
    ic = tk.Label(root, text="Initial capital", font="arial 10")
    fa = tk.Label(root, text="Final asset", font="arial 10")
    fl = tk.Label(root, text="Final liability", font="arial 10")
    mt = tk.Label(root, text="Captal added (if any)", font="arial 10")
    fc = tk.Label(root, text="Final capital", font="arial 10")
    pol = tk.Label(root, text="Profit / Loss", font="arial 10")

    ia.place(x=50, y=20)
    il.place(x=50, y=60)
    am.place(x=50, y=100)
    ic.place(x=50, y=140)
    fa.place(x=50, y=190)
    fl.place(x=50, y=230)
    mt.place(x=50, y=270)
    fc.place(x=50, y=310)
    pol.place(x=50, y=360)

    iavalue = tk.StringVar()
    ilvalue = tk.StringVar()
    amvalue = tk.StringVar()
    favalue = tk.StringVar()
    flvalue = tk.StringVar()
    mtvalue = tk.StringVar()

    iaentry = tk.Entry(root, textvariable=iavalue, font="arial 15", width=15)
    ilentry = tk.Entry(root, textvariable=ilvalue, font="arial 15", width=15)
    amentry = tk.Entry(root, textvariable=amvalue, font="arial 15", width=15)
    faentry = tk.Entry(root, textvariable=favalue, font="arial 15", width=15)
    flentry = tk.Entry(root, textvariable=flvalue, font="arial 15", width=15)
    mtentry = tk.Entry(root, textvariable=mtvalue, font="arial 15", width=15)

    iaentry.place(x=250, y=20)
    ilentry.place(x=250, y=60)
    amentry.place(x=250, y=100)
    faentry.place(x=250, y=190)
    flentry.place(x=250, y=230)
    mtentry.place(x=250, y=270)

    tk.Button(root,text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=400)
    tk.Button(root,text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=350, y=400)

    root.mainloop()

#################_________________________________

def actt3():
    root = tk.Toplevel()
    root.title("Act 3")
    root.geometry("500x400")

    def Calculation():
        kt = int(ktvalue.get())
        hj = int(hjvalue.get())
        kbs = int(kbsvalue.get())

        mcs = (hj - kbs)
        tk.Label(root, text=f"{mcs}", font="arial 15 bold").place(x=270, y=170)

        mcs2 = (kt / (hj - kbs))
        tk.Label(root, text=f"{mcs2}", font="arial 15 bold").place(x=270, y=210)

        mcs1 = int(mcs * hj)
        tk.Label(root, text=f"{mcs1}", font="arial 15 bold").place(x=270, y=250)

    kt = tk.Label(root, text="Fixed cost", font="arial 10")
    hj = tk.Label(root, text="Selling price per unit", font="arial 10")
    kbs = tk.Label(root, text="Current variable cost", font="arial 10")
    mcs = tk.Label(root, text="Contribution margin per unit", font="arial 10")
    mcs2 = tk.Label(root, text="Capital return point per unit in units ", font="arial 10")
    mcs1 = tk.Label(root, text="Capital return point per unit in RM", font="arial 10")

    kt.place(x=50, y=20)
    hj.place(x=50, y=70)
    kbs.place(x=50, y=120)
    mcs.place(x=50, y=170)
    mcs2.place(x=50, y=210)
    mcs1.place(x=50, y=250)

    ktvalue = tk.StringVar()
    hjvalue = tk.StringVar()
    kbsvalue = tk.StringVar()

    ktentry = tk.Entry(root, textvariable=ktvalue, font="arial 15", width=15)
    kbsentry = tk.Entry(root, textvariable=kbsvalue, font="arial 15", width=15)
    hjentry = tk.Entry(root, textvariable=hjvalue, font="arial 15", width=15)

    ktentry.place(x=250, y=20)
    kbsentry.place(x=250, y=120)
    hjentry.place(x=250, y=70)

    tk.Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=300)
    tk.Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=350, y=300)

    root.mainloop()

#############_________________________________________

def actt4():
    root = tk.Toplevel()
    root.title("Act 4")
    root.geometry("500x400")

    def Calculation():
        kt = int(ktentry.get())
        kbs = int(kbsentry.get())
        hj = int(hjentry.get())
        us = int(usentry.get())

        mcs = (hj - kbs)
        tk.Label(text=f"{mcs}", font="arial 15 bold").place(x=250, y=210)

        jp = int(kt + us / mcs)
        tk.Label(text=f"{jp}", font="arial 15 bold").place(x=250, y=250)

    kt = tk.Label(root, text="Fixed cost", font="arial 10")
    kbs = tk.Label(root, text="Current variable cost", font="arial 10")
    hj = tk.Label(root, text="Selling price per unit", font="arial 10")
    us = tk.Label(root, text="Target profit", font="arial 10")
    mcs = tk.Label(root, text="Contribution margin per unit", font="arial 10")
    jp = tk.Label(root, text="Units need to be sold", font="arial 10")

    kt.place(x=50, y=20)
    kbs.place(x=50, y=70)
    hj.place(x=50, y=120)
    us.place(x=50, y=170)
    mcs.place(x=50, y=210)
    jp.place(x=50, y=250)

    ktvalue = tk.StringVar()
    kbsvalue = tk.StringVar()
    hjvalue = tk.StringVar()
    usvalue = tk.StringVar()

    ktentry = tk.Entry(root, textvariable=ktvalue, font="arial 15", width=15)
    kbsentry = tk.Entry(root, textvariable=kbsvalue, font="arial 15", width=15)
    hjentry = tk.Entry(root, textvariable=hjvalue, font="arial 15", width=15)
    usentry = tk.Entry(root, textvariable=usvalue, font="arial 15", width=15)

    ktentry.place(x=250, y=20)
    kbsentry.place(x=250, y=70)
    hjentry.place(x=250, y=120)
    usentry.place(x=250, y=170)

    tk.Button(root,text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=300)
    tk.Button(root,text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=350, y=300)
    root.mainloop()

###################____________________________

def actt5():
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
    tbh0 = tk.Label(root, text="Time it takes for establishment to pay debt in days", font="arial 10")

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

    kjvalue = tk.StringVar()
    i1value = tk.StringVar()
    i2value = tk.StringVar()

    abbvalue = tk.StringVar()
    bkvalue = tk.StringVar()

    abtvalue = tk.StringVar()
    jkvalue = tk.StringVar()

    kjentry = tk.Entry(root, textvariable=kjvalue, font="arial 13", width=8)
    i1entry = tk.Entry(root, textvariable=i1value, font="arial 13", width=8)
    i2entry = tk.Entry(root, textvariable=i2value, font="arial 13", width=8)

    abbentry = tk.Entry(root, textvariable=abbvalue, font="arial 13", width=8)
    bkentry = tk.Entry(root, textvariable=bkvalue, font="arial 13", width=8)

    abtentry = tk.Entry(root, textvariable=abtvalue, font="arial 13", width=8)
    jkentry = tk.Entry(root, textvariable=jkvalue, font="arial 13", width=8)

    kjentry.place(x=450, y=50)
    i1entry.place(x=450, y=80)
    i2entry.place(x=450, y=110)

    abbentry.place(x=450, y=210)
    bkentry.place(x=450, y=240)

    abtentry.place(x=450, y=330)
    jkentry.place(x=450, y=360)

    tk.Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=475)
    tk.Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=350, y=475)

    root.mainloop()


###################___________________________-
window = tk.Tk()
window.geometry('500x500')
window.title('Multi windows')

button1 = ttk.Button(window, text='act 1: Statement of financial position', command=actt1)
button1.pack(expand=True)
button1.place(x=100, y=150)

button2 = ttk.Button(window, text='act 2: Profit or Loss', command=actt2)
button2.pack(expand=True)
button2.place(x=100, y=200)

button3 = ttk.Button(window, text='act 3: Capital return point', command=actt3)
button3.pack(expand=True)
button3.place(x=100, y=250)

button4 = ttk.Button(window, text='act 4: Profit model', command=actt4)
button4.pack(expand=True)
button4.place(x=100, y=300)

button5 = ttk.Button(window, text='act 5: Business model', command=actt5)
button5.pack(expand=True)
button5.place(x=100, y=350)

button_main=ttk.Button(text="Exit",  width=8, command=lambda:exit()).place(x=350, y=450)


window.mainloop()
