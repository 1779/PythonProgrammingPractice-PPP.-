from threading import Thread
import time

def test():
    print("没事，就试试看")
    time.sleep(1)

for i in range(5):
    t = Thread(target=test)
    t.start()


