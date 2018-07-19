def w1(func):
    def inner():
        print("-----正在进行验证-----")
        func()
    return inner

def f1():
    print("-----f1-----")
f1 = w1(f1)
f1()

