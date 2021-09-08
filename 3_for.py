# # practice1
# list1 = []
# for i in range(1, 10):
#     list1.append(i)
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
    score_sum = 0
    for dict1 in score_list:
        for score in dict1['scores']:
            score_sum += score
    print(score_sum/len(dict1['scores']))

    score_sum1 = 0
    for score in score_list[0]['scores']:
        score_sum1 += score
    print(score_sum1 / len(score_list[0]['scores']))

    score_sum2 = 0
    for score in score_list[1]['scores']:
        score_sum2 += score
    print(score_sum2 / len(score_list[1]['scores']))

    score_sum3 = 0
    for score in score_list[2]['scores']:
        score_sum3 += score
    print(score_sum3 / len(score_list[2]['scores']))


if __name__ == "__main__":
    main(total_scores)
