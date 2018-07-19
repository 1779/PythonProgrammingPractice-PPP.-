class Animal:
    def eat(self):
        print("------吃------")

    def drink(self):
        print("------喝------")

    def run(self):
        print("------跑------")

    def sleep(self):
        print("------睡------")


class Dog(Animal):
    def bark(self):
        print("------汪汪叫------")

class Tedi(Dog):
    def bark(self):
        print("-----小声叫------")
        super().bark()


dog=Tedi()
dog.bark()
dog.eat()


