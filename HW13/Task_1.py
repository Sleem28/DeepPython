# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним
from Exceptions import PositiveValueException


def get_triangle_side(side_num: str) -> float:
    work = True
    res = -1.0
    while work:
        s_num = input('Введите размер ' + side_num + ' стороны треугольника: ')
        try:
            res = float(s_num)
        except ValueError as e:
            print('Значение должно быть вещественным числом')
            continue
        else:
            if res < 0:
                raise PositiveValueException
            else:
                return res


a = b = c = 0
while True:
    try:
        a = get_triangle_side(side_num='первой')
        b = get_triangle_side(side_num='второй')
        c = get_triangle_side(side_num='третьей')
        break
    except PositiveValueException as e:
        print(e)
        continue


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