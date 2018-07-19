def test1():
    while True:
        print("------1------")
        yield None

def test2():
    while True:
        print("------2------")
        yield None
a = test1()
b = test2()

while True:
    a.__next__()
    b.__next__()



