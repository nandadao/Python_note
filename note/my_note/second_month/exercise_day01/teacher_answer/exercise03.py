"""
    ３．一个目录，在目录下有若干个文件（有子目录和普通文件），

    编程：该目录下的　普通文件　复制到家目录下的"备份"这个目录中/home/tarena/备份（这个目录可以提前创建好）
"""
import os

# 备份的目录
DIR = "/home/tarena/备份/"
dir = input(">>")

# 如果输入的路径中没有斜杠，自动加上一个
if dir[-1] != "/":
    dir += "/"


#　拷贝文件
def copy(file):
    fr = open(dir+file, "rb")
    fw = open(DIR+file, "wb")
    while True:
        data = fr.read(1024)
        if not data:   #读到文件结尾，会读到一个空
            break
        fw.write(data)
    fr.close()
    fw.close()


#　选择要拷贝的文件
def main():
    file_list = os.listdir(dir)
    for file in file_list:
        if os.path.isfile(dir+file):
            copy(file)


if __name__ == "__main__":
    main()

























