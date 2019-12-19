"""
    输入：abcdaaa
    输出：每个字符的数量
        a:2
        b:2
        c:3
"""
str_zimu = "ABCACDECB"
dict_01 = {}
for i in str_zimu:
    if i not in dict_01:
        dict_01[i] = 1  # 这里的思想是，如果这个键不再字典中，则添加
    else:
        dict_01[i] += 1 # 这里的是，如果存在，则修改，键的值

print(dict_01)
for key,value in dict_01.items():
    print("%s:%d"%(key, value))








