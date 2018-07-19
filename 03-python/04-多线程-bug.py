from threading import Thread
import time
num = 0

def test1():
    global num
    for i in range(1000000):
        num += 1
    print("------test1--%d---"%num)

def test2():
    global num
    for i in range(1000000):
        num += 1
    print("------test2--%d---"%num)

t1 = Thread(target=test1)
t1.start()

time.sleep(0.06)
t2 = Thread(target=test2) 
t2.start()
