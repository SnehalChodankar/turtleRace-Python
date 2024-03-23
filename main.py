import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win race? Color: ")
# print(user_bet)
is_race_on = False

x = 500
y = -100
print(y)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    y += 30
    tim.goto(x=-230, y=y)
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        x_pos = turtle.xcor()
        if x_pos >= 230:
            # print(turtle.color())
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won!!! The {winner} turtle finished first!!!")
            else:
                print(f"You have lost!!! The {winner} turtle finished first!!!")

        dist = random.randint(0, 10)
        turtle.forward(dist)

# print(turtles)
screen.exitonclick()
