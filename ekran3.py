from time import sleep
from threading import Thread
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk


root = tk.Tk()
color1 = '#607e9e'
root.geometry("1024x600")
root.minsize(750, 400)
s = ttk.Style()
s.configure('new.TFrame', background=color1)
content = ttk.Frame(root, padding=(3, 3, 3, 3), style='new.TFrame')
root.configure(bg=color1)

'''background_image=tk.PhotoImage(file=r"OLO2DM0.png")
background_label = tk.Label(content, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)'''
'''///////////////////// ICONS //////////////////////'''
pwm_add = tk.PhotoImage(file=r"add.png")
pwm_add = pwm_add.subsample(5, 5)

pwm_minus = tk.PhotoImage(file=r"minus.png")
pwm_minus = pwm_minus.subsample(5, 5)

arrow_up = tk.PhotoImage(file=r"up-arrow-in-square.png")
arrow_up = arrow_up.subsample(5, 5)

arrow_down = tk.PhotoImage(file=r"down-arrow-square.png")
arrow_down = arrow_down.subsample(5, 5)

motor1_icon = tk.PhotoImage(file=r"icons8-airbag-80.png")
motor1_icon = motor1_icon.subsample(1, 1)
namelbl1 = ttk.Label(content, image=motor1_icon, background=color1)

'''/////////////////// MOTOR 1 ////////////////////'''
motor1_ileri = tk.Button(content, image = arrow_up, bg=color1, border=0, activebackground=color1)
motor1_geri = tk.Button(content, image = arrow_down, bg=color1, border=0, activebackground=color1)
def motor1Ileri(event):
    global hold_on
    hold_on = True
    motor1_ileri.configure(image=arrow_down)
    while hold_on:
        print("motor 1 ileri")
        sleep(0.01)

def motor1Geri(event):
    global hold_on
    hold_on = True
    while hold_on:
       print("motor 1 geri")
       sleep(0.01)
def motor1Stop(event):
    global hold_on
    hold_on = False
    motor1_ileri.configure(image=arrow_up)
    print("motor 1 stop")
motor1_ileri.bind(
    "<ButtonPress>",
    lambda event: Thread(target=motor1Ileri, args=(event,)).start()
)
motor1_ileri.bind("<ButtonRelease>", motor1Stop)
motor1_geri.bind(
    "<ButtonPress>",
    lambda event: Thread(target=motor1Geri, args=(event,)).start()
)
motor1_geri.bind("<ButtonRelease>", motor1Stop)
'''///////////////////////PWM BUTTONS///////////////////////////'''
def pwmUp():
   print("pwm up")
pwm_up = tk.Button(content, image = pwm_add, command = pwmUp, bg=color1, border=0, activebackground=color1)

def pwmDown():
   print("pwm down")
pwm_down = tk.Button(content, image = pwm_minus, command = pwmDown, bg = color1, border = 0, activebackground=color1)
'''/////////////////////////CONFIGURATIONS///////////////////////////////'''
content.grid(column=0, row=0, sticky=(N, S, E, W))
pwm_up.grid(column=4, row=1)
pwm_down.grid(column=4, row=3)
motor1_ileri.grid(column=0, row=1)
motor1_geri.grid(column=0, row=3)
namelbl1.grid(column=0, row=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=2)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=4)
content.columnconfigure(4, weight=1)
content.rowconfigure(0, weight=0)
content.rowconfigure(1, weight=2)
content.rowconfigure(2, weight=2)
content.rowconfigure(3, weight=2)

root.mainloop()