# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
from sys import argv

def check_date(str_date: str) -> bool:
    days_in_month ={1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11: 30, 12:31}
    try:
        date_list = str_date.split('.')
    except:
        print('The inputed date is incorrect. Wrong delimeter.')
        return False
    
    if len(date_list) != 3:
        print('The wrong format of date. The date format should look as DD.MM.YYYY')
        return False
    try:
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
    except:
        print("The items of date had integer digits.")

    if year < 1 or year > 9999:
        print('Incorrect date. The year is wrong.')
        return False
    if month < 1 or month > 12:
        print('Incorrect date. The month is wrong.')
        return False
    if day < 1 or day > days_in_month[month]:
        print('Incorrect date. The day is wrong.')
        return False
    if not __is_leap_year__(year=year) and month == 2 and day > 28:
        print('Incorrect date. The check of the leap year is failed.')
        return False
    
    print('The date is correct.')
    return True

    
def __is_leap_year__(year: int) -> bool:
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return True
    elif year%4 == 0:
        return True
    else:
        return False

check_date(argv[1])