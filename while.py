# 45 Присвойте total значение 0. Пока значение total равно 50 или менее, предложите пользователю
# ввести число. Прибавьте это число к total и выведите сообщение «The total# is… [total]».
# Цикл должен остановиться, когда значение total превысит 50.
#
# total = 0
# while total <= 50:
#     num = int(input('Enter number >>> '))
#     total += num
#     print('The total is... ', total)
#
# 46 Предложите пользователю ввести число. Продолжайте запрашивать число, пока введенное число не
# будет больше 5, после чего выведите сообщение «The last number you entered was a [число]» и
# остановите программу.

# num = int(input('Enter number >>> '))
# while num < 5:
#     num = int(input('Enter number >>> '))
#     print('The last number you entered was a', num)

# 47 Предложите пользователю ввести сначала одно число, а затем другое. Сложите два числа и спросите,
# хочет ли он прибавить еще одно. Если он введет «y», предложите ввести еще одно число; это продолжается до тех
# пор, пока пользователь не введет ответ «y». После того как цикл  oстановится, выведите сумму.

# num1 = int(input('Enter number one >>> '))
# num2 = int(input('Enter number two >>> '))
# summa = num1 + num2
# ask = input('Do you want add one more? ')
# while ask == 'y':
#     num = input('Enter number three >>> ')
#     summa += int(num)
#     ask = input('Do you want add one more? ')
#
# print(summa)
#
# 48 Предложите пользователю ввести имя человека, которого пользователь хочет пригласить на вечеринку.
# После этого выведите сообщение «[имя] has been invited» и увеличьте счетчик на 1. Спросите, хочет ли
# пользователь пригласить кого-то еще. Продолжайте запрашивать имена, пока пользователь неответит отрицательно,
# и выведите количество приглашенных.

# name = input('Enter the name of the invitee >>> ')
# print(name, 'has been invited!')
# i = 1
# ask = input(' Do you want invite one more?')
#
# while ask == 'y':
#     name = input('Enter the name of the invitee >>> ')
#     print(name, 'has been invited!')
#     i += 1
#     ask = input(' Do you want invite one more?')
# print(name, 'has been invited!', ' All invatings is - ', i)

# 49 Создайте переменную с именем compnum и присвойте ей значение 50. Предложите пользователю
# ввести число. Пока предположение не совпадает со значением compnum, сообщите, больше оно или меньше
# compnum, и предложите ввести другое число. Если введенное значение совпадет с compnum, выведите
# сообщение «Well done, you took [попытки] attempts».
#
# compnum = 50
# guess_num = int(input('Enter number >>> '))
# i = 0
# while guess_num != compnum:
#     if guess_num > compnum:
#         print('the number you age give is above')
#     else:
#         print('the number you are give is below')
#     guess_num = int(input('take number again >>> '))
#     i += 1
# print('Well Done, you took ', i, ' attempts')

# 50 Предложите пользователю ввести число от 10 до 20. Если введенное значение меньше 10,
# выведите сообщение «Too low» и предложите повторить попытку. Если введенное значение больше 20,
# выведите сообщение «Too high» и предложите повторить попытку. Повторяйте до тех пор, пока не
# будет введено значение из диапазона от 10 до 20, после чего выведите сообщение «Thank you».

# number = int(input('Enter number from 10 to 20 >>> '))
#
# while number < 10 or number > 20:           #10 < number < 20:
#     if number < 10:
#         print('too low')
#     else:
#         print('too high')
#     number = int(input('Enter number from 10 to 20 >>> '))
# print('Thank you')

# # 51 Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles
# # hanging on the wall, and if 1 green bottle should accidentally fall». Затем выведите вопрос: «how many
# # green bottles will be hanging on the wall?». Если пользователь ответит правильно, выведите сообще-
# # ние «There will be [счетчик] green bottles hanging on the wall». Если пользователь ответит неправиль-
# # но, выведите сообщение «No, try again», пока не будет дан правильный ответ. Когда счетчик умень-
# # шится до 0, выведите сообщение «There are no more green bottles hanging on the wall».
# num = int(input('Enter quantity bottles >>> '))
# print('There are', num, 'green bottles hanging on the wall,', num, '''green bottles hanging on the wall,
# and if 1 green bottle should accidentally fall''')
# num1 = int(input('how many green bottles will be hanging on the wall?'))
# print(num)
# while num1 != 0:
#     num -= num1
#     print(num1)


 #51 Выведите строки «[счетчик] зеленых бутылки стояли на столе, [счетчик] зеленых бутылки стояли на столе
# и есил одна бутылка упала со стола». Затем выведите вопрос: «сколько зеленых бутылок осталось на столе?».
# Если пользователь ответит правильно, выведите сообщение «Да, [счетчик] зеленых бутылки осталось на столе
# Если пользователь ответит неправильно, выведите сообщение «No, try again», пока не будет дан правильный ответ.
# Когда счетчик уменьшится до 0, выведите сообщение «больше не осталось бутылок на столе».
# num = int(input('сколько пузырей >>> '))
# while num > 0:
#     print(num, 'зеленых бутылки стояли на столе,', num, '''зеленых бутылки стояли на столе,
#     но вдруг одна бутылка упала со стола''')
#     num -= 1
#     num1 = int(input('то сколько бутылок осталось на столе?'))
#     if num1 == num:
#         print(num1, ' бутылок осталось на столе')
#     else:
#         while num1 != num:
#             num1 = int(input('НЕПРАВИЛЬНО'))
# print('Всё кончились пузыри')



