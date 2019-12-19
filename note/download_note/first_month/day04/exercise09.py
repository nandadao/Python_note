"""
    练习
    1. 创建列表，存储“水星”,"金星","地球","木星","天王星"
    2. 在列表中末尾追加"海王星",在地球后面插入"火星"
    3. 打印距离太阳最近的行星(列表第一个元素)
    4. 打印距离太阳最远的行星(列表最后一个元素)
    5. 打印太阳距离到地球中间的所有行星(一行一个)
    6. 将地球后面的所有行星删除。
"""

list_planets = ["水星", "金星", "地球", "木星", "天王星"]
list_planets.append("海王星")
list_planets.insert(3, "火星")
print(list_planets[0])
print(list_planets[-1])
for item in list_planets[:2]:
    print(item)
del list_planets[3:]
print(list_planets)
