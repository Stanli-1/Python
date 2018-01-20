import turtle
import sys
import random

#oldballcord = {0,0}

oldballX = 0
oldballY = 0

scrL = 850
scrH = 500
halfL = scrL/2
halfH = scrH/2
##scrsize = 550
##halfsize = scrsize/2
boardlength = 60
oldboardx = 0
preDir = 0

brickL = 100
brickH = 20
##colors = ["turquoise", "dark blue", "light blue", "blue", "turquoise", "dark blue", "light blue", "blue", "turquoise", "dark blue", "light blue", "blue", "turquoise", "dark blue", "light blue", "blue","turquoise", "dark blue", "light blue", "blue", "turquoise", "dark blue", "light blue", "blue"]

w, h = 10, 2;
bricks = []

scr = turtle.Screen()
scr.bgcolor("black")
scr.colormode(255)

def getNumber():
    return random.randint(100,255)

def drawBrick(posX, posY):
    brick = turtle.Pen()
    brick.speed(0)
    brick.color(getNumber(), getNumber(), getNumber())
    #brick.pencolor(0x92, 0x03, 0x10)
    brick.pensize(20)
    brick.penup()
    brick.setposition(posX + 10, posY + 10)
    brick.pendown()
    brick.fd(brickL - 40)
    brick.rt(90)
    brick.fd(brickH)
    brick.rt(90)
    brick.fd(brickL - 40)
    brick.rt(90)
    brick.fd(brickH)
    brick.rt(90)
    brick.hideturtle()
    bricks.append(brick)

def checkBrickHit(ball, brick):
    return touchBoard(ball, brick.xcor() + 30, brick.xcor() - 30, brick.ycor() + 5, brick.ycor() - 5)        

def checkBricksHit(ball):
    for i in bricks:
        if checkBrickHit(ball, i):
            bricks.remove(i)
            i.hideturtle()
            i.clear()
            #print("hit")

def drawBricks():
    x = -halfL
    y = halfH - 20
    for row in range(0,h):
        for num in range(0,w):
            drawBrick(x, y)
            x = x + brickL - 20
        y = y - brickH - 20
        x = -halfL + brickL/2
    

def touchBoard(turt, upperX, lowerX, upperY, lowerY):
    buffer = 17
    #print ("ballX = %d, ballY = %d, upperX = %d, lowerX = %d, upperY = %d, lowerY = %d" % (turt.xcor(), turt.ycor(), upperX, lowerX, upperY, lowerY))
    if turt.xcor() >= lowerX - buffer and turt.xcor() <= upperX + buffer and turt.ycor() >= lowerY - buffer and turt.ycor() <= upperY + buffer:
        #print("touch board!")
        return True
    else:
        #print ("upperX = %d, lowerX = %d" % (upperX, lowerX))
        #print ("xcor = %d, ycor = %d" % (turt.xcor(), turt.ycor()))
        #print ("upperY = %d, lowerY = %d" % (upperY, lowerY))
        #print("not touch board")
        return False

def  insideSquare(turt, upperX, lowerX, upperY, lowerY):
    if turt.xcor() <= upperX and turt.xcor() >= lowerX and \
        turt.ycor() <= upperY and turt.ycor() >= lowerY:
        #print ("ballX = %d, ballY = %d, upperX = %d, lowerX = %d, upperY = %d, lowerY = %d" % (turt.xcor(), turt.ycor(), upperX, lowerX, upperY, lowerY))
##        print ("xcor = %d, ycor = %d" % (turt.xcor(), turt.ycor()))
        #print("stan")
        return True
    else:
        print ("ballX = %d, ballY = %d, upperX = %d, lowerX = %d, upperY = %d, lowerY = %d" % (turt.xcor(), turt.ycor(), upperX, lowerX, upperY, lowerY))
        #print ("xcor = %d, ycor = %d" % (turt.xcor(), turt.ycor()))
        #print ("upperY = %d, lowerY = %d" % (upperY, lowerY))
        #print("Ying")
        return False
    


def drawBounds():
    bounds = turtle.Pen()
    bounds.speed(0)
    bounds.color(255,255,255)
    bounds.pensize(5)
    bounds.penup()
    bounds.setposition(-halfL, -halfH)
    bounds.pendown()
    bounds.fd(scrL)
    bounds.lt(90)
    bounds.fd(scrH)
    bounds.lt(90)
    bounds.fd(scrL)
    bounds.lt(90)
    bounds.fd(scrH)
    bounds.lt(90)
    bounds.hideturtle()
    
##for i in range(4):
##    bounds.fd(scrsize)
##    bounds.lt(90)

board = turtle.Pen()

def drawBoard():
    global board
    board = turtle.Pen()
    board.speed(0)
    board.penup()
    board.setposition(-30, -halfH + 20)
    board.color(255,255,255)
    board.pensize(10)
    board.hideturtle()
    board.pendown()
    board.showturtle()
    board.fd(60)
    board.hideturtle()
    board.speed(0)
    oldboardx = board.xcor()

ew = turtle.Pen()
ew.speed(0)
ew.penup()
ew.bk(200)
ew.rt(90)
ew.fd(30)
ew.lt(90)
ew.hideturtle()

spd = 5

def rightPressed():
    if board.xcor() > halfL - 20:
        return

    global preDir
    
    if preDir < 0:
        board.setposition(board.xcor() + 60, board.ycor())

    preDir = 1
    board.clear()
    board.showturtle()
    oldboardx = board.xcor()
    board.bk(30)
    board.pendown()
    board.fd(60)
    board.penup()
    board.hideturtle()

def leftPressed():
    
    if board.xcor() < -halfL + 30:
        return

    global preDir

    #If your stupid/retarded there is a equal sign here because the turtle
    #is on the right side at the beggining, future Stan
    if preDir >= 0:
        board.setposition(board.xcor() - 60, board.ycor())

    preDir = -1
    board.clear()
    board.showturtle()
    oldboardx = board.xcor()
    board.fd(30)
    board.pendown()
    board.bk(60)
    board.penup()
    board.hideturtle()
    
turtle.listen()
turtle.onkeypress(leftPressed, "a")
turtle.onkeypress(rightPressed, "d")

ball = turtle.Pen()
ball.rt(90)
ball.speed(10)
ball.shape("circle")
ball.color("green")
ball.penup()

def moveball(distance):
    oldballX = ball.xcor()
    oldballY = ball.ycor()
    ball.fd(distance)

health = 1
havelost = False

#DRAW THE GAME
drawBounds()
drawBoard()
drawBricks()

while not havelost:

    checkBricksHit(ball)
    if len(bricks) == 0:
        ew.fd(35)
        ew.color("green")
        ew.write("YOU WIN!", font=("Arial", 50, "bold"))
        sys.exit()
    
    if touchBoard(ball, board.xcor() + 30, board.xcor() - 30, \
                      board.ycor() + 5, board.ycor() - 5):
        if oldboardx < board.xcor():
            ball.rt(135)
            
        elif oldboardx > board.xcor():
            ball.lt(135)
        else:
            ball.lt(180)

        ball.fd(20)
    ball.fd(4)

#        moveball(20)
#    moveball(2)

    # x case
    if ball.xcor()>halfL or ball.xcor()<-halfL:
            ball.setheading(180-ball.heading())

    # y case
    if ball.ycor()>halfH or ball.ycor()<-halfH:
            ball.setheading(360-ball.heading())
            
##    if not insideSquare(ball, halfsize, -halfsize, halfsize, -halfsize):
##        ball.setheading(180 - ball.heading())

            #ball.lt(180)
        
    if ball.ycor() <= -halfH:
        health = health - 1

    if health == 0:
        ew.color("red")
        ew.write("GAME OVER", font=("Arial", 50, "bold"))
        havelost = True

    
