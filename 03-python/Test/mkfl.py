import os

file_name_list=[]
for i in range(200):
    file_name = "test"+str(i)+".txt"
    file_name_list.append(file_name)

#print(file_name_list )
for i in file_name_list:
    new_file = open(i,"w")
    new_file.write("""-----------------------
                    此文件为了验证多文件copy程序而创立
                    文件名为：%s"""%i)

