# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random

QUEENS_QTY = 8
MIN_NUM_FIELD = 1
MAX_NUM_FIELD = 8
QTY_SUCCESSFUL_VARIANTS = 4

def create_rnd_coordinates()-> dict:
    '''Генерит словарь с координатами'''
    q_coord = dict()
    counter = 1
    while counter <= QUEENS_QTY:
        x = random.randint(MIN_NUM_FIELD, MAX_NUM_FIELD)
        y = random.randint(MIN_NUM_FIELD, MAX_NUM_FIELD)

        if check_coord_in_dict(dictionary=q_coord, coords=[x, y]):
            q_coord[counter] = [x, y]
            counter += 1
    return q_coord


def check_coord_in_dict(dictionary: dict, coords: list) -> bool:
    '''Проверяет есть ли в словаре координаты по условию'''
    values = dictionary.values()
    for item in values:
        if item == coords:
            return False
    return True


def check_queens_intersections(q_coord: dict) -> bool:
    ''' Проверяет координаты ферзей на пересечение'''
    control_queen = 1
    queens_keys = q_coord.keys()
    found = False

    while control_queen <= 8: # Пока не переберем всех ферзей
        for queen in queens_keys:
            if queen != control_queen: # Если проверяемый ферзь не текущий

                control_queen_coord = q_coord[control_queen] # Координаты проверяемого ферзя
                current_queen_coord = q_coord[queen] # Координаты текущего ферзя

                x_isec = True if control_queen_coord[0] == current_queen_coord[0] else False 
                y_isec = True if control_queen_coord[1] == current_queen_coord[1] else False

                x_coord_diff = abs(control_queen_coord[0] - current_queen_coord[0])
                y_coord_diff = abs(control_queen_coord[1] - current_queen_coord[1])

                diag_isec = True if x_coord_diff == y_coord_diff else False

                if x_isec or y_isec or diag_isec:
                    # print(f'Wrong variant: {q_coord}')
                    found = True
                    break
        if found:
            return False            
        control_queen += 1
    print(f'Found the good variant: {q_coord}')
    return True


def find_unintersection_variants() -> list:
    '''Ищет 4 валидных расстановки ферзей'''
    variants = []
    var_succ_counter = 0

    while var_succ_counter < 4:
        gen_var = create_rnd_coordinates()

        if check_queens_intersections(q_coord=gen_var):
            variants.append(gen_var)
            var_succ_counter += 1
    return variants

res = find_unintersection_variants()
print(res)
# Раскоментируй и проверь
# test = {1:[1,2], 2:[2,4], 3:[3,6], 4:[4,8], 5:[5,3], 6:[6,1], 7:[7,7], 8:[8,5]} # Верный вариант расстановки

# check_queens_intersections(test)
