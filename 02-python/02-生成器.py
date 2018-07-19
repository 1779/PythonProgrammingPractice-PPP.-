def creat_num():
    print("--------start-------")
    a,b = 0,1
    for i in range(5):
        yield b
        a,b = b,a+b
    print("-------end--------")

