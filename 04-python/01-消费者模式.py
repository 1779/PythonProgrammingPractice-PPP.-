import threading 
import time
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(5):
                    count = count + 1
                    msg = "---生产产品---"+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(5):
                    msg = "---消费产品---"+self.name+queue.get()
                    print(msg)

                print("*"*50)    
                print("---仓库剩余---%d"%queue.qsize())
                print("*"*50)    
            time.sleep(0.5)


if __name__ =="__main__":
    queue = Queue()

    for i in range(500):
        queue.put("---初始产品---"+str(i))

    for i in range(5):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()

        
