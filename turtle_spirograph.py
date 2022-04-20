import random
import turtle
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
# tim.shape("turtle")
# tim.color("blue", "deeppink")
# # for i in range(60):
# #     timmy_the_turtle.forward(140)
# #     timmy_the_turtle.left(105)
# #     timmy_the_turtle.circle(150)
# #     i+=1
#CHALLANGE1
# for i in range (4):
#     tim.forward(100)
#     tim.right(90)
#

#

# screen.exitonclick()

# import heroes
# print(heroes.gen())


#CHALLANGE2

# for i in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
# screen.exitonclick()

#CHALLANGE3


# import random
# y=3
# def change_color():
#     R=random.random()
#     G=random.random()
#     B=random.random()
#     tim.color(R,G,B)
#
# for i in range (3,11):
#     x=360/y
#     change_color()
#     for j in range (y):
#
#         tim.forward(100)
#         tim.right(x)
#     y=y+1
#     x=x-30
# screen.exitonclick()

#CHALLANGE4
# tim.pendown()
# angle = [0,90,180,270]
# def change_color():
#     R=random.random()
#     G=random.random()
#     B=random.random()
#     tim.color(R,G,B)
# x=True
# tim.pensize(10)
# tim.speed('fastest')
# while x == True:
#     change_color()
#     actually_angle = random.choice(angle)
#     tim.setheading(actually_angle)
#     tim.forward(30)


#CHALLANGE5
def change_color():
    R=random.random()
    G=random.random()
    B=random.random()
    tim.color(R,G,B)
teta=5
angle = 0
tim.speed('slowest')
rang = int(360/teta)
for x in range (rang):


    angle = angle + teta
    tim.setheading(angle)
    change_color()

    tim.circle(100)
screen.exitonclick()


# color_list = [ (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]
#
# tim = Turtle()
# screen = Screen()
#
#
# j=0
# for i in range (10):
#     tim.pendown()
#     tim.color(color_list[j])
#     tim.forward(20)
#     tim.penup()
#     tim.forward(50)
#     j+=1
# screen.exitonclick()

