# 练习:将下列代码，定义成函数。
def print_rectangle(r_count,c_count,char):
    # 外层循环控制行
    for r in range(r_count):
        # 内层循环控制列
        for c in range(c_count):
            print(char, end=" ")
        print()  # 换行

print_rectangle(2,3,"#")

