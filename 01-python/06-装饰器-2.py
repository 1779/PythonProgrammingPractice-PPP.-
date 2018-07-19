#语法糖
def w1(func):
    def inner():
        print("-----正在进行验证-----")
        key = input("请输入验证密码：")

        if key == "123123":
            func()
        else :
            print("没有权限")
    return inner

@w1
def f1():
   print("-----f1-----")
@w1
def f2():
   print("-----f2-----")
@w1
def f3():
   print("-----f3-----")
@w1
def f4():
   print("-----f4-----")

f1()
f2()
f3()
f4()

