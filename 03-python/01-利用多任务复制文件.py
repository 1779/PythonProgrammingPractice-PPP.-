from multiprocessing import Pool,Manager
import os
import time

def copy_file(name,old_forder_name,new_forder_name,queue):
    
    fr = open(old_forder_name + "/" + name)
    fw = open(new_forder_name+"/"+name,"w")
    
    content = fr.read()
    fw.write(content)
    
    fr.close()
    fw.close()

    queue.put(name)
    time.sleep(0.2)


def __main__():
    #1.获取要复制的文件夹名称
    old_forder_name = input("请输入要复制的文件夹名字：")

    #2.创建一个新的文件夹
    new_forder_name = old_forder_name + "-复件" 
    os.mkdir(new_forder_name)

    #print(new_forder_name)

    #3.获取old forder里面所有文件的名
    file_names = os.listdir(old_forder_name)
    #print(file_names)

    #4.使用多进程将源文件夹里面的文件 copy 到新文件夹中
    pool = Pool(5)
    queue = Manager().Queue()

    for name in file_names:
        pool.apply_async(copy_file,args=(name,old_forder_name,new_forder_name,queue))
    
    num = 0
    all_num = len(file_names)
    print("-"*50)
    while True:
        queue.get()
        num += 1
        copy_rate = num/all_num
        print("\r当前copy的进程是:%d %%" %(copy_rate*100), end="")
        if num == all_num:
            print("")
            break


if __name__ == "__main__":
    __main__()

