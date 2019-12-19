"""
    ３．一个目录，在目录下有若干个文件（有子目录和普通文件），
    编程：该目录下的　普通文件　
         复制到家目录下的"备份"这个目录中/home/tarena/备份（这个目录可以提前创建好）
"""
import os

ADDR = "/home/tarena/note/my_note/second_month/day01/"

target_addr = "/home/tarena/备份/"

# 查看文件列表
list_dir = os.listdir(ADDR)
print(list_dir)

for item in list_dir:
    # 判断文件类型
    type_file = os.path.isfile(ADDR+item)
    if type_file:
        f = open(ADDR+item, "rb")
        fr = open(target_addr+item, "wb")
        while True:
            data = f.read(1024)
            if not data:
                break
            fr.write(data)


        fr.close()
        f.close()
























