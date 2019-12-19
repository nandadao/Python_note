

from socket import *
import struct

st = struct.Struct("i16sif")

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("127.0.0.1", 9999))

f = open("student.txt", "a")

while True:
    data, addr = s.recvfrom(1024)
    # 对数据解包处理  (1, b"Lily ,15, 1.66)
    data = st.unpack(data)
    print(data[1].decode())
    # 将数据写入文件,%-10s左对齐占十个宽度
    info = "%d %-10s %d %.2f\n"%(data[0], data[1].decode().strip("\0"), data[2], data[3])

    f.write(info)
    f.flush()

f.close()
s.close()













