from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time
#global variables
score = 0

# screen setup
screen = Screen()
screen.title("snake game")
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.tracer(0)



#snake class object declaration
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#food class object declaration
food = Food()

#Scoreboard class object declaration
scoreboard = ScoreBoard()

#creating the snake in the screen
snake.create_snake()

#moving the snake
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    snake.move_snake(Flag= False)
    screen.update()
    if snake.head.distance(food) <= 10:
        food.new_location()
        scoreboard.increase_score()
        snake.move_snake(Flag=True)
    if abs(snake.head.xcor()) > 235 or  abs(snake.head.ycor()) > 235:
        scoreboard.game_over()
        is_game_on = False



screen.exitonclick()










