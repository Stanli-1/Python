import pygame
import random
from snakeClasses import snakeSegment

#constants
screenH = 750
screenL = 1000

livecherrycolor = (255,0,0)
deadcherrycolor = (0,0,0)

gridL = 50
halfGridL = 25

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

pygame.init()
screen = pygame.display.set_mode((screenL, screenH))
hasLost = False
is_green = True

snake = []
SnakeColor = (0,0,255)
oldSnakeHeadCor = [-10,-10]

step = 50

clock = pygame.time.Clock()

#center of circle
#print(cherryList[cherryIndex,0])
#print(cherryList[cherryIndex,1])

cherrycolor = livecherrycolor

cherryList = []
currentCherryIndex = 0

'''
case 1
       +-----+     +-----+
       |  a  |-> <-|  b  |   CXa <= CXb
       +-----+     +-----+
case 2
       +-----+     +-----+
       |  b  |-> <-|  a  |   CXa >= CXb
       +-----+     +-----+
'''
def Xoverlapping(CXa, CXb, aX1, aX2, bX1, bX2):
    #case 1
    if CXa <= CXb and aX2 >= bX1:
        return True

    #case 2
    if CXa >= CXb and aX1 <= bX2:
        return True

    return False

'''
       case 1      case 2
       +-----+     +-----+
       |  a  |     |  b  |   
       +-----+     +-----+
         ||           ||
         \/           \/
       +-----+     +-----+
       |  b  |     |  a  |   
       +-----+     +-----+
       CYa <= CYb  CYa >= CYb
'''
def Yoverlapping(CYa, CYb, aY1, aY2, bY1, bY2):
    if CYa <= CYb and aY2 >= bY1:
        return True

    if CYa >= CYb and aY1 <= bY2:
        return True

    return False


# check if two rectangles are touched
# rectA: topleft x, y, height, length
# rectB: topleft x, y, height, length
def checkHit(Xa, Ya, Ha, La, Xb, Yb, Hb, Lb):
    #translate into x/y min/max(1/2)
    Rax1 = Xa
    Rax2 = Xa + La
    Ray1 = Ya
    Ray2 = Ya + Ha
    Rbx1 = Xb
    Rbx2 = Xb + Lb
    Rby1 = Yb
    Rby2 = Yb + Hb

    if Xoverlapping(Rax1 + La/2, Rbx1 + Lb/2, Rax1,Rax2,Rbx1,Rbx2) \
       and Yoverlapping(Ray1 + Ha/2, Rby1 + Hb/2, Ray1,Ray2,Rby1,Rby2):
        return True
    
    return False

#make sure snake head can't go outside the bound
#move the head
#remember previous head location
def checkBounds(snakeHead,pressed):
    global screenH, screenL

    if pressed == pygame.K_UP:
        if snakeHead.Y() > 1:
            oldSnakeHeadCor[0] = snakeHead.X()
            oldSnakeHeadCor[1] = snakeHead.Y()
            snakeHead.SetY(snakeHead.Y() - step)
            moveSnakeBody(snake, UP)
            print("UP: old x/y:%d/%d, new x/y:%d/%d" % (oldSnakeHeadCor[0],oldSnakeHeadCor[1],snakeHead.X(),snakeHead.Y()))
    if pressed == pygame.K_DOWN:
        if snakeHead.Y() < screenH - gridL:
            oldSnakeHeadCor[0] = snakeHead.X()
            oldSnakeHeadCor[1] = snakeHead.Y()
            snakeHead.SetY(snakeHead.Y() + step)
            moveSnakeBody(snake, DOWN)
            print("Down: old x/y:%d/%d, new x/y:%d/%d" % (oldSnakeHeadCor[0],oldSnakeHeadCor[1],snakeHead.X(),snakeHead.Y()))
    if pressed == pygame.K_LEFT:
        if snakeHead.X() > 1:
            oldSnakeHeadCor[0] = snakeHead.X()
            oldSnakeHeadCor[1] = snakeHead.Y()
            snakeHead.SetX(snakeHead.X() - step)
            moveSnakeBody(snake, LEFT)
            print("Left: old x/y:%d/%d, new x/y:%d/%d" % (oldSnakeHeadCor[0],oldSnakeHeadCor[1],snakeHead.X(),snakeHead.Y()))
    if pressed == pygame.K_RIGHT:
        if snakeHead.X() < screenL - gridL:
            oldSnakeHeadCor[0] = snakeHead.X()
            oldSnakeHeadCor[1] = snakeHead.Y()
            snakeHead.SetX(snakeHead.X() + step)
            moveSnakeBody(snake, RIGHT)
            print("Right: old x/y:%d/%d, new x/y:%d/%d" % (oldSnakeHeadCor[0],oldSnakeHeadCor[1],snakeHead.X(),snakeHead.Y()))

def moveSnakeBody(snake, direction):
    for s in snake:
        if not s.isHead():
            if direction == UP:
                s.SetY(s.Y() - step)
            elif direction == DOWN:
                s.SetY(s.Y() + step)
            elif direction == LEFT:
                s.SetX(s.X() - step)
            elif direction == RIGHT:
                s.SetX(s.X() + step)

def drawSnake(screen, snake):
    for s in snake:
        if s.isHead():
            pygame.draw.rect(screen, (0,0,255), (s.X()-halfGridL,s.Y()-halfGridL, gridL,gridL))
        else:
            pygame.draw.circle(screen, (0,255,0), (s.X(),s.Y()), halfGridL)
#            print('not head')
            
def growSnake(snake, isHead, color):
    global oldSnakeHeadCor
    if isHead:
        x = halfGridL
        y = halfGridL
    else:
        #segment x and y
        snakeHead = snake[0]
        segLen = len(snake) - 1

        #head moves verticaly
        #down
        if snakeHead.Y() > oldSnakeHeadCor[1]:
            y = snakeHead.Y() - (gridL * segLen + gridL)
            x = snakeHead.X()
            moveSnake(snake,x,y, isHead, color)
            print("Head down")
            print('headx/y:%d/%d, new x/y: %d/%d, dY:%d' % (snakeHead.X(),snakeHead.Y(),x,y,abs(snakeHead.Y()-y)))
            return
        else: #up
            y = snakeHead.Y() + gridL * segLen + gridL
            x = snakeHead.X()
            moveSnake(snake,x,y, isHead, color)
            print("Head up")
            print('headx/y:%d/%d, new x/y: %d/%d, dY:%d' % (snakeHead.X(),snakeHead.Y(),x,y,abs(snakeHead.Y()-y)))
            return
        #head moves horizontaly
        #right
        if snakeHead.X() > oldSnakeHeadCor[0]:
            x = snakeHead.X() - (gridL * segLen + gridL)
            y = snakeHead.Y()
            moveSnake(snake,x,y, isHead, color)
            print("Head right")
            print('headx/y:%d/%d, new x/y: %d/%d, dX:%d' % (snakeHead.X(),snakeHead.Y(),x,y,abs(snakeHead.X()-x)))
            return
        else:#left
            x = snakeHead.X() + gridL * segLen + gridL
            y = snakeHead.Y()
            moveSnake(snake,x,y, isHead, color)
            print("Head left")
            print('headx/y:%d/%d, new x/y: %d/%d, dX:%d' % (snakeHead.X(),snakeHead.Y(),x,y,abs(snakeHead.X()-x)))
            return

def moveSnake(snake,x,y, isHead, color):
    s = snakeSegment(x,y)
    s.SetIsHead(isHead)
#    print('head? %d' % (isHead))
    s.SetColor(color)
    snake.append(s)


def cherryOrchard():
    for i in range(100):
        x = random.randint(0,19)*50 + 25
        y = random.randint(0,14)*50 + 25
        cherryList.append([x,y])

def getNextCherryIndex():
    return currentCherryIndex + 1

cherryOrchard()

#create snake head
moveSnake(snake,halfGridL,halfGridL, True, SnakeColor)

#def newCherry():
  #  pygame.draw.circle(screen, (255, 0, 0), (ncherryX, ncherryY), 25)


while not hasLost:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                hasLost = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN \
               or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #pressed = pygame.key.get_pressed()
            #checkHit1(pressed)
                #make sure snake head can't go outside the bound
                #move the head
                #remember previous head location
                checkBounds(snake[0],event.key)

                #check if snake eats the cherry
                if checkHit(cherryList[currentCherryIndex][0] - halfGridL, cherryList[currentCherryIndex][1] - halfGridL, 50, 50, \
                            snake[0].X(), snake[0].Y(), 50, 50):
                    currentCherryIndex = getNextCherryIndex()
                    #bad name, need to handle only direction of head a time
                    growSnake(snake,False,SnakeColor)

        #print('chery x,y = %d,%d' % (cherryList[currentCherryIndex][0],cherryList[currentCherryIndex][1]))
        #print(currentCherryIndex)
        #pygame.draw.circle(screen, (255,0,0), (ncherryX, ncherryY), 25)
        #newCherry()
        #pygame.draw.circle(screen, (0, 255, 0), (cherryX, cherryY),25)
        #pygame.draw.circle(screen, color, nake.X() - 25, snake.Y() - 25), 25)
    
    screen.fill((0, 0, 0))

    #draws snakes head
    drawSnake(screen,snake)
    #pygame.draw.rect(screen,(0,0,255), pygame.Rect(snake.X(), snake.Y(), gridL, gridL))
    
    #draws cherry
    pygame.draw.circle(screen, \
                       cherrycolor, \
                       (cherryList[currentCherryIndex][0], cherryList[currentCherryIndex][1]),
                       25)
    #pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
quit()
