from time import sleep
from tkinter import ttk
import tkinter as tk
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35, GPIO.OUT)
pwm35 = GPIO.PWM(35, 100)
pwm35.start(0)
dutyCycle = 0

motor1_ileri_pin = 38
motor1_geri_pin = 40
motor2_ileri_pin = 5
motor2_geri_pin = 3
motor3_ileri_pin = 11
motor3_geri_pin = 7

pin_list = [motor1_ileri_pin,motor1_geri_pin,motor2_ileri_pin,motor2_geri_pin,motor3_ileri_pin,motor3_geri_pin]
for i in pin_list:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 0)
'''/////////////////////////////Lock Page//////////////////////////////'''
def lockButton():
    winColor="#106181"
    win = tk.Toplevel(background=winColor)
    win.wm_title("Password")
    win.wm_attributes('-fullscreen', 'true')
    win.wm_attributes('-topmost', 'true')

    s = ttk.Style()
    s.configure('new.TFrame', background=winColor)
    winFrame = ttk.Frame(win, style='new.TFrame')
    winFrame.grid(column=0, row=1, sticky="nsew")

    def dele():
        e.delete(len(e.get()) - 1, tk.END)

    def passOk():
        if len(e.get()) == 4:
            if parola == e.get():
                root.wm_attributes('-fullscreen','true')
                root.wm_attributes('-topmost', 'true')
                win.destroy()
            elif parola_sys_exit == e.get():
                sys.exit(0)
            else:
                e.delete(0, tk.END)
        else:
            e.delete(0, tk.END)

    def limitSizeDay(*args):
        value = password.get()
        if len(value) > 3: password.set(value[:4])

    labelColor = "#51719c"
    parola = "1922"
    parola_sys_exit = "4269"
    password = tk.StringVar()  # Password variable
    password.trace('w', limitSizeDay)
    entryLabel = tk.Label(win, bg=labelColor)
    entryLabel.grid(row=0, column=0, sticky='ewns', columnspan=1)
    e = tk.Entry(entryLabel, textvariable=password, show='*', justify='center', width=20, font="Helvetica 44 bold",
                 bg=labelColor, foreground="black", highlightthickness=0, border=0)
    e.grid(column=0, row=0, sticky="nsew")

    buttoncolor=winColor
    b1 = tk.Button(winFrame, text="1", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "1"))
    b1.grid(column=0, row=0)

    b2 = tk.Button(winFrame, text="2",bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "2"))
    b2.grid(column=1, row=0)

    b3 = tk.Button(winFrame, text="3", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "3"))
    b3.grid(column=2, row=0)

    b4 = tk.Button(winFrame, text="4", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "4"))
    b4.grid(column=0, row=1)

    b5 = tk.Button(winFrame, text="5", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "5"))
    b5.grid(column=1, row=1)

    b6 = tk.Button(winFrame, text="6", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "6"))
    b6.grid(column=2, row=1)

    b7 = tk.Button(winFrame, text="7", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "7"))
    b7.grid(column=0, row=2)

    b8 = tk.Button(winFrame, text="8", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "8"))
    b8.grid(column=1, row=2)

    b9 = tk.Button(winFrame, text="9", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "9"))
    b9.grid(column=2, row=2)

    bok = tk.Button(winFrame, text="OK", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=passOk)
    bok.grid(column=0, row=3)

    b0 = tk.Button(winFrame, text="0", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                      font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "0"))
    b0.grid(column=1, row=3)

    bdel = tk.Button(winFrame, text="DEL", bg=buttoncolor, width=7, border=0, highlightthickness=0, activebackground=buttoncolor,
                      font="Helvetica 44 bold", command=dele)
    bdel.grid(column=2, row=3)

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=3)
    entryLabel.columnconfigure(0, weight=1)
    entryLabel.rowconfigure(0, weight=1)
    winFrame.columnconfigure(0, weight=2)
    winFrame.columnconfigure(1, weight=2)
    winFrame.columnconfigure(2, weight=2)
    winFrame.rowconfigure(0, weight=2)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=2)
    winFrame.rowconfigure(3, weight=2)

    win.config(cursor='none')


'''/////////////////////////////Home Position Page//////////////////////////////'''
def exit(event):
    root.destroy()

def homePos():
    GPIO.output(motor1_geri_pin, 1)
    GPIO.output(motor2_geri_pin, 1)
    GPIO.output(motor3_geri_pin, 1)
    global dutyCycle
    if dutyCycle < 20:
        x = 0.5
    else:
        x = (dutyCycle / 10) - 1.5
    for dc in range(dutyCycle, 15, -5):
        pwm35.ChangeDutyCycle(dc)
        sleep(0.5)
    dutyCycle = 0
    pwm35.ChangeDutyCycle(dutyCycle)
    sleep(12 - x)  # motorlar 12 saniye pwm max 8 saniye
    GPIO.output(motor1_geri_pin, 0)
    GPIO.output(motor2_geri_pin, 0)
    GPIO.output(motor3_geri_pin, 0)
    print("all positions going to zero")
def resetButton():
    winColor="#106181"
    bottomColor="#106181"
    yesColor="#51719c"
    noColor="#51719c"
    win = tk.Toplevel(background=winColor)
    win.wm_title("Home Position")
    w = 475
    h = 225
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.overrideredirect(True)
    win.wm_attributes('-topmost', 'true')
    win.grab_set()
    s = ttk.Style()
    s.configure('new.TFrame', background=winColor,highlightcolor=winColor,highlightthickness=3,bd=3)
    winFrame = ttk.Frame(win, style='new.TFrame')
    '''//////'''


    '''//////'''
    def yesButton():
        homePos()
        root.update()
        win.destroy()

    headLabel = tk.Label(winFrame, text="Reset Positions", bg=winColor)
    headLabel.config(font=("Courier", 14))
    textLabel = tk.Label(winFrame, text="Are you sure?",bg=winColor)
    textLabel.config(font=("Courier",11))

    yesLabel = tk.Label(winFrame, bg=bottomColor)
    yesLabel.grid(row=2, column=0, sticky='ewns', columnspan=1)
    b_yes = tk.Button(winFrame, image=check, bg=bottomColor, border=0, highlightthickness=0, activebackground=bottomColor, command=yesButton)

    noLabel = tk.Label(winFrame, bg=bottomColor)
    noLabel.grid(row=2, column=4, sticky='ewns', columnspan=1)
    b_no = tk.Button(winFrame, image = delete, bg=bottomColor, border=0, highlightthickness=0, activebackground=bottomColor, command=win.destroy)

    area1 = tk.Label(winFrame, bg=bottomColor)
    area1.grid(row=2, column=1, sticky='ewns', columnspan=1)
    area2 = tk.Label(winFrame, bg=bottomColor)
    area2.grid(row=2, column=2, sticky='ewns', columnspan=1)
    area3 = tk.Label(winFrame, bg=bottomColor)
    area3.grid(row=2, column=3, sticky='ewns', columnspan=1)
    '''//////////////////////////yes button events///////////////////////////////////'''

    def yesClick(event):
        yesLabel.configure(bg=yesColor)
        b_yes.configure(bg=yesColor, activebackground=yesColor)

    def yesRelease(event):
        yesLabel.configure(bg=bottomColor)
        b_yes.configure(bg=bottomColor, activebackground=bottomColor)
        yesButton()

    b_yes.bind("<ButtonPress>", yesClick)
    b_yes.bind("<ButtonRelease>", yesRelease)
    '''////////////////////////////no button events/////////////////////////////////'''
    def noClick(event):
        noLabel.configure(bg=noColor)
        b_no.configure(bg=noColor, activebackground=noColor)

    def noRelease(event):
        noLabel.configure(bg=bottomColor)
        b_no.configure(bg=bottomColor, activebackground=bottomColor)
        win.grab_release()
        win.destroy()

    b_no.bind("<ButtonPress>", noClick)
    b_no.bind("<ButtonRelease>", noRelease)
    '''////////////////////////////////////////////////////////////////'''

    winFrame.grid(column=0, row=0, sticky="nsew")
    headLabel.grid(row=0, column=2)
    textLabel.grid(row=1, column=2)
    b_yes.grid(row=2, column=0)
    b_no.grid(row=2, column=4)

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    winFrame.columnconfigure(0, weight=2)
    winFrame.columnconfigure(1, weight=0)
    winFrame.columnconfigure(2, weight=2)
    winFrame.columnconfigure(3, weight=0)
    winFrame.columnconfigure(4, weight=2)
    winFrame.rowconfigure(0, weight=2)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=2)

    win.config(cursor='none')
'''///////////////////////////tkinter config//////////////////////////////'''
root = tk.Tk()
root.title("EKMAY GUI")

color1 = '#f09609'
s = ttk.Style()
s.configure('new.TFrame', background=color1)
content = ttk.Frame(root, style='new.TFrame')
'''////////////////////////COLUMN COLORS///////////////////////////'''
'''column 0'''
col0Color = '#1ebbd7'
col0label0 = tk.Label(content, bg=col0Color)
col0label0.grid(row=0, column=0, sticky='ewns', columnspan=1)
col0label1 = tk.Label(content, bg=col0Color)
col0label1.grid(row=1, column=0, sticky='ewns', columnspan=1) # sticky='ew' expands the label horizontally
col0label2 = tk.Label(content, bg=col0Color)
col0label2.grid(row=2, column=0, sticky='ewns', columnspan=1)
col0label3 = tk.Label(content, bg=col0Color)
col0label3.grid(row=3, column=0, sticky='ewns', columnspan=1)
col0label4 = tk.Label(content, bg=col0Color)
col0label4.grid(row=4, column=0, sticky='ewns', columnspan=1)
'''column 1'''
col1Color = '#189ad3'
col1label0 = tk.Label(content, bg=col1Color)
col1label0.grid(row=0, column=1, sticky='ewns', columnspan=1)
col1label1 = tk.Label(content, bg=col1Color)
col1label1.grid(row=1, column=1, sticky='ewns', columnspan=1) # sticky='ew' expands the label horizontally
col1label2 = tk.Label(content, bg=col1Color)
col1label2.grid(row=2, column=1, sticky='ewns', columnspan=1)
col1label3 = tk.Label(content, bg=col1Color)
col1label3.grid(row=3, column=1, sticky='ewns', columnspan=1)
col1label4 = tk.Label(content, bg=col1Color)
col1label4.grid(row=4, column=1, sticky='ewns', columnspan=1)
'''column 2'''
col2Color = '#107dac'
col2row0 = tk.Label(content, bg=col2Color)
col2row0.grid(row=0, column=2, sticky='ewns', columnspan=1)
col2row1 = tk.Label(content, bg=col2Color)
col2row1.grid(row=1, column=2, sticky='ewns', columnspan=1)
col2row2 = tk.Label(content, bg=col2Color)
col2row2.grid(row=2, column=2, sticky='ewns', columnspan=1)
col2row3 = tk.Label(content, bg=col2Color)
col2row3.grid(row=3, column=2, sticky='ewns', columnspan=1)
col2row4 = tk.Label(content, bg=col2Color)
col2row4.grid(row=4, column=2, sticky='ewns', columnspan=1)
'''column 3'''
col3Color = '#189ad3'
col3label0 = tk.Label(content, bg=col3Color)
col3label0.grid(row=0, column=3, sticky='ewns', columnspan=1)
col3label1 = tk.Label(content, bg=col3Color)
col3label1.grid(row=1, column=3, sticky='ewns', columnspan=1) # sticky='ew' expands the label horizontally
col3label2 = tk.Label(content, bg=col3Color)
col3label2.grid(row=2, column=3, sticky='ewns', columnspan=1)
col3label3 = tk.Label(content, bg=col3Color)
col3label3.grid(row=3, column=3, sticky='ewns', columnspan=1)
col3label4 = tk.Label(content, bg=col3Color)
col3label4.grid(row=4, column=3, sticky='ewns', columnspan=1)
'''column 4'''
col4Color = '#1ebbd7'
col4label0 = tk.Label(content, bg=col4Color)
col4label0.grid(row=0, column=4, sticky='ewns', columnspan=1)
col4label1 = tk.Label(content, bg=col4Color)
col4label1.grid(row=1, column=4, sticky='ewns', columnspan=1) # sticky='ew' expands the label horizontally
col4label2 = tk.Label(content, bg=col4Color)
col4label2.grid(row=2, column=4, sticky='ewns', columnspan=1)
col4label3 = tk.Label(content, bg=col4Color)
col4label3.grid(row=3, column=4, sticky='ewns', columnspan=1)
col4label4 = tk.Label(content, bg=col4Color)
col4label4.grid(row=4, column=4, sticky='ewns', columnspan=1)
'''///////////////////// ICONS //////////////////////'''
pwm_add = tk.PhotoImage(file=r"add.png")
pwm_add = pwm_add.subsample(5, 5)

pwm_minus = tk.PhotoImage(file=r"minus.png")
pwm_minus = pwm_minus.subsample(5, 5)

arrow_up = tk.PhotoImage(file=r"up.png")
arrow_up = arrow_up.subsample(5, 5)

arrow_down = tk.PhotoImage(file=r"down.png")
arrow_down = arrow_down.subsample(5, 5)

motor1_icon = tk.PhotoImage(file=r"motor1.png")
motor1_icon = motor1_icon.subsample(4, 4)

motor2_icon = tk.PhotoImage(file=r"motor2.png")
motor2_icon = motor2_icon.subsample(4, 4)

motor3_icon = tk.PhotoImage(file=r"motor3.png")
motor3_icon = motor3_icon.subsample(4, 4)

motor4_icon = tk.PhotoImage(file=r"motor4.png")
motor4_icon = motor4_icon.subsample(4, 4)

reset_icon = tk.PhotoImage(file=r"reload-arrow.png")
reset_icon = reset_icon.subsample(5, 5)

check = tk.PhotoImage(file=r"check-button.png")
check = check.subsample(7, 7)

delete = tk.PhotoImage(file=r"cancel-button.png")
delete = delete.subsample(7, 7)

lock_icon = tk.PhotoImage(file=r"lock-icon.png")
lock_icon = lock_icon.subsample(5, 5)

ekmay_logo = tk.PhotoImage(file=r"ekmay-logo.png")
ekmay_logo = ekmay_logo.subsample(3, 3)

iconlbl1 = ttk.Label(content, image=motor1_icon, background=col0Color)
iconlbl2 = ttk.Label(content, image=motor2_icon, background=col1Color)
iconlbl3 = ttk.Label(content, image=motor3_icon, background=col3Color)
iconlbl4 = ttk.Label(content, image=motor4_icon, background=col4Color)
iconlbl5 = tk.Label(content, image=ekmay_logo, background=col2Color,height=100)
'''/////////////////// MOTOR 1 ////////////////////'''
motor1_ileri = tk.Button(content, image = arrow_up, bg=col0Color, border=0, highlightthickness=0, activebackground=col0Color)
motor1_geri = tk.Button(content, image = arrow_down, bg=col0Color, border=0, highlightthickness=0, activebackground=col0Color)
def motor1Ileri(event):
    global hold_on
    hold_on = True
    col0label1.configure(bg=color1)
    motor1_ileri.configure(bg=color1, activebackground=color1)
    GPIO.output(motor1_ileri_pin, 1)
def motor1Geri(event):
    global hold_on
    hold_on = True
    col0label3.configure(bg=color1)
    motor1_geri.configure(bg=color1, activebackground=color1)
    GPIO.output(motor1_geri_pin, 1)
def motor1Stop(event):
    global hold_on
    hold_on = False
    col0label3.configure(bg=col0Color)
    col0label1.configure(bg=col0Color)
    motor1_ileri.configure(bg=col0Color, activebackground=col0Color)
    motor1_geri.configure(bg=col0Color, activebackground=col0Color)
    GPIO.output(motor1_ileri_pin, 0)
    GPIO.output(motor1_geri_pin, 0)
motor1_ileri.bind("<ButtonPress>", motor1Ileri)
motor1_ileri.bind("<ButtonRelease>", motor1Stop)
motor1_geri.bind("<ButtonPress>", motor1Geri)
motor1_geri.bind("<ButtonRelease>", motor1Stop)
'''/////////////////// MOTOR 2 ////////////////////'''
motor2_ileri = tk.Button(content, image = arrow_up, bg=col1Color, border=0, highlightthickness=0, activebackground=col1Color)
motor2_geri = tk.Button(content, image = arrow_down, bg=col1Color, border=0, highlightthickness=0, activebackground=col1Color)
def motor2Ileri(event):
    global hold_on
    hold_on = True
    col1label1.configure(bg=color1)
    motor2_ileri.configure(bg=color1, activebackground=color1)
    GPIO.output(motor2_ileri_pin, 1)
def motor2Geri(event):
    global hold_on
    hold_on = True
    col1label3.configure(bg=color1)
    motor2_geri.configure(bg=color1, activebackground=color1)
    GPIO.output(motor2_geri_pin, 1)
def motor2Stop(event):
    global hold_on
    hold_on = False
    col1label3.configure(bg=col1Color)
    col1label1.configure(bg=col1Color)
    motor2_ileri.configure(bg=col1Color, activebackground=col1Color)
    motor2_geri.configure(bg=col1Color, activebackground=col1Color)
    GPIO.output(motor2_ileri_pin, 0)
    GPIO.output(motor2_geri_pin, 0)
motor2_ileri.bind("<ButtonPress>", motor2Ileri)
motor2_ileri.bind("<ButtonRelease>", motor2Stop)
motor2_geri.bind("<ButtonPress>", motor2Geri)
motor2_geri.bind("<ButtonRelease>", motor2Stop)
'''/////////////////// MOTOR 3 ////////////////////'''
motor3_ileri = tk.Button(content, image = arrow_up, bg=col3Color, border=0, highlightthickness=0, activebackground=col3Color)
motor3_geri = tk.Button(content, image = arrow_down, bg=col3Color, border=0, highlightthickness=0, activebackground=col3Color)
def motor3Ileri(event):
    global hold_on
    hold_on = True
    col3label1.configure(bg=color1)
    motor3_ileri.configure(bg=color1, activebackground=color1)
    GPIO.output(motor3_ileri_pin, 1)
def motor3Geri(event):
    global hold_on
    hold_on = True
    col3label3.configure(bg=color1)
    motor3_geri.configure(bg=color1, activebackground=color1)
    GPIO.output(motor3_geri_pin, 1)
def motor3Stop(event):
    global hold_on
    hold_on = False
    col3label3.configure(bg=col3Color)
    col3label1.configure(bg=col3Color)
    motor3_ileri.configure(bg=col3Color, activebackground=col3Color)
    motor3_geri.configure(bg=col3Color, activebackground=col3Color)
    GPIO.output(motor3_ileri_pin, 0)
    GPIO.output(motor3_geri_pin, 0)
motor3_ileri.bind("<ButtonPress>", motor3Ileri)
motor3_ileri.bind("<ButtonRelease>", motor3Stop)
motor3_geri.bind("<ButtonPress>", motor3Geri)
motor3_geri.bind("<ButtonRelease>", motor3Stop)
'''///////////////////////PWM BUTTONS///////////////////////////'''
pwm_up = tk.Button(content, image = pwm_add, bg=col4Color, border=0, highlightthickness=0, activebackground=col4Color)
pwm_down = tk.Button(content, image = pwm_minus, bg=col4Color, border=0, highlightthickness=0, activebackground=col4Color)
def pwmUpClick(event):
    col4label1.configure(bg=color1)
    pwm_up.configure(bg=color1, activebackground=color1)
def pwmDownClick(event):
    col4label3.configure(bg=color1)
    pwm_down.configure(bg=color1, activebackground=color1)
def pwmUpRelease(event):
    col4label1.configure(bg=col4Color)
    pwm_up.configure(bg=col4Color, activebackground=col4Color)
    global dutyCycle
    if dutyCycle > 95:
        dutyCycle = 100
    elif dutyCycle < 20:
        dutyCycle = 20
    else:
        dutyCycle = dutyCycle + 5
    pwm35.ChangeDutyCycle(dutyCycle)
    print(dutyCycle)
def pwmDownRelease(event):
    col4label3.configure(bg=col4Color)
    pwm_down.configure(bg=col4Color, activebackground=col4Color)
    global dutyCycle
    if dutyCycle <= 20:
        dutyCycle = 0
    else:
        dutyCycle = dutyCycle - 5
    pwm35.ChangeDutyCycle(dutyCycle)
    print(dutyCycle)
pwm_up.bind("<ButtonPress>", pwmUpClick)
pwm_up.bind("<ButtonRelease>", pwmUpRelease)
pwm_down.bind("<ButtonPress>", pwmDownClick)
pwm_down.bind("<ButtonRelease>", pwmDownRelease)
'''////////////////////////////////HOME BUTTON//////////////////////////////'''
home_button = tk.Button(content, image=reset_icon, bg=col2Color, border=0, highlightthickness=0, activebackground=col2Color)
def homeButtonClick(event):
    col2row2.configure(bg=color1)
    home_button.configure(bg=color1, activebackground=color1)
def homeButtonRelease(event):
    col2row2.configure(bg=col2Color)
    home_button.configure(bg=col2Color, activebackground=col2Color)
    resetButton()

home_button.bind("<ButtonPress>", homeButtonClick)
home_button.bind("<ButtonRelease>", homeButtonRelease)
'''////////////////////////////////LOCK BUTTON//////////////////////////////'''
lock_button = tk.Button(content, image=lock_icon, bg=col2Color, border=0, highlightthickness=0, activebackground=col2Color)
def lockButtonClick(event):
    col2row3.configure(bg=color1)
    lock_button.configure(bg=color1, activebackground=color1)
def lockButtonRelease(event):
    col2row3.configure(bg=col2Color)
    lock_button.configure(bg=col2Color, activebackground=col2Color)
    lockButton()
lock_button.bind("<ButtonPress>", lockButtonClick)
lock_button.bind("<ButtonRelease>", lockButtonRelease)
'''/////////////////////////CONFIGURATIONS///////////////////////////////'''
content.grid(column=0, row=0, sticky="nsew")
pwm_up.grid(column=4, row=1)
pwm_down.grid(column=4, row=3)
motor1_ileri.grid(column=0, row=1)
motor1_geri.grid(column=0, row=3)
motor2_ileri.grid(column=1, row=1)
motor2_geri.grid(column=1, row=3)
motor3_ileri.grid(column=3, row=1)
motor3_geri.grid(column=3, row=3)
iconlbl1.grid(column=0, row=2)
iconlbl2.grid(column=1, row=2)
iconlbl3.grid(column=3, row=2)
iconlbl4.grid(column=4, row=2)
iconlbl5.grid(column=2, row=1,sticky="ew")
home_button.grid(column=2, row=2)
lock_button.grid(column=2, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=3)
content.columnconfigure(4, weight=3)
content.rowconfigure(0, weight=2)
content.rowconfigure(1, weight=2)
content.rowconfigure(2, weight=2)
content.rowconfigure(3, weight=2)
content.rowconfigure(4, weight=2)

root.config(cursor='none')
root.bind("<Escape>", exit)
lockButton()
root.mainloop()