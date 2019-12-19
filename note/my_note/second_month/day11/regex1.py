"""
    regex1 正则表达式
"""
import re

s = "今年是2019年12月10日，2019年初的目标实现了吗" \
    "保持95斤的愿望还记得吗"

pattern = r"\d+"

# 获取匹配内容的迭代器
result = re.finditer(pattern, s)
# for i in result:
    # 迭代得到每处匹配内容的match对象
    # < _sre.SRE_Match object; span = (3, 7), match = '2019' >
    # print(i.group())  # 2019 ...


# 完全匹配
# obj = re.fullmatch(r".+", s)
# print(obj)


# 匹配开始位置
obj = re.match("\w+", s)
print(obj.group())


# 匹配第一处
obj = re.search("\d+", s)
print(obj.group())




















