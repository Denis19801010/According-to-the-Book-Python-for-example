# file = open('delete.txt', 'w')
# file.write('Italy -Loxi\n')
# file.write('Mexiko -good\n')
# file.write('Estoni -Loxi\n')
# выводит все сообщения в текстовом файле
# file = open('delete.txt', 'r')
# print(file.read())

# 105  Создайте новый файл с именем Numbers.txt. Добавьте в него пять чисел, которые хранятся в одной стро-
# ке и разделяются только запятыми. После запуска программы найдите папку, в которой располагается ваша
# программа; убедитесь в том, что файл был создан. В системе Windows для просмотра содержимого нового
# текстового файла проще всего вос пользоваться «Блокнотом».
# file = open('105 Lesson.txt', 'w')
# file.write('1, 2, 3, 4, 5')
# file.close()

# 106 Создайте новый файл с именем Names.txt. Добавьте в него пять имен, отображающихся на разных строках.
# После запуска программы найдите папку, в которой располагается ваша программа; убедитесь в том, что файл
# был создан.
# file = open('Names.txt', 'w')
# file.write('Vasa\n')
# file.write('Gasa\n')
# file.write('Vada\n')
# file.write('Gaada\n')
# file.write('Aaada\n')
# file.close()

# 107 Откройте файл Names.txt и выведите данные из кода Python.
# file = open('Names.txt', 'w')
# file.write('Vasa\n')
# file.write('Gasa\n')
# file.write('Vada\n')
# file.write('Gaada\n')
# file.write('Aaada\n')
# file.close()
# file = open('Names.txt', 'r')
# print(file.read())

# 108 Откройте файл Names.txt. Предложите пользователю ввести новое имя. Добавьте его в конец
# файла и выведите все содержимое файла.
# file = open('Names.txt', 'w')
# file.write('Vasa\n')
# file.write('Gasa\n')
# file.write('Vada\n')
# file.write('Gaada\n')
# file.write('Aaada\n')
# file.close()
# file = open('Names.txt', 'r')
# print(file.read())
# name_add = input('Enter name to add in file >>> ')
# file = open('Names.txt', 'a')
# file.write('name_add')
# file.close()
# file = open('Names.txt', 'r')
# print(file.read())

# 109 Выведите следующее меню:
# 1) Create a new file
# 2) Display the file
# 3) Add a new item to the file
# Make a selection 1, 2 or 3:
# Предложите пользователю выбрать один из вариантов. Если пользователь введет что-либо, кроме 1, 2 и 3, про-
# грамма должна вывести соответствующее сообщение об ошибке. Если пользователь выберет 1, предложите ему ввести на-
# звание школьного предмета и сохраните его в новом файле с именем Subject.txt. Существующий файл с таким именем
# должен быть заменен новым файлом. Если пользователь выберет 2, выводится содержимое файла Subject.txt.
# Если пользователь выберет 3, предложите пользователю ввести новый предмет, сохраните его в файле, а затем вы-
# ведите все его содержимое. Запустите программу несколько раз, чтобы протестировать разные команды.
# menu = ('1) Create a new file', '2) Display the file', '3) Add a new item')
# for i in menu:
#     print(i)
# choice = int(input('Make a selection 1, 2 or 3 >>> '))
# if choice == 1:
#     school_subject = input('Enter subject >>> ')
#     file = open('Subject.txt', 'w')
#     file.write(school_subject + '\n')
# elif choice == 2:
#     file = open('Subject.txt', 'r')
#     print(file.read())
# elif choice == 3:
#     new_subject = input('Enter new subject >>> ')
#     file = open('Subject.txt', 'a')
#     file.write(new_subject + '\n')
#     file = open('Subject.txt', 'r')
#     print(file.read())
# else:
#     print('You can read! CHOICE 1, 2 OR 3 MOTHERFUCKER!! ')

# 110 С помощью созданного ранее файла Names.txt выведите список имен в Python. Попросите пользователя
# ввести одно из имен, а затем сохраните все, кроме выбранного в новом файле, под названием Names2.txt.
# file = open('Names.txt', 'r')
# print(file.read())
# file.close()
#
# file = open('Names.txt', 'r')
# name = input('Enter new name >>> ')
# name = name + '\n'
# for row in file:
#     if row != name:
#         file = open('Names2.txt', 'a')
#         newrecord = row
#         file.write(newrecord)
#         file.close()
# file.close()
#


