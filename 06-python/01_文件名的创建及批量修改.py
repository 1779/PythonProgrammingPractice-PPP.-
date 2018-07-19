


import os

print("-"*50)

#创建文件
def mk_file():
    """文件的创建"""
    attention="--------现在开始创建文件--------"
    print(attention)
    os.chdir(now_folder)
    i = 0
    name = input("请输入要创建的文件名：")
    name_number = int(input("请输入要创建文件的个数："))
    
    while i < name_number:
        file_name =name + str(i+1) + ".txt" 
        f=open(file_name,"w")
        f.write("0")
        i+=1

#获得文件夹
def get_folder():
    new_folder = input("请输入要选择的文件夹：")
    return new_folder


#获取文件名
def get_name():
    name=input("请输入要提取的文件名：")


def change_names():
    #global old_name
      
    global now_folder
    file_names=os.listdir(now_folder)
    os.chdir(now_folder)
    for name in file_names:
        #new_name='【XXXXX出品】'+name
        os.rename(name,"【xxxx出品】"+name)



now_folder = get_folder()

change_names()


