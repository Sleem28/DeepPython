from Animal import Animal
from Dog import Dog
from Cat import Cat
from Mouse import Mouse


class Factory:
    def __init__(self, a_type: str, *args):
        self.__a_type = a_type
        self.__args = args
        self.__animal = self.__create_animal()

    def __create_animal(self) -> Animal:
        if self.__a_type == 'Cat':
            return Cat(self.__args[0], self.__args[1], self.__args[2], self.__args[3], self.__args[4], self.__args[5])
        elif self.__a_type == 'Dog':
            return Dog(self.__args[0], self.__args[1], self.__args[2], self.__args[3], self.__args[4], self.__args[5])
        elif self.__a_type == 'Mouse':
            return Mouse(self.__args[0], self.__args[1], self.__args[2], self.__args[3], self.__args[4])
        else:
            print('Wrong class name')

    def get_animal(self) -> Animal:
        return self.__animal

