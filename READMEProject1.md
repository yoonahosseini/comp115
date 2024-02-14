The Night Sky House
Author: Yoona Hosseini

##General Info. This project displays images that have been coded to create the starry night sky and a house with basic detailing. 
##Techniques. Through this code, the use of turtle, pen drawing, for loops, and random generator is used to create the image.
##Technologies. This project is created by using Visual Studio Code with Python
##Setup. To install this project, write this code using Visual Studio Code by downloading Python into it as well

## How to Set Up
# set up turtle screen
import turtle
screen = turtle.Screen()
screen.bgcolor("black")

# create a turtle instance
t = turtle.Turtle()
t.speed(0)


# Draw the night sky as show in code by using t.penup() etc. Then following by using a for __ to create the range.
# Draw moon and beams by setting up your turtle pen as shown in code by continuing to use t.penup() etc.
# To draw the cloud, you can draw multiple circles to merge together into a cloud
# Draw the house, roof, and chimney and choose colour by using the previous code and implementing the for loop
# To create the window cross, you may play around with using (x,y) and moving your turtle around accordingly
# To create the stars, we set up a new turtle by using the following,
import random

t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)
w.bgcolor("black")
t.color("white")

# make the function to draw the stats
def stars():
    for i in range(5):
        t.fd(10)
        t.right(144)

# draw the stars and use the random code for the generator
for i in range(100):

    # generate random integer values for x and y
    x = random.randint(-640, 640)
    y = random.randint(-330, 330)
    stars()
    t.up()
    t.goto(x, y)
    t.down()

t.up()
t.goto(0, 170)
t.down()
t.color("white")
t.begin_fill()

## To hide the turtle, use...
t.hideturtle()

##Usage
After you add Visual Studio Code to your desktop, go to its root directory and run npm install to install its dependencies.
Once the dependencies are installed, you can run VSC start to start the application. You will then be able to access it


##License
You can check out the full license here
https://code.visualstudio.com/license
https://docs.python.org/3/license.html
This project is licensed under the terms of the Microsoft license.

##Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

##Inspiration
Inspiration is used from class examples throughout this semester. 
Examples include:
https://github.com/COMP115-Bravo/comp115_project1
