import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
pen = turtle.Turtle()

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move the turtle forward by 100 units
    pen.right(90)     # Turn the turtle right by 90 degrees

# Move the turtle to a new starting position
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Draw a circle
pen.circle(100)  # Draw a circle with a radius of 100 units

# Move the turtle to a new starting position
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a triangle
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Customize and combine shapes
pen.color("red")
pen.begin_fill()  # Begin filling the shape with the chosen color
for _ in range(6):
    pen.forward(50)
    pen.right(60)
pen.end_fill()    # End the filling process

# Close the turtle graphics window on click

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Move the turtle to a new starting position
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Draw a circle
pen.circle(100)

# Move the turtle to a new starting position
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a triangle
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Customize and combine shapes
pen.color("red")
pen.begin_fill()
for _ in range(6):
    pen.forward(50)
    pen.right(60)
pen.end_fill()

# Move the turtle to a new starting position
import random
pen.penup()
pen.goto(0, -150)
pen.pendown()
colors = ['red', 'blue', 'green']
# Draw concentric circles
for i in range(1, 10):
    pen.color(colors[random.randint(0, len(colors) - 1)])
    pen.circle(20 * i , )
    pen.circle(-20 * i )
    

# Simple animation - move the turtle in a circular path
pen.penup()
pen.goto(0, 150)
pen.pendown()

for _ in range(360):  # 36 steps to complete a full circle
    pen.forward(1)
    pen.right(1)

# Close the turtle graphics window on click
screen.exitonclick()
