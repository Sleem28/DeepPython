#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint

LOWER_LIMIT = -10
UPPER_LIMIT = 10
TRY_LIMIT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)



def get_number() -> int:
    s_value = input(f'Введите целое число от {LOWER_LIMIT} до {UPPER_LIMIT}: ')
    if string_is_integer_digit(s_value):
        return int(s_value)


def string_is_integer_digit(string: str) -> bool:
    for char in string:
        if char.isalpha():
            print('Введенное значение содержит буквы. ', end='')
            return False
        elif char.__contains__(',') or char.__contains__('.'):
            print('Ошибка ввода. Введенное число не целое.', end='')
            return False
    return True


def run_game():
    count = 1
    print(f'Сгенерировано случайное число в промежутке от {LOWER_LIMIT} до {UPPER_LIMIT}.')
    print(f'Вам необходимо его отгадать за {TRY_LIMIT} попыток.')

    while count <= TRY_LIMIT:
        print(f'Попытка номер {count}.')
        number = get_number()

        if number == num:
            print(f'Поздравляю!!! Вы угадали!!! Случайное число равно {num}!!!')
            break
        elif number < num:
            print('Введенное число меньше искомого. Попробуйте еще раз.')
            count += 1
        elif number > num:
            print('Введенное число больше искомого. Попробуйте еще раз.')
            count += 1
    else:
        print('Попытки закончились. Вы проиграли.')


run_game()