"""
    文件偏移量
    seek.py
    注意：r  w 打开文件默认文件偏移量在开头
         a 打开文件偏移量在结尾
         读写使用的是一个偏移量
"""
f = open("file", "w+")

f.write("hello world ande you")
f.flush()
print("文件偏移量：", f.tell())  # 查看偏移量
# 移动一下偏移量
f.seek(5, 0)
f.write("你好")
data = f.read()
print(data)





f.close()












