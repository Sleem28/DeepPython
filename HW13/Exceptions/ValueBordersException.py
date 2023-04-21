from .MyException import MyException


class ValueBordersException(MyException):
    def __init__(self, dn_board, up_board):
        self.__dn_board = dn_board
        self.__up_board = up_board

    def __str__(self):
        return f'Значение должно быть больше {self.__dn_board} и меньше {self.__up_board}.'

