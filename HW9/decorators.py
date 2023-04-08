# Нахождение корней квадратного уравнения
#
# Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
#
# Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
#
# Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

from typing import Callable
from random import uniform
import csv
import json


def csv_generator() -> None:
    qty = 100
    dn_num = -100.0
    up_num = 100.0

    with open('data\\nums.csv', 'a', newline='') as writer:
        csv_writer = csv.writer(writer)

        for _ in range(0, qty):
            lst = [uniform(dn_num, up_num), uniform(dn_num, up_num), uniform(dn_num, up_num)]
            csv_writer.writerow(lst)


def check_square_equation(func: Callable):
    def wrapper() -> list:
        results = []
        with open('data\\nums.csv', 'r', newline='') as reader:
            csv_list = csv.reader(reader)
            for nums in csv_list:
                a = float(nums[0])
                b = float(nums[1])
                c = float(nums[2])
                results.append([a, b, c, func(float(nums[0]), float(nums[1]), float(nums[2]))])
        return results
    return wrapper


def to_json(func: Callable):
    def wrapper():
        results = func()
        with open('data\\nums_results.json', 'a', encoding='utf-8') as writer:
            json.dump(results, writer)
    return wrapper


@to_json
@check_square_equation
def discr(a: float, b: float, c:float) -> str:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'Not roots'
    elif discriminant == 0:
        return 'One root'
    else:
        return 'Two roots'


csv_generator()
discr()




