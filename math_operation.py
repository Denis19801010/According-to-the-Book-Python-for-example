import math

# 27 Предложите пользователю ввести число с большим количеством знаков в дробной
# части. Умножьте это число на 2 и выведите ответ.

# num_float = float(input('Enter float number >>> '))
# print(num_float * 2)

# 28 Измените программу из задачи 027 так, чтобы она выводила результат с точностью до двух
# знаков в дробной части.

# num_float = float(input('Enter float number >>> '))
# print(round(num_float * 2, 2))

# 29 Предложите пользователю ввести целое число больше 500. Вычислите квадратный корень из этого числа
# и выведите его с точностью до двух знаков в дробной части.

# num = int(input('Enter the number more than 500 >>> '))
# num = math.sqrt(num)
# print(round(num, 2))

# # 30 Выведите число «пи» (π) с точностью до 5 знаков.
# print(round(math.pi, 5))

# 31  Предложите пользователю ввести радиус круга (расстояние от центра до внешней границы.) Вычислите
# площадь круга (π * радиус2).
#
# radius = int(input('Enter radius >>> '))
# s = math.pi * (radius ** 2)
# print(s)

# 32 Предложите пользователю ввести радиус и высоту цилиндра. Вычислите его объем (площадь круга * высота)
# и выведите его с точностью до трех знаков.

# radius = int(input('Enter radius >>> '))
# high = int(input('Enter high '))
# s = math.pi * (radius ** 2)
# volume = s * high
# print('Volume is ', volume)

# 33 Предложите пользователю ввести два числа. Используйте целочисленное деление, чтобы разделить пер-
# вое число на второе; вычислите остаток и выведите ответ в виде, удобном для пользователя (например,
# если пользователь ввел 7 и 2, выведите строку вида «если разделить 7 на 2, получится 3 с остатком 1»).

# num1 = int(input('Enter number one >>> '))
# num2 = int(input('Enter number two >>> '))
# res = num1 // num2
# res1 = num1 % num2
# print('если разделить', num1, ' на', num2, ' получится', res, ' с остатком', res1)

# 34 Выведите следующее сообщение:
#   1) Square
#   2) Triangle
#   Enter a number:

# Если пользователь вводит 1, программа запрашивает длину стороны квадрата и выводит его площадь. Если
# пользователь вводит 2, программа запрашивает длину стороны и высоту треугольника, проведенную к этой
# стороне, после чего выводит его площадь. Если пользователь вводит что-то другое, программа должна вы-
# дать подходящее сообщение об ошибке.
# num = int(input(' 1) Square \n 2) Triangle \n \n Enter a number: '))
# if num == 1:
#     a = int(input('Enter long line square >>> '))
#     s_square = a ** 2
#     print('The area of square is ', s_square)
# elif num == 2:
#     a = int(input('Enter long side triangle >>> '))
#     h = int(input('Enter high triangle >>> '))
#     s_triangle = (a * h) * .5
#     print('The area of triangle is ', s_triangle)
# else:
#     print('You are stupid, fuckin asshole, enter only 1 OR 2')



