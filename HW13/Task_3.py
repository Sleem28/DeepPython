#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint
from Exceptions import ValueBordersException

LOWER_LIMIT = -10
UPPER_LIMIT = 10
TRY_LIMIT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)


def get_number() -> int:
    s_value = input(f'Введите целое число от {LOWER_LIMIT} до {UPPER_LIMIT}: ')
    value = 0
    try:
        value = int(s_value)
    except ValueError as e:
        print(e)

    if value < LOWER_LIMIT or value > UPPER_LIMIT:
        raise ValueBordersException(LOWER_LIMIT, UPPER_LIMIT)
    return value


def run_game():
    count = 1
    print(f'Сгенерировано случайное число в промежутке от {LOWER_LIMIT} до {UPPER_LIMIT}.')
    print(f'Вам необходимо его отгадать за {TRY_LIMIT} попыток.')

    while count <= TRY_LIMIT:
        print(f'Попытка номер {count}.')
        while True:
            try:
                number = get_number()
                break
            except ValueError:
                print('Введенное значение не число.')
            except ValueBordersException as e:
                print(e)

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


if __name__ == '__main__':
    run_game()

