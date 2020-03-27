from time import sleep
def a():
    sleep(3)
    print("a")
def b():
    sleep(2)
    print("b")

def ab():
    a()
    b()
ab()