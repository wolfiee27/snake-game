import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5, 1)
        self.color("blue")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        x_pos = random.randint(-230 ,230)
        y_pos = random.randint(-230, 230)
        self.goto(x=x_pos,y= y_pos)