from tkinter import *
import math

def print1():
    a = entry1.get()
    print(a)

def add_digit(digit):
    a = entry1.get()
    if a[0]=='0' and len(a)==1:
        a = a[1:]
    entry1.delete(0, END)
    entry1.insert(0, a + str(digit))

def solve():
    a = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, eval(a))

def add_oper(oper):
    a = entry1.get()
    if a[-1] in '+-*/':
        a = a[:-1]
    elif '+' in a or '-' in a or '*' in a or '/' in a:
        solve()
        a = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, a+oper)

def delit():
    entry1.delete(0, END)
    entry1.insert(0, '0')

root = Tk()
root.title("Калькулятор")
root['bg'] = 'black'
root.geometry(f"250x280")

button1 = Button(text = '1',font = 'arial 14', bd = 5, command = lambda : add_digit(1))
button2 = Button(text = '2',font = 'arial 14', bd = 5, command = lambda : add_digit(2))
button3 = Button(text = '3',font = 'arial 14', bd = 5, command = lambda : add_digit(3))
button4 = Button(text = '4',font = 'arial 14', bd = 5, command = lambda : add_digit(4))
button5 = Button(text = '5',font = 'arial 14', bd = 5, command = lambda : add_digit(5))
button6 = Button(text = '6',font = 'arial 14', bd = 5, command = lambda : add_digit(6))
button7 = Button(text = '7',font = 'arial 14', bd = 5, command = lambda : add_digit(7))
button8 = Button(text = '8',font = 'arial 14', bd = 5, command = lambda : add_digit(8))
button9 = Button(text = '9',font = 'arial 14', bd = 5, command = lambda : add_digit(9))
button0 = Button(text = '0',font = 'arial 14', bd = 5, command = lambda : add_digit(0))

button_plus = Button(text = '+', fg = 'red', font = 'arial 17', bd = 5, command = lambda : add_oper('+'))
button_mins = Button(text = '-', fg = 'red', font = 'arial 17', bd = 5, command = lambda : add_oper('-'))
button_umng = Button(text = '*', fg = 'red', font = 'arial 17', bd = 5, command = lambda : add_oper('*'))
button_deln = Button(text = '/', fg = 'red', font = 'arial 17', bd = 5, command = lambda : add_oper('/'))
button_rawn = Button(text = '=', fg = 'red', font = 'arial 17', bd = 5, command = solve)
button_C = Button(text = 'C', fg = 'red', font = 'arial 17', bd = 5, command = delit)

entry1  = Entry(justify = 'right', font = 'arial 15')
entry1.insert(0, '0')

entry1.grid(row = 0, column = 0, columnspan = 4, stick = 'we')
button1.grid(row = 3, column = 0, stick = 'wens', padx = 5, pady = 5)
button2.grid(row = 3, column = 1, stick = 'wens', padx = 5, pady = 5)
button3.grid(row = 3, column = 2, stick = 'wens', padx = 5, pady = 5)
button4.grid(row = 2, column = 0, stick = 'wens', padx = 5, pady = 5)
button5.grid(row = 2, column = 1, stick = 'wens', padx = 5, pady = 5)
button6.grid(row = 2, column = 2, stick = 'wens', padx = 5, pady = 5)
button7.grid(row = 1, column = 0, stick = 'wens', padx = 5, pady = 5)
button8.grid(row = 1, column = 1, stick = 'wens', padx = 5, pady = 5)
button9.grid(row = 1, column = 2, stick = 'wens', padx = 5, pady = 5)
button0.grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)
button_plus.grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)
button_mins.grid(row = 4, column = 3, stick = 'wens', padx = 5, pady = 5)
button_umng.grid(row = 2, column = 3, stick = 'wens', padx = 5, pady = 5)
button_deln.grid(row = 3, column = 3, stick = 'wens', padx = 5, pady = 5)
button_rawn.grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)
button_C.grid(row = 1, column = 3, stick = 'wens', padx = 5, pady = 5)

root.grid_columnconfigure(0, minsize = 60)
root.grid_columnconfigure(1, minsize = 60)
root.grid_columnconfigure(2, minsize = 60)
root.grid_columnconfigure(3, minsize = 60)
root.grid_rowconfigure(1, minsize = 60)
root.grid_rowconfigure(2, minsize = 60)
root.grid_rowconfigure(3, minsize = 60)
root.grid_rowconfigure(4, minsize = 60)

root.mainloop()