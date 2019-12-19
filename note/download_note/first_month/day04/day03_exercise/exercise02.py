"""
在终端中获取年龄，显示
   婴儿(0-1) 儿童(2-13)  青少年(14-20)
   成年人(21-65) 老年人(66-150) 那是不可能的(以上)
   要求：重复判断，直到年龄录入空停止。
"""
while True:
    str_age = input("请输入年龄：")
    if str_age == "":
        break
    int_age = int(str_age)
    if int_age < 0:
        print("输入有误")
    elif int_age <= 1:
        print("婴儿")
    elif int_age <= 13:
        print("儿童")
    elif int_age <= 20:
        print("青少年")
    elif int_age <= 65:
        print("成年人")
    elif int_age <= 150:
        print("老年人")
    else:
        print("那是不可能的")
