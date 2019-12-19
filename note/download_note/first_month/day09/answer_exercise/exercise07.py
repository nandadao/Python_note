"""
    二分查找
    定义函数，在有序数字列表中找到目标值，并返回其索引。
    如果目标值不在列表中，返回它可以按顺序插入的索引。
    输入：[1,2,6,8,9]  8
    输出：3

    输入：[1,2,6,8,9]  5
    输出：2
"""
def search_insert_index(list_number, target):
    left = 0
    right = len(list_number) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_number[mid] == target:
            return mid
        elif list_number[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(search_insert_index([1, 2, 6, 8, 9], 5))
