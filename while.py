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

number = int(input('Enter number from 10 to 20 >>> '))

while number > 20:
    print('too high')
if number <10:
    print('too low')
    number = int(input('Enter number from 10 to 20 >>> '))
print('Thank you')


