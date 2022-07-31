import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race (pink, blue, orange, "
                                                           "magenta, red, green)? Enter a color: ")

print(user_bet)
colors = ["pink", "blue", "orange", "magenta", "red", "green"]
y_pos = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle won.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)










screen.exitonclick()


# def move_forwards():
#     skipper.fd(10)
#
#
# def move_backwards():
#     skipper.back(10)
#
#
# def turn_clockwise():
#     skipper.right(10)
#
#
# def turn_counterclock():
#     skipper.left(10)
#
#
# def clear_drawing():
#     skipper.clear()
#     skipper.penup()
#     skipper.home()
#     skipper.pendown()
#
#
# screen.listen()
# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_backwards, key="s")
# screen.onkey(fun=turn_counterclock, key="a")
# screen.onkey(fun=turn_clockwise, key="d")
# screen.onkey(fun=clear_drawing, key="c")
#
# screen.exitonclick()
