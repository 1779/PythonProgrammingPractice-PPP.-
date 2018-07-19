from socket import *
import time
udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(("",7788))

def recv_message():
    global udp_socket
    temp = udp_socket.recvfrom(1024)    
    return temp

def main():
    while True:
        message_temp = recv_message()
        message = str(message_temp[0].decode("gb2312"))
        ip = str(message_temp[1])
        current_time = time.ctime()
        print(current_time +" "+ ip + " : " +message)


if __name__ == "__main__":
    main()
