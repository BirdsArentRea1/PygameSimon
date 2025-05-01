import pygame
import random
import math
import winsound

pygame.init()
pygame.display.set_caption("!")
screen = pygame.display.set_mode((800,800))

def collision(xpos, ypos):
    if math.sqrt((xpos - 400)**2 + (ypos - 400)**2) > 200:
        #print("OUT")
        return -1
    elif xpos < 400 and ypos < 400:
        #print("GREEN")
        pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi / 2, pi, 100)
        pygame.display.flip()
        winsound.Beep(640, 500)
        return 0
    elif xpos < 400 and ypos > 400:
        #print("YELLOW")
        pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
        pygame.display.flip()
        winsound.Beep(240, 500)
        return 1
    elif xpos > 400 and ypos > 400:
        #print("RED")
        pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), 0, pi / 2, 100) 
        pygame.display.flip()
        winsound.Beep(440, 500)
        return 2
    elif xpos > 400 and ypos < 400:
        #print("BLUE")
        pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (3 * pi / 2), 2 * pi, 100) 
        pygame.display.flip()
        winsound.Beep(40, 500)
        return 3

# game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
hasClicked = False 
pattern = []
playerPattern = []
playerTurn = True
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196
4428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273
7245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094
3305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912
ded = False

# game loop ###############################################################################################
while True:
    event = pygame.event.wait()

    # input
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        hasClicked = True
        print("!")

    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

    collision(mousePos[0], mousePos[1])

    # update

    pattern.append(random.randrange(0, 4))

    for i in range(len(pattern)):

        if pattern[i] == 0: # GREEN
            pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi / 2, pi, 100)
            pygame.display.flip()
            winsound.Beep(640, 500)
        
        elif pattern[i] == 1: # RED
            pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), 0, pi / 2, 100) 
            pygame.display.flip()
            winsound.Beep(440, 500)

        elif pattern[i] == 2: # YELLOW
            pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
            pygame.display.flip()
            winsound.Beep(240, 500)

        elif pattern[i] == 3: # BLUE
            pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (3 * pi / 2), 2 * pi, 100) 
            pygame.display.flip()
            winsound.Beep(40, 500)

    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi / 2, pi, 100) 
    pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), 0, pi / 2, 100)
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3 * pi / 2), 2 * pi, 100)
    pygame.display.flip()
    #pygame.time.wait(800)

    # PLAYER TURN ========================================================================================
    print("starting player turn")
    if playerTurn == True:
        if len(playerPattern) < len(pattern):
            if hasClicked == True:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False

    else:
        playerTurn = False
        pygame.time.wait(800)

    # MACHINE TURN =======================================================================================

    # render
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi / 2, pi, 100) # GREEN
    pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), 0, pi / 2, 100) # RED
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100) # YELLOW
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3 * pi / 2), 2 * pi, 100) # BLUE

    pygame.display.flip()

# end game loop ########################################################################################### 
pygame.quit()
