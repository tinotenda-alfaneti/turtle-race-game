from turtle import Turtle, Screen
import random

is_race_on = False
writer = Turtle()
writer_1 = Turtle()
writer.penup()
writer_1.penup()
writer.hideturtle()
writer_1.hideturtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet ", prompt="What turtle will win? Enter color: ")
colours = ["red", "yellow", "purple", "blue", "pink"]

racers = []
race_participants = []
for turtle in range(5):
    racer = Turtle()
    racers.append(racer)

n = 0
colour_index = 0
for racer in racers:
    racer.penup()
    racer.shape("turtle")
    racer.goto(-240, -140 + n)
    racer.color(colours[colour_index])
    colour_index += 1
    n += 60
    race_participants.append(racer)
if user_bet:
    is_race_on = True

while is_race_on:
    writer_1.goto(-120, 130)
    writer_1.write(f"Your bet is {user_bet.upper()} ", False, align="right", font=("Arial", 10, "italic"))
    for participant in race_participants:
        if participant.xcor() > 240:
            if user_bet.lower() == participant.pencolor():
                writer.write(f"{participant.pencolor()} won", False, align="center", font=("Arial", 24, "bold"))
                print(f"You won. The turtle that won is {participant.pencolor()}")
            else:
                writer.write(f"{participant.pencolor()} won", False, align="center", font=("Arial", 24, "bold"))
                print(f"You lose. The turtle that won is {participant.pencolor()}")
            is_race_on = False
        else:
            participant.forward(random.randint(0, 10))


screen.exitonclick()
