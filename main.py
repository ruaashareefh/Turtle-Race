from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
screen = Screen()
is_race_on = False
all_turtles = []

screen.setup(width=500, height=400)

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






screen.exitonclick()

