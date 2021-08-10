import turtle 
window = turtle.Screen()
window.title("Ping-Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
# acceleartes the drawings of complex graphics, 
# handy when we move the padles and ball
window.tracer(0)

# scores of the players
score_a = 0
score_b = 0

# initial speed of ball 
initial_speed = 0.10

# left paddle 
lpaddle = turtle.Turtle()
# sets the animation speed to maximum when given value 0
lpaddle.speed(0)
lpaddle.shape("square")
lpaddle.color("blue")
lpaddle.penup()
lpaddle.goto(-350,0)
lpaddle.shapesize(stretch_wid = 5,stretch_len = 1)


# right paddle 
rpaddle = turtle.Turtle()
# sets the animation speed to maximum when given value 0
rpaddle.speed(0)
rpaddle.shape("square")
rpaddle.color("green")
rpaddle.penup()
rpaddle.goto(350,0)
rpaddle.shapesize(stretch_wid = 5,stretch_len = 1)

# the ball
ball = turtle.Turtle()
# sets the animation speed to maximum when given value 0
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
# separating the ball's movement by 
# initializing and setting the change in x and y direction
ball.dx = initial_speed
ball.dy = initial_speed

# pen-score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0",align="center",font =("courier",20,"normal"))
# Moving lpaddle up
def lpaddle_up():
    y = lpaddle.ycor()
    y = y + 30
    lpaddle.sety(y)

# Moving lpaddle down
def lpaddle_down():
    y = lpaddle.ycor()
    y = y - 30
    lpaddle.sety(y)

# Moving rpaddle up
def rpaddle_up():
    y = rpaddle.ycor()
    y = y + 30
    rpaddle.sety(y)

# Moving rpaddle down
def rpaddle_down():
    y = rpaddle.ycor()
    y = y - 30
    rpaddle.sety(y)

# keyboard binding
window.listen()
window.onkeypress(lpaddle_up,"w")
window.onkeypress(lpaddle_down,"s")
window.onkeypress(rpaddle_up,"Up")
window.onkeypress(rpaddle_down,"Down")

while True:
    window.update()
    # the ball should move continuously without waiting for a trigger
    newx = ball.xcor() + ball.dx
    newy = ball.ycor() + ball.dy
    # changing the coordinates of th ball everytime the main game runs
    ball.setx(newx)
    ball.sety(newy)
    
    # border check- to avoid the ball go off the screen
    # checking for top border, total height is 600(300, -300) and ball is 20 pixels
    if ball.ycor() > 290: 
        ball.sety(290)
        # forces the ball to diagonally move downwards(-1) instead
        ball.dy = ball.dy * -1
    
    # border check for bottom border
    elif ball.ycor() < -290: 
        ball.sety(-290)
        # forces the ball to diagonally move downwards(-1) instead
        ball.dy = ball.dy * -1

    # border check for left border
    elif ball.xcor() > 390:
        ball.dx = initial_speed
        score_a += 1 
        pen.clear()  # to clear the existing data
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center",font =("courier",20,"normal"))
        #starts from centre again
        ball.goto(0,0)
        # forces the ball to diagonally move downwards(-1) instead
        ball.dx = ball.dx * -1
    
    # border check for right border
    elif ball.xcor() < -390: 
        ball.dx = initial_speed #resetting to initial speed
        score_b += 1 
        pen.clear()  
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center",font =("courier",20,"normal"))
        #starts from centre again
        ball.goto(0,0)
        # forces the ball to diagonally move downwards(-1) instead
        ball.dx = ball.dx * -1
    
    # ball needs to bounce off the lpaddle
    if (-350 < ball.xcor() < -340) and ball.ycor() < lpaddle.ycor() + 50 and ball.ycor() > lpaddle.ycor() - 50:
        ball.setx(-340)
        ball.dx = ball.dx * -1
        # increases the speed everytime ball hits paddle
        ball.dx += 0.10

    # ball needs to bounce off the rpaddle
    if (350 > ball.xcor() > 340) and ball.ycor() < rpaddle.ycor() + 50 and ball.ycor() > rpaddle.ycor() - 50:
        ball.setx(340)
        ball.dx = ball.dx * -1
        # increases the speed everytime ball hits paddle
        ball.dx -= 0.10
        

    
    
