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
import turtle
turtle.shape('turtle')
turtle.color('black', 'yellow')
turtle.begin_fill()
for i in range(1, 5):
    turtle.forward(60)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.begin_fill()
for i in range(1, 5):
    turtle.forward(60)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.exitonclick()

