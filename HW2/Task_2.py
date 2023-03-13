# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions


def get_fraction(num_fraction: str) -> list:
    list_fraction = []
    is_correct = False
    while not is_correct:
        s_fraction = input(f'Enter {num_fraction} fraction which has a view a/b: ')
        if not s_fraction.__contains__('/'):
            print('The fraction should has a backslash as a delimiter!!!')
            continue

        list_fraction = s_fraction.split('/')

        if not list_fraction[0].isdigit():
            print("Wrong numerator's value.")
        elif not list_fraction[1].isdigit():
            print("Wrong dominator's value.")
        else:
            is_correct = True

    return list_fraction


def fractions_operations(first_fraction: list[str], second_fraction: list[str], type: str) -> list:
    result = []
    first_numer: int = int(first_fraction[0])
    first_domin: int = int(first_fraction[1])
    second_number: int = int(second_fraction[0])
    second_domin: int = int(second_fraction[1])

    if type == 'sum':
        if first_domin == second_domin: # Если знаменатели равны
            result.insert(0, first_numer + second_number)
            result.insert(1, first_domin)
            return fraction_simpler(result)
        else:
            result.insert(0, first_numer * second_domin + second_number * first_domin)
            result.insert(1, first_domin * second_domin)
            return  fraction_simpler(result)
    elif type == 'mult':
        result.insert(0, first_numer * second_number)
        result.insert(1, first_domin * second_domin)
        return fraction_simpler(result)


def fraction_simpler(fraction: list[int]) -> list[float]:
    result_list = []
    numerator = fraction[0]
    dominator = fraction[1]
    length = (numerator if numerator < dominator else dominator)
    nod = 1

    for i in range(2, length + 1):
        if numerator % i == 0 and dominator % i == 0:
            nod = i

    result_list.insert(0, numerator / nod)
    result_list.insert(1, dominator / nod)

    return result_list


def run():
    is_work = True
    print('Main menu:')
    f1 = get_fraction('first')
    f2 = get_fraction('second')
    fr1 = fractions.Fraction(int(f1[0]), int(f1[1]))
    fr2 = fractions.Fraction(int(f2[0]), int(f2[1]))

    while is_work:
        print('\nTo add two fractions enter 1')
        print('To multiple two fractions enter 2')
        print('To exit press 0')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                res = fractions_operations(f1, f2, 'sum')
                print(f'\nThe result of adding two fractions {f1[0]}/{f1[1]} and {f2[0]}/{f2[1]} from my decide '
                      f'is {int(res[0])}/{int(res[1])}')
                print(f'\nThe result of adding two fractions {f1[0]}/{f1[1]} and {f2[0]}/{f2[1]} from included '
                      f'functions is {fr1 + fr2}')
            case '2':
                res = fractions_operations(f1, f2, 'mult')
                print(f'\nThe result of multiple two fractions {f1[0]}/{f1[1]} and {f2[0]}/{f2[1]} from my decide '
                      f'is {int(res[0])}/{int(res[1])}')
                print(f'\nThe result of multiple two fractions {f1[0]}/{f1[1]} and {f2[0]}/{f2[1]} from included '
                      f'functions is {fr1 * fr2}')
            case '0':
                quit()


run()

