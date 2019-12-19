"""
 写一个程序，实现对一个文件进行拷贝

       * input() 输入一个文件位置
       * 将该文件'拷贝'到主目录下
       * 文件可能是文本文件也可能是二进制文件
       * 文件可能比较大，不允许一次性读取

温馨提示： 从源文件读取内容，写入到目标新文件中
字符串函数，进制转换
"""
home = "/home/tarena/"

img = input(">>")

# 打开源文件
fr = open(img,'rb')

#提取文件名称
filename = img.split('/')[-1]

# 打开新的文件
fw = open(home+filename,'wb')

# 边读边写
while True:
    data = fr.read(1024)
    if not data:
        break
    fw.write(data)

fr.close()
fw.close()




