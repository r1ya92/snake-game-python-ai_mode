from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def get_greedy_move(self, food):
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        food_x = food.xcor()
        food_y = food.ycor()

        moves = [
            (UP, head_x, head_y + MOVE_DISTANCE),
            (DOWN, head_x, head_y - MOVE_DISTANCE),
            (LEFT, head_x - MOVE_DISTANCE, head_y),
            (RIGHT, head_x + MOVE_DISTANCE, head_y),
        ]

        opposites = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
        current_heading = self.head.heading()

        best_heading = None
        best_distance = float("inf")

        for heading, next_x, next_y in moves:
            if heading == opposites[current_heading]:
                continue

            dist = abs(next_x - food_x) + abs(next_y - food_y)

            if dist < best_distance:
                best_distance = dist
                best_heading = heading

        return best_heading






