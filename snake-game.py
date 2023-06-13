################################################################################

# Turtle Game
# Author Brayan Cordova - #BLC

################################################################################


# library import.
import turtle

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
snake.direction = "stop"  # when the program end, restart the game.
snake.color("green")  # snake color

##### End - Building Snake #####

turtle.done()  # keep the windows open.
