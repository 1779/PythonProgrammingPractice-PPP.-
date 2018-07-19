from multiprocessing import Process
import time

class MyNewProsecc(Process):
    def run(self): #在调用start方法时会自动调用
        while True:
            print("-----1-----")
            time.sleep(1)

p = MyNewProsecc()

p.start()

while True:
    print("------main------")
    time.sleep(1)


