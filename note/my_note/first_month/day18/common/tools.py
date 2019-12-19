class IterableHelper:
    # 静态方法 -- 不会自动传递参数
    """
        可迭代对象助手
            微软  集成操作框架
    """
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
    def find_one(iterable, func_condition):
        """
            通用的查找满足条件的第一个元素。
        :param iterable:需要被搜索的可迭代对象
        :param func_condition:搜索的条件
        :return:生成器类型,可以推算出满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                return item




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
    def add_func(iterable, func_handle):
        """
            通用累加功能
        :param iterable:需要累加的可迭代对象
        :param func_handle:累加的逻辑
        :return:累加的结果
        """
        total = 0
        for item in iterable:
            total += func_handle(item)
        return total

    @staticmethod
    def delete_all(iterable, func_condition):
        count = 0
        for i in range(len(iterable)-1, -1, -1):
            if func_condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, func_condition):
        biggest = iterable[0]
        for item in iterable:
            if func_condition(item) > func_condition(biggest):
                biggest = item
        return biggest


    @staticmethod
    def get_min(iterable, func_condition):
        min = iterable[0]
        for item in iterable:
            if func_condition(item) < func_condition(min):
                min = item
        return min



    @staticmethod
    def order_by_small_to_big(iterable, func_condition):
        for r in range(len(iterable)-1):
            for c in range(r+1, len(iterable)):
                if func_condition(iterable[r]) > func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def order_by_big_to_small(iterable, func_condition):
        for r in range(len(iterable)-1):
            for c in range(r+1, len(iterable)):
                if func_condition(iterable[r]) < func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]










