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

# 38 Измените программу из упражнения 37 так, чтобы она также запрашивала число. Выведите
# имя (по одной букве в каждой строке) и по вторите вывод равное введенному числу коли-
# чество раз.

name = input('Enter your name >>> ')
num = int(input('Enter number >>> '))
for k in range(0, num):
    for i in name:
        print(i)

