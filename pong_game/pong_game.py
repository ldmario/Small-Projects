import turtle
import os

score_a = 0
score_b = 0

windows = turtle.Screen()
windows.title("Pong Game")
windows.bgcolor("black")
windows.setup(width=800, height=600)
windows.tracer(0)

# Import Paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Import Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score. goto(0, 260)
score.write("Player A : 0   Player B : 0", False, align="center", font=("Arial", 25, "normal"))
score.hideturtle()

# Paddle movements


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
windows.listen()
windows.onkeypress(paddle_a_up, "w")
windows.onkeypress(paddle_a_down, "s")
windows.onkeypress(paddle_b_up, "Up")
windows.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    windows.update()

    # Winner
    if score_a > 9:
        pass
    elif score_b > 9:
        pass

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay border_sound.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay border_sound.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write(f"Player A : {score_a}   Player B : {score_b}", False, align="center", font=("Arial", 25, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write(f"Player A : {score_a}   Player B : {score_b}", False, align="center", font=("Arial", 25, "normal"))

    # Ball bouncing from paddle
    if 340 < ball.xcor() < 350 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        os.system("afplay paddle_sound.wav&")
        ball.setx(340)
        ball.dx *= -1
    if -350 < ball.xcor() < -340 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        os.system("afplay paddle_sound.wav&")
        ball.setx(-340)
        ball.dx *= -1
