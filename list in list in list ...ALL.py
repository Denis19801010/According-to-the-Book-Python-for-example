# 96 Создайте следующий набор данных в виде простого двумерного списка со стандартными индексами Python:
#
#         0 1 2
#       0 2 5 8
#       1 3 7 4
#       2 1 6 9
#       3 4 2 0
# list1 = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# print(list1)

# 97 Используя двумерный список из задачи 096, предложите пользователю выбрать строку и столбец и выведите
# выбранное значение.
# list1 = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# row = int(input(' select row >>>  '))
# column = int(input('select column >>>'))
# print(list1[row][column])

# 98 Используя двумерный список из задачи 096, предложите пользователю выбрать строку и выведите
# только ее. Предложите ввести новое значение, добавьте его в конец строки, после чего снова выведите
# измененную строку.
# list1 = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# line = int(input('Enter number of line >>> '))
# print(list1[line])
# num = int(input('Enter a new value >>>> '))
# list1[line].append(num)
# print(list1[line])

# 99 Измените программу из задачи 098.Предложите пользователю выбрать строку и выведите только ее.
# Предложите выбрать столбец из выведенной строки и выведите только хранящееся там значение.
# Спросите, хочет ли пользователь изменить его. Если ответ будет положительным, предложите ввести
# новое значение и измените данные. Наконец, снова выведите измененную строку.

# list1 = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# line = int(input('Enter line >>> '))
# print(list1[line])
# row = int(input('Enter row >>> '))
# print(list1[line][row])
# change = input('Do you want to change the number (y/n)?')
#
# if change == 'y':
#     change_line = int(input('Enter new number  >>> '))
#     (list1[line][row]) = change_line
# print(list1)


# 100  Создайте следующий набор данных, представляющий объемы продаж по регионам, в виде двумерного словаря:


    #         N    S   E    W
    # John  3056 8463 8441 2694
    # Tom   4832 6786 4737 3612
    # Anna  5239 4802 5820 1859
    # Fiona 3904 3645 8821 2451
# dictionary = {"John":
#             {'N': 3056, 'S': 8463, 'E': 8441,'W': 2694},
#         "Tom":
#             {'N': 4832, 'S': 6786, 'E': 4737,'W': 3612},
#         "Anna":
#             {'N': 5239, 'S': 4802, 'E': 5820,'W': 1859},
#         "Fiona":
#             {'N': 3904, 'S': 3645, 'E': 8821,'W': 2451}
#               }
# print(dictionary)

# 101 Используя программу из задачи 100, запросите у пользователя имя и регион. Выведите соответствующие данные.
# Запросите у пользователя имя и регион того значения, которое он хочет изменить, и позвольте скорректировать
# объем продаж. Выведите объемы продаж по всем регионам для имени, выбранного пользователем.
#
# dictionary = {"John":
#             {'N': 3056, 'S': 8463, 'E': 8441,'W': 2694},
#         "Tom":
#             {'N': 4832, 'S': 6786, 'E': 4737,'W': 3612},
#         "Anna":
#             {'N': 5239, 'S': 4802, 'E': 5820,'W': 1859},
#         "Fiona":
#             {'N': 3904, 'S': 3645, 'E': 8821,'W': 2451}
#               }
# print(dictionary)
# name = input('Enter name  >>> ').title()
# region = input('Enter region >>> ').upper()
# print(dictionary[name][region])
#
# name_change = input('Enter name to change >>> ')
# dictionary[name][region] = name_change
# print(dictionary[name])
#
#
# 102 Предложите пользователю ввести имя, возраст и размер обуви для четырех человек. Запросите имя одного из них
# в списке и выведите значения его возраста и размера обуви.
# list_1 = {}
# for i in range(2):
#     name = input('Enter name >>> ')
#     age = int(input('Enter age >>>'))
#     size = int(input('Enter foot size >>> '))
#     list_1[name] = {'Age': age, 'Foot Size': size}
#
# call_name = input('Enter name and see age and foot size : ')
# print(list_1[call_name])


# 103 Измените программу 102, чтобы она выводила имя и возраст для всех людей в списке, но не их размер обуви.
# list_1 = {}
# for i in range(2):
#     name = input('Enter name >>> ')
#     age = int(input( 'Enter age >>> '))
#     foot_size = int(input('Enter foot size >>> '))
#     list_1[name] = {'Age': age, 'Foot size': foot_size}
# for name in list_1:
#     print(name, list_1[name]['Age'])
#
# 104 После получения имени, возраста и размера обуви для четырех человек запросите у пользователя имя человека
# для удаления из списка. Удалите эту строку и выведите остальные данные с разбивкой по строкам.
# list_1 = {}
# for i in range(3):
#     name = input('Enter name ')
#     age = int(input('Enter age '))
#     foot_size = int(input('Enter foot size '))
#     list_1[name] = {'Age': age, 'Foot_size': foot_size}
# delete_name = input('Enter name to delete >>> ')
# del list_1[delete_name]
# for name in list_1:
#     print(list_1)