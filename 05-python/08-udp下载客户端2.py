from socket import *
import time


udp_client = socket(AF_INET,SOCK_DGRAM)

ip = input("请输入对方ip：")
port = int(input("请输入对方端口："))
client_addr =(ip,port)

udp_client.bind(("",8080))
udp_client.sendto(b"",client_addr)
f = open("test.rar","ba")
start_time = time.time()
i=0
while True:
    recv_data, server_addr = udp_client.recvfrom(1024)
    udp_client.sendto(b"",server_addr)
    if recv_data:
        i+=1
        f.write(recv_data)
        print("\r--正在接收：%3f Mb--"%(i/1024),end="")
        if len(recv_data) < 1024:
            print("接收完毕！")
            f.close()
            udp_client.close()
            break
end_time = time.time()
print("---共用时：%.2f 秒"%(start_time - end_time))

