from socket import *

secer_socket = socket(AF_INET,SOCK_STREAM)

secer_socket.bind(("",8899))

secer_socket.listen(5)

clint_socket,clint_info = secer_socket.accept()

recv_data = clint_socket.recv(1024)

print("%s：%s"%(str(clint_info),recv_data.decode("gb2312")))

clint_socket.close()
secer_socket.close()

