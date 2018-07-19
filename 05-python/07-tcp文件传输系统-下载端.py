
from socket import *

f = open("test2.jpg","ba")
i = 0
ip ="192.168.130.132" #input("请输入ip:")
port =8899 #int(input("请输入端口："))
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect((ip,port))

while True:
    recv_data = client_socket.recv(1024)
    if recv_data:
        f.write(recv_data )
        i+=1
        #print(len(recv_data))
        print("---第%d次接收---"%i)
        #client_socket.send(b"ok")
        if len(recv_data) < 1024:
            print("---接收完毕---")
            f.close()
            client_socket.close()
            break


