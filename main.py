from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
position_list = [(0, 0), (-20, 0), (-40, 0)]
turtle_list = []
screen.setup(600, 600)
# print(screen.screensize())
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

print(len(turtle_list))
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        # print("Got Snack")
        snake.extend_snake_segment()
        scorecard.update_score()
        food.refresh()

    # To detect colliding with the Wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        # print("hit Wall")
        game_on = False
        # print(snake.head.pos())
        scorecard.game_over()

    # To detect colliding with the Tail

    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scorecard.game_over()
screen.exitonclick()
