import os
import time

ret = os.fork()

if ret == 0:
    print("----1----")
    time.sleep(2)
else:
    print("----2----")
    time.sleep(3)

ret = os.fork()

if ret == 0:
    print("----11----")
    time.sleep(3)
else:
    print("----22----")
    time.sleep(2)
