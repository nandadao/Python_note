"""
    1 3  5 7
    元组
"""
month = int(input("请输入："))
if month < 1 or month > 12:
    print("输入有无")
elif month == 2:
    print("28天")
elif month in (4, 6, 9, 11):
    print("30天")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31天")












