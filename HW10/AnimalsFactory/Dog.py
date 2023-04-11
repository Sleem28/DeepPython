from Animal import Animal


class Dog(Animal):
    def __init__(self, legs: int, height: float, weight: float, cry: str, name: str, trained: bool):
        super().__init__(legs, height, weight, cry)
        self.__name = name
        self.__trained = trained

    def get_info(self):
        super_info = super().get_info()
        return f'name = {self.__name} {super_info} trained = {self.__trained}'

