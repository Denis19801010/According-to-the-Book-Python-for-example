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