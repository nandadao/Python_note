"""
    3.画出下列代码内存图
        图一
        list01 = [
                10,{101:"悟空"}
            ]
        list02 = list01[:] # 切片
        list01[1][101] = "孙悟空"
        print(list02)
"""
# list01 = [
# 	10, {101: "悟空"}
# ]
# list02 = list01
# list01[1][101] = "孙悟空"
# print(list02)
#
# # 结果是：[10, {101: '孙悟空'}]

"""
        图二
        dict01 = {
            "唐僧":[25, "男"],
            "八戒":[28, "男"],
        }
        dict02 = dict01
        dict01["八戒"][0] = 29
        print(dict02)
"""
# dict01 = {
# 	"唐僧": [25, "男"],
# 	"八戒": [28, "男"],
# }
# dict02 = dict01
# dict01["八戒"][0] = 29
# print(dict02)

# {'八戒': [29, '男'], '唐僧': [25, '男']}

"""
    4.定义数据结构存储以下信息：
        1.存储多个人的多个 爱好
            "qtx":"编码","看书","跑步"
            "lzmly":"看电影","编码","美食","唱歌"  
            （想想数据结构）
        2.打印qtx的所有爱好（一行一个）
          打印所有人的所有爱好（一行一个）
"""
# dict_like = {
#     "qtx":["编码","看书","跑步"],
#     "lzmly":["看电影","编码","美食","唱歌"]
# }
#
# for i in dict_like["qtx"]:
#     print("qtx",i)
#
# # 所有人的爱好
# for item in dict_like:
#     for i in dict_like[item]:
#         print(item, i)


"""
	    5.定义数据结构存储以下信息：
        1.存储多个城市的多个景区和美食
            "北京"
                "景区":"天安门","天坛","故宫"
                "美食":"驴打滚","豆汁"
            "四川"
                "景区":"九寨沟","宽窄巷子"
                "美食":"火锅","串串香"
        2.打印北京的所有美食（一行一个）
          打印所有城市（一行一个）
          （扩展）打印所有城市的所有景区（一行一个）
"""

dict_city = {
    "北京": {
        "景区": ["天安门", "天坛", "故宫"],
        "美食": ["驴打滚", "豆汁"]
    },
    "四川": {
        "景区": ["九寨沟", "宽窄巷子"],
        "美食": ["火锅", "串串香"]
    },
}

for i in dict_city["北京"]["景区"]:
    print("北京美食", i)

for item in dict_city:
    print("城市有：", item)

for item in dict_city:
    for i in dict_city[item]["景区"]:
        print(item, i)