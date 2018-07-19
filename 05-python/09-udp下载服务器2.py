from socket import *

udp_server = socket(AF_INET,SOCK_DGRAM)

udp_server.bind(("",8899))

f = open("test.jpg","br")
client_infor, client_addr = udp_server.recvfrom()
while True:
    temp = f.read(1024)
    if temp:
        udp_server.sendto(temp,client_addr)
    else :
        f.close()
        udp_server.close()
        print("发送完毕！")
