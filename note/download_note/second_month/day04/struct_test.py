"""
struct_test.py
struct模块示例
"""

import struct

# 生成格式对象i-->int  f-->float  s-->bytes
st = struct.Struct('i4sif')

# 数据打包
data = st.pack(1,b'Lily',172,8)
# print(data)

# st = struct.Struct('i3sif')
# print(st.unpack(data))
print(struct.unpack('i4sif',data))