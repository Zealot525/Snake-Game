from turtle import Screen
import time
from snakebrain import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snek Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")


is_on = True
while is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.food_move_location()
        snake.extend_snake()
        score.add_score()
    # losing conditions
    # 1 lose when touch 4 walls
    if snake.head.xcor() > 290 or  snake.head.xcor() < -290 or snake.head.ycor() >  290 or snake.head.ycor() < -290 :
        is_on= False
        score.you_lose()
    # 2 lose when touching its own body
    for parts in snake.snake_body[1:]:
        if snake.head.distance(parts) < 10:
            is_on = False
            score.you_lose()
    

screen.exitonclick()






