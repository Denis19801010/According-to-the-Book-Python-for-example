# 20 Предложите пользователю ввести имя. Выведите длину имени.

# name = input('Enter your name >>> ')
# print(len(name))

# 21 Предложите пользователю ввести сначала имя, а затем фамилию. Соедините их, разделив про-
# белом, после чего выведите полное имя и его длину.

# name = input('Enter your name >>> ')
# surname = input('Enter your surname >>> ')
# print(name + ' ' + surname)

# 22 Предложите пользователю ввести имя и фамилию в нижнем регистре.
# Преобразуйте строки к титульному регистру и соедините их.

# name = input('Enter your name in lowercase >>> ').title()
# surname = input('Enter your surname in lowercase >>> ').title()
# # name = name.title()
# # surname = surname.title()
# print(name + ' ' + surname)

# 23 Предложите пользователю ввести первую строку какого нибудь стихотворения, выве-
# дите длину строки. Запросите начальную и конечную позицию и выведите только эту часть строки
#
# poem = input('Enter your poem >>> ')            # I love you, i need you, i fuck you!
# print('This poem have a', len(poem), 'symbols')
# begin_pos = int(input('Enter begin position: '))
# end_pos = int(input('Enter end position'))
# print(poem[begin_pos:end_pos])

# 24 Предложите пользователю ввести имя. Выведите его в верхнем регистре

# name = input('Enter your name >>> ').upper()
# print(name)

# 25 Предложите пользователю ввести имя. Если длина имени меньше 5 символов, предложите ввести фамилию,
# соедините их (без пробела) и выведите полное имя в верхнем регистре. Если длина имени составляет 5 и
# более символов, выведите имя в нижнем регистре.

# name = input('Enter your name >>> ')
# if len(name) < 5:
#     surname = input('Enter your surname >>> ')
#     print(name.upper() + surname)
# else:
#     print(name.lower())

# 26 В шифре «поросячья латынь» начальная согласная буква слова перемещается в конец слова, и к ней до-
# бавляется суффикс «ay». Если слово начинается с гласной, к нему просто добавляется суффикс «way». Напри-
# мер, pig превращается в igpay, banana — в ananabay, а aardvark — в aardvarkway. Напишите программу,
# которая предлагает пользователю ввести слово и преобразует его в «поросячью латынь». Проследите за тем,
# чтобы новое слово выводилось в нижнем регистре.


words1 = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
words2 = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
word = input('Enter your word, motherfucker >>>> ').lower()
if word[0] in words1:
    word = word + 'ай'
    print(word)

elif word[0] in words2:
    word = word[1:] + 'айяяяй' + word[:1]
    print(word)



