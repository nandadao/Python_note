"""
    刷新缓冲区
    buffer.py
"""

f = open("file", "w", 1)
while True:
    data = input(">>")
    if not data:
        break
    f.write("abc\n")
    # f.flush()   # 自己刷新缓冲

f.close()





