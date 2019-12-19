"""
    文件函数
"""

import os
print(os.path.getsize("file"))

print("查看目录内容",os.listdir("."))

print("查看文件是否存在", os.path.exists("file"))

print("返回是否普通文件", os.path.isfile("file"))

os.remove("file")



