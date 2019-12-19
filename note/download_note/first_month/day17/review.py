"""
    复习
        异常处理
            异常现象：程序不再向下执行,而是不断返回给调用者。
            处理目的：异常现象(向上翻) --> 正常现象(向下走)
            手段：
                try:
                    可能出错的代码
                except 错误类型:
                    针对一种错误的处理逻辑
                except:  # except Exception:
                    真对所有错误的处理逻辑
                else:
                    没有错误的逻辑
                finally:
                    不论对错，一定执行的逻辑
            主动抛出异常：
                快速传递错误信息
                如果信息过多，将数据封装到自定义异常类中。
            原则：就近处理
        迭代iter
            可迭代对象iter able
                __iter_()
                价值：能够被for

            迭代器iter ator
                __next__()
                价值：能够获取下一个元素
"""
list01 = [1, 2, 43, 4, 5]
list02 = [1, 2, 43, 4, 5]

# 快捷键：iter + tab +tab +tab
for item in list01:
    print(item)





















