from pathlib import Path
import os


class FileRenamer:
    '''Ренеймит файлы по указанным условиям'''
    PREV_NAME_LETTERS_DIAP: tuple
    END_FILENAME: str
    NUMS_COUNTER: int
    FILE_EXTENSION: str
    PATH_TO_FILES: Path

    def __init__(self, letters_diap: tuple,
                 end_filename: str,
                 nums_counter: int,
                 extension: str,
                 path: Path):
        self.PREV_NAME_LETTERS_DIAP = letters_diap
        self.END_FILENAME = end_filename
        self.NUMS_COUNTER = nums_counter
        self.FILE_EXTENSION = extension
        self.PATH_TO_FILES = path

    def __change_filename__(self, file_name: str, counter: int) -> str:
        '''Создает новое имя файла на основе входящего по условию'''
        str_counter = self.__get_str_counter(counter)
        prev_letter = self.__get_prev_letters__(file_name)
        return f'{prev_letter}{self.END_FILENAME}{str_counter}{self.FILE_EXTENSION}'

    def change(self):
        '''Изменяет имена файлов в каталоге по условию'''
        counter = 0
        old_filenames = self.__get_old_filenames__()
        for filename in old_filenames:
            new_filename = self.__change_filename__(file_name=filename, counter=counter)
            counter += 1
            Path(Path.cwd() / self.PATH_TO_FILES / filename).rename(Path.cwd() / self.PATH_TO_FILES / new_filename)

    def __get_old_filenames__(self) -> list:
        '''Получает список имен файлов по условию'''
        flnms = os.listdir(self.PATH_TO_FILES)
        return flnms

    def __get_prev_letters__(self, filename: str):
        '''Создает начало имени файла по условию'''
        res = ''
        start_index = self.PREV_NAME_LETTERS_DIAP[0]-1
        last_index = self.PREV_NAME_LETTERS_DIAP[1]-1
        filename = filename.split('.')[0] if filename.__contains__('.') else filename
        max_index = len(filename)-1
        if max_index <= start_index:
            start_index = max_index
            last_index = max_index
        elif max_index <= last_index:
            last_index = max_index

        for i in range(start_index, last_index+1):
            res += filename[i]
        return res

    def __get_str_counter(self, counter: int) -> str:
        '''Создает префикс к счетчику по условию'''
        counter_length = len(str(counter))
        if counter_length > self.NUMS_COUNTER:
            return '_wrong_counter'
        prefix = ''

        for _ in range(counter_length, self.NUMS_COUNTER):
            prefix += '0'

        return f'{prefix}{counter}'

