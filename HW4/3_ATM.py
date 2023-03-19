# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
from decimal import Decimal

def add_money(money: Decimal):
    global cur_money, money_in_out_counter
    if money % 50 == 0:
        cur_money += money
        print(f'Добавлены средства в размере {money}\n')
        money_in_out_counter += 1
    else:
        print('Пополнение невозможно. Количество вносимых средств должно быть кратно 50!!!\n')


def get_money(money: Decimal):
    global cur_money, money_in_out_counter
    if cur_money - money < 0:
        print('Недостаточно средств на счете.\n')
    elif money % 50 == 0:
        commission = calc_commision(money=money)
        cur_money -= money + commission
        print(f'Средства сняты. Взята коммиссия за снятие {commission}\n')
        money_in_out_counter += 1
    else:
        print('Снятие невозможно. Количество вносимых средств должно быть кратно 50!!!\n')


def calc_commision(money: Decimal) -> Decimal:
    global withdraw_percent, withdraw_min, withdraw_max, cur_money
    commision = money * withdraw_percent

    if commision < withdraw_min:
        return withdraw_min
    elif commision > withdraw_max:
        return withdraw_max
    else:
        return commision


def check_operation_counter():
    global bonus_percent, cur_money, money_in_out_counter
    if money_in_out_counter == 3:
        bonus = cur_money*bonus_percent
        cur_money += bonus
        print(f'Начислен бонус за 3 операции {bonus}\n')
        money_in_out_counter = 0


def get_wealth_tax():
    global cur_money, rich_percent
    if cur_money > max_balance:
        commission = cur_money*rich_percent
        print(f'Взята комиссия за богатство 10% {commission}у.е.\n')
        cur_money -= cur_money*rich_percent


cur_money = Decimal('0')
money_in_out_counter = 0
withdraw_percent = Decimal('0.015')
withdraw_min = Decimal(30)
withdraw_max = Decimal(600)
bonus_percent = Decimal('0.03')
max_balance = Decimal('5_000_000')
rich_percent = Decimal('0.1')


def run_atm():
    global cur_money
    choice = -1

    while choice != 0:
        print('Банкомат. Главное меню')
        check_operation_counter()
        get_wealth_tax()
        print(f'Текущий балланс равен {cur_money}')
        print('Для внесения средств выберите 1.\nДля снятия средств выберите 2.\nДля выхода нажмите 0.')
        choice = int(input())

        match choice:
            case 1:
                add_money(money=Decimal(input('Введите сумму для пополнения кратную 50: ')))
            case 2:
                get_money(money=Decimal(input('Введите сумму для снятия кратную 50: ')))
            case 0:
                print('Работа завершена')
                quit()

run_atm()