# 练习:
def calculate_weight(total_weight):
    jin = total_weight // 16
    liang = total_weight % 16
    return (jin, liang)


re = calculate_weight(34324234)
print(re)

jin, liang = calculate_weight(34324234)
print(jin)
print(liang)
