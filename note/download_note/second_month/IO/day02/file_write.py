"""
file_write.py
文件写演示
"""

# f = open('file','wb')
f = open('file','a')

# 写操作
# f.write("hi,死鬼\n".encode())
# f.write("哎呀，干啥\n".encode())

f.writelines(['hahaha\n','呵呵呵\n','嘿嘿嘿'])

f.close()