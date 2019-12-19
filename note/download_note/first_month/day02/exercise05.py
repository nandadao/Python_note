# 练习:古代的称,1斤是16量
#     在终端中获取两，计算几斤零几量.
#        35            2     3
int_weight = int(input("请输入量："))
jin = int_weight // 16
liang = int_weight % 16
print(str(jin) + "斤零" + str(liang) + "量")
