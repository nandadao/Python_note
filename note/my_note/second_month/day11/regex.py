"""
    regex.py re模块功能演示
"""
import re

# 目标字符串
s = "Alex:1997,Sunny:1999"
# 正则表达式
pattern = r"(\w+):(\d+)"

# re模块调用
l = re.findall(pattern, s)
# findall()如果有子组，那么只获取子组部分
# [('Alex', '1997'), ('Sunny', '1999')]
print(l)

# complie对象
regex = re.compile(pattern)
l = regex.findall(s, 0, 12) # s[0:12] 作为匹配字符串
print(l)
print("=====================================")

# 分割字符串
l = re.split(r"[:,]", s, 2)
print(l)
# ['Alex', '1997', 'Sunny:1999']

# 字符串替换
s = re.sub(r":", "-", s,1)
print(s)














