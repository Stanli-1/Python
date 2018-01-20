#Import Librarys
import turtle
import random
import time
import winsound

def  insideSquare(turt, upperX, lowerX, upperY, lowerY):
    if turt.xcor() < upperX and turt.xcor() > lowerX and \
       turt.ycor() < upperY and turt.ycor() > lowerY:
        return True
    else:
        return False

def shoot():
    winsound.PlaySound('pulse-gun',
                       winsound.SND_FILENAME | winsound.SND_ASYNC)
def hit():
    winsound.PlaySound('expl',
                       winsound.SND_FILENAME | winsound.SND_ASYNC)

#Creates Game Variables
scrsize = 500
halfsize = scrsize/2

#Makes Screen and set BG
scr = turtle.Screen()
scr.bgcolor("black")
#scr.bgpic("tenor[9].gif")
#scr.register_shape("tenor[1].gif")

#Creates Boundarie Turtle
bounds = turtle.Pen()
bounds.speed(0)
bounds.color("yellow green")
bounds.pensize(5)
bounds.penup()
bounds.setposition(-halfsize, -halfsize)
bounds.pendown()
#Draws Boundaries using For Loop
for i in range(4):
    bounds.fd(scrsize)
    bounds.lt(90)
#Hides Turtle
bounds.hideturtle()
#Creates Turtle
player = turtle.Pen()
player.speed(0)
player.shape("turtle")
player.color("dark green")
player.penup()

#Creates Targets
target = turtle.Pen()
target.speed(0)
target.shape("circle")
target.color("grey")
target.penup()
target.setposition(random.randint(-halfsize, halfsize), \
                   random.randint(-halfsize, halfsize))

missile = turtle.Pen()
missile.speed(0)
missile.penup()
missile.color("white")
missile.hideturtle()

sw = turtle.Pen()
sw.speed(0)
sw.penup()
sw.hideturtle()
sw.setposition(-halfsize, halfsize + 10)
sw.color("yellow")

tw = turtle.Pen()
tw.speed(0)
tw.penup()
tw.hideturtle()
tw.setposition(-10, halfsize + 10)
tw.color("white")
tw.write(60)

ew = turtle.Pen()
ew.speed(0)
ew.penup()
ew.hideturtle()
ew.setposition(halfsize, halfsize + 10)
ew.color("red")

spd = 5

missiles = []

# When the left key is pressed
def leftPressed():
    player.lt(20)

# When the right key is pressed
def rightPressed():
    player.rt(20)

# When the up key is pressed
def upPressed():
    global spd
    spd = spd + 1

# When the down key is pressed
def downPressed():
    global spd
    spd = spd - 1

# Fires missile on space pressed
def spacePressed():
    missile = turtle.Pen()
    missile.speed(0)
    missile.penup()
    missile.color("white")
    missile.setposition(player.xcor(), player.ycor())
    facing = player.heading()
    missile.setheading(facing)
    missiles.append(missile)
    shoot()

# Clears Missiles
def cPressed():
    for i in missiles:
        missiles.remove(i)
        i.hideturtle()
    
turtle.listen()
turtle.onkeypress(leftPressed, "a")# or "Left"
turtle.onkeypress(rightPressed, "d")# or "Right"
turtle.onkeypress(upPressed, "w")# or "Up"
turtle.onkeypress(downPressed, "s")# or "Down"
turtle.onkey(spacePressed, "space")
turtle.onkeypress(cPressed, "c")
tSize = 1

score = 0
health = 1
havelost = False
sw.write("Score: " + str(score))
start = time.time()

#Game Loop
while not havelost:
    #Player Logic
        # Speed of your Player
    player.fd(spd)
        # Size of your Player
    player.shapesize(1.5)
    # player.lt(random.randint(-15,15))
        # Wall bouncing
    if not insideSquare(player, halfsize, -halfsize, halfsize, -halfsize):
        player.lt(180)
        
    if insideSquare(player, target.xcor() + tSize*15, target.xcor() - tSize*15, \
                    target.ycor() + tSize*15, target.ycor() - tSize*15):
        health = health - 1
        
    # Target Logic
        # Speed of your Target
    target.fd(3)
        # Random turning
    target.lt(random.randint(-15,15))
        # Wall bouncing
    if not insideSquare(target, halfsize, -halfsize, halfsize, -halfsize):
        target.lt(180)

        # Missile Bouncing
    for i in missiles:    
        if i.xcor()>halfsize or i.xcor()<-halfsize:
            i.setheading(180-i.heading())

        if i.ycor()>halfsize or i.ycor()<-halfsize:
            i.setheading(360-i.heading())

        if insideSquare(i, target.xcor() + tSize*15, target.xcor() - tSize*15, \
                        target.ycor() + tSize*15, target.ycor() - tSize*15):
            tSize = random.randint(1,3)
            target.shapesize(tSize)
            target.hideturtle() 
            target.setposition(random.randint(-halfsize, halfsize), \
                               random.randint(-halfsize, halfsize))
            score = score + 1
            #print(score)
            sw.clear()
            sw.write("Score: " + str(score))
            target.showturtle()
            hit()

        i.forward(spd + 10)
    if health == 0:
        ew.write("Game Over")
        havelost = True

    now = time.time() - start
    if now >= 60:
        havelost = True
        ew.write("Game Over")
    tw.undo()
    tw.write(round(60-now))





