"""
file_open.py
文件打开方式
"""

# 打开文件
"""
文本文件可以用文本或者二进制方式打开
二进制文件一定要用二进制方式打开
"""
f = open('file','r')  # 只读
f = open('file','w')  # 只写
f = open('file','a')  # 追加
print(f)
# 读写

# 关闭文件
f.close()
