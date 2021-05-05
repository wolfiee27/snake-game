from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_obj = []
        self.create_snake()
        self.head= self.snake_obj[0]

    def create_snake(self):
        x_pos = 0
        y_pos = 0

        for _ in range(0,2):
            new_snake_obj = Turtle(shape="square")
            new_snake_obj.color("white")
            new_snake_obj.penup()
            # new_snake_obj.speed("slowest")
            new_snake_obj.shapesize(0.5, 0.5, 1)
            new_snake_obj.setpos(x_pos, y_pos)
            x_pos -= 12
            self.snake_obj.append(new_snake_obj)


    def move_snake(self,Flag):
        snake_length = len(self.snake_obj)
        len(self.snake_obj)
        self.head.forward(12)
        if Flag == True:
            new_snake_obj = Turtle(shape="square")
            new_snake_obj.color("white")
            new_snake_obj.penup()
            # new_snake_obj.speed("slowest")
            new_snake_obj.shapesize(0.5, 0.5, 1)
            self.snake_obj.append(new_snake_obj)
            snake_length +=1

        for obj_num in range(snake_length - 1 , 0, -1):
            new_x = self.snake_obj[obj_num - 1].xcor()
            new_y = self.snake_obj[obj_num - 1].ycor()
            self.snake_obj[obj_num].goto(new_x, new_y)
        # self.snake_obj[0].forward(12)

    def left(self):
        if self.head.heading() != RIGHT:
         self.snake_obj[0].setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.snake_obj[0].setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_obj[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_obj[0].setheading(DOWN)


