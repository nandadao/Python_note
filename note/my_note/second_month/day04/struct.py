"""
    struct模块打包数据
"""

import struct

# 生成格式对象　　i->int  f---> float  s--> bytes
st = struct.Struct("i4sif")

# 数据打包
data = st.pack(1, b"Lily", 172, 8)
# print(data)

# 解析数据
print(st.unpack(data))
print(type(st.unpack(data)))















