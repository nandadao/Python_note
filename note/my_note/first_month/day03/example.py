# 计算总共的秒数
# hour = int(input('请输入小时数：'))
# minute = int(input('请输入分钟数：'))
# second = int(input('请输入秒数：'))
#
# result = hour * 3600 + minute * 60 + second
# print("总秒数是："+str(result))

# total_second = int(input("请输入总秒数："))
# hour = total_second // 60 // 60
# second = total_second % 60
# minute = total_second // 60 % 60
# print(hour, minute, second)

# degree_centigrade = float(input("请输入摄氏度："))
#
# degree_fanrenheit = degree_centigrade * 1.8 + 32
#
# print("华氏度：" + str(degree_fanrenheit))
#
# n = 1 + \
#     2 + 3 \
#     + 4


# sex = input("请输入性别：")
# if sex == "男":
#     print("您好，先生！")
# if sex == "女":
#     print("您好，女士！")
# else:
#     print("性别未知")


# 根据商品单价
# 1. 获取数据
# str_price = input("请输入商品单价：")
# float_price = float(str_price)
# str_count = input("请输入数量：")
# int_count = int(str_count)
# money = float(input("请输入金额："))
# # 2. 逻辑计算
# result = money - float_price * int_count
# # 3. 显示结果
# print("应该找回:" + str(result))

# float_price = float(input("请输入商品单价:"))
# int_count = int(input("请输入数量："))
# money = float(input("请输入金额："))
# result =  money - float_price * int_count
# if result >= 0:
#     print("应该找回：" + str(result))
# else:
#     print("钱不够！")


# jidu = input("请输入一个季度：")
# if jidu == "春天":
#     print("1月2月3月")
# elif jidu == "夏天":
#     print("4月5月6月")
# elif jidu == "秋天":
#     print("7月8月9月")
# elif jidu == "冬天":
#     print("10月11月12月")
# else:
#     print("请输入正确的季度")

# 练习：获取数字/运算符/数字，根据运算符打印结果
#   如果运算符是+ - * / 打印结果，否这打印运算符有无

# num1 = float(input("请输入第一个数字："))
# num2 = float(input("请输入第二个数字："))
# yunsuanfu = input("请输入一个运算符：")
# if yunsuanfu == "+":
#     result = num1 + num2
#     print(result)
# elif yunsuanfu == "-":
#     result = num1 - num2
#     print(result)
# elif yunsuanfu == "*":
#     result = num1 * num2
#     print(result)
# elif yunsuanfu == "/":
#     result = num1 / num2
#     print(result)
# else:
#     print("运算符有误")


# 在终端中录入四个同学的体重
# 打印最沉的体重
#   思路：假设地一个就是最大的
#          以此与后面的元素进行比较
#           发现更大的，则替换假设的

# num1 = float(input("请输入第一个同学的体重："))
# num2 = float(input("请输入第二个同学的体重："))
# num3 = float(input("请输入第三个同学的体重："))
# num4 = float(input("请输入第四个同学的体重："))
# max = num1
# if max  < num2:
#     max = num2
# if max < num3:
#     max = num3
# if max < num4:
#     max = num4
# print("最大的是"+str(max))

# 在终端中录入一个成绩，打印等级
# 优秀 良好 及格 不及格  成绩有误

# score = float(input("请输入一个成绩："))
# # if 0 <= score <= 59:
# if score >= 0 and score <= 59:
#     print("不及格")
# elif 60 <= score <= 79:
#     print("及格")
# elif 80 <= score <= 89:
#     print("良好")
# elif 90 <= score <= 100:
#     print("优秀")
# else:
#     print("成绩有误")


# if score < 0 or score > 100:
#     print("成绩有误")
#

# 在终端中，录入一个月份，打印天数
# 1 3 5 7 8 10 12 --> 31天
# 2 --> 28
# 4 6 9 11 --> 30天
# 月份有误

# month = int(input("请输入一个月份："))
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print("这个月份有30天")
# elif month == 2:
#     print("这个月份有28天")
# else:
#     print("这个月份有31天")


# 练习一：在终端中录入一个整数，如果是奇数赋值为state赋值为奇数，
#   否则赋值为偶数
# num = int(input("请输入一个整数："))
# state = "奇数" if int(input("请输入一个整数：")) % 2  else "偶数"
# print(state)



# 练习二：在终端中录入一个年份，如果是润年为变量day
#   赋值29,否则复制为28
# year = int(input("请输入一个年份："))
# day = 29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28
# print(day)

# (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 判断是否为润年


# while 1:
#     jidu = input("请输入一个季度：")
#     if jidu == "春天":
#         print("1月2月3月")
#     elif jidu == "夏天":
#         print("4月5月6月")
#     elif jidu == "秋天":
#         print("7月8月9月")
#     elif jidu == "冬天":
#         print("10月11月12月")
#
#     else:
#         print("请输入正确的季度")
#     if jidu == 'q':
#         print("已退出")
#         break



# count = 5
# while count < 10:
#     print(count)
#     count += 1
#

# 练习一：输出0 1 2 3
# count = 0
# while count < 4:
#     print(count)
#     count += 1
# 练习二：输出 2 4 6 8 10
# count = 2
# while count < 11:
#     print(count)
#     count += 2
# 练习三：输出1 4 7 10
# count = 1
# while count < 11:
#     print(count)
#     count += 3
# 练习四：输出8 7 6 5
# count = 8
# while count > 4:
#     print(count)
#     count -= 1
# 练习五：输出-1 -2 -3 -4 -5
# count = -1
# while count > -6:
#     print(count)
#     count -= 1


# 一张纸的厚度是0.01mm,请计算，对折多少次超过8848.43m
# one_pice = 0.00001
# count = 0
#
# while one_pice <= 8848.43:
#     # 第一次 0.001 + 0.001
#     # 第二次
#     one_pice = one_pice * 2
#     count += 1
#     print(count, one_pice)
# print(count)

# 猜数字游戏
# 程序产生一个1--100之间的随机数，让用户不断猜，直到猜出来
# import random  # 准备随机工具
# number = random.randint(1, 100)
# # print(number)
# count = 0
# # print(number)
# while 1:
#     count += 1
#     your_num = int(input("请输入您猜的数："))
#     if your_num > number:
#         print("您猜大了,请重新输入")
#
#     elif your_num < number:
#         print("您猜小了,请重新输入")
#
#     else:
#
#         print("您猜对了，总共猜了"+str(count),"次")
#         break



# 最多猜五次，
import random  # 准备随机工具
number = random.randint(1, 100)
# print(number)
count = 0
# print(number)
while count < 5:
    count += 1
    your_num = int(input("请输入您猜的数："))
    if your_num > number:
        print("您猜大了,请重新输入")

    elif your_num < number:
        print("您猜小了,请重新输入")

    else:

        print("您猜对了，总共猜了"+str(count),"次")
        break
else:
    print("笨死了")






















