# dict_like = {
#     "qtx":["编码","看书","跑步"],
#     "lzmly":["看电影","编码","美食","唱歌"]
# }
#
# # for i in dict_like["qtx"]:
# #     print("qtx",i)
#
# # 所有人的爱好
# for item in dict_like:
#     for i in dict_like[item]:
#         print(item, i)

dict_city = {
    "北京":{
        "景区":["天安门","天坛","故宫"],
        "美食":["驴打滚","豆汁"]
            },
    "四川":{
        "景区":["九寨沟","宽窄巷子"],
        "美食":["火锅","串串香"]
        },
}

for i in dict_city["北京"]["景区"]:
    print("北京美食",i)

for item in dict_city:
    print("城市有：", item)

for item in dict_city:
    for i in dict_city[item]["景区"]:
        print(item, i)









