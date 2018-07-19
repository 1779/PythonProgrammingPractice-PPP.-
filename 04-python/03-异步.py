from multiprocessing import Pool
import os 
import time

def test():
    print("---pid %d,ppid %d---"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d----"%i)
        time.sleep(1)
    return "haha"

def test2(args):
    print("---call_back_func %d---"%os.getpid())
    print("---call_back_args %s---"%args)

pool = Pool(3)
pool.apply_async(func=test,callback=test2)

"""
time.sleep(5)
print("----主进程 %d----"%os.getpid())
"""
i = 0
while True:
    i+=1
    print("---主进程 %d---%d"%(os.getpid(),i))
    time.sleep(1)
