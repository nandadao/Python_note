# 这是一个解决列表里套列表的程序
# 例如[1, [2, [5, 9]]]
def print_list(x):
    for i in x:
        if type(i) == list:
            print_list(i)


        else:
            print(i)


l = [1, [2, [5, 9]], 2]
print_list(l)













