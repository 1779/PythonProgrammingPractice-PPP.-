#轮寻 此种方式效率不高 在执行一个线程时 另一个线程
#在死循环 占用CPU 


from threading import Thread
import time
num = 0
flag = 0

def test1():
    global num
    global flag
    while True:
        if flag == 0:
            for i in range(1000000):
                num += 1
            flag = 1
            print("------test1--%d---"%num)
            break

def test2():
    global num
    global flag
    while True:
        if flag == 1:
            for i in range(1000000):
                num += 1
            flag = 0
            print("------test2--%d---"%num)
            break

t1 = Thread(target=test1)
t1.start()

#time.sleep(0.06)
t2 = Thread(target=test2) 
t2.start()
