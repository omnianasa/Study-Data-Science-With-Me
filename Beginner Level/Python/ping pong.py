#importing main libraries will be needed
import turtle

window = turtle.Screen() #build a window screen
window.title("Ping Pong") #set the title of the game
window.bgcolor("black") #determine the background color
window.setup(width=800, height=600) #set the width and height
window.tracer(0) #prevent the window of updating itself

#design the main characters of the game

# player1
c1 = turtle.Turtle() #make an object
c1.speed(0) #make it as fast as possible c1.shape("square") #it is a square shape
c1.shape("square")#it is a square shape
c1.color("blue") #make its color as blue
c1.penup() #no lines on the screen
c1.goto(-350, 0) #make the position of the player one
c1.shapesize(stretch_wid=5, stretch_len=1) #makeit 5*1 = 5 in area in the shape of a rectangular

# player2
c2 = turtle.Turtle() #make an object
c2.speed(0) #make it as fast as possible 
c2.shape("square") #it is a square shape
c2.color("red") #make its color as red
c2.penup()  #no lines on the screen
c2.goto(350, 0) #make the position of the player two
c2.shapesize(stretch_wid=5, stretch_len=1) #makeit 5*1 = 5 in area in the shape of a rectangular

#ball
ball = turtle.Turtle() #make an object
ball.speed(0)#make it as fast as possible 
ball.shape("circle")#it is a circle shape
ball.color("white")#make its color as white
ball.penup()#no lines on the screen
ball.goto(0, 0)#make the position of the ball
ball.dx = 0.3
ball.dy = 0.3

#score counting
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0 Player2: 0", align= "center", font=("Courier", 24, "normal"))

# Movement of the Blue player
# up 
def c1_up():
    y = c1.ycor() #having the y coordinates
    y = y + 20 #update the y coordinate
    c1.sety(y) #set the the new y
    if c1.ycor() > 250:
        c1.sety(250)

#keyboard bindings
window.listen()
window.onkeypress(c1_up, "w")

# down
def c1_down():
    y = c1.ycor() #having the y coordinates
    y = y - 20 #update the y coordinate
    c1.sety(y) #set the the new y
    if c1.ycor() < -250:
        c1.sety(-250)

#keyboard bindings
window.listen()
window.onkeypress(c1_down, "s")


#Movement of the Red Player
#up
def c2_up():
    y = c2.ycor() #having the y coordinates
    y = y + 20 #update the y coordinate
    c2.sety(y) #set the the new y
    if c2.ycor() > 250:
        c2.sety(250)

#keyboard bindings
window.listen()
window.onkeypress(c2_up, "Up")
#down
def c2_down():
    y = c2.ycor() #having the y coordinates
    y = y - 20 #update the y coordinate
    c2.sety(y) #set the the new y
    if c2.ycor() < -250:
        c2.sety(-250)

#keyboard bindings
window.listen()
window.onkeypress(c2_down, "Down")

# main Loop of the game
while True:
    window.update()  # update the screen every time it is running

    # movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border Check and scoring
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # if ball crosses the right edge (Player 2 missed)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # reverse ball's direction after scoring
        score1 += 1  # player 1 scores
        score.clear()
        score.write(f"Player1: {score1} Player2: {score2}", align="center", font=("Courier", 24, "normal"))

    # if ball crosses the left edge (Player 1 missed)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  # reverse ball's direction after scoring
        score2 += 1  # player 2 scores
        score.clear()
        score.write(f"Player1: {score1} Player2: {score2}", align="center", font=("Courier", 24, "normal"))

    # ball collision with Player 2 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < c2.ycor() + 50 and ball.ycor() > c2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # reverse ball direction

    # ball collision with Player 1 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < c1.ycor() + 50 and ball.ycor() > c1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # reverse ball direction
      
        

