from turtle import Screen
import time
from Snake import Snake1
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake1()
food =Food()
score = Score()

def to_start_game():  
        snake.move()
        
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")



   
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    to_start_game()
    
    
    if snake.head.distance(food) <15 :
        food.refresh()
        snake.extend()
        score.increment_point()

    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_scoreboard()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
           score.reset_scoreboard()
           snake.reset_snake()





screen.exitonclick()