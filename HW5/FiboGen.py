# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibo_gen(qty: int):
    a = 0
    b = 1
    c = 0

    for _ in range(qty+1):
        c = a + b
        a = b
        b = c
        yield c


def print_gen(gen):
    for item in gen:
        print(item, end=' ')

print_gen(fibo_gen(10))
