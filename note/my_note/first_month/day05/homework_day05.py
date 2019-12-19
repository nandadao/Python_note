# 3.
# 将1970年到2050年之间所有润年，存入列表

# 闰年判断方法
# year = int(input("请输入年份："))
# result = year % 4 == 0  and  year % 100 != 0 or year % 400 == 0
# print(result)


# list_year = []
# for i in range(1970, 2051):
# 	if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
# 		list_year.append(i)
# list_year = [i for i in range(1970, 2051) if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]
# print(list_year)


"""
    4.彩票
        双色球
            红色：6个  1-33  不能重复
            蓝色：1个  1-16
        问：
            一：随机产生一注彩票（列表）  （in）
            二：在终端中购买一注彩票
                “请输入第1个红球号码：”
                “号码超过范围”  （如果超出了）
                “请输入第2个红球号码：”
                “已经存在了” （如果重复了）


                “请输入一个红色球”
"""
# 一
# import random
#
# red_lottery = []
# blue_lottery = []
# while len(red_lottery) < 6:
# 	red = random.randint(1, 33)
# 	if red not in red_lottery:
# 		red_lottery.append(red)
#
# blue = random.randint(1, 16)
# blue_lottery.append(blue)
#
# print("随机彩票为",red_lottery+blue_lottery)

# 二

# red_lottery = []
# blue_lottery = []
# count = 1
# while count <= 6:
# 	red_boll = int(input("请输入第%d个红球号码" % count))
# 	if red_boll not in list(range(1, 34)):
#
# 		print("号码超过范围")
# 		continue
# 	elif red_boll not in red_lottery:
# 		red_lottery.append(red_boll)
# 		# print(red_lottery)
# 		count += 1
# 		continue
# 	else:
# 		print("已经存在了")
# while len(blue_lottery) < 1:
# 	blue_boll = int(input("请输入一个红球号码："))
# 	if blue_boll < 1 or blue_boll > 16:
# 		print("号码超过范围了")
# 		continue
# 	else:
# 		blue_lottery.append(blue_boll)
#
# print("您选的彩票号码为", red_lottery + blue_lottery)

# list_ticket = []
# while len(list_ticket) < 6:
#     number = int(input("请输入%d" % (len(list_ticket)+1)))
#     if number not in list_ticket:
#         print("已经存在")

















