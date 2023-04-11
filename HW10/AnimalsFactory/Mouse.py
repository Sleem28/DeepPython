from Animal import Animal


class Mouse(Animal):
    def __init__(self, legs: int, height: float, weight: float, cry: str, chewing_on_wires: bool):
        super().__init__(legs, height, weight, cry)
        self.__chewing_on_wires = chewing_on_wires

    def get_info(self):
        super_info = super().get_info()
        return f'{super_info} chewing on wires = {self.__chewing_on_wires}'
