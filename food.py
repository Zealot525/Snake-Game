from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # when creating inheritance, can just straight away use superclass's attributes
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.speed(0)
        self.color("grey")
        self.food_move_location()

    def food_move_location(self):
        x_position = random.randrange(-280,280,20)
        y_position = random.randrange(-280,280,20)
        self.goto(x_position,y_position)