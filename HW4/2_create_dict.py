# Напишите функцию принимающую на вход только ключевые
#параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def get_dict(**kwargs)->dict:
    res_dict = dict()
    for key, value in kwargs.items():
        res_dict[value.__hash__()] = key
    return res_dict

print(get_dict(name='john', last_name='connor', age=300, dead='undead'))


