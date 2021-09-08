"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

age = abs(int(input('Введите свой возраст: ')))


def main(user_age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if 0 <= user_age <= 6:
        role = 'учиться в детском саду'
    elif 7 <= user_age <= 16:
        role = 'учиться в  школе'
    elif 17 <= user_age <= 23:
        role = 'учиться в детском ВУЗе'
    else:
        role = 'работать'
    return role


if __name__ == "__main__":
    print(main(age))
