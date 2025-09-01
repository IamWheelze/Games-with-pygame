import turtle

wn = turtle.screen()
wn.title('ping by joshua')
wn.bgcolor('black')
wn,setup(width=800, height=600)
wn.tracer(0)



racket_one = turtle.Turtle()
racket_one.speed(0)
racket_one.shape('circle')
racket_one.color('white')
racket_one.shapesize(stretch_wid=5, stretch_len=1)
racket_one.penup()
racket_one.goto(-350, 0)

racket_two = turtle.Turtle()
racket_two.speed(0)
racket_two.shape('circle')
racket_two.color('black')
racket_two.shapesize(stretch_wid=5, stretch_len=1)
racket_two.penup()
racket_two.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Function
def racket_one_up()
    y = racket_one.ycor()
    y += 20
    racket_one.sety(y)

def racket_one_down()
    y = racket_one.ycor()
    y -= 20
    racket_one.sety(y)

def racket_two_up()
    y = racket_two.ycor()
    y += 20
    racket_two.sety(y)

def racket_two_down()
    y = racket_.ycor()
    y -= 20
    racket_two.sety(y)


wn.listen()
wn.onkeypress(racket_one_up, 'w')
wn.onkeypress(racket_one_down, 's')
wn.onkeypress(racket_two_up, 'Up')
wn.onkeypress(racket_two_down, 'Down')

# Main game loop
while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor + ball.dx)
    ball.setx(ball.ycor + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() > -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > -390:
        ball.goto(0, 0)
        ball.dx *= -1

 
