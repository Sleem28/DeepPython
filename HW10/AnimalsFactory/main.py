# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from Factory import Factory

if __name__ == '__main__':

    cat = Factory('Cat', 4, 0.3, 2.1, 'Miau', 'Vaska', True).get_animal()
    dog = Factory('Dog', 4, 0.7, 10, 'Whoof', 'Bobik', True).get_animal()
    mouse = Factory('Mouse', 4, 0.1, 0.2, 'Pi pi', True).get_animal()

    print(f'Cat info: {cat.get_info()}')
    print(f'Dog info: {dog.get_info()}')
    print(f'Mouse info: {mouse.get_info()}')

