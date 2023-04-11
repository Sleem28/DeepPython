class Animal:

    def __init__(self, legs: int, height: float, weight: float, cry: str):
        self._legs = legs
        self._height = height
        self._weight = weight
        self._cry = cry

    def get_info(self):
        return f' legs = {self._legs}, height = {self._height}, weight = {self._weight}, cry = {self._cry}'
