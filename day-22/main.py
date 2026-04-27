from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.ball.distance(r_paddle.paddle) < 50 and ball.ball.xcor() > 320 or ball.ball.distance(
            l_paddle.paddle) < 50 and ball.ball.xcor() < -320:
        ball.bounce_x()

    # Detect out of bounds
    if ball.ball.xcor() > 380 or ball.ball.xcor() < -380:
        game_is_on = False

screen.exitonclick()
