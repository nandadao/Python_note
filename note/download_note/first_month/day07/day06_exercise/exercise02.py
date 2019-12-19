"""
    4.定义数据结构，存储以下信息：
    -- 多个人的多个爱好
    "qtx":"编码","看书","跑步"
    "lzmly":"看电影","编码","美食","唱歌"
      打印qtx的所有爱好(一行一个)
      所有人的所有爱好(一行一个)
"""
dict_info01 = {
    "qtx": ["编码", "看书", "跑步"],
    "lzmly": ["看电影", "编码", "美食", "唱歌"]
}

for item in dict_info01["qtx"]:
    print(item)

for key in dict_info01:# 所有人
    for item in dict_info01[key]:# 某个人的喜好
        print(item)
