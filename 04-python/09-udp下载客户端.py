from socket import *
import struct
import sys
import time

"""
if len(sys.argv)!=2:
    print("-"*30)
    print("tips:")
    print("python xxx.py 192.168.1.1")
    print("-"*30)
    exit()

else:
    ip = sys.argv[1]
"""

ip = input("请输入对方ip：")
port = int(input("请输入对方端口："))
file_name = input("请输入要下载的文件名：")
name_len = len(file_name)
first_temp ="!H"+str(name_len)+"sb5sb"
file_bname = file_name.encode("utf-8")

udp_socket = socket(AF_INET,SOCK_DGRAM)
cmd_buf = struct.pack(first_temp,1,file_bname,0,b"octet",0)
send_addr = (ip,port)
udp_socket.sendto(cmd_buf,send_addr)

p_num = 0
recv_file = ""
start_time = time.time()

while True:
    recv_data,recv_addr = udp_socket.recvfrom(1024)
    len_recv_data = len(recv_data)
    cmd_tuple = struct.unpack("!HH",recv_data[:4])
    cmd = cmd_tuple[0]
    current_pack_num = cmd_tuple[1]

    if cmd == 3:

        if current_pack_num ==1:
            recv_file = open(file_name,"ba")

        if p_num+1 == current_pack_num:
            recv_file.write(recv_data[4:])
            p_num += 1
            if p_num < 2*1024:
                print("\r正在下载：%.2f K "%float(p_num*0.5),end = "B")
            elif p_num < 2*1024*1024 :
                print("\r正在下载：%.2f M "%float(p_num*0.0005),end = "B")
            else :
                print("\r正在下载：%.2f G "%float(p_num*0.0000005),end = "B")

            ack_buf = struct.pack("!HH",4,p_num)
            udp_socket.sendto(ack_buf,recv_addr)

        if len_recv_data < 516:
            recv_file.close()
            all_time = time.time() - start_time
            print("已经成功下载!")
            if all_time < 60:
                print("-----共用时：%.2f秒-----"%all_time)
            elif all_time < 60*60:
                minutes = all_time // 60
                seconds = all_time % 60
                print("-----共用时：%d分 %d秒-----"%(minutes,seconds))
            elif all_time >= 60*60:
                hours = all_time // 3600
                minutes = (all_time - 60*hours) //60
                seconds = (all_time - 60*hours - 60*minutes)
                print("-----共用时：%d 小时 %d分 %d秒-----"%(hours,minutes,seconds))
            break


    elif cmd == 5:
        print("error:%d"%current_pack_num)
        break

udp_socket.close()

