from .MyException import MyException


class PositiveValueException(MyException):

    def __str__(self):
        return 'Число должно быть положительным'

