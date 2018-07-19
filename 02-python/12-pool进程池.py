from multiprocessing import Pool
import os
import time
import random

def worker(num):
    for i in range(5):
        print("-----pid=%d-----%d"%(os.getpid(),num))
        time.sleep(0.2)

pool = Pool(3)

for i in range(10):
    print("-----%d-----"%i)
    pool.apply_async(worker,(i,))


pool.close()
pool.join()

