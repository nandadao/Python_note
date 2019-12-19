"""
    空洞文件
"""


f = open("file", "wb")
f.write(b"START")

# 以末尾为基准，向后移动10M
f.seek(1024*1024*10, 2)


f.write(b"END")

f.close()


