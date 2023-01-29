# 080 Предложите пользователю ввести свое имя, а затем выведите длину имени. Запросите фамилию и выведите длину
# фамилии. Соедините имя с фамилией, разделив их пробелом и выведите результат. Наконец, выведите длину полно-
# го имени (включая пробел).

# name = input('Enter your name >>> ')
# print(len(name))
# surname = input('Enter your surname >>> ')
# print((len(surname)))
# print(name + ' ' + surname)
# print(len(name + ' ' + surname))

# 81 Предложите пользователю ввести его любимый школьный предмет. Выведите
# его так, чтобы после каждой буквы следовал дефис например, S-p-a-n-i-s-h-.
# school_subject = input('Enter favourite subject >>> ')
# for i in school_subject:
#     print(i, end='-')

# 82 Выведите строку из своего любимого стихотворения и предложите пользователю
# ввести начальную и конечную позицию. Выведите символы, находящиеся между ними.

# poem = input(' Enter favourite poem: ')
# begin = int(input('Enter begin position >>> '))
# end = int(input('Enter end position >>> '))
# print(poem[begin:end])

# 83 Предложите пользователю ввести слово в верхнем регистре. Если не все буквы
# слова будут указаны в верхнем регистре, попросите ввести слово заново.
# Повторяйте попытки, пока пользователь не введет сообщение в верхнем регистре.

word = input('Enter word in UPPER: ')
word.isupper()
while not word.isupper():  # у меня было while word.isupper() == False:
    word = input('Enter word in UPPER: ')

