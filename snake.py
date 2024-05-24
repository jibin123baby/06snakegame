from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90.0
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_segments()
        self.head = self.segment_list[0]
        # print(self.head)

    def create_segments(self):
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[i - 1].xcor()
            new_y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            # print(self.head.heading())
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            # print(self.head.heading())
            self.head.setheading(LEFT)

    def add_snake_segment(self,position):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.setpos(position)
        self.segment_list.append(new_turtle)
        # print(len(self.segment_list))

    def extend_snake_segment(self):
        self.add_snake_segment(self.segment_list[-1].position())