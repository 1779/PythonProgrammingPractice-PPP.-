from threading import Thread
import threading
import time

def test1():
    num = 100
    name = threading.current_thread().name
    print("------threading name is :%s---"%name)
    if name == "Thread-1":
        num=num + 1
    else :
        time.sleep(2)
    print("-----------%s  %d----------"%(name,num))
"""
def test2():
    num = 100
    num += 1
    print("------test2--%d---"%num)
"""

t1 = Thread(target=test1)
t1.start()

t2 = Thread(target=test1) 
t2.start()
