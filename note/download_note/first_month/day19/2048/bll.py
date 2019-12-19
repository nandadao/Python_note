import random

from model import Location


class GameController:
    """
        负责处理游戏核心逻辑
    """

    def __init__(self):
        self.__list_merge = None
        # self.__map = [
        #     [2, 8, 0, 2],
        #     [2, 2, 0, 4],
        #     [0, 4, 0, 4],
        #     [2, 2, 2, 0],
        # ]
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    # 只读属性
    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移动
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def move_up(self):
        """
            向上移动
        """
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        """
            向下移动
        """
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def generate_new_number(self):
        """
            生成新数字　
        """
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0: return
        # 在空位置列表中，随机选择一个位置
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r][loc.c] = self.__create_random_number()

    def __create_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    # 记录r c
                    # self.__list_empty_location.append((r, c))
                    self.__list_empty_location.append(Location(r, c))


# 目的：不是主模块才执行测试代码
if __name__ == "__main__":
    controller = GameController()
    controller.generate_new_number()
    controller.generate_new_number()
    # controller.move_right()
    print(controller.map)
