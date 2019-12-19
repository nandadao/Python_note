"""
    练习：
        使用进程池，备份一个目录，该目录中包含若干个普通文件，
    提示：
        os.listdir()得到目录下所有文件
        os.path.getsize()获取文件大小
        os.mkdir()创建一个目录
    要求：
        至少同时拷贝４个文件，并且只能创建４个进程，使用进程池Pool(4)
        事件：拷贝一个文件就是一个事件


    进阶版：拷贝过程中实时打印拷贝的百分比　０％　－－　％１００
           不断获取已经拷贝的大小，flush()
           然后，已经拷贝的/源文件大小　* 100%
"""

from multiprocessing import Pool, Queue
import os

q = Queue(3)


# 拷贝一个文件
# 拷贝啥，从哪拷，拷到哪
def copy_file(file, old_dir, new_dir):
    fr = open(old_dir+"/"+file, "rb")
    fw = open(new_dir+ "/"+file, "wb")
    while True:
        data = fr.read(1024*10)
        if not data:
            break
        n = fw.write(data)
        q.put(n)  # 字节数传入消息对垒
    fr.close()
    fw.close()

def main():
    """
    创建进程池，调用拷贝文件的函数作为事件
    """
    base_path = "/home/tarena/"  # 基准目录
    dir = input("Dir:")  #要备份的目录
    old_dir = base_path + dir  # 要备份的目录的全路径
    new_dir = old_dir + "-备份"  # 拷贝到这里
    os.mkdir(new_dir)  # 创建新地址
    file_list = os.listdir(old_dir)  # 拷这些文件

    # 获取目录的总大小
    total_size = 0
    for i in file_list:
        total_size += os.path.getsize(old_dir+"/"+i)


    # 创建进程池
    pool = Pool(4)
    for file in file_list:
        pool.apply_async(copy_file, args=(file, old_dir, new_dir))

    pool.close()


    print("目录大小：%.2fM"%(total_size/1024/1024))
    copy_size = 0  #　已经拷贝的大小
    while copy_size < total_size:
        copy_size += q.get()
        print("拷贝了　%.1f%%"%(copy_size/total_size*100))

    pool.join()


if __name__ == '__main__':
    main()




















# from multiprocessing import Pool
# import os
#
#
#
# file_addr = "/home/tarena/hello/"
# file_num = os.listdir(file_addr)
# # print(file_num)　　　['b.txt', 'e.txt', 'd.txt', 'c.txt', 'a.sql', 'f.txt']
# os.mkdir("copy_file")
#
#
# def copy_1_file(file_name):
#     fr = open(file_addr+file_name, "rb")
#     fw = open("copy_file"+file_name, "wb")
#     fw.write(fr.read())
#     fr.close()
#     fw.close()
#
#
#
#
# pool = Pool(4)
#
#
# for i in range(4):
#
#     pool.apply_async(func=copy_1_file, args=(file_name, ))























