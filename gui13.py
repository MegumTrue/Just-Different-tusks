from tkinter import *
from tkinter import ttk
import math as mt
import numpy as np
rt = Tk()
rt.title(" Функции ")
rt.geometry("400x300")
rt.resizable(False, False)
rt.attributes("-fullscreen", False)



m = Menu()
rt.config(menu=m)


def sqrt(dx, x1, x2):
    points = []
    for i in range(x1, x2, dx):
        y = -mt.sqrt(1 + (i)**2)
        p = (i, y)
        points.append(p)
        print(p)
        rest = Text(wrap=points)
        rest.place(x=150, y = 20)


def sqrt3(dx,x2,x1):
    points = []
    for i in range(x1, x2, dx):
        y = (1+i)/(np.cbrt(1 + mt.exp(-0.2*i)) + 1)
        p = (i,y)
        points.append(p)
        print(p)
        rest = Text(wrap=points)
        rest.place(x=150, y = 20)

labx = Label(text="x1=")
labx.place(x=10, y = 45)
xx1 = StringVar()
en_adr = ttk.Entry(textvariable=xx1)
en_adr.insert(0, "1")
en_adr.place(x=35, y=45, width=30)

lab2 = Label(text="x2=")
lab2.place(x=10, y = 75)
xx2 = StringVar()
et_adr = ttk.Entry(textvariable=xx2)
et_adr.insert(0, "1")
et_adr.place(x=35, y=75, width=30)

labd = Label(text="dx=")
labd.place(x=10, y = 105)
dxx= StringVar()
nt_adr = ttk.Entry(textvariable=dxx)
nt_adr.insert(0, "1")
nt_adr.place(x=35, y=105, width=30)

x1 = int(xx1.get())
x2 = int(xx2.get())
dx = int(dxx.get())

fm = Menu(m)
m.add_cascade(label="Функции", menu=fm)
fm.add_command(label="y = sqrt(1 + x**2)", command=sqrt(dx, x1, x2))
fm.add_command(label="y = (1 + x) / sqrt3(1 + e**-x)", command=sqrt3(dx,x2,x1))

rt.mainloop()