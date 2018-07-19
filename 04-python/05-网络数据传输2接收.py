from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

#udpSocket.sendto(b"haha",("192.168.130.132",8080))

udpSocket.bind(("", 1522))

recv_data = udpSocket.recvfrom(1024)

print(recv_data)
