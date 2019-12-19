"""
温度转换器
   摄氏度 = (华氏度 - 32 ) / 1.8
   已知：摄氏度
   计算：华氏度

   公式：华氏度 = 摄氏度 × 1.8 + 32
"""
degree_centigrade = float(input("请输入摄氏度："))
degree_fahrenheit = degree_centigrade * 1.8 + 32
print("华氏度是" + str(degree_fahrenheit))
