from tkinter import ttk
import tkinter as tk
import configparser
import threading
from time import sleep
config = configparser.ConfigParser()
config.read('config.ini')
dutyCycle = 0
adim = 0.8 #meter in 1 step
class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        i = 0
        global dutyCycle
        try:
            while True:
                config.read('config.ini')
                dutyCycle = config.getint('section_a', 'dutyCycle')
                if dutyCycle > 0:
                    stepinfoValue.configure(text=i)
                    i = i + 1
                    sleep((100/dutyCycle)/2)
                else:
                    sleep(.5)
        except:
            pass
class App2(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        global dutyCycle
        i = 0
        try:
            while True:
                config.read('config.ini')
                dutyCycle = config.getint('section_a', 'dutyCycle')
                if dutyCycle > 0:
                    distanceinfoValue.configure(text="{:.1f} meter".format(i))
                    i = i + adim
                    sleep((100/dutyCycle)/2)
                else:
                    sleep(.5)
        except:
            pass


class App3(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        global dutyCycle
        i = 0
        try:
            while True:
                config.read('config.ini')
                dutyCycle = config.getint('section_a', 'dutyCycle')
                if dutyCycle > 0:
                    speedinfoValue.configure(text="{:.2f} km/h".format(i))
                    i = ((adim*2)/1000)/((100/dutyCycle)/(60*60))
                    sleep(0.5)
                else:
                    sleep(.5)
        except:
            pass

class App4(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        try:
            while True:
                sleep(.08)
                config.read('config.ini')
                test = config.get('section_a', 'show_hide')
                if test == "0":
                    info.withdraw()
                    print("icon")
                elif test == "1":
                    print("deicon")
                    info.deiconify()
        except:
            pass
def exit(event):
    info.destroy()
def hide_root():
    config.set("section_a", "show_hide", "0")
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
def lock_key():
    config.set("section_a", "lock_key", "1")
    config.set("section_a", "show_hide", "0")
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
info = tk.Tk()
info.title("INFO")
info.wm_attributes('-fullscreen', 'true')
info.wm_attributes('-topmost', 'true')
info.columnconfigure(0, weight=1)
info.rowconfigure(0, weight=1)
'''///////////////////////////////////////'''
rootColor = "#106181"#"#51719c"
buttoncolor = "#106181"
cancelColor = "#f09609" #"#ff5722"
activeColor = "#f09609"
font = "Helvetica 22 bold"
textFont = "Helvetica 26 bold"
valueFont = "Helvetica 20 bold"
stepLabelColor=buttoncolor
distanceLabelColor=buttoncolor
speedLabelColor=buttoncolor
timeLabelcolor=buttoncolor


lifewalk_image = tk.PhotoImage(file=r"lifewalk.png")
lifewalk_image = lifewalk_image.subsample(2, 2)

home_icon = tk.PhotoImage(file=r"home.png")
home_icon = home_icon.subsample(7, 7)

lock_icon = tk.PhotoImage(file=r"lock-icon.png")
lock_icon = lock_icon.subsample(6, 6)

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
brandLabel.grid(column=0,row=0,sticky="ewns")
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
                       activebackground=rootColor,command=lock_key)
lockButton.grid(column=0, row=0, sticky="ewns")
'''///////////////////////////////////////////////'''
infoLabel = tk.Label(content, bg=buttoncolor)
infoLabel.grid(column=0, row=1, sticky="ewns")
infoLabel.columnconfigure(0, weight=1)
infoLabel.columnconfigure(1, weight=1)
infoLabel.rowconfigure(0, weight=1)

infoLabel0 = tk.Label(infoLabel, bg=buttoncolor)
infoLabel0.grid(column=0, row=0, sticky="ewns")
infoLabel0.columnconfigure(0, weight=1)
infoLabel0.rowconfigure(0, weight=1)
infoLabel0.rowconfigure(1, weight=1)

infoLabel1 = tk.Label(infoLabel, bg=buttoncolor)
infoLabel1.grid(column=1, row=0, sticky="ewns")
infoLabel1.columnconfigure(0, weight=1)
infoLabel1.rowconfigure(0, weight=1)
infoLabel1.rowconfigure(1, weight=1)
'''///'''
stepLabel=tk.Label(infoLabel0, bg=stepLabelColor)
stepLabel.grid(column=0, row=0, sticky="ewns")
stepLabel.columnconfigure(0, weight=1)
stepLabel.columnconfigure(1, weight=2)
stepLabel.rowconfigure(0, weight=1)
stepiconLabel=tk.Label(stepLabel, image=step_icon, bg=stepLabelColor)
stepiconLabel.grid(column=0, row=0, sticky="ewns")
stepinfoLabel=tk.Label(stepLabel, bg=stepLabelColor)
stepinfoLabel.grid(column=1, row=0, sticky="ewns")
stepinfoLabel.columnconfigure(0, weight=1)
stepinfoLabel.rowconfigure(0, weight=1)
stepinfoLabel.rowconfigure(1, weight=1)
stepinfoText=tk.Label(stepinfoLabel, text="Step", bg=stepLabelColor, font=textFont,width=10)
stepinfoText.grid(column=0, row=0, sticky="ewns")
stepinfoValue=tk.Label(stepinfoLabel, text="0", font=valueFont, bg=stepLabelColor,width=10)
stepinfoValue.grid(column=0, row=1, sticky="ewns")
'''///'''
distanceLabel = tk.Label(infoLabel0, bg=distanceLabelColor)
distanceLabel.grid(column=0, row=1, sticky="ewns")
distanceLabel.columnconfigure(0, weight=1)
distanceLabel.columnconfigure(1, weight=2)
distanceLabel.rowconfigure(0, weight=1)
distanceiconLabel = tk.Label(distanceLabel, image=distance_icon, bg=distanceLabelColor)
distanceiconLabel.grid(column=0, row=0, sticky="ewns")
distanceinfoLabel = tk.Label(distanceLabel, bg=distanceLabelColor)
distanceinfoLabel.grid(column=1, row=0, sticky="ewns")
distanceinfoLabel.columnconfigure(0, weight=1)
distanceinfoLabel.rowconfigure(0, weight=1)
distanceinfoLabel.rowconfigure(1, weight=1)
distanceinfoText = tk.Label(distanceinfoLabel, text="Distance", bg=distanceLabelColor, font=textFont,width=10)
distanceinfoText.grid(column=0, row=0, sticky="ewns")
distanceinfoValue = tk.Label(distanceinfoLabel, text="0 meter", bg=distanceLabelColor, font=valueFont,width=10)
distanceinfoValue.grid(column=0, row=1, sticky="ewns")
'''///'''
speedLabel = tk.Label(infoLabel1, bg=speedLabelColor)
speedLabel.grid(column=0, row=0, sticky="ewns")
speedLabel.columnconfigure(0, weight=1)
speedLabel.columnconfigure(1, weight=2)
speedLabel.rowconfigure(0, weight=1)
speediconLabel = tk.Label(speedLabel, image=speed_icon, bg=speedLabelColor)
speediconLabel.grid(column=0, row=0, sticky="ewns")
speedinfoLabel = tk.Label(speedLabel, bg=speedLabelColor)
speedinfoLabel.grid(column=1, row=0, sticky="ewns")
speedinfoLabel.columnconfigure(0, weight=1)
speedinfoLabel.rowconfigure(0, weight=1)
speedinfoLabel.rowconfigure(1, weight=1)
speedinfoText = tk.Label(speedinfoLabel, text="Speed", bg=speedLabelColor, font=textFont,width=10)
speedinfoText.grid(column=0, row=0, sticky="ewns")
speedinfoValue = tk.Label(speedinfoLabel, text="0 km/h",font=valueFont, bg=speedLabelColor,width=10)
speedinfoValue.grid(column=0, row=1, sticky="ewns")
'''///'''
timeLabel = tk.Label(infoLabel1, bg=distanceLabelColor)
timeLabel.grid(column=0, row=1, sticky="ewns")
timeLabel.columnconfigure(0, weight=1)
timeLabel.columnconfigure(1, weight=2)
timeLabel.rowconfigure(0, weight=1)
timeiconLabel = tk.Label(timeLabel, image=time_icon, bg=distanceLabelColor)
timeiconLabel.grid(column=0, row=0, sticky="ewns")
timeinfoLabel = tk.Label(timeLabel, bg=distanceLabelColor)
timeinfoLabel.grid(column=1, row=0, sticky="ewns")
timeinfoLabel.columnconfigure(0, weight=1)
timeinfoLabel.rowconfigure(0, weight=1)
timeinfoLabel.rowconfigure(1, weight=1)
timeinfoText = tk.Label(timeinfoLabel, text="Time", bg=distanceLabelColor, font=textFont,width=10)
timeinfoText.grid(column=0, row=0, sticky="ewns")
timeinfoValue = tk.Label(timeinfoLabel, text="05:47:36", bg=distanceLabelColor, font=valueFont,width=10)
timeinfoValue.grid(column=0, row=1, sticky="ewns")
'''///////////////////////////////////////////'''
bottomLabel = tk.Label(content, bg=cancelColor, text="Total Time = 04:05:08" ,font=font)
bottomLabel.grid(column=0, row=2, sticky="ewns")

info.bind("<Escape>", exit)

APP = App()
APP2 = App2()
App3 = App3()
App4 = App4()
info.mainloop()
