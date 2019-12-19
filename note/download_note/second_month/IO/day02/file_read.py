"""
file_read.py
读文件操作
"""

# 打开文件
f = open('/home/tarena/examples.desktop','r') # 默认r

# 读文件
"""
每次读取100字符  读主目录下 examples.desktop文件内容，并打印出来
"""
# while True:
#     s = f.read(100)
#     if not s:
#         # 当s为空则到了文件结尾
#         break
#     print(s,end='')
# s = f.read(100)
# s = f.read()
# print("读取内容:",s)

# 读取一行
data = f.readline()
print("一行内容：",data)

# 读取若干行
data = f.readlines(24)
print("多行内容：",data)

# 迭代特性
for i in f:
    print(i)  # 每次获取一行


f.close()