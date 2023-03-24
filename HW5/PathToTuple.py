# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import pathlib


PATH = 'D:\Programming\Python\DeepPythonHomeWorks\HW5\PathToTuple.py'

def path_to_tuple(path: str):
    p_path = pathlib.PurePath(path).parent
    p_file_name = pathlib.PurePath(path).name
    s_file_name = str(p_file_name).split('.')
    return (p_path, s_file_name[0], s_file_name[1])
    
    
print (path_to_tuple(PATH))