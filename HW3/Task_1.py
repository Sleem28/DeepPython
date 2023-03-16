# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

my_list = [1, 1, 1, 3, 3, 3, 3, 'asd', 'asd', 3.2, 3.2, 8, 16]
print(f'The input list before a treatment looks like: {my_list}')
new_list = []

for item in my_list:
    count = my_list.count(item)

    if item not in new_list:
        for _ in range(count-1):
            new_list.append(item)
            my_list.remove(item)


print(f'The output list after a treatment contains next dublicates: {new_list}')
print(f'The input list now contains only unique elements: {my_list}')