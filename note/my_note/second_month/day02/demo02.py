"""
    file_reda.py
    读文件操作
"""

# 一打开文件
# f = open("file", "r")  # 默认r
#
# s = f.read(100)
# s = f.read()
# print("读取内容是",s)


# 每次读取100字符，读主目录下  examples.desktop文件内容，并打印出来

f = open("/home/tarena/examples.desktop", "r")

# while f.read(100):
#     s = f.read(100)
#     print("读取内容：", s)

# while True:
#     s = f.read(100)
#     # 当s为空则到了文件结尾
#     if not s:
#         break
#     print(s, end="")

# data = f.readline()
# print("一行内容:", data)

# 读取若干行
# data = f.readlines(20)
# print("多行内容：", data)

# 迭代特性
for i in f:
    print(i)  # 每次获取一行


f.close()








