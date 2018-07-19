from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)

f = open("test.jpg","br")
while True:
    temp = f.read(512)
    if temp:
        udp_socket.sendto(temp,("192.168.130.139",8080))
    else :
        f.close()
        break

