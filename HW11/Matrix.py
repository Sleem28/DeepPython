from typing import Type


class Matrix:
    m_list: list

    def __new__(cls, m_list: list):
        if not cls._check_m_list(m_list):
            return None
        else:
            return super().__new__(cls)

    def __init__(self, m_list: list):
        self.m_list = m_list

    def __str__(self):
        res = f''
        for row in self.m_list:
            res += '|'
            for item in row:
                res += f'{item}|'
            res += '\n'
        return res

    def __eq__(self, other):
        for row_index in range(len(self.m_list)):
            for item_index in range(len(self.m_list[row_index])):
                if self.m_list[row_index][item_index] != other.m_list[row_index][item_index]:
                    return False
        return True

    def __add__(self, other):
        if len(self.m_list) != len(other.m_list):
            print('These matriсes have different sizes.')
            return None
        else:
            res = []
            for row_index in range(len(self.m_list)):
                if len(self.m_list[row_index]) != len(other.m_list[row_index]):
                    print('These matriсes have different sizes.')
                    return None
                res.append([])
                for item_index in range(len(self.m_list[row_index])):
                    item_sum = self.m_list[row_index][item_index] + other.m_list[row_index][item_index]
                    res[row_index].append(item_sum)
        return Matrix(res)

    def __mul__(self, other):
        if not self._check_matriсes_before_multiple(self.m_list, other.m_list):
            return None
        else:
            res = []
            for row_index in range(len(self.m_list)):
                res.append([])
                for other_index in range(len(other.m_list[row_index])):
                    val = 0
                    for item_index in range(len(self.m_list[row_index])):
                        val += self.m_list[row_index][item_index] * other.m_list[item_index][other_index]
                    res[row_index].append(val)
            return Matrix(res)


    @staticmethod
    def _check_m_list(m_list: list) -> bool:
        row_items = -1
        for row in m_list:
            if row_items < 0:
                row_items = len(row)
            else:
                if len(row) != row_items:
                    print('This list is not a matrix')
                    return False
        return True

    @staticmethod
    def _check_matriсes_before_multiple(first_m: list, sec_m: list) -> bool:
        row_qty = len(first_m)

        for row in sec_m:
            if len(row) != row_qty:
                print('Multiplying these matrices are not possible. They have the wrong sizes.')
                return False
        return True
