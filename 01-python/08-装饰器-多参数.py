def func(function):
    print("---func---")
    def inner(*args,**kwargs):
        print("---inner---")
        function(*args,**kwargs)
    return inner

@func
def test1(a,b,c):
    print("----test1----")
    print("----a=%d---b=%d---c=%d----"%(a,b,c))

test1(1,2,3)
