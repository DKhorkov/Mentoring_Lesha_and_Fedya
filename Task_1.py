"""Пусть будет небольшой скрипт на работу с юзером. Задача принимать от юзера два числа и возвращать ему на экран
результат их перемножения. Далее юзеру задаётся вопрос, хочет ли он повторить. Если ответ "да", то повторяем,
 если "нет", программа завершается."""


def check_input(user_input):  # Тут у нас в скобочках параметр функции
    """Функция на проверку ввода пользователя. Если ввод нельзя преобразуется к целочисленному формату (например текст),
     то пользователь будет уведомлен об этом и вынужден совершить повторный ввод."""
    while True:
        try:  # Пробуем преобразовать к целочисленному формату
            result = float(user_input)
        except ValueError:  # Если возникнет ошибка, то пользователь должен снова ввести данные, а цикл пойдет по новой
            user_input = input('Error, you need to write number, try again: ')
        else:  # А если все ок, то функция вернет пользователю результат преобразования.
            return result


def check_continuation(cont):
    """Функция для проверки, хочет ли пользователь повторить операцию."""
    answer = input("Do u want to repeat? (Y/n): ").lower()  # Приводим ввод к нижнему регистру дял простоты

    # Пока ввод не равен 'y' или 'n' - у пользователя повторно будет запрашиваться ответ на вопрос о продолжении:
    while answer != 'y' and answer != 'n':
        answer = input("Error. Do u want to repeat? (Y/n): ").lower()
    if answer == 'n':
        cont = False
    return cont


def main():
    """Основная функция программы."""
    cont = True  # Создаем флаг для цикла while. Пока флаг равен True, цикл будет работать.
    while cont:
        first_num = check_input(input('Enter first number: '))  # Передаем функции проверки ввод пользователя
        second_num = check_input(input('Enter second number: '))

        # Выводим результат:
        print(f'The result of multiplication of {first_num:,.1f} on {second_num:,.1f} is '
              f'{second_num * first_num:,.2f}.')

        cont = check_continuation(cont)


if __name__ == '__main__':
    main()
