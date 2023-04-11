from decimal import Decimal


class ATM:
    __MONEY = Decimal('0')
    __MONEY_COUNTER = 0
    __WITHDRAW_P = Decimal('0.015')
    __MIN_W = Decimal(30)
    __MAX_W = Decimal(600)
    __BONUS = Decimal('0.03')
    __MAX_B = Decimal('5_000_000')
    __RICH_P = Decimal('0.1')

    def __init__(self):
        self.__cur_money = ATM.__MONEY
        self.__money_in_out_counter = ATM.__MONEY_COUNTER
        self.__withdraw_percent = ATM.__WITHDRAW_P
        self.__withdraw_min = ATM.__MIN_W
        self.__withdraw_max = ATM.__MAX_W
        self.__bonus_percent = ATM.__BONUS
        self.__max_balance = ATM.__MAX_B
        self.__rich_percent = ATM.__RICH_P

    def __add_money(self, money: Decimal):
        if money % 50 == 0:
            self.__cur_money += money
            print(f'Добавлены средства в размере {money}\n')
            self.__money_in_out_counter += 1
        else:
            print('Пополнение невозможно. Количество вносимых средств должно быть кратно 50!!!\n')

    def __get_money(self, money: Decimal):
        if self.__cur_money - money < 0:
            print('Недостаточно средств на счете.\n')
        elif money % 50 == 0:
            commission = self.__calc_commission(money=money)
            self.__cur_money -= money + commission
            print(f'Средства сняты. Взята коммиссия за снятие {commission}\n')
            self.__money_in_out_counter += 1
        else:
            print('Снятие невозможно. Количество вносимых средств должно быть кратно 50!!!\n')

    def __calc_commission(self, money: Decimal) -> Decimal:
        commission = money * self.__withdraw_percent

        if commission < self.__withdraw_min:
            return self.__withdraw_min
        elif commission > self.__withdraw_max:
            return self.__withdraw_max
        else:
            return commission

    def __check_operation_counter(self):
        if self.__money_in_out_counter == 3:
            bonus = self.__cur_money * self.__bonus_percent
            self.__cur_money += bonus
            print(f'Начислен бонус за 3 операции {bonus}\n')
            self.__money_in_out_counter = 0

    def __get_wealth_tax(self):
        if self.__cur_money > self.__max_balance:
            commission = self.__cur_money * self.__rich_percent
            print(f'Взята комиссия за богатство 10% {commission}у.е.\n')
            self.__cur_money -= self.__cur_money * self.__rich_percent

    def run_atm(self):
        choice = -1

        while choice != 0:
            print('Банкомат. Главное меню')
            self.__check_operation_counter()
            self.__get_wealth_tax()
            print(f'Текущий балланс равен {self.__cur_money}')
            print('Для внесения средств выберите 1.\nДля снятия средств выберите 2.\nДля выхода нажмите 0.')
            choice = int(input())

            match choice:
                case 1:
                    self.__add_money(money=Decimal(input('Введите сумму для пополнения кратную 50: ')))
                case 2:
                    self.__get_money(money=Decimal(input('Введите сумму для снятия кратную 50: ')))
                case 0:
                    print('Работа завершена')
                    quit()
