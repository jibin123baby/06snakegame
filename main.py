from turtle import Screen
import time
from snake import Snake


screen = Screen()
position_list = [(0, 0), (-20, 0), (-40, 0)]
turtle_list = []
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()
