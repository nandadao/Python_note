"""
BMI:用体重(千克)除以身高(米)的平方。
   根据BMI打印身体状况
   小于18.5(不包含) --> 体重过低
   18.5(包含) -- 24(不包含) --> 正常
   24(包含) -- 28(不包含) --> 超重
   28(包含) -- 30(不包含) --> 一度肥胖
   30(包含) -- 40(不包含) --> 二度肥胖
   大于等于40 --> 重度肥胖
"""
height = float(input("请输入身高（米）："))
weight = float(input("请输体重（千克）："))
bmi = weight / height ** 2
if bmi < 18.5:
    print("体重过轻")
elif bmi < 24:
    print("正常")
elif bmi < 28:
    print("超重")
elif bmi < 30:
    print("一度肥胖")
elif bmi < 40:
    print("二度肥胖")
else:
    print("重度肥胖")
