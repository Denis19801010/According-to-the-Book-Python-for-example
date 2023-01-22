# 35 Предложите пользователю ввести имя. Выведите имя три раза.
# name = input('Enter your name >>> ')
# for i in range(0, 3):
#     print(name)

# 36 Измените программу из упражнения 35 так, чтобы она предлагала пользователю ввести имя и число,
# а затем выводила имя заданное количество раз.
# name = input('Enter your name >>> ')
# num = int(input('Enter number >>> '))
# for i in range(0, num):
#     print(name)

# 37 Предложите пользователю ввести имя. Выведите каждую букву имени в отдельной строке.
#
# name = input('Enter your name >>> ')
# for name in name:
#     print(name)

# ДРУГОЕ РЕШЕНИЕ

# name = input('Enter your name >>> ')
# for i in name:
#     print(i)

# еще другие решения
# word = input()
# for i in word:
#     print(i)

# 38 Измените программу из упражнения 37 так, чтобы она также запрашивала число. Выведите
# имя (по одной букве в каждой строке) и по вторите вывод равное введенному числу количество раз.
#
# name = input('Enter your name >>> ')
# num = int(input('Enter number >>> '))
# for k in range(0, num):
#     for i in name:
#         print(i)
#
# 39 Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого числа.

# num = int(input('Enter number from 1 to 12 >>> '))
# for k in range(0, 11):
#     num2 = k * num
#     print(num, ' * ', k, ' =', num2)

# 40 Предложите пользователю ввести число до 50. Проведите обратный отсчет от 50 до введенного числа.
# Проследите за тем, чтобы введенное число было включено в вывод.

# num = int(input('Enter number until 50 >>> '))
# for i in range(50, num - 1, -1):
#     print(i)

# 41 Предложите пользователю ввести имя и число. Если число меньше 10, программа должна вы-
# вести имя заданное количество раз; в противном случае она выводит сообщение «Too high» три раза.

# name = input('Enter name >>> ')
# num = int(input('Enter number >>> '))
# if num < 10:
#     for i in range(0, num):
#         print(name)
# else:
#     for i in range(3):
#         print('Too high')

# 42 Присвойте переменной с именем total значение 0. Предложите пользователю ввести пять чисел, и
# после каждого ввода спрашивайте, хочет ли он включить это число в суммирование. Если ответ будет
# положительным, прибавьте введенное число к total. Если же ответ будет отрицательным, число к total
# не прибавляется. После ввода всех пяти чисел выведите значение total.

# total = 0
# for i in range(5):
#     num = int(input('Enter number >>> '))
#     if input('Would you want to summ this number? ') == 'yes':
#         total += num
#
# print(total)

# 43 Спросите у пользователя, в каком направлении он хочет вести отсчет (в прямом или обратном). Если
# выбран прямой отсчет, запросите число и проведите отсчет от 1 до введенного числа. Если выбран
# обратный отсчет, запросите число меньше 20, а затем проведите обратный отсчет от 20 до заданного числа.
# Если введено что-то другое, выведите сообщение «I don’t understand».

# word = input('forward or backward ')
# if word == 'forward':
#     num = int(input('Enter number '))
#     for i in range(1, num, 1):
#         print(i)
#     print(num)
# elif word == 'backward':
#     num = int(input('Enter number less than 20: '))
#     for i in range(20, num, -1):
#         print(i)
#     print(num)
# else:
#     print(' I don`t understand')

# 44 Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено
# число меньше 10, запросите имена и после каждого имени выведите строку «[имя] has been invited».
# Если введенное число больше или равно 10, выведите сообщение «Too many people».

guests = int(input('How many people you want to invite? >>> '))
if guests < 10:
    for i in range(0, guests):
        name = input('enter another guest:  >>> ')
        print(name, 'has been invited')
else:
    print('Too many people')

