import random
from turtle import Turtle, Screen
from random import choice

#Screen
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Who will win the race? Enter a colour: ")

#Preparations
colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
is_race_on = False
i = 0

# Turtle
for colour in colours:
    turtle_colour = colour
    colour = Turtle(shape = "turtle")
    colour.penup()
    spacing = -70 + (30 * i)
    colour.goto(x = -230, y = spacing )
    i += 1
    colour.color(f"{turtle_colour}")
    all_turtles.append(colour)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            winning_colour = turtle.pencolor()

            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
                
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

