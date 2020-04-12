from time import sleep
from tkinter import ttk
import tkinter as tk
import sys
import lockPage2
import configparser
import threading
dutyCycle = 100
config = configparser.ConfigParser()
config.read('config.ini')
run_mode = config.get('section_a', 'run_mode') #if use pc write "pc" // if using raspberry write "rasp"
config.set("section_a", "dutyCycle", "{}".format(dutyCycle))
config.set("section_a", "show_hide", "0")
config.set("section_a", "lock_key", "0")
with open("config.ini", 'w') as configfile:
    config.write(configfile)
stop_threads = False
if run_mode == "rasp":
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(35, GPIO.OUT)
    pwm35 = GPIO.PWM(35, 100)
    pwm35.start(0)

    motor1_ileri_pin = 38
    motor1_geri_pin = 40
    motor2_ileri_pin = 5
    motor2_geri_pin = 3
    motor3_ileri_pin = 11
    motor3_geri_pin = 7

    pin_list = [motor1_ileri_pin, motor1_geri_pin, motor2_ileri_pin, motor2_geri_pin, motor3_ileri_pin, motor3_geri_pin]
    for i in pin_list:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, 0)
'''/////////////////////////////Lock Page//////////////////////////////'''


def lock_Button():
    winColor="#107dac"
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
        global stop_threads
        if len(e.get()) == 4:
            config.read('config.ini')
            parola = config.get('section_a', 'parola')
            if parola == e.get():
                root.wm_attributes('-fullscreen','true')
                root.wm_attributes('-topmost', 'true')
                win.destroy()
            elif parola_sys_exit == e.get():
                stop_threads = True
                sys.exit()
            else:
                e.delete(0, tk.END)
        else:
            e.delete(0, tk.END)

    def limitSizeDay(*args):
        value = password.get()
        if len(value) > 3: password.set(value[:4])

    def passChange():
        e.delete(0, tk.END)
        lockPage2.root_tk()
    labelColor = "#189ad3"
    #parola = config.get('section_a', 'parola')
    config.read('config.ini')
    parola_sys_exit = config.get('section_a', 'parola_sys_exit')
    password = tk.StringVar()  # Password variable
    password.trace('w', limitSizeDay)
    entryLabel = tk.Label(win, bg=labelColor)
    entryLabel.grid(row=0, column=0, sticky='ewns', columnspan=1)
    e = tk.Entry(entryLabel, textvariable=password, show='*', justify='center', width=20, font="Helvetica 44 bold",
                 bg=labelColor, foreground="black", highlightthickness=0, border=0)
    e.grid(column=1, row=0, sticky="nsew")
    b_pc = tk.Button(entryLabel, image=password_change, bg=labelColor, width=7, border=0, highlightthickness=0,
                     activebackground=labelColor, command=passChange)
    b_pc.grid(column=2, row=0, sticky="ewns", ipadx=15)
    b_pc_set = tk.Label(entryLabel,bg=labelColor, border=0)
    b_pc_set.grid(column=0, row=0,sticky="ewns", ipadx=40)
    buttoncolor = winColor
    b1 = tk.Button(winFrame, text="1", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "1"))
    b1.grid(column=1, row=0)

    b2 = tk.Button(winFrame, text="2", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "2"))
    b2.grid(column=2, row=0)

    b3 = tk.Button(winFrame, text="3", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "3"))
    b3.grid(column=3, row=0)

    b4 = tk.Button(winFrame, text="4", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "4"))
    b4.grid(column=1, row=1)

    b5 = tk.Button(winFrame, text="5", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "5"))
    b5.grid(column=2, row=1)

    b6 = tk.Button(winFrame, text="6", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "6"))
    b6.grid(column=3, row=1)

    b7 = tk.Button(winFrame, text="7", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "7"))
    b7.grid(column=1, row=2)

    b8 = tk.Button(winFrame, text="8", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "8"))
    b8.grid(column=2, row=2)

    b9 = tk.Button(winFrame, text="9", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "9"))
    b9.grid(column=3, row=2)

    bok = tk.Button(winFrame, image=okey, bg=buttoncolor, width=7, border=0, highlightthickness=0,
                    activebackground=buttoncolor, font="Helvetica 44 bold", command=passOk)
    bok.grid(column=1, row=3, sticky="ewns")

    b0 = tk.Button(winFrame, text="0", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor, font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "0"))
    b0.grid(column=2, row=3)

    bdel = tk.Button(winFrame, image=delete, bg=buttoncolor, width=7, border=0, highlightthickness=0,
                     activebackground=buttoncolor, font="Helvetica 44 bold", command=dele)
    bdel.grid(column=3, row=3, sticky="ewns")

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=3)
    entryLabel.columnconfigure(0, weight=1)
    entryLabel.columnconfigure(1, weight=4)
    entryLabel.columnconfigure(2, weight=3)
    entryLabel.rowconfigure(0, weight=1)

    winFrame.columnconfigure(0, weight=2)
    winFrame.columnconfigure(1, weight=2)
    winFrame.columnconfigure(2, weight=2)
    winFrame.columnconfigure(3, weight=2)
    winFrame.columnconfigure(4, weight=2)
    winFrame.rowconfigure(0, weight=2)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=2)
    winFrame.rowconfigure(3, weight=2)

    if run_mode == "rasp":
        win.config(cursor='none')

'''/////////////////////////////Home Position Page//////////////////////////////'''


def exit(event):
    global stop_threads
    stop_threads = True
    root.destroy()


def homePos():
    global dutyCycle
    if run_mode == "rasp":
        GPIO.output(motor1_geri_pin, 1)
        GPIO.output(motor2_geri_pin, 1)
        GPIO.output(motor3_geri_pin, 1)
        config.read('config.ini')
        dutyCycle = config.getint('section_a', 'dutyCycle')
        if dutyCycle < 20:
            x = 0.5
        else:
            x = (dutyCycle / 10) - 1.5
        for dc in range(dutyCycle, 15, -5):
            pwm35.ChangeDutyCycle(dc)
            sleep(0.5)
        config.set("section_a", "dutyCycle", "0")
        with open("config.ini", 'w') as configfile:
            config.write(configfile)
        pwm35.ChangeDutyCycle(0)
        sleep(20 - x)
        GPIO.output(motor1_geri_pin, 0)
        GPIO.output(motor2_geri_pin, 0)
        GPIO.output(motor3_geri_pin, 0)
    elif run_mode == "pc":
        print("all positions going to zero")


def resetButton():
    winColor = "#106181"
    bottomColor = "#106181"
    yesColor = "#51719c"
    noColor = "#51719c"
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
    s.configure('new.TFrame', background=winColor, highlightcolor=winColor, highlightthickness=3, bd=3)
    winFrame = ttk.Frame(win, style='new.TFrame')
    '''//////////////////////////////////'''
    def yesButton():
        global dutyCycle
        textLabel.configure(text="Please wait..!", foreground=color1)
        win.update()
        homePos()
        config.read('config.ini')
        dutyCycle = config.getint("section_a", "dutyCycle")
        col4label0text.configure(text="%{}".format(dutyCycle))
        win.destroy()

    headLabel = tk.Label(winFrame, text="Reset Positions", bg=winColor, font="Courier 18")
    textLabel = tk.Label(winFrame, text="Are you sure?", bg=winColor, font="Courier 16")

    yesLabel = tk.Label(winFrame, bg=bottomColor)
    yesLabel.grid(row=2, column=0, sticky='ewns', columnspan=1)
    b_yes = tk.Button(winFrame, image=check, bg=bottomColor, border=0, highlightthickness=0,
                      activebackground=bottomColor, command=yesButton)

    noLabel = tk.Label(winFrame, bg=bottomColor)
    noLabel.grid(row=2, column=4, sticky='ewns', columnspan=1)
    b_no = tk.Button(winFrame, image=cancel, bg=bottomColor, border=0, highlightthickness=0,
                     activebackground=bottomColor, command=win.destroy)

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

    if run_mode == "rasp":
        win.config(cursor='none')
'''/////////////////////////////lock therad///////////////////////////////'''


def App():
    global stop_threads
    try:
        while True:
            config.read('config.ini')
            lock_key = config.get('section_a', 'lock_key')
            sleep(.08)
            if stop_threads:
                break
            if lock_key == "1":
                lock_Button()
                config.set("section_a", "lock_key", "0")
                with open("config.ini", 'w') as configfile:
                    config.write(configfile)
    except:
        pass

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
col0label1.grid(row=1, column=0, sticky='ewns', columnspan=1)
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
col1label1.grid(row=1, column=1, sticky='ewns', columnspan=1)
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
col3label1.grid(row=1, column=3, sticky='ewns', columnspan=1)
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
col4label0.columnconfigure(0, weight=1)
col4label0.rowconfigure(0, weight=1)
col4label0text = tk.Label(col4label0, bg=color1, text="%{}".format(dutyCycle), highlightthickness=0,
                          font="Helvetica 24", foreground="#1c1c1c", border=0, width=6)
col4label0text.grid(column=0, row=0)
col4label1 = tk.Label(content, bg=col4Color)
col4label1.grid(row=1, column=4, sticky='ewns', columnspan=1)
col4label2 = tk.Label(content, bg=col4Color)
col4label2.grid(row=2, column=4, sticky='ewns', columnspan=1)
col4label3 = tk.Label(content, bg=col4Color)
col4label3.grid(row=3, column=4, sticky='ewns', columnspan=1)
col4label4 = tk.Label(content, bg=col4Color)
col4label4.grid(row=4, column=4, sticky='ewns', columnspan=1, ipady=15)

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

cancel = tk.PhotoImage(file=r"cancel-button.png")
cancel = cancel.subsample(7, 7)

lock_icon = tk.PhotoImage(file=r"lock-icon.png")
lock_icon = lock_icon.subsample(2, 2)

info_icon = tk.PhotoImage(file=r"info_icon.png")
info_icon = info_icon.subsample(1, 1)

ekmay_logo = tk.PhotoImage(file=r"lifewalk.png")
ekmay_logo = ekmay_logo.subsample(1, 1)

okey = tk.PhotoImage(file=r"checkbox.png")
okey = okey.subsample(6, 6)

delete = tk.PhotoImage(file=r"delete.png")
delete = delete.subsample(5, 5)

password_change = tk.PhotoImage(file=r"password-change3.png")
password_change = password_change.subsample(4, 4)

iconlbl1 = ttk.Label(content, image=motor1_icon, background=col0Color)
iconlbl2 = ttk.Label(content, image=motor2_icon, background=col1Color)
iconlbl3 = ttk.Label(content, image=motor3_icon, background=col3Color)
iconlbl4 = ttk.Label(content, image=motor4_icon, background=col4Color)
iconlbl5 = tk.Label(content, image=ekmay_logo, background=col2Color, height=100)
'''/////////////////// MOTOR 1 ////////////////////'''
motor1_ileri = tk.Button(content, image=arrow_up, bg=col0Color, border=0, highlightthickness=0,
                         activebackground=col0Color)
motor1_geri = tk.Button(content, image=arrow_down, bg=col0Color, border=0, highlightthickness=0,
                        activebackground=col0Color)


def motor1Ileri(event):
    col0label1.configure(bg=color1)
    motor1_ileri.configure(bg=color1, activebackground=color1)
    if run_mode == "rasp":
        GPIO.output(motor1_ileri_pin, 1)
    elif run_mode == "pc":
        print("motor1 ileri")


def motor1Geri(event):
    col0label3.configure(bg=color1)
    motor1_geri.configure(bg=color1, activebackground=color1)
    if run_mode == "rasp":
        GPIO.output(motor1_geri_pin, 1)
    elif run_mode == "pc":
        print("motor1 geri")


def motor1Stop(event):
    col0label3.configure(bg=col0Color)
    col0label1.configure(bg=col0Color)
    motor1_ileri.configure(bg=col0Color, activebackground=col0Color)
    motor1_geri.configure(bg=col0Color, activebackground=col0Color)
    if run_mode == "rasp":
        GPIO.output(motor1_ileri_pin, 0)
        GPIO.output(motor1_geri_pin, 0)
    elif run_mode == "pc":
        print("motor1 stop")


motor1_ileri.bind("<ButtonPress>", motor1Ileri)
motor1_ileri.bind("<ButtonRelease>", motor1Stop)
motor1_geri.bind("<ButtonPress>", motor1Geri)
motor1_geri.bind("<ButtonRelease>", motor1Stop)
'''/////////////////// MOTOR 2 ////////////////////'''
motor2_ileri = tk.Button(content, image=arrow_up, bg=col1Color, border=0, highlightthickness=0,
                         activebackground=col1Color)
motor2_geri = tk.Button(content, image=arrow_down, bg=col1Color, border=0, highlightthickness=0,
                        activebackground=col1Color)


def motor2Ileri(event):
    col1label1.configure(bg=color1)
    motor2_ileri.configure(bg=color1, activebackground=color1)
    if run_mode == "rasp":
        GPIO.output(motor2_ileri_pin, 1)
    elif run_mode == "pc":
        print("motor2 ileri")


def motor2Geri(event):
    col1label3.configure(bg=color1)
    motor2_geri.configure(bg=color1, activebackground=color1)
    if run_mode == "rasp":
        GPIO.output(motor2_geri_pin, 1)
    elif run_mode == "pc":
        print("motor2 geri")


def motor2Stop(event):
    col1label3.configure(bg=col1Color)
    col1label1.configure(bg=col1Color)
    motor2_ileri.configure(bg=col1Color, activebackground=col1Color)
    motor2_geri.configure(bg=col1Color, activebackground=col1Color)
    if run_mode == "rasp":
        GPIO.output(motor2_ileri_pin, 0)
        GPIO.output(motor2_geri_pin, 0)
    elif run_mode == "pc":
        print("motor2 stop")


motor2_ileri.bind("<ButtonPress>", motor2Ileri)
motor2_ileri.bind("<ButtonRelease>", motor2Stop)
motor2_geri.bind("<ButtonPress>", motor2Geri)
motor2_geri.bind("<ButtonRelease>", motor2Stop)
'''/////////////////// MOTOR 3 ////////////////////'''
motor3_ileri = tk.Button(content, image=arrow_up, bg=col3Color, border=0, highlightthickness=0,
                         activebackground=col3Color)
motor3_geri = tk.Button(content, image=arrow_down, bg=col3Color, border=0, highlightthickness=0,
                        activebackground=col3Color)


def motor3Ileri(event):
    col3label1.configure(bg=color1)
    motor3_ileri.configure(bg=color1, activebackground=color1)
    if run_mode == "rasp":
        GPIO.output(motor3_ileri_pin, 1)
    elif run_mode == "pc":
        print("motor3 ileri")


def motor3Geri(event):
    col3label3.configure(bg=color1)
    motor3_geri.configure(bg=color1, activebackground=color1)
    if run_mode == "rasp":
        GPIO.output(motor3_geri_pin, 1)
    elif run_mode == "pc":
        print("motor3 geri")


def motor3Stop(event):
    col3label3.configure(bg=col3Color)
    col3label1.configure(bg=col3Color)
    motor3_ileri.configure(bg=col3Color, activebackground=col3Color)
    motor3_geri.configure(bg=col3Color, activebackground=col3Color)
    if run_mode == "rasp":
        GPIO.output(motor3_ileri_pin, 0)
        GPIO.output(motor3_geri_pin, 0)
    elif run_mode == "pc":
        print("motor3 stop")


motor3_ileri.bind("<ButtonPress>", motor3Ileri)
motor3_ileri.bind("<ButtonRelease>", motor3Stop)
motor3_geri.bind("<ButtonPress>", motor3Geri)
motor3_geri.bind("<ButtonRelease>", motor3Stop)
'''///////////////////////PWM BUTTONS///////////////////////////'''
pwm_up = tk.Button(content, image=pwm_add, bg=col4Color, border=0, highlightthickness=0, activebackground=col4Color)
pwm_down = tk.Button(content, image=pwm_minus, bg=col4Color, border=0, highlightthickness=0, activebackground=col4Color)


def pwmUpClick(event):
    col4label1.configure(bg=color1)
    pwm_up.configure(bg=color1, activebackground=color1)


def pwmDownClick(event):
    col4label3.configure(bg=color1)
    pwm_down.configure(bg=color1, activebackground=color1)


def pwmUpRelease(event):
    col4label1.configure(bg=col4Color)
    pwm_up.configure(bg=col4Color, activebackground=col4Color)
    if run_mode == "rasp":
        config.read('config.ini')
        dutyCycle = config.getint("section_a", "dutyCycle")
        if dutyCycle > 95:
            config.set("section_a", "dutyCycle", "100")
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
        elif dutyCycle < 25:
            config.set("section_a", "dutyCycle", "25")
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
        else:
            dutyCycle = dutyCycle + 5
            config.set("section_a", "dutyCycle", "{}".format(dutyCycle))
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
        config.read('config.ini')
        dutyCycle = config.getint("section_a", "dutyCycle")
        pwm35.ChangeDutyCycle(dutyCycle)
        col4label0text.configure(text="%{}".format(dutyCycle))
    elif run_mode == "pc":
        print("pwmup release")


def pwmDownRelease(event):
    col4label3.configure(bg=col4Color)
    pwm_down.configure(bg=col4Color, activebackground=col4Color)
    if run_mode == "rasp":
        config.read('config.ini')
        dutyCycle = config.getint("section_a", "dutyCycle")
        if dutyCycle <= 25:
            config.set("section_a", "dutyCycle", "0")
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
        else:
            dutyCycle = dutyCycle - 5
            config.set("section_a", "dutyCycle", "{}".format(dutyCycle))
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
        config.read('config.ini')
        dutyCycle = config.getint("section_a", "dutyCycle")
        pwm35.ChangeDutyCycle(dutyCycle)
        col4label0text.configure(text="%{}".format(dutyCycle))
    elif run_mode == "pc":
        print("pwmdown release")


pwm_up.bind("<ButtonPress>", pwmUpClick)
pwm_up.bind("<ButtonRelease>", pwmUpRelease)
pwm_down.bind("<ButtonPress>", pwmDownClick)
pwm_down.bind("<ButtonRelease>", pwmDownRelease)
'''////////////////////////////////HOME BUTTON//////////////////////////////'''
home_button = tk.Button(content, image=reset_icon, bg=col2Color, border=0, highlightthickness=0,
                        activebackground=col2Color)


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
    lock_Button()


lock_button.bind("<ButtonPress>", lockButtonClick)
lock_button.bind("<ButtonRelease>", lockButtonRelease)
'''///////////////////////////INFO BUTTON////////////////////////////////'''
info_button = tk.Button(content, image=info_icon, bg=col2Color, border=0, highlightthickness=0,
                        activebackground=col2Color)


def infoButtonClick(event):
    col2row0.configure(bg=color1)
    info_button.configure(bg=color1, activebackground=color1)


def infoButtonRelease(event):
    col2row0.configure(bg=col2Color)
    info_button.configure(bg=col2Color, activebackground=col2Color)
    config.set("section_a", "show_hide", "1")
    with open("config.ini", 'w') as configfile:
        config.write(configfile)


info_button.bind("<ButtonPress>", infoButtonClick)
info_button.bind("<ButtonRelease>", infoButtonRelease)
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
iconlbl5.grid(column=2, row=1, sticky="snew")
home_button.grid(column=2, row=2)
lock_button.grid(column=2, row=3)
info_button.grid(column=2, row=0, sticky="snew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=3)
content.columnconfigure(4, weight=3)
content.rowconfigure(0, weight=3)
content.rowconfigure(1, weight=3)
content.rowconfigure(2, weight=3)
content.rowconfigure(3, weight=3)
content.rowconfigure(4, weight=3)

if run_mode == "rasp":
    root.config(cursor='none')
root.bind("<Escape>", exit)

lock_Button()
APP = threading.Thread(target=App)
APP.start()
root.mainloop()