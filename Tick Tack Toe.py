import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

UserWin = False
UserLose = False
Tie = False

rectLength = 200
gap = 10
boardColor = (255, 255, 255)
yellow = (0,255,255)

#0 to 8
pieces = ['e','e','e','e','e','e','e','e','e']

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def message_display(text):
    if text != 'Tic Tac Toe':
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(190,100,630,115))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (500,150)
    screen.blit(TextSurf, TextRect)

def draw_Text(text,x,y):
    if text == 'e':
        return

    
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)
    
def drawBoard():
    x = 190
    y = 200
    for i in range(3):
        for n in range(3):
            pygame.draw.rect(screen, boardColor, pygame.Rect(x,y,rectLength,rectLength))
            x += rectLength + gap
        x = 190
        y += rectLength + gap

def drawPiece(r,c,p):
    if r == 1 and c == 1:
        draw_Text(p,290,300)
        
    if r == 1 and c == 2:
        draw_Text(p,500,300)
        
    if r == 1 and c == 3:
        draw_Text(p,710,300)
        
    if r == 2 and c == 1:
        draw_Text(p,290,510)
        
    if r == 2 and c == 2:
        draw_Text(p,500,510)
        
    if r == 2 and c == 3:
        draw_Text(p,710,510)
        
    if r == 3 and c == 1:
        draw_Text(p,290,720)

    if r == 3 and c == 2:
        draw_Text(p,500,720)
        
    if r == 3 and c == 3:
        draw_Text(p,710,720)

def drawPieces():
    i = 0
    for p in pieces:
        if i == 0:
            r = 1
            c = 1

        if i == 1:
            r = 1
            c = 2
            
        if i == 2:
            r = 1
            c = 3
            
        if i == 3:
            r = 2
            c = 1
            
        if i == 4:
            r = 2
            c = 2
            
        if i == 5:
            r = 2
            c = 3
            
        if i == 6:
            r = 3
            c = 1
            
        if i == 7:
            r = 3
            c = 2
            
        if i == 8:
            r = 3
            c = 3
        
        drawPiece(r,c,p)
        i += 1

#detects the user's input and draws piece
def userMove(eventKey):
    #print("patato")
    if eventKey == pygame.K_KP7:
        drawPiece(1,1,'O')
        pieces[0] = 'O'
    if eventKey == pygame.K_KP8:
        drawPiece(1,2,'O')
        pieces[1] = 'O'
    if eventKey == pygame.K_KP9:
        drawPiece(1,3,'O')
        pieces[2] = 'O'
    if eventKey == pygame.K_KP4:
        drawPiece(2,1,'O')
        pieces[3] = 'O'
    if eventKey == pygame.K_KP5:
        drawPiece(2,2,'O')
        pieces[4] = 'O'
    if eventKey == pygame.K_KP6:
        drawPiece(2,3,'O')
        pieces[5] = 'O'
    if eventKey == pygame.K_KP1:
        drawPiece(3,1,'O')
        pieces[6] = 'O'
    if eventKey == pygame.K_KP2:
        drawPiece(3,2,'O')
        pieces[7] = 'O'
    if eventKey == pygame.K_KP3:
        drawPiece(3,3,'O')
        pieces[8] = 'O'

#returns true if piece wins, otherwise it's false
#piece is either O or X
def checkWin(piece):
    #row 1
    if piece == pieces[0] and piece == pieces[1] and piece == pieces[2]:
        return True

    #row 2
    if piece == pieces[3] and piece == pieces[4] and piece == pieces[5]:
        return True

    #row 3
    if piece == pieces[6] and piece == pieces[7] and piece == pieces[8]:
        return True

    #col 1
    if piece == pieces[0] and piece == pieces[3] and piece == pieces[6]:
        return True

    #col 2
    if piece == pieces[1] and piece == pieces[4] and piece == pieces[7]:
        return True
    
    #col 3
    if piece == pieces[2] and piece == pieces[5] and piece == pieces[8]:
        return True

    #top left to bottem right
    if piece == pieces[0] and piece == pieces[4] and piece == pieces[8]:
        return True

    #top right tp bottem left
    if piece == pieces[2] and piece == pieces[4] and piece == pieces[6]:
        return True

    return False

#randomly picks a number between r1 and r2 inclusively exept e 
def randomMove(r1,r2,e):
    number = random.randint(r1,r2)
    while number == e:
        number = random.randint(r1,r2)
    return number

def numberToCoord(i):
    r,c = 0,0
    if i == 0:
        r = 1
        c = 1

    if i == 1:
        r = 1
        c = 2
        
    if i == 2:
        r = 1
        c = 3
        
    if i == 3:
        r = 2
        c = 1
        
    if i == 4:
        r = 2
        c = 2
        
    if i == 5:
        r = 2
        c = 3
        
    if i == 6:
        r = 3
        c = 1
        
    if i == 7:
        r = 3
        c = 2
        
    if i == 8:
        r = 3
        c = 3
        
    return r,c

def AIDefensive():
    if pieces[0] == 'O' and pieces[1] == 'O':
        pieces[2] = 'X'
        drawPiece(1,3,'X')
        return

    if pieces[1] == 'O' and pieces[2] == 'O':
        pieces[0] = 'X'
        drawPiece(1,1,'X')
        return

    if pieces[0] == 'O' and pieces[2] == 'O':
        pieces[1] = 'X'
        drawPiece(1,2,'X')
        return

    if pieces[3] == 'O' and pieces[4] == 'O':
        pieces[5] = 'X'
        drawPiece(2,3,'X')
        return

    if pieces[4] == 'O' and pieces[5] == 'O':
        pieces[3] = 'X'
        drawPiece(2,1,'X')
        return

    if pieces[3] == 'O' and pieces[5] == 'O':
        pieces[4] = 'X'
        drawPiece(2,2,'X')
        return

    if pieces[6] == 'O' and pieces[7] == 'O':
        pieces[8] = 'X'
        drawPiece(3,3,'X')
        return

    if pieces[7] == 'O' and pieces[8] == 'O':
        pieces[6] = 'X'
        drawPiece(3,1,'X')
        return

    if pieces[6] == 'O' and pieces[8] == 'O':
        pieces[7] = 'X'
        drawPiece(3,2,'X')
        return

    if pieces[0] == 'O' and pieces[3] == 'O':
        pieces[6] = 'X'
        drawPiece(3,1,'X')
        return

    if pieces[3] == 'O' and pieces[6] == 'O':
        pieces[0] = 'X'
        drawPiece(1,1,'X')
        return

    if pieces[0] == 'O' and pieces[6] == 'O':
        pieces[3] = 'X'
        drawPiece(2,1,'X')
        return

    if pieces[1] == 'O' and pieces[4] == 'O':
        pieces[7] = 'X'
        drawPiece(3,2,'X')
        return

    if pieces[4] == 'O' and pieces[7] == 'O':
        pieces[1] = 'X'
        drawPiece(1,2,'X')
        return

    if pieces[1] == 'O' and pieces[7] == 'O':
        pieces[4] = 'X'
        drawPiece(2,2,'X')
        return

    if pieces[2] == 'O' and pieces[5] == 'O':
        pieces[8] = 'X'
        drawPiece(3,3,'X')
        return

    if pieces[5] == 'O' and pieces[8] == 'O':
        pieces[2] = 'X'
        drawPiece(1,3,'X')
        return

    if pieces[2] == 'O' and pieces[8] == 'O':
        pieces[5] = 'X'
        drawPiece(2,3,'X')
        return

    if pieces[0] == 'O' and pieces[4] == 'O':
        pieces[8] = 'X'
        drawPiece(3,3,'X')
        return

    if pieces[4] == 'O' and pieces[8] == 'O':
        pieces[0] = 'X'
        drawPiece(1,1,'X')
        return

    if pieces[0] == 'O' and pieces[8] == 'O':
        pieces[4] = 'X'
        drawPiece(2,2,'X')
        return

    if pieces[2] == 'O' and pieces[4] == 'O':
        pieces[6] = 'X'
        drawPiece(3,1,'X')
        return

    if pieces[4] == 'O' and pieces[6] == 'O':
        pieces[2] = 'X'
        drawPiece(1,3,'X')
        return

    if pieces[2] == 'O' and pieces[6] == 'O':
        pieces[4] = 'X'
        drawPiece(2,2,'X')
        return

def AIOffensive():
    #puts X in the best position
    if pieces[4] == 'e':
        pieces[4] = 'X'
        drawPiece(2,2,'X')
        return True
    else:
        number = randomMove(0,8,4)
        print(number)
        pieces[number] = 'X'
        r,c = numberToCoord(number)
        drawPiece(r,c,'X')
        return True

    return False

def AImove():
    if not AIOffensive():
        AIDefensive()

def checkTie():
    for p in pieces:
        if p == 'e':
            return False
    return True

message_display('Tic Tac Toe')
#message_display('You Win!')
while not (UserWin or UserLose or Tie):
    drawBoard()
    drawPieces()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            userMove(event.key)
            UserWin = checkWin('O')
            UserLose = checkWin('X')
            Tie = checkTie()
            AImove()
            UserWin = checkWin('O')
            UserLose = checkWin('X')
            Tie = checkTie()
            #print("patato")
    
##    coord = input()
##    r,c = coord.split(',')
##    drawPiece(r,c)
            
    if UserWin == True:
        message_display('You Win!')
        print('UserWin %d' % (UserWin))
    elif UserLose == True:
        message_display('You Lost!')
        print('UserLose %d' % (UserLose))
    elif Tie == True:
        message_display('Tie!')
    
    pygame.display.flip()
    clock.tick(1)



if UserWin == True:
    message_display('You Win!')
    print('UserWin %d' % (UserWin))
elif UserLose == True:
    message_display('You Lost!')
    print('UserLose %d' % (UserLose))
else:
    message_display('Tie!')



##pygame.quit()
##quit()
