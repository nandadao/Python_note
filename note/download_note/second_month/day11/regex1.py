"""
正则演示2  生产match对象
"""
import re

s = "今年是2019年12月10日，" \
    "2019年初的目标实现了么，" \
    "保持95斤的愿望还记得么"
pattern = r'\d+'

# 获取匹配内容的迭代器
# result = re.finditer(pattern,s)
# for i in result:
#     # 迭代得到每处匹配内容的match对象
#     print(i.group()) # 获取match对象对应数值


# 完全匹配
# obj = re.fullmatch('.+',s)
# print(obj.group())

# 匹配开始位置
obj = re.match('\w+',s)
print(obj.group())

# 匹配第一处
obj = re.search('\d+',s)
print(obj.group())









