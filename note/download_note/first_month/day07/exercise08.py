# 练习2: 定义函数，将一维列表所有元素打印在终端(一行一个)
def print_list(list_target):
    for item in list_target:
        print(item)

list01 = [45,5,65,678]
# 调试：F7 逐语句  F8 逐过程
print_list(list01)
print_list( [45,5,65,678])