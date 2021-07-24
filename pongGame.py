import os
import turtle
import time

# window setup
wn = turtle.Screen()
wn.title("Pong by @Quint")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Middle Circle
circle = turtle.Turtle()
circle.speed(0)
circle.penup()
circle.color("white")
circle.shape("circle")
circle.shapesize(stretch_wid=2, stretch_len=2)

# Dotted Line
dottedLine = turtle.Turtle()
dottedLine.speed(0)
dottedLine.penup()
dottedLine.shapesize(stretch_wid=100, stretch_len=0.2)
dottedLine.color("white")

# paddleA
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.color("white")
paddleA.shape("square")
paddleA.penup()
paddleA.goto(-350, 0)
paddleA.shapesize(stretch_wid=5, stretch_len=0.5)

# paddleB
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.color("white")
paddleB.shape("square")
paddleB.penup()
paddleB.goto(350, 0)
paddleB.shapesize(stretch_wid=5, stretch_len=0.5)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()

ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0   Player B: 0", align="center", font=("Courier", 24, "normal"))

# Winner
winnerText = turtle.Turtle()
winnerText.color("white")
winnerText.penup()
winnerText.speed(0)
winnerText.goto(0, 130)
winnerText.hideturtle()

# Functions Paddle A
def paddleA_up():
    y = paddleA.ycor()
    if y < 250:
        y += 20
    paddleA.sety(y)
def paddleA_down():
    y = paddleA.ycor()
    if y > -240:
        y -= 20
    paddleA.sety(y)

# Functions Paddle B
def paddleB_up():
    y = paddleB.ycor()
    if y < 250:
        y += 20
    paddleB.sety(y)
def paddleB_down():
    y = paddleB.ycor()
    if y > -240:
        y -= 20
    paddleB.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")

wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety((ball.ycor() + ball.dy))

    # Border checker
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A:{}   Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/bounce.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A:{}   Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/bounce.wav&")

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.dx *= -1
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.dx *= -1
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/bounce.wav&")

    # Max Score
    if scoreA >= 5:
        pen.clear() #clears score board
        pen.write("Player A:0   Player B: 0", align="center", font=("Courier", 24, "normal")) #score board back to nil
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/celebration.wav&")
        winnerText.write("Player A wins!", align="center", font=("Courier", 30, "bold"))
        time.sleep(1.5)
        winnerText.clear() #clears winner text after 1,5 sec
        scoreA = 0 #resets score board
        scoreB = 0 #resets score board

    if scoreB >= 5:
        pen.clear() #clears score board
        pen.write("Player A:0   Player B: 0", align="center", font=("Courier", 24, "normal")) #score board back to nil
        winnerText.write("Player B wins!", align="center", font=("Courier", 30, "bold")) #winner text
        os.system("afplay /Users/quint/Desktop/PycharmProjects/pythonProject/PongGame/celebration.wav&")
        winnerText.write("Player B wins!", align="center", font=("Courier", 30, "bold"))
        time.sleep(1.5)
        winnerText.clear() #clears winner text after 1,5 sec
        scoreA = 0 #resets score board
        scoreB = 0 #resets score board



