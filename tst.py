import configparser

config = configparser.ConfigParser()
config.read('config.ini')
dutyCycle = config.getint("section_a", "dutyCycle")
a = 115
dutyCycle = dutyCycle + 15
config.set("section_a", "dutyCycle", "{}".format(dutyCycle))
with open("config.ini", 'w') as configfile:
    config.write(configfile)
dutyCycle = config.getint("section_a", "dutyCycle")
print(dutyCycle)
print(a)
'''from tkinter import *

class Main_screen(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.text = Label(text="Janela")
        self.text.grid()
        root.withdraw()
        self.create_login()

    def create_login(self):
        self.root2 = Toplevel()
        self.app2 = Login_screen(self.root2)

class Login_screen(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.botao1 = Button(self,text="Appear",command = lambda: self.show_main())
        self.botao1.grid()

    def show_main(self):
        self.master.destroy()
        root.deiconify()


root = Tk()
app = Main_screen(root)
root.mainloop()'''



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