class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = "cpp"

    def __getattribute__(self,obj):
        print("---->1%s"%obj)
        if obj == "subject1":
            print("logsubject1")
            return "redirect python"
        else :
            temp = object.__getattribute__(self,obj)
            print("---->2%s"%str(temp))
            return temp
    def show(self):
            print("this is Itcast")


s = Itcast('pyhton')
print(s.subject1)
print(s.subject2)
s.show()
