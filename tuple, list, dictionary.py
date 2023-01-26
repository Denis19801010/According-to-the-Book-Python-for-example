# 69 Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа. Предложите пользователю
# ввести название одной из этих стран и выведите индекс (то есть позицию в списке) этого элемента кортежа.

# country = ('Russia', 'China', 'Brasil', 'Mongoliya', 'Japan')
# print(country)
# country_name = input('Enter country')
# print(country.index(country_name))

# 70 Доработайте программу 069 так, чтобы она предлагала пользователю ввести число и выводила название
# страны, находящейся в заданной позиции.

# country = ('Russia', 'China', 'Brasil', 'Mongoliya', 'Japan')
# print(country)
# country_index = int(input('Enter number country >>> '))
# print(country[country_index])

# 71 Создайте список с названиями двух видов спорта. Предложите пользователю ввести свой любимый вид
# спорта и добавьте его в конец списка. Отсортируйте список и выведите его.
# list = ['Basketball', 'Baseball']
# print(list)
# list.append(input('Enter your favourite kind of sport >>> '))
# list.sort()
# print(list)

# 72 Создайте список с названиями шести школьных предметов. Спросите у пользователя, какие из этих
# предметов ему не нравятся. Удалите выбранные предметы из списка и выведите его повторно.
#
# list = ['Chimestry', 'Match', 'Algebra', 'Geometry', 'Astronomy', 'Literature']
# print(list)
# list.remove(input('What kind of  discipline you don`t like >>> '))
# print(list)

# 73 Предложите пользователю ввести названия четырех любимых блюд и сохраните их в словаре с числовыми
# индексами, начиная c 1. Выведите содержимое словаря с указанием индексов и элементов. Спросите пользова-
# теля, какой элемент он хочет исключить, и удалите его из списка. Отсортируйте оставшиеся данные и выведите
# содержимое словаря.
# dict = {}
#
# add1 = input('Enter your first favourite food >>> ')
# dict[1] = add1
# add2 = input('Enter your second favourite food >>>')
# dict[2] = add2
# add3 = input('Enter your third favourite food >>> ')
# dict[3] = add3
# add4 = input('Enter your fourth favourite food >>> ')
# dict[4] = add4
# delete = int(input('What you want to remove? >>> '))
# dict.pop(delete)
#
# print(sorted(dict.items()))

# 74 Введите список из десяти цветов. Предложите пользователю ввести начальное число в диапазоне от
# 0 до 4 и конечное число в диапазоне от 5 до 9. Выведите список цветов из интервала, заданного
# начальным и конечным числом.
#  Н Е Т   Р Е Ш Е Н И Я
#
# colours = ["red", "black", "white", "green", "purple", "gray", "orange", "blue", "yellow", "silver"]
# num1 = int(input('Enter the color from 0 to 4 >>> '))
# num2 = int(input('Enter color from 5 to 9 >>> '))
# print(colours(num1 : num2))

# 75 Создайте список из четырех трехзначных чисел. Выведите содержимое списка, при этом каждый
# элемент должен выводиться на отдельной строке. Предложите пользователю ввести число из трех
# цифр. Если введенное число совпадает с одним из чисел в списке, выведите позицию этого числа;
# в противном случае выведите сообщение «That is not in the list».

# num_list = [123, 456, 789, 012]
# for i in num_list:
# 	print(i)
# num = int(input('Enter number >>> '))
# if num in num_list:
# 	print(num_list.index(num))
# else:
# 	print('That is not in the list')


# 76 Предложите пользователю ввести имена трех людей, которых он хочет пригласить на вечеринку,
# и сохраните их в списке. После того как будут введены все три числа, спросите, хочет ли
# пользователь добавить еще одно имя. Если ответ будет положительным, предложите ему добавлять
# имена, пока не получите ответ «no». После ответа «no» выведите количество людей, приглашенных на вечеринку.

# on_party = []
# people_on_party = on_party.append(input('Enter people >>> '))
# for i in range(0, 2):
# 	people_on_party = on_party.append(input('Enter people >>> '))
#
# more_people = input('Did you want more people?: ')
# while more_people != 'no':
# 	people_on_party = on_party.append(input('Enter people >>> '))
# 	more_people = input('Did you want more people?: ')
# print('All people .... :', len(on_party))
#
# 77 Измените программу 076, чтобы после ввода списка имен программа выводила полный список.
# Предложите пользователю ввести одно из имен в списке и выведите позицию имени в списке. Спро-
# сите, хочет ли пользователь, чтобы этот человек присутствовал на вечеринке. Если пользователь от-
# ветит «no», удалите элемент из списка и снова выведите список.

# on_party = []
# people_on_party = on_party.append(input('Enter people >>> '))
# for i in range(0, 2):
# 	people_on_party = on_party.append(input('Enter people >>> '))
# 	print(on_party)
#
# more_people = input('Did you want more people?: ')
# while more_people != 'no':
# 	people_on_party = on_party.append(input('Enter people >>> '))
# 	print(on_party)
# 	more_people = input('Did you want more people?: ')
#
# print('All people .... :', len(on_party))
#
# name = input('Enter the name from list >>> ')
# print(on_party.index(name))
# name_remove = input('Do you want to see that man on the party?: ')
# if name_remove == 'no':
# 	on_party.remove(name)
# print(on_party)

# 78 Создайте список с названиями четырех телевизионных передач и выведите их на отдельных строках.
# Предложите пользователю ввести название еще одной передачи и позицию, на которой она должна быть
# вставлена в список. Снова выведите список, в котором все пять передач находятся на новых позициях.
#
# tv_programs = ['Vesti', '1 channel', 'tnt4', 'ctc']
# for i in tv_programs:
# 	print(i)
#
# place = int(input('Enter place for programm >>> '))
# progr = input('Enter one more tv programm >>> ')
# tv_programs.insert(place, progr)
# print(tv_programs)

# 79 Создайте пустой список с именем nums. Предложите пользователю последовательно вводить числа. После ввода
# каждого числа добавьте его в конец списка nums и выведите список. После того как пользователь введет
# три числа, спросите, хочет ли он оставить последнее введенное число в списке. Если пользователь от-
# ветит «no», удалите последний элемент из списка. Выведите список.

nums = []
num = nums.append(input('Enter numbers >>> '))
print(nums)




