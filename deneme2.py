from tkinter import *

'''def show():
    p = password.get() #get password from entry
    print(p)


app = Tk()
password = StringVar() #Password variable
passEntry = Entry(app, textvariable=password, show='*').pack()
submit = Button(app, text='Show Console',command=show).pack()

app.mainloop()'''

from tkinter import *
from tkinter import ttk
def set_text(text):

    e.insert(0,text)
    return

win = Tk()
parola ="1212"
password = StringVar() #Password variable
e = ttk.Entry(win,textvariable=password, show='',width=10)
e.pack()

b1 = Button(win,text="animal",command=lambda:e.insert(END,"1"))
b1.pack()

b2 = Button(win,text="plant",command=lambda:e.insert(END,"2"))
b2.pack()
def dele():
    e.delete(len(e.get())-1,END)
b3 = Button(win,text="delete",command=dele)
b3.pack()
def passOk():
    if len(e.get())==4:
        if parola == e.get():
            print("parola doğru")
        else:
            print("parola yanlış")
    elif len(e.get())<4:
        print("yetersiz")
    elif len(e.get())>7:
        e.delete(0,END)
b4 = Button(win,text="ok",command=passOk)
b4.pack()
a = ["1","2"]

win.mainloop()