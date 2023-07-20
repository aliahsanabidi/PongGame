from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

BALL_MOVEMENT = 10

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((310, 0))
l_paddle = Paddle((-320, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) #The screen sleep time is recorded in an attribute in Ball class
    screen.update()
    ball.move_ball()

    #Detect collision with up or down wall
    if ball.ycor() >= 260 or ball.ycor() <= -260:
        ball.bounce_y()

    #Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 280 or ball.distance(l_paddle) < 50 and ball.xcor() < -290:
        ball.bounce_x()



    #Detect paddle missing the ball
    if ball.xcor() > 305:
        ball.reset_position()
        scoreboard.update_lscore()


    if ball.xcor() < -325:
        ball.reset_position()
        scoreboard.update_rscore()










screen.exitonclick()

