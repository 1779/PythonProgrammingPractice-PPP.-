def w1(func):
    def inner():
        print("-----正在进行验证-----")
        f = func()
        return f
    return inner
@w1
def f1():
    print("-----f1-----")
    return "haha"
f = f1()
print(f)
