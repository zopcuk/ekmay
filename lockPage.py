import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
def lockButton2():
    winColor="#106181"
    win = tk.Toplevel(background=winColor)
    win.wm_title("Password2")
    win.wm_attributes('-fullscreen', 'true')
    win.wm_attributes('-topmost', 'true')
    s = ttk.Style()
    s.configure('new.TFrame', background=winColor)
    winFrame = ttk.Frame(win, style='new.TFrame')
    winFrame.grid(column=0, row=1, sticky=(N, S, E, W))

    def dele():
        e.delete(len(e.get()) - 1, tk.END)

    def passOk():
        if len(e.get()) == 4:
            if parola == e.get():
                print("parola doğru")
                root.wm_attributes('-topmost', 'true')
                win.destroy()
            else:
                print("parola yanlış")
                e.delete(0, END)
        else:
            e.delete(0, END)

    def limitSizeDay(*args):
        value = password.get()
        if len(value) > 3: password.set(value[:4])

    labelColor = "#51719c"
    parola = "1922"
    password = tk.StringVar()  # Password variable
    password.trace('w', limitSizeDay)
    entryLabel = tk.Label(win, bg=labelColor)
    entryLabel.grid(row=0, column=0, sticky='ewns', columnspan=1)
    e = tk.Entry(entryLabel, textvariable=password, show='', justify='center', width=20, font="Helvetica 44 bold",
                 bg=labelColor, foreground="black", highlightthickness=0, border=0)
    e.grid(column=1, row=0, sticky ="ewns")
    pass_change = tk.Button(entryLabel, image = password_change, bg=labelColor, width=7, border=0, highlightthickness=0,
                   activebackground=labelColor,
                   font="Helvetica 44 bold", command=root.destroy)
    pass_change.grid(column=2, row=0, sticky ="ewns")

    buttoncolor = winColor
    b1 = tk.Button(winFrame, text="1", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "1"))
    b1.grid(column=1, row=0)

    b2 = tk.Button(winFrame, text="2", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "2"))
    b2.grid(column=2, row=0)

    b3 = tk.Button(winFrame, text="3", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "3"))
    b3.grid(column=3, row=0)

    b4 = tk.Button(winFrame, text="4", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "4"))
    b4.grid(column=1, row=1)

    b5 = tk.Button(winFrame, text="5", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "5"))
    b5.grid(column=2, row=1)

    b6 = tk.Button(winFrame, text="6", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "6"))
    b6.grid(column=3, row=1)

    b7 = tk.Button(winFrame, text="7", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "7"))
    b7.grid(column=1, row=2)

    b8 = tk.Button(winFrame, text="8", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "8"))
    b8.grid(column=2, row=2)

    b9 = tk.Button(winFrame, text="9", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "9"))
    b9.grid(column=3, row=2)

    bok = tk.Button(winFrame, image=okey, bg=buttoncolor, width=7, border=0, highlightthickness=0,
                    activebackground=buttoncolor,
                    font="Helvetica 44 bold", command=passOk)
    bok.grid(column=1, row=3, sticky="ewns")

    b0 = tk.Button(winFrame, text="0", bg=buttoncolor, width=7, border=0, highlightthickness=0,
                   activebackground=buttoncolor,
                   font="Helvetica 44 bold", command=lambda: e.insert(tk.END, "0"))
    b0.grid(column=2, row=3)

    bdel = tk.Button(winFrame, image=delete, bg=buttoncolor, width=7, border=0, highlightthickness=0,
                     activebackground=buttoncolor,
                     font="Helvetica 44 bold", command=dele)
    bdel.grid(column=3, row=3, sticky="ewns")

    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=3)
    entryLabel.columnconfigure(0, weight=1)
    entryLabel.columnconfigure(1, weight=3)
    entryLabel.columnconfigure(2, weight=1)
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

    # root.config(cursor='none')
def popup_showinfo():
    showinfo("Window", "Hello World!")


def exit(event):
    root.destroy()



root = tk.Tk()
root.geometry("500x500")
root.wm_attributes('-fullscreen', 'true')
root.wm_attributes('-topmost', 'true')


okey = tk.PhotoImage(file=r"checkbox.png")
okey = okey.subsample(6, 6)

delete = tk.PhotoImage(file=r"delete.png")
delete = delete.subsample(5, 5)

password_change = tk.PhotoImage(file=r"password-change.png")
password_change = password_change.subsample(4, 4)

b1 = Button(root, text="animal", command=lockButton2)
b1.pack()
b2 = Button(root, text="destroy", command=root.destroy)
b2.pack()
root.bind("<Escape>", exit)

root.mainloop()