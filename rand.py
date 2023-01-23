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
import random
num = random.randint(1, 5)
guess = int(input('Enter number between 1 and 5 >>> '))
print(num)

if guess == num:
    print('Well done!)')
while guess != num:
    if guess > num:
        print('your number is too low')
    else:
        guess < num
        print('your number is too low')
    guess + int(input('Enter number between 1 and 5 >>> '))
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

