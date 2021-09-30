from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title('Smart Calculator')
screen.geometry('520x470')
screen.minsize(width=423, height=470)
screen.maxsize(width=520, height=470)
screen.iconbitmap('my_passport.ico')

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)
def clear():
    global operator
    operator = ""
    tex.set(operator)
def equal():
    try:
        global operator
        operator = str(eval(operator))
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Not a Valid operation")
def cmsin():
    try:
        global operator
        operator = str(math.sin(eval(tex.get())))
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Not a Valid operation")
            
def cmcos():
    try:
        global operator
        operator = str(math.cos(eval(tex.get())))
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Not a Valid operation")

def cmtan():
    try:
        global operator
        operator = str(math.tan(eval(tex.get())))
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Not a Valid operation")

def cmsqrt():
    try:
        global operator
        operator = str(math.sqrt(eval(tex.get())))
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Not a Valid operation")

def cmlog():
    try:
        global operator
        operator = str(math.log(eval(tex.get())))
        tex.set(operator)
    except:
        messagebox.showinfo("Notification","Not a Valid operation")

tex = StringVar()
operator = ''

entry1 = Entry(screen, bg='#ccc', font=('Monospace', 25, 'bold'), bd='30', justify='right', textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(7), activebackground='#454cad', activeforeground='#fff')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(8), activebackground='#454cad', activeforeground='#fff')
btn8.grid(row=1,column=1)
btn9 = Button(screen,text='9', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(9), activebackground='#454cad', activeforeground='#fff')
btn9.grid(row=1,column=2)
btnadd = Button(screen,text='+', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click('+'), activebackground='#454cad', activeforeground='#fff')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(4), activebackground='#454cad', activeforeground='#fff')
btn4.grid(row=2,column=0)
btn5 = Button(screen,text='5', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(5), activebackground='#454cad', activeforeground='#fff')
btn5.grid(row=2,column=1)
btn6 = Button(screen,text='6', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(6), activebackground='#454cad', activeforeground='#fff')
btn6.grid(row=2,column=2)
btnsub = Button(screen,text='-', font=('Monospace',20,'bold'), bd='8', padx='20', pady=12, command=lambda:click('-'), activebackground='#454cad', activeforeground='#fff')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(1), activebackground='#454cad', activeforeground='#fff')
btn1.grid(row=3,column=0)
btn2 = Button(screen,text='2', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(2), activebackground='#454cad', activeforeground='#fff')
btn2.grid(row=3,column=1)
btn3 = Button(screen,text='3', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(3), activebackground='#454cad', activeforeground='#fff')
btn3.grid(row=3,column=2)
btnmul = Button(screen,text='*', font=('Monospace',20,'bold'), bd='8', padx='20', pady=12, command=lambda:click('*'), activebackground='#454cad', activeforeground='#fff')
btnmul.grid(row=3,column=3)

btn0 = Button(screen,text='0', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=lambda:click(0), activebackground='#454cad', activeforeground='#fff')
btn0.grid(row=4,column=0)
btnclear = Button(screen,text='C', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=clear, activebackground='#454cad', activeforeground='#fff')
btnclear.grid(row=4,column=1)
btnequal = Button(screen,text='=', font=('Monospace',20,'bold'), bd='8', padx='16', pady=12, command=equal, activebackground='#454cad', activeforeground='#fff')
btnequal.grid(row=4,column=2)
btndiv = Button(screen,text='/', font=('Monospace',20,'bold'), bd='8', padx='20', pady=12, command=lambda:click('/'), activebackground='#454cad', activeforeground='#fff')
btndiv.grid(row=4,column=3)
# scientific buttons
btnsin = Button(screen,text='sin', font=('Monospace',15,'bold'), bd='8', padx='16', pady=20, command=cmsin, activebackground='#454cad', activeforeground='#fff')
btnsin.grid(row=0,column=4)
btncos = Button(screen,text='cos', font=('Monospace',15,'bold'), bd='8', padx='13', pady=20, command=cmcos, activebackground='#454cad', activeforeground='#fff')
btncos.grid(row=1,column=4)
btntan = Button(screen,text='tan', font=('Monospace',15,'bold'), bd='8', padx='16', pady=20, command=cmtan, activebackground='#454cad', activeforeground='#fff')
btntan.grid(row=2,column=4)
btnsqrt = Button(screen,text='sqrt', font=('Monospace',15,'bold'), bd='8', padx='13', pady=20, command=cmsqrt, activebackground='#454cad', activeforeground='#fff')
btnsqrt.grid(row=3,column=4)
btnlog = Button(screen,text='log', font=('Monospace',15,'bold'), bd='8', padx='17', pady=20, command=cmlog, activebackground='#454cad', activeforeground='#fff')
btnlog.grid(row=4,column=4)

screen.mainloop()
