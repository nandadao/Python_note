"""
    练习:在终端中录入四个同学体重
        打印最沉的体重。
        55   43   36  57
        心中
        思路：
            假设第一个就是最大的
            依次与后面元素进行比较
            发现更大，则替换假设的。
"""
wight01 = float(input("请输入第1个同学体重："))
wight02 = float(input("请输入第2个同学体重："))
wight03 = float(input("请输入第3个同学体重："))
wight04 = float(input("请输入第4个同学体重："))
#  55   43   36  57
max_value = wight01
if max_value < wight02:
    max_value = wight02
if max_value < wight03:
    max_value = wight03
if max_value < wight04:
    max_value = wight04
print(max_value)
