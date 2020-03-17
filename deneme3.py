import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
def homePos():
    print("all positions going to zero")
def resetButton():
    winColor="brown"
    bottomColor="yellow"
    yesColor="green"
    noColor="green"
    win = tk.Toplevel(background=winColor)
    win.wm_title("Window")
    win.wm_attributes('-fullscreen', 'true')
    #win.overrideredirect(True)
    win.wm_attributes('-topmost', 'true')

    s = ttk.Style()
    s.configure('new.TFrame', background=winColor,highlightcolor="green",highlightthickness=3,bd=3)
    winFrame = ttk.Frame(win, style='new.TFrame')

    def yesButton():
        homePos()
        win.destroy()

    headLabel = tk.Label(winFrame, text="Reset Positions", bg=winColor)
    headLabel.config(font=("Courier", 12))
    textLabel = tk.Label(winFrame, text="Are you sure?",bg=winColor)
    textLabel.config(font=("Courier", 9))

    yesLabel = tk.Label(winFrame, bg=bottomColor)
    yesLabel.grid(row=2, column=0, sticky='ewns', columnspan=1)
    b_yes = tk.Button(winFrame, image=check, bg=bottomColor, border=0, highlightthickness=0, activebackground=bottomColor, command=yesButton)

    noLabel = tk.Label(winFrame, bg=bottomColor)
    noLabel.grid(row=2, column=4, sticky='ewns', columnspan=1)
    b_no = tk.Button(winFrame, image = delete, bg=bottomColor, border=0, highlightthickness=0, activebackground="green", command=win.destroy)

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
        print("yesButtonClick")

    def yesRelease(event):
        yesLabel.configure(bg=bottomColor)
        b_yes.configure(bg=bottomColor, activebackground=bottomColor)
        print("yesButtonRelease")
        yesButton()

    b_yes.bind("<ButtonPress>", yesClick)
    b_yes.bind("<ButtonRelease>", yesRelease)
    '''////////////////////////////no button events/////////////////////////////////'''
    def noClick(event):
        noLabel.configure(bg=noColor)
        b_no.configure(bg=noColor, activebackground=noColor)
        print("yesButtonClick")

    def noRelease(event):
        noLabel.configure(bg=bottomColor)
        b_no.configure(bg=bottomColor, activebackground=bottomColor)
        print("yesButtonRelease")
        yesButton()
    a =[b_no,b_yes]
    a[0].bind("<ButtonPress>", noClick)
    a[0].bind("<ButtonRelease>", noRelease)
    '''////////////////////////////////////////////////////////////////'''

    winFrame.grid(column=0, row=0, sticky=(N, S, E, W))
    headLabel.grid(row=0, column=2)
    textLabel.grid(row=1, column=2)
    b_yes.grid(row=2, column=0)
    b_no.grid(row=2, column=4)

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    winFrame.columnconfigure(0, weight=4)
    winFrame.columnconfigure(1, weight=1)
    winFrame.columnconfigure(2, weight=1)
    winFrame.columnconfigure(3, weight=1)
    winFrame.columnconfigure(4, weight=4)
    winFrame.rowconfigure(0, weight=2)
    winFrame.rowconfigure(1, weight=2)
    winFrame.rowconfigure(2, weight=2)

def popup_showinfo():
    showinfo("Window", "Hello World!")

class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.button_bonus = ttk.Button(self, text="Bonuses", command=resetButton)
        self.button_bonus.pack()

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()
def exit(event):
    root.destroy()
root = tk.Tk()
root.geometry("500x500")


check = tk.PhotoImage(file=r"check-button.png")
check = check.subsample(1, 1)

delete = tk.PhotoImage(file=r"delete-button.png")
delete = delete.subsample(1, 1)
b1 = Button(root,text="animal",command=resetButton)
b1.pack()
root.bind("<Escape>", exit)

root.mainloop()