from multiprocessing import Process
import time

def test1():
    while True:
        print("----1----")
        time.sleep(1)
def test2():
    while True:
        print("----2----")
        time.sleep(1)

p1 = Process(target=test1)
p1.start()
p2 = Process(target=test2)
p2.start()

def test3():
    while True:
        print("----3----")
        time.sleep(3)
def test4():
    while True:
        print("----4----")
        time.sleep(2)

p3 = Process(target=test3)
p3.start()
p4 = Process(target=test4)
p4.start()
while True:
    print("-------------")
    time.sleep(1)

