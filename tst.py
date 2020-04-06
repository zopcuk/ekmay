try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
root = tk.Tk()
root.title('background image')
# pick a .gif image file you have in the working directory
fname = "add.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
cv.create_text(15, 20, text="Python Greetings", fill="red", anchor='nw')
# now add some button widgets
btn1 = tk.Button(cv, text="Click")
btn1.pack(side='right', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="Quit", command=root.destroy)
btn2.pack(side='left', padx=10, pady=5, anchor='sw')
root.mainloop()

'''from time import sleep
import lockPage2
def a():
    sleep(3)
    print("a")
def b():
    sleep(2)
    print("b")

def ab():
    a()
    b()
for i in range(9):
    print(i)
ab()
lockPage2.root_tk()'''