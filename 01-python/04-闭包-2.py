def func(a,b):
    def num(x):
        return x*a+b
    return num

test_a = func(3,2)

for i in range(10):
    a = test_a(i)
    print(i,a)

