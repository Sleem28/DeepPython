# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
MODUL = 16
OxRAW = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
result = ''

try:
    dec_num: int = int(input('Enter an integer number: '))
except:
    print('Error!!! The entered value is not integer.')

tmp = dec_num
while tmp > 0:
    result = OxRAW[tmp % MODUL] + result
    tmp //= MODUL

print(f'The value from hex() equals: {hex(dec_num)}')
print(f'The value which i calculated myself equals: 0x{result}')

