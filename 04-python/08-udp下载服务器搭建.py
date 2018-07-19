from socket import *
import struct
import sys
import time


udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(("",8899))
recv_data,recv_addr = udp_socket.recvfrom(1024)

#1.获取文件名

file_name_len = len(recv_data.decode()[2:-7])
print("名字的长度是：%d"%file_name_len)
file_name_temp_1 = "!"+str(file_name_len)+"s"
file_name_temp = struct.unpack(file_name_temp_1,recv_data[2:2 + file_name_len])
#print(file_name_temp)
a = file_name_temp[0]
#print(a)
file_name = file_name_temp[0].decode()
print("文件名：%s"%file_name)

#2.发送文件
i = 0
f = open(file_name,"r")
while i <= 0:
    #file_temp =f.read(10)
    #print(file_temp)
    #time.sleep(0.5)

    file_temp = f.read(512)
    file_temp_len = len(file_temp)
    send_temp_1 = "!HH"+str(file_temp_len)+"b"
    send_temp = struct.pack(send_temp_1,3,i,file_temp)
    udp_socket.sendto(send_temp,recv_addr)

    i += 1




