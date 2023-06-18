################################################################################

# Turtle Game
# Author Brayan Cordova - #BLC

################################################################################


# library import.
import turtle
import time
import random

# delay for snake
delay = 0.1

# score marker
score = 0
high_score = 0

###### Start - Customizing the game #####

s = turtle.Screen()  # show screen.
s.setup(650, 650)  # size of screen.
s.title("Turtle Game by Brayan Cordova - #BLC")  # title of window.
s.bgcolor("black")  # background color.

##### End - Customizing the game #####


###### Start - Building Snake #####

snake = turtle.Turtle()
snake.speed(2)  # speed snake.
snake.shape("square")  # snake shape.
snake.penup()  # i give him the instruction not to draw.
snake.goto(0, 0)  # starting point for snake.
snake.direction = "stop"  # when the program end, restart the game.
snake.color("green")  # snake color

# food for snake
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.speed(0)

##### End - Building Snake #####


# body for snake
body = []

# show the score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0\t\tHigh Score: 0", align="center", font=("verdana", 24, "normal"))

##### Start - movements of the snake with the keys up, down, right, left #####


# up
def up():
    snake.direction = "up"


# down
def down():
    snake.direction = "down"


# right
def right():
    snake.direction = "right"


# left
def left():
    snake.direction = "left"


##### End - movements of the snake with the keys up, down, right, left #####


###### Start - Snake Movement #####


def movement():
    # up move
    if snake.direction == "up":
        y = snake.ycor()  # shows object's location on the y-axis.
        snake.sety(y + 20)  # moves an object on the y-axis.

    # down move
    if snake.direction == "down":
        y = snake.ycor()  # shows object's location on the y-axis.
        snake.sety(y - 20)

    # right move
    if snake.direction == "right":
        x = snake.xcor()  # shows object's location on the y-axis.
        snake.setx(x + 20)

    # left move
    if snake.direction == "left":
        x = snake.xcor()  # shows object's location on the y-axis.
        snake.setx(x - 20)


# Key Mapping
s.listen()  # screen listen
s.onkeypress(up, "Up")  # up key press
s.onkeypress(down, "Down")  # down key press
s.onkeypress(right, "Right")  # right key press
s.onkeypress(left, "Left")  # left key press


while True:
    s.update()  # update the screen with information

    # game edges
    if (
        snake.xcor() > 300
        or snake.xcor() < -300
        or snake.ycor() > 300
        or snake.ycor() < -300
    ):
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = "stop"
        body.clear()

        # reset score
        score = 0
        text.clear()
        text.write(
            "Score:{}\t\tHigher Score:{}".format(score, high_score),
            align="center",
            font=("verdana", 24, "normal"),
        )

    # food movement
    if snake.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        # food for snake
        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        new_body.goto(0, 0)
        new_body.speed(0)
        body.append(new_body)  # adding new body, but not follow the snake

        # score
        score += 10
        if score > high_score:
            high_score = score
            text.clear()
            text.write(
                "Score:{}\t\tHigher Score:{}".format(score, high_score),
                align="center",
                font=("verdana", 24, "normal"),
            )

    total = len(body)  # return the body len
    for i in range(total - 1, 0, -1):  # we go through the list
        # we got coordinates of the new body of the snake are obtained
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)  # we send the new created body to the serpent

    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    movement()

    # collisions with body
    for i in body:
        if i.distance(snake) < 20:
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            body.clear()
            snake.direction = "stop"

    time.sleep(delay)  # delay for snake

##### End - Snake Movement #####

turtle.done()  # keep the windows open.
