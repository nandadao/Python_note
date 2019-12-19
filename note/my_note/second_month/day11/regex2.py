"""
    match对象属相方法
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
# 获得match对象
obj = regex.search("abcdefgh123", 0, 9)


# 属相变量
print(obj.pos)   # 目标字符串的开始位置
print(obj.endpos) # 目标字符串结束位置
print(obj.lastgroup)  # 最后一组的名称
print(obj.lastindex)  # 最后一个组的组号



print("================================")
# 属性方法
print(obj.span())   # 匹配内容的起止位置
print(obj.start())   # s[start():end()
print(obj.end())
print(obj.groupdict())  # 捕获组字典
print(obj.groups())  # 子组对应内容
print(obj.group())   # 获取match对象锁对应的内容
print(obj.group(1))
print(obj.group("pig"))

























