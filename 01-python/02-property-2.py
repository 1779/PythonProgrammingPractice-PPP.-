class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        print("-----get_num-----")
        return self.__num
    @num.setter
    def num(self,new_num):
        print("-----set_num-----")
        self.__num = new_num
        
t=Test()
t.num=200
print(t.num)
