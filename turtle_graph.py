# # # 60 Нарисуйте квадрат.
# import turtle
# turtle.shape('turtle')
# for i in range(1, 5):
#     turtle.forward(60)
#     turtle.right(90)
# turtle.exitonclick()

# #
# # 61 Нарисуйте треугольник
# import turtle
# turtle.shape('turtle')
# for i in range (1, 4):
#     turtle.forward(50)
#     turtle.right(120)
# turtle.exitonclick()

# 62 Нарисуйте круг.
# import turtle
# turtle.shape('turtle')
# for i in range(1):
#     turtle.circle(100)
# turtle.exitonclick()

# 63 Нарисуйте в один ряд три квадрата, разделенных промежутками. Заполните их тремя разными цветами.
# import turtle
#
# turtle.shape('turtle')
# turtle.color("black", "red")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
#
# turtle.pendown()
# turtle.color("black", "yellow")
# turtle.begin_fill()
# for i in range(1, 5):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
#
# turtle.pendown()
# turtle.color("red", "blue")
# turtle.begin_fill()
# for i in range(1, 5):
#
#     turtle.forward(70)
#     turtle.right(90)
# turtle.end_fill()
#
# turtle.exitonclick()

# 64  Нарисуйте пятиконечную звезду.
# import turtle
# turtle.shape('turtle')
# #
# for i in range(1):
#     turtle.forward(150)
#     turtle.right(144)
#     turtle.forward(150)
#     turtle.right(144)
#     turtle.forward(150)
#     turtle.right(144)
#     turtle.forward(150)
#     turtle.right(144)
#     turtle.forward(150)

# ДРУГОЙ ВАРИАНТ
#
# for i in range(0, 125):
#
#     turtle.forward(140)
#     turtle.right(170)
# turtle.exitonclick()

# 65 Нарисуйте цифры, изображенные ниже, начиная от нижней точки цифры 1.( 1, 2, 3, 4 ,5, 6, 7 ,8 ,9, 0)
# import turtle
# turtle.shape('turtle')
# scr = turtle.Screen()
# scr.bgcolor("gray")
# turtle.left(90)
# turtle.forward(100)
# turtle.left(145)
# turtle.forward(50)
# turtle.penup()
# turtle.forward(180)
# turtle.pendown()
# turtle.right(145)
# turtle.forward(30)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(60)
# turtle.right(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(30)
# turtle.left(90)
# turtle.forward(50)
# turtle.penup()
# turtle.forward(180)
# turtle.pendown()
# turtle.forward(60)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(60)
# turtle.left(180)
# turtle.forward(60)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(60)
# turtle.penup()
# turtle.forward(350)
# turtle.left(90)
# turtle.forward(150)
# turtle.pendown()
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(180)
# turtle.forward(80)
# turtle.penup()
# turtle.left(90)
# turtle.forward(40) # расстояние между цифрами в нижнем ряду
# turtle.pendown()
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(40)
# turtle.penup()
# turtle.forward(40) # расстояние между цифрами в нижнем ряду
# turtle.pendown()
# turtle.forward(40)
# turtle.right(180)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(180)
# turtle.penup()
# turtle.forward(80)
# turtle.left(90)
# turtle.forward(40)
# turtle.right(90)
# turtle.pendown()
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(80)
# turtle.penup()
# turtle.left(90)
# turtle.forward(40)
# turtle.pendown()
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(180)
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(40)
# turtle.penup()
# turtle.forward(80)
# turtle.pendown()
# turtle.right(180)
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(40)
# turtle.right(90)
# turtle.forward(80)
# turtle.right(90)
# turtle.forward(40)
# turtle.penup()
# turtle.left(180)
# turtle.forward(80)
# turtle.pendown()
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(155)
# turtle.penup()
# turtle.forward(30)
# turtle.pendown()
# turtle.forward(35)
#
# turtle.hideturtle()
# turtle.exitonclick()

# 66 Нарисуйте восьмиугольник, все стороны которого окрашены в разные цвета (случайно выбираемые
# из списка шести возможных цветов).
# import turtle
# import random
# turtle.pensize(16)
# turtle.shape('turtle')
#
# for i in range(8):
#     turtle.color(random.choice(['red', 'blue', 'green', 'yellow', 'pink', 'purple']))
#     turtle.forward(100)
#     turtle.right(45)
# turtle.exitonclick()

# 67 нарисуйте узор ВАСИЛЁК получился
# import turtle
# turtle.shape('turtle')
# for i in range(50):
#     turtle.forward(60)
#     turtle.right(72)
#     turtle.forward(60)
#     turtle.right(172)
# turtle.exitonclick()

# 67 нарисуйте узор
# import turtle
# turtle.shape('turtle')
# for i in range(0, 40, 1):
#     turtle.right(40)
#     for j in range(0, 8, 1):
#         turtle.forward(60)
#         turtle.right(45)
# turtle.exitonclick()

# 68 Нарисуйте узор, который меняется при каждом запуске программы. Используйте функцию random для
# выбора количества линий, длины каждой линии и каждого угла поворота.
# import turtle
# import random
# a, b, c = random.randint(0,100), random.randint(0, 100), random.randint(0, 100)
#
# turtle.shape('turtle')
# for i in range(0, 40, 1):
#     turtle.right(c)
#     for j in range(0, 8, 1):
#         turtle.forward(b)
#         turtle.right(a)
# turtle.exitonclick()

# ДРУГОЙ СПОСОБ ЭТО ВООБЩЕ СУМАШЕДШАЯ ЧЕРЕПАХЫРЬ
import random
import turtle
turtle.shape('turtle')
lines = random.randint(5, 1000)

for i in range(0, lines):
    length = random.randint(2, 100)
    rotate = random.randint(4, 360)
    turtle.forward(length)
    turtle.right(rotate)
turtle.exitonclick()
