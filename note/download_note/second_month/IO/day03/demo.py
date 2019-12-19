# 文件描述符
f = open('file')
print("fd:",f.fileno())

# 文件管理函数
import os
print("文件大小:",os.path.getsize('file'))
print("查看目录内容：",os.listdir('.'))
print("文件存在么：",os.path.exists('./file'))
print("是一个普通文件：",os.path.isfile('file'))
print("删除一个文件：",os.remove('file'))

