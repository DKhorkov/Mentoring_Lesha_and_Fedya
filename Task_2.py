"""Задача написать программу, которая будет выполнять функцию терминала в ресторане. Должен быть объект,
 хранящий информацию о возможных для заказа типов блюд (салатов, супов, основных блюд, десертов и напитков) по 5 штук.
 Пользователь должен выбрать по блюду из каждого типа. После выбора блюд должна быть проверка, все ли корректно.
 Если нет, пользователь должен изменить выбор. Дальше снова идет проверка. Если все корректно, то пользователь
 должен быть уведомлен о том, что заказ находится в процессе приготовления."""


class Order:

    # Создаем атрибут самого класса, а не экземпляра, который будет хранить в себе словарь блюд и не будет меняться:
    MEALS = {'burgers': ['Макчикен Премьер Острый', 'Монблан Бургер с курицей', 'Чикен Панини Тоскана', 'Роял Барбекю',
                         'Биг Тейсти Три Сыра'],
             'snacks': ['Большой Снэк Бокс с Крыльями', 'Большой Снэк Бокс со Стрипсами',
                        'Тирольский картофель МакФлэйвор Фрайз по-деревенски', 'Снэк Бокс',
                        'Картошка Фри Большая порция'],
             'sauces': ['Соус Сырный', 'Соус Кисло-Сладкий', 'Соус Терияки', 'Соус Горчичный', 'Кетчуп'],
             'drinks': ['Липтон Айс Ти – Зеленый Чай', 'Липтон Айс Ти – Лимон', 'Спрайт', 'Фанта', 'Кока-Кола']}

    def __init__(self):
        """Инициализируем основные атрибуты, которым будут присвоены блюда, а также создаем словарь для будущего
        собранного заказа, а также флаг, для проверки, что пользователь собрал заказ, котоырй хотел."""
        self.burger = None
        self.snack = None
        self.sauce = None
        self.drink = None
        self.order_dict = {}
        self.correctness = False
        self.continuation = True
        self.category_num = None

    def check_input(self, user_input, max_num):  # Тут у нас в скобочках параметр функции
        """Функция на проверку ввода пользователя. Если ввод нельзя преобразуется к целочисленному формату
        (например текст), то пользователь будет уведомлен об этом и вынужден совершить повторный ввод."""
        while True:
            try:  # Пробуем преобразовать к целочисленному формату
                result = int(user_input)
            except ValueError:  # Если возникнет ошибка, то пользователь должен снова ввести данные, цикл обновится
                user_input = input("Ошибка! Необходимо ввести целое число (Пример: 1, 2, 3 и т.д.)."
                                   " Пожалуйста, попробуйте снова: ")
            else:  # А если все ок, то функция вернет пользователю результат преобразования.
                result = self.check_num(result, max_num)  # Проверяем, находится ли число в нужно диапазоне
                return result

    def check_num(self, choice, max_num):
        """Функция для проверки того, что пользователь ввел значение в нужном диапазоне (от 1 до 5). Если ввод не
        соответствует нашему условию, он будет запрошен повторно, а также к нему будет применена функция "check_input".
        """
        while choice not in range(1, max_num):
            try:
                choice = int(input(f'Ошибка! Номер должен быть в диапозоне от 1 до {max_num - 1} включительно'
                                   ' Пожалуйста, попробуйте снова: '))
            except ValueError:
                choice = self.check_input(input("Ошибка! Необходимо ввести число. Пожалуйста, опробуйте снова: "),
                                          max_num)
            # else:
            #     return choice
        else:
            return choice

    def get_burger(self):
        """Функция для получения выбора пользователем определенного бургера из списка доступных"""
        print('Пожалуйста выберите бургер из списка доступных: ')

        # Выводим дял пользователя пронумерованный список доступных бургеров:
        for num, burger in enumerate(Order.MEALS['burgers'], 1):
            print(f'{num:5}) {burger}')
        burger_num = self.check_input(input('Пожалуйста введите номер бургера, который вы хотите купить: '), 6)

        # Присваиваем переменной бургер нашего экземпляра класса значение из списка бургеров, соответствующее выбору
        # пользователя:
        self.burger = Order.MEALS['burgers'][burger_num - 1]

    def get_snack(self):
        """Функция для получения выбора пользователем определенного снека из списка доступных"""
        print('Пожалуйста выберите снек из списка доступных: ')
        for num, snack in enumerate(Order.MEALS['snacks'], 1):
            print(f'{num:5}) {snack}')
        snack_num = self.check_input(input('Пожалуйста введите номер снека, который вы хотите купить: '), 6)
        self.snack = Order.MEALS['snacks'][snack_num - 1]

    def get_sauce(self):
        """Функция для получения выбора пользователем определенного соуса из списка доступных"""
        print('Пожалуйста выберите соус из списка доступных: ')
        for num, sauce in enumerate(Order.MEALS['sauces'], 1):
            print(f'{num:5}) {sauce}')
        sauce_num = self.check_input(input('Пожалуйста введите номер соуса, который вы хотите купить: '), 6)
        self.sauce = Order.MEALS['sauces'][sauce_num - 1]

    def get_drink(self):
        """Функция для получения выбора пользователем определенного напитка из списка доступных"""
        print('Пожалуйста выберите напиток из списка доступных: ')
        for num, drink in enumerate(Order.MEALS['drinks'], 1):
            print(f'{num:5}) {drink}')
        drink_num = self.check_input(input('Пожалуйста введите номер напитка, который вы хотите купить: '), 6)
        self.drink = Order.MEALS['drinks'][drink_num - 1]

    def summing_order(self):
        """Для каждого блюда, если оно было создано клиентом, добавляем его в гаш словарь заказов как значение
        к соответствующему ключу."""
        if self.burger:
            self.order_dict['burger'] = self.burger
        if self.snack:
            self.order_dict['snack'] = self.snack
        if self.sauce:
            self.order_dict['sauce'] = self.sauce
        if self.drink:
            self.order_dict['drink'] = self.drink

    def check_order_correctness(self):
        """Функция для получения ответа пользователя на вопрос о том, правильно ли собран заказ, а также для обработки
        полученного ответа на правильность для целей программы."""
        self.answer = input('Пожалуйста, подтвердите, что ваш заказ собран полностью и верно (да/нет): ').lower()
        while self.answer != 'да' and self.answer != "нет":
            self.answer = input('Ошибка! Пожалуйста, подтвердите,'
                                ' что ваш заказ собран полностью и верно (да/нет): ').lower()
        if self.answer == 'да':
            print('\n\nСпасибо за покупку! Ваш заказ уже готовится!')
            return True
        else:
            print('\n\nДавайте изменим заказ!\n\n')
            return False

    def check_order_completeness(self):
        """Проверяем, что пользователь правильно собрал свой заказ и не хочет ничего менять."""
        print("Пожалуйста, проверьте ваш заказ. Вы заказали следующее: ")
        for num, key_value in enumerate(self.order_dict.items(), 1):
            print(f'{num:5}) {key_value[0].capitalize()}: {key_value[1]};')
        self.correctness = self.check_order_correctness()
        return self.correctness

    def check_answer(self):
        """Функция для проверки ввода пользователя ("да" или "нет")."""
        self.answer = input('Добро пожаловать. Вы хотите сделать заказ? (да/нет): ').lower()
        while self.answer != 'да' and self.answer != 'нет':
            self.answer = input('Ошибка! Пожалуйста введите "да", чтобы продолжить, или "нет", чтобы прервать '
                                'оформление заказа: ').lower()
        if self.answer == 'нет':
            return False
        return True

    def choose_category(self):
        """Функция для выбора пользователем категории еды, чтобы в дальнейшем выбрать еду из этой категории и
        добавить в заказ."""
        print('Пожалуйста выберите категорию из списка доступных: ')
        for num, category in enumerate(Order.MEALS.keys(), 1):
            print(f'{num:5}) {category}')
        self.category_num = self.check_input(input('Пожалуйста введите номер категории, который вы хотите купить: '), 5)

    def add_food_from_category(self, category):
        """Функция для вызова функций добавления еды в заказ в зависимости от выбранной пользователем категории.
        После добавления еды также происходит обновление состава заказа пользователя в целом."""
        if category == 1:
            self.get_burger()
        elif category == 2:
            self.get_snack()
        elif category == 3:
            self.get_sauce()
        elif category == 4:
            self.get_drink()
        self.summing_order()

    def main(self):
        """Основная функция программы."""
        self.continuation = self.check_answer()
        while not self.correctness and self.continuation:
            self.choose_category()
            self.add_food_from_category(self.category_num)
            self.correctness = self.check_order_completeness()
        else:
            print('\n\nВсего доброго! Надеемся, вы скоро вернетесь!')


if __name__ == '__main__':
    order = Order()
    order.main()
