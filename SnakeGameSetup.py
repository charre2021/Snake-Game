import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Create window screen.
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("gainsboro")

# Set window height and width.
width = 800
height = 600
left_border = -width/2
right_border = width/2
top_border = height/2
bottom_border = -height/2
wn.setup(width, height)
wn.tracer(0)

# Create head of snake.
head = turtle.Turtle()
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "Stop"

# Create food for snake.
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'blue'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, top_border - 50)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))