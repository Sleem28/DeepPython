import csv
from Descriptors import CheckName, CheckGrade


class Student:
    """Class student"""
    __down_grade = 2
    __up_grade = 5
    __down_test_grade = 0
    __up_test_grade = 100
    __first_name = CheckName(str.istitle, str.isalpha)
    __last_name = CheckName(str.istitle, str.isalpha)
    __grade = CheckGrade(__down_grade, __up_grade)
    __test_grade = CheckGrade(__down_test_grade, __up_test_grade)
    __matters = dict()

    def __init__(self, first_name: str, last_name:str, matters_file: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__matters_file = matters_file
        self._get_matters_from_file()

    def _get_matters_from_file(self,):
        with open(self.__matters_file, 'r', newline='') as reader:
            file = csv.reader(reader)
            for line in file:
                self.__matters.update({line[0]: {'grades': [], 'tests': []}})

    def set_grade(self, matter: str, grade: int):
        self.__grade = grade
        self.__matters[matter]['grades'].append(grade)

    def set_test_grade(self, matter: str, test_grade: int):
        self.__test_grade = test_grade
        self.__matters[matter]['tests'].append(test_grade)

    def get_average_grade_by_tests(self, matter: str):
        ag = sum(self.__matters[matter]['tests'])/len(self.__matters[matter]['tests'])
        print(ag)
        return ag

    def get_average_grade_by_all_matters(self,):
        all_grades = 0
        for matter in self.__matters:
            if len(self.__matters[matter]['grades']) > 0:
                all_grades += sum(self.__matters[matter]['grades'])/len(self.__matters[matter]['grades'])
        avg = all_grades/ len(self.__matters)
        print(avg)
        return avg
