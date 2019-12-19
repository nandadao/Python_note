"""
    字符串字面值
        练习：exercise06
"""

name01 = "悟空"
name02 = '悟空'
# 可见即所得
name03 = '''
    悟

空'''
print(name03)
name03 = """悟空"""

message = '我是"齐天大圣"。'
message = "我是'齐天大圣'。"
message = '''我是'齐"天"大圣'。'''

# 转义符:改变原始含义的特殊符号
# \"  \'  \n  \\   \t Tab水平制表格
message = "我是\"齐天\n大圣\"。"
print(message)

url = "C:\\arogramFiles(x86)\\breative\ProdCat"
# 原始字符：字符串中没有转义符
url = r"C:\arogramFiles(x86)\breative\ProdCat"
print(url)

message = "你好\tqtx"
print(message)

# 字符串格式化
# "..%s..%d..%f.."%(数据1,数据2,数据3)
# 在字符串中插入变量
# %f 四舍  六入  五平分
name = "唐僧"
age = 28

print("我叫:" + name + ",今年" + str(age) + "岁了.")
print("我叫:%s,今年%d岁了." % (name, age))
