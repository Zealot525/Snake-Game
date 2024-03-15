from turtle import Turtle

X_STARTING_POSITION = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.start_snake_parts()
        self.head = self.snake_body[0]
        
    
    def start_snake_parts(self):
        global X_STARTING_POSITION
        for i in range(3):
            parts =Turtle(shape="square")
            parts.color("white")
            parts.up()
            parts.goto(X_STARTING_POSITION,0)
            X_STARTING_POSITION -= 20
            self.snake_body.append(parts)
 

    def move(self):
        for parts in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[parts -1].xcor()
            new_y  = self.snake_body[parts -1].ycor()
            self.snake_body[parts].goto(new_x, new_y)
        self.head.fd(20)


    def extend_snake(self):
        parts = Turtle(shape="square")
        parts.color("white")
        parts.up()
        tail_x_position = self.snake_body[len(self.snake_body) - 1].xcor()
        tail_y_position = self.snake_body[len(self.snake_body) - 1].ycor()
        parts.goto(tail_x_position,tail_y_position)
        self.snake_body.append(parts)


    def up(self):
        if  self.head.heading() != DOWN:
            self.head.setheading(UP)


    def left(self):
        if  self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

    def right(self):
        if  self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def down(self):
        if  self.head.heading() != UP:
            self.head.setheading(DOWN)