import time
t1 = time.time()
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            k +=1
        j += 1
    i +=1

t2 = time.time()

t = t2 - t1
print(t)
