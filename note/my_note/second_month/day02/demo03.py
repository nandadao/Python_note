"""
    文件的写操作
    file_write.py
"""

f = open("file", "a")


# 写操作
# a = f.write("hi，死鬼\n".encode())
# b = f.write("哎呀，砸了\n".encode())
# print("hi，死鬼\n".encode())
# print(a)
# print(b)

f.writelines(["hahaha\n", "哈哈哈\n", "嘿嘿\n"])
print("文件已经写入")




f.close()

















