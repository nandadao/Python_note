"""
buffer.py
缓冲区示例
"""
f = open('file','w',1) # buffering=1表示行缓冲
while True:
    data = input(">>")
    if not data:
        break
    f.write("abc\n")
    # f.flush() # 自己刷新缓冲

f.close()