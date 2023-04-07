# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
# обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. Для каждого
# объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
import os


def wolk_by_folder(path: str) -> None:
    items = os.listdir(path)
    is_folder = False

    for item in items:
        cur_path = f'{path}\\{item}'
        is_dir = os.path.isdir(cur_path)
        if is_dir:
            if not is_folder:
                is_folder = True
            serializer(parent_path=path, item=item)
            wolk_by_folder(path=cur_path)  # рекурсивный вызов
        else:
            serializer(parent_path=path, item=item)
    return


def serializer(parent_path: str, item: str) -> None:
    path = f'{parent_path}\\{item}'
    is_dir = os.path.isdir(path)
    if is_dir:
        size = total_size(path)
    else:
        size = os.path.getsize(path)
    data = {'parent_path': parent_path, 'item': item, 'is_folder': is_dir, 'size': size}
    header = ['parent_path', 'item', 'is_folder', 'size']

    with open(f'jsons\\{item}_data.json', 'a', encoding='utf-8') as writer:
        json.dump(data, writer)

    with open(f'csv\\{item}_data.csv', 'a', encoding='utf-8') as writer:
        csw_writer = csv.DictWriter(writer, fieldnames=header)
        csw_writer.writeheader()
        csw_writer.writerows([data])

    with open(f'pickle\\{item}_data.pickle', 'wb') as writer:
        pickle.dump(data, writer, protocol=pickle.HIGHEST_PROTOCOL)


def total_size(path: str) -> int:
    total = 0
    for dir, _, files in os.walk(path):
        for fn in files:
            total += os.path.getsize(os.path.join(dir, fn))
    return total


wolk_by_folder('..')
