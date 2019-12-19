"""
    创建函数，生成指定行数的杨辉三角。
    杨辉三角：
    每行端点与结尾的数为1，每个数是它左上方和右上方的数的和
    输入：6
    输出：
         [
                    [1],
                   [1, 1],
                  [1, 2, 1],
                 [1, 3, 3, 1],
               [1, 4, 6, 4, 1],
             [1, 5, 10, 10, 5, 1]
         ]
"""


def get_yang_hui_triangle(row_count):# 6
    """
        获取杨辉三角
    :param row_count: int类型,行数
    :return: list类型，杨辉三角
    """
    triangle = []
    for row_index in range(row_count):# 0 1 2 3 .. 5
        # 创建行
        row = [None] * (row_index + 1)
        # 设置首尾
        row[0], row[-1] = 1, 1
        # 设置中间(从第三行开始)
        for i in range(1, 2):#1
            # 当前元素 = 上一行
            row[i] = triangle[row_index - 1][i - 1] + triangle[row_index - 1][i]
        triangle.append(row)
    return triangle


print(get_yang_hui_triangle(6))