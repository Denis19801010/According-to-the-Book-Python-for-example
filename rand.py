# # 52 Вывести случайное число в диапазоне от 1 до 100 включительно.
# import random
# num = random.randint(0, 100)
# print(num)
import random

# 53 Вывести случайное название фрукта из списка содержащего пять названий.
# fruit = random.choice(['apple', 'carrot', 'cucumber', 'banana', 'potato'])
# print(fruit)

# 54 Случайным образом выберите «орел» или «решку» ("h" или "t"). Предложите пользователю угадать ваш выбор.
# Если ваш выбор совпадает со случайно выбранным значением, выведите сообщение «You win»;
# в противном случае выве дите сообщение «Bad luck». В конце сообщите пользователю, какое значение
# было загадано — «орел» или «решка».

# import random
# name = random.choice(['h', 't'])
# guess = input('Enter name (h/y)')
# if guess == name:
#     print('You win')
# else:
#     print('Loooooser')
# print(name)

# 55 Выберите случайное число в диапазоне от 1 до 5. Предложите пользователю выбрать число.
# Если он угадал, выведите сообщение «Well done»; в противном случае сообщите, что его число
# больше или меньше вашего, и предложите выбрать другое число. Если со второго раза пользователь
# угадал, выведите сообщение «Correct», а если нет — сообщение «You lose».
# import random
# num = random.randint(1, 5)
# guess = int(input('Enter number between 1 and 5 >>> '))
# print('Загаданное число = ', num)
#
# if guess == num:
#     print('Well done!)')
# if guess > num:
#     print('your number is too high')
#     guess = int(input('Enter number between 1 and 5 >>> '))
#     if guess != num:
#         print('Looser')
#     else:
#         print('Correct')
# if guess < num:
#     print('your number is too low')
#     guess = int(input('Enter number between 1 and 5 >>> '))
#     if guess != num:
#         print('Looser')
#     else:
#         print('Correct')


# 56 Выберите случайное целое число в диапазоне от 1 до 10. Предложите пользователю ввести число и проверьте,
# совпадает ли оно с загаданным. Продолжайте запрашивать числа до тех пор, пока пользователь не введет
# случайно выбранное число.
# import random
#
# rand_num = random.randint(1, 10)
# num = int(input('Enter number from 1 to 10 >>> '))
#
# if num == rand_num:
#     print('Ok')
# while num != rand_num:
#     print('Enter number')
#     num = int(input('Enter number from 1 to 10 >>> '))
# print('Ok')

# 057 Измените программу так, чтобы перед повторным предположением она сообщала пользователю, является ли его предпо-
# ложение больше или меньше загаданного числа.
# import random
#
# rand_num = random.randint(1, 10)
# num = int(input('Enter number from 1 to 10 >>> '))
# if num == rand_num:
#     print('OK')
# while num != rand_num:
#     if num > rand_num:
#         print('too high')
#     else:
#         print('too low')
#     num = int(input('Enter number from 1 to 10 >>> '))
# print('OK')

# 58 Напишите математическую игру, в которой пользователь должен ответить на пять вопросов. Каждый вопрос строит-
# ся из двух случайно сгенерированных целых чисел (например, [num1] + [num2]). Предложите пользователю ввести
# ответ.
# import random
# num1, num2 = random.randint(1, 5), random.randint(1, 5)
# num = num1 + num2
# score = 0
# i = 0
# guess_num = int(input('Enter num >>> '))
# print(' number is-', num,)
#
# while i < 4:
#     guess_num = int(input('Enter num >>> '))
#     num1, num2 = random.randint(1, 5), random.randint(1, 5)
#     num = num1 + num2
#     i += 1
#     print(' number is-', num, )
#     if guess_num == num:
#         score += 1
#     print(score)



 # 59 Выведите названия пяти цветов, случайным образом выберите один и предложите сделать то же пользователю.
# Если пользователь выберет тот же цвет, который выбрала программа, выведите сообщение «Well done»; в про-
# тивном случае выведите ответ, в котором скрывается намек на правильный цвет. Предложите пользователю повторить
# попытку; если пользователь и на этот раз не угадает, снова выведите ту же подсказку и предложите выбрать
# цвет (и так далее, пока пользователь не выдаст правильный ответ).
# print('red', 'green', 'black', 'yellow', 'white')
# color_comp = random.choice(['red', 'green', 'black', 'yellow', 'white'])
# print(color_comp)
# choice1 = input('Enter color').lower()
# if color_comp == choice1:
#     print('Well done')
# while choice1 != color_comp:
#
#     if color_comp == 'Red':
#         print('The ... hat')
#     elif color_comp == 'Green':
#         print('The ... grass')
#     elif color_comp == 'Black':
#         print('The ... whole')
#     elif color_comp == 'white':
#         print('The ... snow')
#     elif color_comp == 'yellow':
#         print('The ... sun and sand')
#     choice1 = input('Enter color')
# print('well done')
#




#
#
#
#
#
#
#
#
#
#
#
#
#
# while guess != num:
#     if guess > 5:
#         print('your number is too big')
#     elif guess < 5:
#         print('your number is too low')
