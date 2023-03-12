#Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def get_correct_number() -> int:
    work = True
    s_num = ''
    result = None
    while work:
        s_num = input('Введите положительное число более 1 и менее 100 000 включительно: ')

        if string_is_integer_digit(string=s_num):
            result = int(s_num)
            if result < 2:
                print('Введенное число должно быть больше 1')
            elif result > 100000:
                print('Введенное число должно быть меньше 100 000')
            else:
                work = False
        else:
            print('Неверные данные. Введите еще раз.')
    return result


def string_is_integer_digit(string: str) -> bool:
    for char in string:
        if char.isalpha():
            print('Введенное значение содержит буквы. ', end='')
            return False
        elif char.__contains__(',') or char.__contains__('.'):
            print('Ошибка ввода. Введенное число не целое.', end='')
            return False
    return True


def check_number_is_whole(num: int) -> bool:
    dev_counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            dev_counter += 1
            if dev_counter > 2:
                return False
    return True


number = get_correct_number()
if check_number_is_whole(num=number):
    print("Введенное число простое")
else:
    print('Введенное число составное')