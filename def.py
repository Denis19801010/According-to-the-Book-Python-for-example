# def get_name():
#     user_name = input('Enter your name: ')
#     return user_name
#
# def print_Msg(user_name):
#     print('Hello', user_name)
#
# def main():
#     user_name = get_name()
#     print_Msg(user_name)
#
# main()
#
# def get_data():
#     user_name = input('Enter your name: ')
#     user_age = int(input('Enter your age: '))
#     data_tuple = (user_name, user_age)
#     return data_tuple
#
#
#
# def message(user_name, user_age):
#     if user_age > 10:
#         print('Hello', user_name)
#     else:
#         print('Hi', user_name)
#
#
# def main():
#     user_name, user_age = get_data()
#     message(user_name, user_age)
#
#
# main()

# 118  Определите подпрограмму, которая предлагает пользователю ввести число и сохраняет его в переменной num.
# Определите другую подпрограмму, которая использует значение num и проводит отсчет от 1 до этого числа.
# def number():
#     num = int(input('Enter number >>> '))
#     return num
#
#
# def number_1(num):
#     n = 1
#     while n <= num:
#         print(n)
#         n += 1
#
#
# def main():
#     num = number()
#     number_1(num)
#
#
# main()

# 119  Определите подпрограмму, которая предлагает пользователю выбрать большое и маленькое число, а затем генерирует
# случайное число из этого диапазона и сохраняет его в переменной с именем comp_num. Определите другую подпрограмму,
# которая выводит сообщение «I am thinking of a number…», после чего предлагает пользователю угадать загаданное число.
# Определите третью подпрограмму, которая проверяет, совпадает ли comp_num с предположением пользователя. Если
# совпадает, то подпрограмма выводит сообщение «Correct, you win»; в противном случае цикл продолжается, а подпрограм-
# ма сообщает, больше или меньше их предположение загаданного числа, и предлагает сделать новую попытку до тех пор,
# пока пользователь его не угадает.
#
# import random
#
#
# def big_low():
#     big = int(input('Enter max number >>> '))
#     low = int(input('Enter min number >>> '))
#     comp_num = random.randint(big, low)
#     print(comp_num)
#     return comp_num
#
#
# def message():
#     guess = int(input('I am thinking of a number... '))
#     return guess
#
#
# def gess_num(comp_num, guess):
#     while guess != comp_num:
#         if guess == comp_num:
#             print('Correct, you win! ')
#         elif guess > comp_num:
#             print('The number you a call is more bigger than comp_num >>> ')
#             guess = int(input('Enter the number you want to guess >>> '))
#         else:
#             guess < comp_num
#             print('The number you a call is more lower than comp_num >>> ')
#             guess = int(input('Enter the number you want to guess >>> '))
#
#     print('Correct, you win! ')
#
#
# def main():
#
#     comp_num = big_low()
#     guess = message()
#     gess_num(comp_num, guess)
#
#
# main()


# 120 Отобразите для пользователя следующее меню:
# 1) Addition
# 2) Subtraction
# Enter 1 or 2:
# Если пользователь выбирает 1, запускается подпрограмма, генерирующая два случайных числа из диапазона между 5 и 20.
# Предложите пользователю сложить их. Рассчитайте правильный ответ и выведите его для пользователя вместе с его ответом.
# Если он выбирает 2, должна запускаться подпрограмма, генерирующая случайное число между 25 и 50, а затем еще одно
# между 1 и 25. Попросите пользователя вычесть второе из первого: так ему не придется беспокоиться об отрицательных
# значениях. Выведите правильный ответ вместе с ответом пользователя. Создайте еще одну подпрограмму, которая будет
# проверять совпадение ответа пользователя с правильным ответом. Если ответы совпали, выведите сообщение «Correct»;
# в противном случае выведите «Incorrect, the answer is» и правильный ответ. Если пользователь ввел некорректное
# значение в самом первом меню, выведите соответствующее сообщение
#
# import random
#
# print(' 1) Addition\n', '2) Subtraction \n\n', 'Enter 1 or 2')
#
#
# def random_1():
#     num1, num2 = random.randint(5, 21), random.randint(5, 21)
#     print(num1, num2)
#     correct_answer = num1 + num2
#     addition_nums = int(input('Enter the sum of the displayed numbers >>> '))
#     print('My answer', addition_nums)
#     print('Comp answer', correct_answer)
#     answers = (addition_nums, correct_answer)
#     return answers
#
#
# def random_2():
#     num3, num4 = random.randint(25, 50), random.randint(1, 25)
#     print(num3, num4)
#     correct_answer = num3 - num4
#     addition_nums = int(input('Enter the difference of the displayed numbers '))
#     print('My answer', addition_nums)
#     print('Comp answer', correct_answer)
#     answers = (addition_nums, correct_answer)
#     return answers
#
#
# def correct(correct_answer, answers):
#     if correct_answer == answers:
#         print('Correct, ёпта! ')
#     else:
#         print('Не correct нифига!', ' the correct answer is... ', answers)
#
#
# def main():
#     num_menu = int(input('Enter the number of menu:'))
#     if num_menu == 1:
#         correct_answer, answers = random_1()
#         correct(correct_answer, answers)
#     elif num_menu == 2:
#         correct_answer, answers = random_2()
#         correct(correct_answer, answers)
#     else:
#         print('Incorrect, selection')
# main()

# 121 Напишите программу, которая помогает пользователю легко управлять списком имен. Программа должна выводить меню,
# дающее возможность добавлять, изменять и удалять имена из списка, а также отображать их все. Кроме того, в меню должна
# присутствовать команда для завершения работы программы. Если пользователь выбрал несуществующую команду, программа
# выводит соответствующее сообщение. После того как пользователь выбрал команду добавления, изменения или удаления имени
# или просмотра всех имен, меню должно выводиться снова без необходимости перезапуска программы. Программа должна быть
# по возможности простой и удобной в использовании.

#
# def add_names():
#     name = input('Enter а name to add to the list >>> ')
#     names.append(name)
#     return names
#
#
# def change_name():
#     num = 0
#     for x in names:
#         print(num, x)
#         num += 1
#     sel_num = int(input('Enter the number of the name you want  to change >>> '))
#     name = input('Enter new name >>> ')
#     names[sel_num] = name
#     return names
#
#
# def del_names():
#     name = input('Enter а name to remove from the list >>> ')
#     names.remove(name)
#     return names
#
#
# def view_names():
#     for x in names:
#         print(x)
#     print()
#
#
# def main():
#     again = 'y'
#     while again == 'y':
#         print(' 1) Append to list\n', '2) Сhange list\n', '3) Remove from list\n', '4) Show list\n', '5) Exit\n\n',
#               'Select: ')
#         num_menu = int(input('Enter a number from the menu >>> '))
#         if num_menu == 1:
#             name = add_names()
#             # print(name)
#         elif num_menu == 2:
#             name = change_name()
#         elif num_menu == 3:
#             name = del_names()
#         elif num_menu == 4:
#             print(names)
#             print()
#         elif num_menu == 5:
#             again = 'n'
#         else:
#             print(' Incorrect select ')
#         data = (names, again)
#
#
# names = []
# main()
