import random
from turtle import Turtle, Screen

screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

all_turtles = []

turtle_colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
k = 0
dy = -100
for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colours[k])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=dy)
    dy += 25
    k += 1
    all_turtles.append(new_turtle)

winning_colour=""
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
if user_bet == winning_colour:
    print(f"You have won the game! {winning_colour} turtle is the winner")
else:
    print(f"You have lost the game :(, {winning_colour} turtle is the winner")


screen.exitonclick()