# 练习:定义函数fun01,统计被调用的次数.
count = 0

def fun01():
    global count
    count += 1

fun01()
fun01()
fun01()
print("总共执行了%d次" % count)
