# 088 Предложите пользователю ввести пять целых чисел и сохраните их в массиве. Отсортируйте список
# и выведите его содержимое в обратном порядке.
#
#
# from array import *
#
# nums = array('i', [])
# new_num = int(input('Enter number of characters in the array'))
# for y in range(0, new_num):
#     newValue = int(input('Enter number for append to array: '))
#     nums.append(newValue)
# nums = sorted(nums)
# print(nums)
# nums.reverse()
# print(nums)

# 089 Создайте массив для хранения целых чисел. Сгенерируйте пять случайных чисел и сохраните их в массиве.
# Выведите массив (каждый элемент должен выводиться в отдельной строке).
#
# import random
# from array import *
#
# arrays = array('i', [])
# for i in range(0, 5):
#     newValue = random.randint(0, 50)
#     arrays.append(newValue)
# for i in arrays:
#     print(i)
# #
# 090 Предложите пользователю вводить целые числа. Если пользователь вводит число от 10 до 20, сохраните его в массиве;
# в противном случае выведите сообщение «Outside the range».После того как пять чисел будут успешно добавлены в массив,
# выведите сообщение «Thank you» и выведите массив, каждый элемент которого находился бы на отдельной строке.
# from array import *
# array = array('i', [])
# while len(array) < 5:
#     num = int(input(' Enter integer numbers from 10 to 20 >>> '))
#     if 10 < num < 20:
#         array.append(num)
#     else:
#         print('Out of range')
# for x in array:
#     print(x)
# 091 Создайте массив, содержащий пять чисел (два из которых должны повторяться). Выведите весь массив. Предложите
# пользователю ввести одно из чисел массива, после чего выведите сообщение, в котором указано, сколько раз число
# встречается в этом массиве.

# from array import *
# array = array('i', [12, 13, 176, 12, 4])
# print(array)
# num = int(input('Enter one number from array >>> '))
# print('The number ', num, 'is', array.count(num), ' times in array')

# 092 Создайте два массива: один будет содержать три числа, введенных пользователем, а другой — пять случайных чисел.
# Объедините эти два массива в один большой. Отсортируйте и выведите его, при этом каждое число должно выводиться
# в отдельной строке.
# from array import *
# import random
#
# array1 = array('i', [])
# array2 = array('i', [])
# i = 0
# j = 0
# while i < 3:
#     num1 = int(input('Enter 3 number in to a array >>> '))
#     array1.append(num1)
#     i += 1
# while j < 5:
#     num2 = random.randint(0, 100)
#     array2.append(num2)
#     j += 1
# array = array2 + array1
# array = sorted(array)
# print(array)
# for x in array:
#     print(x)

# 093 Предложите пользователю ввести пять чисел. Отсортируйте их и выведите для пользователя. Предложите вы-
# брать одно из чисел. Удалите выбранное число из исходного массива и сохраните его в новом.
# from array import *
#
# array1 = array('i', [])
# array2 = array('i', [])
# i = 0
# while i < 5:
#     num = int(input('Enter number >>> '))
#     i += 1
#     array1.append(num)
# array1 = sorted(array1)
# num = int(input('Enter number to remove from first array and added him in second array >>> '))
# array1.remove(num)
# array2.append(num)
# print(array1)
# print(array2)
#

# 094 Выведите массив из пяти чисел. Предложите пользователю выбрать одно из них. После того как число
# будет выбрано, выведите его позицию в маcсиве. Если пользователь введет значение, отсутствующее
# в массиве, предложите ему выбрать снова, пока не будет выбрано допустимое значение.
# from array import *
# array = array('i', [12, 32, 523, 213, 545])
# print(array)
# num = int(input('choice the number from array >>> '))
# while not array.count(num):
#     print(' Error ')
#     num = int(input('choice the number from array >>> '))
# print(array.index(num))

# 095 Создайте массив из пяти чисел от 10 до 100, каждое из которых содержит два знака в дроб-
# ной части. Предложите пользователю ввести целое число от 2 до 5. Если пользователь введет
# значение, выходящее за границы диапазона, выведите сообщение об ошибке и предложите вы-
# брать снова, пока не будет введено допустимое значение. Разделите каждое из чисел в массиве
# на число, введенное пользователем, и выведите ответы с точностью до двух знаков.

from array import *
import math
array1 = array('f', [12.32, 16.27, 67.21, 98.23, 63.32])
num = int(input('Enter integer number, from 2 to 5 >>>'))
while num > 5 or num < 2:
    print('Wrong number, do it again ')
    num = int(input('Enter integer number, from 2 to 5 >>>'))

for n in range(0, 5):
    print(round(array1[n]/num, 2))







































