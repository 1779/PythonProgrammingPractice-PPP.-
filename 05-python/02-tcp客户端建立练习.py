from socket import *


ip = input("请输入ip:")
port = int(input("请输入端口："))
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect((ip,port))

send_data = input("请输入要发送的信息：")
client_socket.send(send_data.encode("gb2312"))

client_socket.close()
