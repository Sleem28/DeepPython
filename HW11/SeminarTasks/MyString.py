import time
from datetime import datetime


class MyString(str):
    value: str
    def __new__(cls, name, value):
        """
        Class expands the immutable class str
        :param name: - user name
        :param value: - str value
        """
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.time = datetime.now()
        return instance

    def __str__(self):
        return f'Created {self.name = } in {self.time}'

    def __repr__(self):
        return f'MyString(name={self.name}, value={self.value})'


mystr = MyString('Sleem', 'sregfdgdg')
print(mystr.__repr__())
print(mystr.name)
