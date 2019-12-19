# 1. 打印扑克牌
# 花色:["红桃","黑桃","方片","梅花"]
# 数字:["A","2","3","4","5","6","7","8","9","10","J","Q","k"]
list_suit = ["红桃", "黑桃", "方片", "梅花"]
list_number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k"]
list_poket = [suit + number for suit in list_suit for number in list_number]
print(list_poket)

# 2. 一個色子有1--6個數字range(1,7)
# 請打印出3个色子所有的数字
# list_result = []
# for x in range(1,7):
#     for y in range(1,7):
#         for z in range(1,7):
#             list_result.append((x,y,z))
list_result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(list_result)
