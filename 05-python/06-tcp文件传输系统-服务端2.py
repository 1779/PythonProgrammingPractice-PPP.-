from socket import *

tcp_server = socket(AF_INET,SOCK_STREAM)

tcp_server.bind(("",8899))

tcp_server.listen()

tcp_clint,clint_infor = tcp_server.accept()

f = open("test.jpg","br")
i = 0
while True:
    temp = f.read(512)
    if temp:
        i += 1
        tcp_clint.send(temp)
        print("---第%d次发送---"%i)
    else :
        print("---发送完毕---")
        f.close()
        tcp_server.close()
        break


