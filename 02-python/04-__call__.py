class Test(object):
    def __init__(self,func):
        print("---正在进行初始化---")
        print("----调用的函数是%s----"%func.__name__)
        self.__func = func

    def __call__(self):
        print("------__call__------")
        self.__func()

@Test
def test():
    print("------test------")

test() 
