from turtle import Turtle
BALL_MOVEMENT = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.xcor_move = 10
        self.ycor_move = 10
        self.move_speed = 0.1
        #This the sleep time of our screen refresh. We will decrease this number to increase
        # the speed of our ball
    def move_ball(self):
        self.penup()
        new_x = self.xcor() + self.xcor_move
        new_y = self.ycor() + self.ycor_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ycor_move *= -1

    def bounce_x(self):
        self.xcor_move *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 #Resetting the screen sleep timer after any player loses a point
        self.bounce_x()
