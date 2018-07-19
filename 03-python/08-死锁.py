#反面教材 平时应该避免死锁
        
import threading
import time

class Test1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name+"------do1---up----")
            time.sleep(1)
            if mutexB.acquire():
                print(self.name+"------do1---down--")
                mutexB.release()
            mutexA.release()

class Test2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name+"------do2---up----")
            time.sleep(1)

            if mutexA.acquire():
                print(self.name+"------do2---down--")
                mutexA.release()
            mutexB.release()



if __name__ == "__main__":
    mutexA = threading.Lock()
    mutexB = threading.Lock()
    t1 = Test1()
    t2 = Test2()
    t1.start()
    t2.start()

