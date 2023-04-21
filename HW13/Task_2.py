#Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
from Exceptions import ValueBordersException


def get_correct_number() -> int:
    dn_board = 1
    up_board = 100000
    result = None
    s_num = input('Введите положительное число более 1 и менее 100 000 включительно: ')
    try:
        result = int(s_num)
    except ValueError as e:
        print(e)
        raise ValueError

    if result <= dn_board or result >= up_board:
        raise ValueBordersException(dn_board, up_board)

    return result


def check_number_is_whole(num: int) -> bool:
    dev_counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            dev_counter += 1
            if dev_counter > 2:
                return False
    return True


while True:
    try:
        number = get_correct_number()
        if check_number_is_whole(num=number):
            print("Введенное число простое")
        else:
            print('Введенное число составное')
        break
    except ValueError as e:
        print(e)
    except ValueBordersException as e:
        print(e)
