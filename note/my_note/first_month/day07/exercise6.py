# 扑克牌
# 数字

# 1.打印扑克牌
# list_num = ["A", "2", "3", "4", "5","6","7","8","9","10","J","Q","K"]
# list_h = ["红桃","黑桃","方片","梅花"]
# for i in list_h:
#     for j in list_num:
#         print(i,j)





# 2.一个骰子有 1-- 6个数字
# 请打印出3个骰子素有的数字

# for i in range(1, 7):
#     for j in range(1, 7):
#         for k in range(1, 7):
#             print(i, j , k)

list_s = [(i,j,k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]
# for i in list_s:
#     print(i)
print(list_s)
