
import turtle

wn = turtle.Screen()
wn.title("Ping Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# wn.tracer(0) estää ruudun automaattisen päivittämisen
wn.tracer(0)

#pisteet
score_a = 0
score_b = 0

# Maila A
paddle_a = turtle.Turtle()
# animaation nopeus(0) eli nopein
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Maila B
paddle_b = turtle.Turtle()
# animaation nopeus(0) eli nopein
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Pallo
ball = turtle.Turtle()
# animaation nopeus(0) eli nopein
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
# pallon liikkumiseen käytettävät funktio dx(delta x) tässä säädetään pallon vauhtia
ball.dx = 0.03
ball.dy = 0.03

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# funktiot
def paddle_a_up():
    y = paddle_a.ycor()
    # tämä lisää 20 pikseliä y-koordinaattiin
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    # tämä lisää 20 pikseliä y-koordinaattiin
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    # tämä lisää 20 pikseliä y-koordinaattiin
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    # tämä lisää 20 pikseliä y-koordinaattiin
    y -= 20
    paddle_b.sety(y)


# window listen
# tällä kuunnellaan näppäimistön painalluksia
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# looppi peliä varten
while True:
    # joka kerta kun looppi alkaa alusta ikkuna päivitettään
    wn.update()

    # pallo liikkuu
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # rajojen asetukset
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # kun pallo osuu mailaan
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
