from Animal import Animal


class Cat(Animal):
    def __init__(self, legs: int, height: float, weight: float, cry: str, name: str, crap_in_slippers: bool):
        super().__init__(legs, height, weight, cry)
        self.__name = name
        self.__crap_in_slippers = crap_in_slippers

    def get_info(self):
        super_info = super().get_info()
        return f'name = {self.__name} {super_info} crap in slippers = {self.__crap_in_slippers}'




