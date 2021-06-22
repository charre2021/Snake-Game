import turtle
import time
import random
from SnakeGameSetup import *
from SnakeGameMovement import *

segments = []

# Main Gameplay
while True:
	wn.update()
	if head.xcor() > right_border - 10 or head.xcor() < left_border + 10 or head.ycor() > top_border - 10 or head.ycor() < bottom_border + 10:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {}  High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
	if head.distance(food) < 20:
		x = random.randint(left_border + 30, right_border - 30)
		y = random.randint(bottom_border + 30, top_border - 30)
		food.goto(x, y)

		# Adding Segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("black") # Tail color.
		new_segment.penup()
		segments.append(new_segment)
		delay += 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))
	# Checking head collisions with body segments.
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x,y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()

			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))
	time.sleep(delay)

wn.mainloop()





