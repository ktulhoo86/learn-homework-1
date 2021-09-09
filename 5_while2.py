"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"вы готовы дети?": "Да, Капитан!",
                         "я не слыыышуууу!": "ТАК ТОЧНО, КАПИТАН!",
                         "кто проживает на дне океана?": "Спанч Боб Square Pants!",
                         "желтая губка, малыш без изъяна?": "Спанч Боб Square Pants!",
                         "кто побеждает всегда и везде?": "Спанч Боб Square Pants!",
                         "кто также ловок как рыба в воде?": "Спанч Боб Square Pants!",
                         "спанч Боб Square Pants!": "Спанч Боб Square Pants!",
                         "спанч Боб Square Pants!!": "Спанч Боб Square Pants!!"
                         }


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    print('Подпевай!!!')
    while True:
        question = str(input('Пользователь:')).lower()
        for key, value in answers_dict.items():
            if question == key:
                print(f'Программа: {value}')

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
