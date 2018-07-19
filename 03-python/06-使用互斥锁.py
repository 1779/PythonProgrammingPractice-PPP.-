#使用互斥锁

from threading import Thread,Lock
import time

num = 0

def test1():
    global num
    metux.acquire()
    for i in range(1000000):
        num += 1
    print("------test1--%d---"%num)
    metux.release()

def test2():
    global num
    metux.acquire()
    for i in range(1000000):
        num += 1
    print("------test2--%d---"%num)
    metux.release()

#创建一把互斥锁，这个锁默认是没有上锁的
metux = Lock()

t1 = Thread(target=test1)
t1.start()

#time.sleep(0.06)
t2 = Thread(target=test2) 
t2.start()
