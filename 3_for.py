# # practice1
# list1 = list(range(10))
#
# for line in list1:
#     line += 1
#     print(line)
#
# # practice2
# line = str(input('Введите строку: '))
# for letter in line:
#     print(letter)

"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

total_scores = [{'school_class': '4a', 'scores': [2, 4, 4, 5, 2]},
                {'school_class': '4б', 'scores': [3, 4, 4, 5, 3]},
                {'school_class': '4в', 'scores': [5, 5, 5, 3, 4]}]


def main(score_list):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    klass_average_sum = []
    school_average_sum = []
    for klass in score_list:
        for scores in klass['scores']:
            school_average_sum.append(scores)
        klass_average = (sum(klass['scores']) / len(klass['scores']))
        klass_average_sum.append(klass_average)
    print(sum(school_average_sum) / len(school_average_sum))
    for score in klass_average_sum:
        print(score)


if __name__ == "__main__":
    main(total_scores)
