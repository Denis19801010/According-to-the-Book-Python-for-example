import csv
# file = open('Stars.csv ', 'w')
# newRecord = 'Baran, 42, Tupiza\n'
# file.write(str(newRecord))
# file.close()

# 111 Создайте файл .csv с данными, приведенными в следующей таблице. Назовите его Books.csv.
#               Книга                                   Автор               Год выпуска
#      0   To Kill a Mockingbird                    Harper Lee                1960
#      1   A Brief History of Time                  Stephen Hawking           1988
#      2   The Great Gatsby                         F. Scott Fitzgerald       1922
#      3   The Man Who Mistook His Wife for a Hat   Oliver Sacks              1985
#      4   Pride and Prejudice                      Jan Austen                1813

# file = open('Books.csv', 'w')
# newRecord = 'To Fill a Mockingbird, Harper Lee, 1960\n'
# file.write(str(newRecord))
# newRecord = 'A Brief history of Time, Stephen Hawkinge, 1988\n'
# file.write(str(newRecord))
# newRecord = 'A Great Getsby, F. Scott Fitzgerald, 1922\n'
# file.write(str(newRecord))
# newRecord = 'The Man who Mistook His Wife for a Hat, Oliver Sacks, 1985\n'
# file.write(str(newRecord))
# newRecord = 'Pride and Prejudice, Jan Austen, 1813\n'
# file.write(str(newRecord))
# file.close()
# file = open('Books.csv', 'r')
# for row in file:
#     print(row)

#  112 Используя файл Books.csv из программы 111, предложите пользователю ввести новую запись и до-
# бавьте ее в конец файла. Выведите каждую строку файла .csv в отдельной строке.
# file = open('Books.csv', 'a')
# work = str(input('Enter new work >>> '))
# name = str(input('Enter new name >>> '))
# age = input('Enter year of writing >>>  ')
# newRecord = work + ', ' + name + ', ' + age + '\n'
# file.write(str(newRecord))
# file.close()
# file = open('Books.csv', 'r')
# print(file.read())
# file.close()


# 113 Используя файл Books.csv, спросите пользователя, сколько записей он хочет добавить в список, и предоставьте
# ему такую возможность. После того как данные будут добавлены, запросите автора и выведите все книги указан-
# ного автора из списка. Если в списке нет ни одной книги этого автора, выведите соответствующее сообщение.
#
# add_note = int(input('Enter how many note you want to add >>> '))
# for i in range(0, add_note):
#     file = open('Books.csv', 'a')
#     work = str(input('Enter new work >>> '))
#     name = str(input('Enter new name >>> '))
#     age = input('Enter year of writing >>>  ')
#     newRecord = work + ', ' + name + ', ' + age + '\n'
#     file.write(str(newRecord))
#     file.close()
# file = open('Books.csv', 'r')
# print(file.read())
# file.close()
# file = open('Books.csv', 'r')
# search = input('Enter author, to see his books >>> ')
# reader = csv.reader(file)
# count = 0
# for row in file:
#     if search in str(row):
#         print(row)
#         count += 1
# if count == 0:
#     print('Wrong')
# file.close()

# 114 Используя файл Books.csv, предложите пользователю ввести начальный и конечный год. Выведите все книги,
# выпущенные в заданном промежутке времени.
#
# search_begin = int(input('Enter year from >>> '))
# search_end = int(input('Enter year to >>>'))
#
# file = list(csv.reader(open('Books.csv', 'r')))
# tmp = []
# for row in file:
#     tmp.append(row)
#     print(row)
#
# x = 0
# for row in tmp:
#     if search_begin >= int(tmp[x][2]) <= search_end:
#         print(tmp[x])
#     x += 1

# 115 Используя файл Books.csv, выведите данные с нумерацией строк.
# lines = 0
# file = open('Books.csv', 'r')
# for row in file:
#     # display = 'Row: ' + str(lines) + ' - ' + row
#     # print(display)
#     print(row + str(lines))
#     lines += 1

# 116 Импортируйте данные из файла Books.csv в список. Выведите список, предложите пользователю выбрать, какую строку
# он хочет исключить, и удалите ее. Спросите пользователя, какие данные он хочет изменить, и предоставьте ему
# соответствующую возможность. Запишите данные обратно в файл .csv с заменой существующих.
#
# file = list(csv.reader(open('Books.csv')))
# tmp = []
# for row in file:
#     tmp.append(row)
#
# x = 0
# for row in tmp:
#     display = x, tmp[x]
#     print(display)
#     x += 1
# del_str = int(input('Enter str to remove >>> '))
# del tmp[del_str]
#
#
#
# print(file)
 НЕ ДОДЕЛАЛ 116 УПРАЖНЕНИЕ И ДАЛЬШЕ