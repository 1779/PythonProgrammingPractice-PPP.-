def test(number):
    print("--1--")
    def test_in(number2):
        print("--2--")
        print(number+number2)

    print("--3--")
    return test_in

print("-"*50)
ret = test(100)
print("-"*50)
ret(100)
print("-"*50)
ret(200)
print("-"*50)
ret2 = test(1)
print("-"*50)
ret2(300)
print("-"*50)
ret(300)
print("-"*50)

