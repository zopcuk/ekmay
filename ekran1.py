from time import sleep
from threading import Thread
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
root = Tk()

root.geometry("1024x600")
root.minsize(1024, 600)
content = ttk.Frame(root, padding=(3, 3, 3, 3))
frame = ttk.Frame(content)

photo = PhotoImage(file=r"up-chevron.png")
photoimage = photo.subsample(3, 5)

def helloCallBack():
   print("pwm button")

B = Button(root, image = photoimage, command = helloCallBack).pack(side = LEFT , pady = 50)


button = Button(root, text="Button")
button.pack()

button2 = Button(root, text="Button2")
button2.pack()

def start(event):
    global hold_on
    hold_on = True
    while hold_on:
        print(hold_on)
        sleep(0.01)


def b2(event):
   global hold_on
   hold_on = True
   while hold_on:
      print("button2")
      sleep(0.01)

def end(event):
    global hold_on
    hold_on = False
    print(hold_on)


button.bind(
    "<ButtonPress>",
    lambda event: Thread(target=start, args=(event,)).start()
)
button.bind("<ButtonRelease>", end)


button2.bind(
    "<ButtonPress>",
    lambda event: Thread(target=b2, args=(event,)).start()
)
button2.bind("<ButtonRelease>", end)

'''
def pwmUp(event):
   print("pwm up")
pwm_up = tk.Label(content, image = pwm_add)
pwm_up.bind('<Button-1>', pwmUp)
def pwmDown(event):
   print("pwm down")
   pwm_down.configure(bg="green")
   pwm_down.configure()
pwm_down = tk.Label(content, image = pwm_minus)
pwm_down.bind('<ButtonRelease>', pwmDown)
'''

root.mainloop()