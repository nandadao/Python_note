"""
    函数内存分配
    练习:exercise01
"""

# 1. 将函数代码存储到内存代码区
def fun01():
    a = 10

# 2. 调用函数时，在内存中开辟一块空间(栈帧)，存储在函数中定义的变量。
fun01()
# 3. 调用结束，栈帧释放。

def fun02(p1,p2):
    # 修改的是栈帧中变量p1存储的地址
    p1 = 200
    # 修改的是p2指向的列表元素
    p2[0] = 200

g01 = 100
g02 = [100]
# 将g01存储的100地址，与g02存储的列表地址，传入函数。
fun02(g01,g02)
print(g01)# ? 100
print(g02)# ?





