from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_segments()
        self.head = self.segment_list[0]
        print(self.head)

    def create_segments(self):
        for position in STARTING_POSITIONS:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.setpos(position)
            self.segment_list.append(new_turtle)

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[i - 1].xcor()
            new_y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)
