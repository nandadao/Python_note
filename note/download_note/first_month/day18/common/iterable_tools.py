class IterableHelper:
    # 静态方法 -- 不会自动传递参数
    @staticmethod
    def find_all(iterable, func_condition):
        """
            通用的查找满足条件的所有元素。
        :param iterable:需要被搜索的可迭代对象
        :param func_condition:搜索的条件
        :return:生成器类型,可以推算出满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def select(iterable,func_handle):

        """
            通用的筛选可迭代对象中的元素。
        :param iterable:需要被筛选的可迭代对象
        :param func_handle:筛选的处理逻辑
        :return:生成器类型,可以推算出筛选的元素
        """
        for item in iterable:
            yield func_handle(item)


    @staticmethod
    def sum(iterable,func_handle):
        """
            通用的累加功能
        :param iterable: 需要累加的可迭代对象
        :param func_handle: 累加的逻辑
        :return:累加结果
        """
        sum_value = 0
        for item in iterable:
            sum_value += func_handle(item)
        return sum_value
