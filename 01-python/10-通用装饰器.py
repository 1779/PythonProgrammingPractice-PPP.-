def func(function):
    def inner(*args,**kwargs):
        print("正在完成验证")
        ret = function(*args,**kwargs)
        return ret
    return inner

@func
def test1():
    print("test1")

@func
def test2(a,b):
    print("test2--a=%d--b=%d"%(a,b))

@func
def test3(a,b):
    print("test3")
    return a+b

test1()
test2(3,4)
num = test3(3,4)
print(num)



