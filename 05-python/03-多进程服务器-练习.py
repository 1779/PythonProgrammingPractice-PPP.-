import time
from socket import *
from multiprocessing import Process

def worker(new_clint,dest_addr):
    try :
        while True:
            recv_data = new_clint.recv(1024)
            if len(recv_data) > 0:
                print("recv[%s]:%s"%(str(dest_addr), recv_data))
            else :
                print("[%s]客户端已关闭！"%str(dest_addr))
                break
    finally :
        new_clint.close()


print("---正在进行初始化---")
#1 建立套接字
tcp_server = socket(AF_INET,SOCK_STREAM)
#tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#2 绑定ip
print("---正在绑定ip---")
local_addr = ("",8080)
tcp_server.bind(local_addr)
time.sleep(0.5)
print("---绑定成功---")
#3 监听
print("---正在接受用户请求---")
tcp_server.listen(5)
while True:
    new_clint,dest_addr = tcp_server.accept()
    print("---新的请求---%s"%str(dest_addr))
    clint = Process(target = worker,args=(new_clint, dest_addr))
    clint.start()




