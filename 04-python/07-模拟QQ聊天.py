from threading import Thread
from socket import *

def recv_data():
    while True:
        recv_info = udp_socket.recvfrom(1024)
        print("\n>>%s:%s\n<<"%(str(recv_info[1]),str(recv_info[0].decode("gb2312"))),end="")

def send_data():
    while True:
        send_info = input("<<")
        udp_socket.sendto(send_info.encode("gb2312"),(dest_ip ,dest_port))


udp_socket = None
dest_ip =""
dest_port = 0
my_port = int(input("请输入自己的端口:"))

def main():
    global my_port
    global udp_socket
    global dest_ip
    global dest_port

    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的端口号:"))

    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(("",my_port))

    tr = Thread(target=recv_data)
    ts = Thread(target=send_data)
    
    tr.start()
    ts.start()

    ts.join()
    tr.join()

if __name__ == "__main__":
    main()
