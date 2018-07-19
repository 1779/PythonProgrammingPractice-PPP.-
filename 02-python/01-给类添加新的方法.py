import types

class Person(object):
    def __init__(self,new_name):
        self.name = new_name

    def eat(self):
        print("----%s正在吃----"%self.name)

def run(self):
    print("----%s正在跑----"%self.name)

laowang = Person("老王")
print(laowang.name)
laowang.eat()

laowang.run = types.MethodType(run,laowang)
laowang.run()

