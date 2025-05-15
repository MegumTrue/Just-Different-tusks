from tkinter import *
from tkinter import ttk
import math as mt
import numpy as np
rt = Tk()
rt.title(" Функции ")
rt.geometry("600x600")
rt.resizable(False, False)
rt.attributes("-fullscreen", False)

canv = Canvas()
canv["height"] = 500
canv["width"] = 500
canv["background"] = "#eeeeff"
canv["borderwidth"] = 2
canv.place(x=100, y=100)

x0 = 50
x1 = 450
dx = 25
y0 = 250
ay = 250


y_a = []
yy = (x0+200,0)
y_a.append(yy)
yy= (x0+200, y0 + ay)
y_a.append(yy)
canv.create_line(y_a, fill="blue", smooth=1)

x_a = []
xx = (0, y0)
x_a.append(xx)
xx = (x1, y0)
x_a.append(xx)
canv.create_line(x_a, fill="blue", smooth=1)


m = Menu()
rt.config(menu=m)

def sqrt():
    dx = 25
    points = []
    for i in range(-50*dx, 60*dx, dx):
        y = -mt.sqrt(1 + (i)**2)
        p = (i + 250, y+250)
        points.append(p)
    canv.create_line(points, fill="black", smooth=1)

def sqrt3():
    dx = 25
    points = []
    for i in range(-50*dx, 50*dx, dx):
        y = (1+i)/(np.cbrt(1 + mt.exp(-0.2*i)) + 1)
        p = (i +250,y + 250)
        print(p)
        points.append(p)
    canv.create_line(points, fill="black", smooth=1)

adress = StringVar()
ent_adr = ttk.Entry(textvariable=adress)
ent_adr.place(x=25, y=40, width=30)

fm = Menu(m)
m.add_cascade(label="Функция", menu=fm)
fm.add_command(label="y = sqrt(1 + x**2)", command=sqrt)
fm.add_command(label="y = (1 + x) / sqrt3(1 + e**-x)", command=sqrt3)

rt.mainloop()