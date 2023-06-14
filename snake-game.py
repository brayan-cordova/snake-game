################################################################################

# Turtle Game
# Author Brayan Cordova - #BLC

################################################################################


# library import.
import turtle
import time

# delay for snake
delay = 0.1

###### Start - Customizing the game #####

s = turtle.Screen()  # show screen.
s.setup(700, 700)  # size of screen.
s.title("Turtle Game by Brayan Cordova - #BLC")  # title of window.
s.bgcolor("black")  # background color.

##### End - Customizing the game #####


###### Start - Building Snake #####

snake = turtle.Turtle()
snake.speed(2)  # speed snake.
snake.shape("square")  # snake shape.
snake.penup()  # i give him the instruction not to draw.
snake.goto(0, 0)  # starting point for snake.
snake.direction = "left"  # when the program end, restart the game.
snake.color("green")  # snake color

##### End - Building Snake #####


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


while True:
    s.update()  # update the screen with information
    movement()
    time.sleep(delay)  # delay for snake

##### End - Snake Movement #####

turtle.done()  # keep the windows open.
