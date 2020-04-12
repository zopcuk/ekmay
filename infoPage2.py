from tkinter import ttk
import tkinter as tk
import configparser
import threading
from time import sleep
config = configparser.ConfigParser()
config.read('config.ini')
dutyCycle = 0
stepinone = 0.8 #meter in 1 step
step = 0
distance = 0
s = 0
m = 0
h = 0
total_s = config.getint("section_a", "total_s")
total_m = config.getint("section_a", "total_m")
total_h = config.getint("section_a", "total_h")
config.set("section_a", "show_hide", "0")
l = threading.Lock()
def App():
    global step
    global distance
    speed_value = 0
    global dutyCycle
    try:
        while True:
            l.acquire()
            config.read('config.ini')
            dutyCycle = config.getint('section_a', 'dutyCycle')
            l.release()
            if dutyCycle > 0:
                stepinfoValue.configure(text=step)
                step = step + 1

                distanceinfoValue.configure(text="{:.1f} meter".format(distance))
                distance = distance + stepinone

                speedinfoValue.configure(text="{:.2f} km/h".format(speed_value))
                speed_value = ((stepinone * 2) / 1000) / ((100 / dutyCycle) / (60 * 60))

                sleep((100 / dutyCycle) / 2)
            else:
                sleep(.5)
    except:
        pass


def App2():
    global dutyCycle, s, m, h, total_h, total_m, total_s
    try:
        while True:
            l.acquire()
            config.read('config.ini')
            dutyCycle = config.getint('section_a', 'dutyCycle')
            l.release()
            bottomLabel.configure(text=("Total Time = {:0>2d}:{:0>2d}:{:0>2d}".format(total_h, total_m, total_s)))
            total_s = total_s + 1
            config.set("section_a", "total_s", "{}".format(total_s))
            if total_s >= 60:
                total_s = 0
                config.set("section_a", "total_s", "{}".format(total_s))
                total_m = total_m + 1
                config.set("section_a", "total_m", "{}".format(total_m))
                if total_m >= 60:
                    total_m = 0
                    config.set("section_a", "total_m", "{}".format(total_m))
                    total_h = total_h + 1
                    config.set("section_a", "total_h", "{}".format(total_h))
            l.acquire()
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
            l.release()
            if dutyCycle > 0:
                timeinfoValue.configure(text=("{:0>2d}:{:0>2d}:{:0>2d}".format(h, m, s)))
                s = s+1
                if s >= 60:
                    s = 0
                    m = m+1
                    if m >= 60:
                        m = 0
                        h = h+1
            sleep(1)
    except:
        pass


def App3():
    info.withdraw()
    try:
        while True:
            sleep(.1)
            l.acquire()
            config.read('config.ini')
            show_hide = config.get('section_a', 'show_hide')
            l.release()
            if show_hide == "1":
                info.deiconify()
                config.set("section_a", "show_hide", "0")
                with open("config.ini", 'w') as configfile:
                    config.write(configfile)
    except:
        pass


def exit(event):
    info.destroy()


def hide_root():
    config.set("section_a", "show_hide", "0")
    info.withdraw()
    with open("config.ini", 'w') as configfile:
        config.write(configfile)


def lock_key():
    config.set("section_a", "lock_key", "1")
    config.set("section_a", "show_hide", "0")
    info.withdraw()
    with open("config.ini", 'w') as configfile:
        config.write(configfile)


def step_reset(event):
    global step
    step = 0


def distance_reset(event):
    global distance
    distance = 0


def time_reset(event):
    global s, m, h
    s = m = h = 0


info = tk.Tk()
info.title("INFO")
info.wm_attributes('-fullscreen', 'true')
info.wm_attributes('-topmost', 'true')
info.columnconfigure(0, weight=1)
info.rowconfigure(0, weight=1)
'''///////////////////////////////////////'''
rootColor = "#107dac" #51719c
buttoncolor = "#106181"
cancelColor = rootColor #ff5722
activeColor = "#f09609"
font = "Helvetica 22 bold"
textFont = "Helvetica 26 bold"
valueFont = "Helvetica 20 bold"
stepLabelColor = "#189ad3"
distanceLabelColor = "#1ebbd7"
speedLabelColor = "#1ebbd7"
timeLabelColor = "#189ad3"


lifewalk_image = tk.PhotoImage(file=r"lifewalk.png")
lifewalk_image = lifewalk_image.subsample(1, 1)

home_icon = tk.PhotoImage(file=r"home.png")
home_icon = home_icon.subsample(7, 7)

lock_icon = tk.PhotoImage(file=r"lock-icon2.png")
lock_icon = lock_icon.subsample(3, 3)

step_icon = tk.PhotoImage(file=r"footprints.png")
step_icon = step_icon.subsample(4, 4)

distance_icon = tk.PhotoImage(file=r"distance.png")
distance_icon = distance_icon.subsample(4, 4)

speed_icon = tk.PhotoImage(file=r"dashboard.png")
speed_icon = speed_icon.subsample(4, 4)

time_icon = tk.PhotoImage(file=r"stopwatch.png")
time_icon = time_icon.subsample(4, 4)
'''//////////////////////////////////////'''
content = ttk.Frame(info)
content.grid(column=0, row=0, sticky="nsew")
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=5)
content.rowconfigure(2, weight=1)
'''////////////////////////////////////////'''
headlabel = tk.Label(content, bg=rootColor)
headlabel.grid(column=0, row=0, sticky="ewns")
headlabel.columnconfigure(0, weight=1)
headlabel.columnconfigure(1, weight=1)
headlabel.columnconfigure(2, weight=1)
headlabel.rowconfigure(0, weight=1)
brandLabel = tk.Label(headlabel, image=lifewalk_image, bg=rootColor)
brandLabel.grid(column=0, row=0, sticky="ewns")
homeLabel = tk.Label(headlabel, bg=rootColor)
homeLabel.grid(column=1, row=0, sticky="ewns")
homeLabel.columnconfigure(0, weight=1)
homeLabel.rowconfigure(0, weight=1)
homeButton = tk.Button(homeLabel, image=home_icon, bg=rootColor, border=0, highlightthickness=0,
                       activebackground=rootColor, command=hide_root)
homeButton.grid(column=0, row=0, sticky="ewns")
lockLabel = tk.Label(headlabel, image=lock_icon, bg=rootColor)
lockLabel.grid(column=2, row=0, sticky="ewns")
lockLabel.columnconfigure(0, weight=1)
lockLabel.rowconfigure(0, weight=1)
lockButton = tk.Button(lockLabel, image=lock_icon, bg=rootColor, border=0, highlightthickness=0,
                       activebackground=rootColor, command=lock_key)
lockButton.grid(column=0, row=0, sticky="ewns", ipadx=70)
'''///////////////////////////////////////////////'''
infoLabel = tk.Label(content, bg=buttoncolor, border=0)
infoLabel.grid(column=0, row=1, sticky="ewns")
infoLabel.columnconfigure(0, weight=1)
infoLabel.columnconfigure(1, weight=1)
infoLabel.rowconfigure(0, weight=1)
infoLabel.rowconfigure(1, weight=1)

'''infoLabel0 = tk.Label(infoLabel, bg=buttoncolor)
infoLabel0.grid(column=0, row=0, sticky="ewns")
infoLabel0.columnconfigure(0, weight=1)
infoLabel0.rowconfigure(0, weight=1)
infoLabel0.rowconfigure(1, weight=1)

infoLabel1 = tk.Label(infoLabel, bg=buttoncolor)
infoLabel1.grid(column=1, row=0, sticky="ewns")
infoLabel1.columnconfigure(0, weight=1)
infoLabel1.rowconfigure(0, weight=1)
infoLabel1.rowconfigure(1, weight=1)'''
'''///'''
stepLabel = tk.Label(infoLabel, bg=stepLabelColor)
stepLabel.grid(column=0, row=0, sticky="ewns")
stepLabel.columnconfigure(0, weight=2)
stepLabel.columnconfigure(1, weight=3)
stepLabel.rowconfigure(0, weight=1)
stepiconLabel = tk.Label(stepLabel, image=step_icon, bg=stepLabelColor, width=10, anchor="e")
stepiconLabel.grid(column=0, row=0, sticky="ewns")
stepiconLabel.bind("<ButtonRelease>", step_reset)
stepinfoLabel = tk.Label(stepLabel, bg=stepLabelColor)
stepinfoLabel.grid(column=1, row=0, sticky="ewns")
stepinfoLabel.columnconfigure(0, weight=1)
stepinfoLabel.rowconfigure(0, weight=1)
stepinfoLabel.rowconfigure(1, weight=1)
stepinfoText = tk.Label(stepinfoLabel, text="Step", bg=stepLabelColor, font=textFont, width=10)
stepinfoText.grid(column=0, row=0, sticky="s")
stepinfoValue = tk.Label(stepinfoLabel, text="0", font=valueFont, bg=stepLabelColor, width=10)
stepinfoValue.grid(column=0, row=1, sticky="ewns")
'''///'''
distanceLabel = tk.Label(infoLabel, bg=distanceLabelColor)
distanceLabel.grid(column=0, row=1, sticky="ewns")
distanceLabel.columnconfigure(0, weight=2)
distanceLabel.columnconfigure(1, weight=3)
distanceLabel.rowconfigure(0, weight=1)
distanceiconLabel = tk.Label(distanceLabel, image=distance_icon, bg=distanceLabelColor, width=10, anchor="e")
distanceiconLabel.grid(column=0, row=0, sticky="ewns")
distanceiconLabel.bind("<ButtonRelease>", distance_reset)
distanceinfoLabel = tk.Label(distanceLabel, bg=distanceLabelColor)
distanceinfoLabel.grid(column=1, row=0, sticky="ewns")
distanceinfoLabel.columnconfigure(0, weight=1)
distanceinfoLabel.rowconfigure(0, weight=1)
distanceinfoLabel.rowconfigure(1, weight=1)
distanceinfoText = tk.Label(distanceinfoLabel, text="Distance", bg=distanceLabelColor, font=textFont, width=10)
distanceinfoText.grid(column=0, row=0, sticky="s")
distanceinfoValue = tk.Label(distanceinfoLabel, text="0 meter", bg=distanceLabelColor, font=valueFont, width=10)
distanceinfoValue.grid(column=0, row=1, sticky="ewns")
'''///'''
speedLabel = tk.Label(infoLabel, bg=speedLabelColor)
speedLabel.grid(column=1, row=0, sticky="ewns")
speedLabel.columnconfigure(0, weight=2)
speedLabel.columnconfigure(1, weight=3)
speedLabel.rowconfigure(0, weight=1)
speediconLabel = tk.Label(speedLabel, image=speed_icon, bg=speedLabelColor, width=10, anchor="e")
speediconLabel.grid(column=0, row=0, sticky="ewns")
speedinfoLabel = tk.Label(speedLabel, bg=speedLabelColor)
speedinfoLabel.grid(column=1, row=0, sticky="ewns")
speedinfoLabel.columnconfigure(0, weight=1)
speedinfoLabel.rowconfigure(0, weight=1)
speedinfoLabel.rowconfigure(1, weight=1)
speedinfoText = tk.Label(speedinfoLabel, text="Speed", bg=speedLabelColor, font=textFont, width=10)
speedinfoText.grid(column=0, row=0, sticky="s")
speedinfoValue = tk.Label(speedinfoLabel, text="0 km/h", font=valueFont, bg=speedLabelColor, width=10)
speedinfoValue.grid(column=0, row=1, sticky="ewns")
'''///'''
timeLabel = tk.Label(infoLabel, bg=timeLabelColor)
timeLabel.grid(column=1, row=1, sticky="ewns")
timeLabel.columnconfigure(0, weight=2)
timeLabel.columnconfigure(1, weight=3)
timeLabel.rowconfigure(0, weight=1)
timeiconLabel = tk.Label(timeLabel, image=time_icon, bg=timeLabelColor, width=10, anchor="e")
timeiconLabel.grid(column=0, row=0, sticky="ewns")
timeiconLabel.bind("<ButtonRelease>", time_reset)
timeinfoLabel = tk.Label(timeLabel, bg=timeLabelColor)
timeinfoLabel.grid(column=1, row=0, sticky="ewns")
timeinfoLabel.columnconfigure(0, weight=1)
timeinfoLabel.rowconfigure(0, weight=1)
timeinfoLabel.rowconfigure(1, weight=1)
timeinfoText = tk.Label(timeinfoLabel, text="Time", bg=timeLabelColor, font=textFont, width=10)
timeinfoText.grid(column=0, row=0, sticky="s")
timeinfoValue = tk.Label(timeinfoLabel, text="00:00:00", bg=timeLabelColor, font=valueFont, width=10)
timeinfoValue.grid(column=0, row=1, sticky="ewns")
'''///////////////////////////////////////////'''
bottomLabel = tk.Label(content, bg=cancelColor, text="Total Time = 00:00:00", font=font, width=0)
bottomLabel.grid(column=0, row=2, sticky="ewns")

info.bind("<Escape>", exit)

APP = threading.Thread(target=App)
APP2 = threading.Thread(target=App2)
APP3 = threading.Thread(target=App3)
APP.start()
APP2.start()
APP3.start()

info.mainloop()
