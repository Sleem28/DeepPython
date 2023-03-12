# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним

def get_triangle_side(side_num: str) -> float:
    work = True
    s_num = ''
    while work:
        s_num = input('Введите размер ' + side_num + ' стороны треугольника: ')
        if string_is_float_digit(string=s_num):
            work = False
        else:
            print('Неверное значение для стороны треугольника. Введите еще раз.')

    return float(s_num)


def string_is_float_digit(string: str) -> bool:
    for char in string:
        if char.isalpha():
            print('Введенное значение содержит буквы. ', end='')
            return False
        elif char.__contains__(','):
            print('Ошибка ввода. Введена запятая вместо точки.', end='')
            return False
    return True


a = get_triangle_side(side_num='первой')
b = get_triangle_side(side_num='второй')
c = get_triangle_side(side_num='третьей')

a_b_check = True if a + b > c else False
b_c_check = True if b + c > a else False
a_c_check = True if a + c > b else False

if a_b_check and b_c_check and a_c_check:
    print(f'Треугольник со сторонами {a}, {b}, {c} может существовать.')
else:
    print(f'Треугольник со сторонами {a}, {b}, {c} НЕ может существовать.')
    quit()

if a == b and b == c and c == a:
    print("Треугольник равнобедренный")
elif a == b or b == c or c == a:
    print("Треугольник ранвосторонний")
else:
    print("Треугольник разносторонний")