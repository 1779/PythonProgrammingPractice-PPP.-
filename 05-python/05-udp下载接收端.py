from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)

udp_socket.bind(("",8080))

f = open("test2.jpg","ba")
while True:
    recv_data,recv_addr = udp_socket.recvfrom(1024)
    if recv_data:
        f.write(recv_data)
    else :
        f.close()
        break
print("-----------")


