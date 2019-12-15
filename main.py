"""
import sys
import pygame
from gameManager import GameManager
pygame.init()

if FULLSCREEN == 1:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    window = pygame.display.set_mode((disp_w, disp_h))

character = Character(0, 0, pygame.Surface((50,50)), window)

clock = pygame.time.Clock()

running = True

while running:

    window.fill(bgColor)

    for event in pygame.event.get():

        if event.type == pygame.quit():

            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                forward = 1
            if event.key == pygame.K_s:
                forward = -1
            if event.key == pygame.K_a:
                side = -1
            if event.key == pygame.K_d:
                side = 1

    pygame.display.update()
    clock.tick(60)

"""
import pygame
from settings import *
import math
from Level import Level
from random import randint

#pygame tööle
pygame.init()

#font tööle
pygame.font.init()

#fondi väärtused
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#Aja muutujad
clock = pygame.time.Clock()
font = pygame.font.Font(None, 54)
font_color = pygame.Color('red')

passed_time = 0
timer_started = False


#kui settingutest on fullscreen 1 siis avab akna FULLSCREEN mode peal
if FULLSCREEN == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    disp_h = 1080
    disp_w = 1920
else:
    screen = pygame.display.set_mode((disp_w, disp_h))

#akna nimi
pygame.display.set_caption("MUTENESS")
#karakteri pilt
playerImage = pygame.image.load("ball.png")
#muudame karakteri suurust
playerImage = pygame.transform.scale(playerImage, (playerSize, playerSize))

#karakter startpositsioonis
screen.blit(playerImage, startPos)

#suunaväärtused
moveRight = 0
moveLeft = 0
moveUp = 0
moveDown = 0

PI = math.pi

#võtame mapi
level = Level("Level1.png")
pilt = level.open_pic() #default size (1440, 1080)

#leveli argumendid
mode = pilt.mode
size = pilt.size
data = pilt.tobytes()

#leveli koordinaadid
x = size[0] + BORDER
y = size[1]

#level image väärtusena, et blittida ekraanile
background = pygame.image.fromstring(data, size, mode)

#kiirendus
acceleration = 0.1

#kiirenduste suunad
acceleratingRight = 0
acceleratingLeft = 0
acceleratingDown = 0
acceleratingUp = 0

#maksimumkiirus
maxSpeed = 3

#põhitsükkel
running = True
while running:

    #taustavärv
    screen.fill(bgColor)

    #lisame leveli
    screen.blit(background, (int(BORDER / 2), 0))

    #event handler
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        #kui nupuvajutus siis vastav muutus
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                moveRight = 1
            if event.key == pygame.K_x:
                moveLeft = -1
            if event.key == pygame.K_c:
                moveDown = 1
            if event.key == pygame.K_v:
                moveUp = -1
            if event.key == pygame.K_ESCAPE:
                running = False
        #kui nupp lastakse lahti siis vastavad muutused
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                moveRight = 0
            if event.key == pygame.K_x:
                moveLeft = 0
            if event.key == pygame.K_c:
                moveDown = 0
            if event.key == pygame.K_v:
                moveUp = 0

    #kontrollib kas karakteri suund on diagonaal
    checkDiagonal = max(1, abs(moveRight + moveLeft) + abs(moveDown + moveUp))

    #kiirendushandler
    if moveRight == 1:
        acceleratingRight = min(maxSpeed, acceleratingRight + acceleration)
    else:
        acceleratingRight = max(0, acceleratingRight - acceleration)

    if moveLeft == -1:
        acceleratingLeft = max(-maxSpeed, acceleratingLeft - acceleration)
    else:
        acceleratingLeft = min(0, acceleratingLeft + acceleration)

    if moveDown == 1:
        acceleratingDown = min(maxSpeed, acceleratingDown + acceleration)
    else:
        acceleratingDown = max(0, acceleratingDown - acceleration)

    if moveUp == -1:
        acceleratingUp = max(-maxSpeed, acceleratingUp - acceleration)
    else:
        acceleratingUp = min(0, acceleratingUp + acceleration)

    #karakteri positsioon X ja Y, kiiruse jaoks
    positionX += (acceleratingRight + acceleratingLeft) / math.sqrt(checkDiagonal) * SPEED
    positionY += (acceleratingDown + acceleratingUp) / math.sqrt(checkDiagonal) * SPEED

    #näitame karaktrit aknas
    screen.blit(playerImage, ((int(positionX), int(positionY))))
    #näitame piksi värvi karakteri  asukohas, tema vasak ülemine nurk
    screen.blit(myfont.render(str(level.get_pixel_value(pilt, (positionX-BORDER/2, positionY))), False, (0, 0, 0)), (10, 10))


    #palli jaoks piiride loomine
    for i in range(1,playerSize+1):
        x = int(playerSize/2*math.sin(math.degrees(360/i))+positionX+playerSize/2)
        y = int(playerSize/2*math.cos(math.degrees(360/i))+positionY+playerSize/2)

        #kontrollimine, kas karkateri piir asub musta piksli peal
        if level.get_pixel_value(pilt, (x-BORDER/2,y)) == (0, 0, 0):
            if restart == True:
                positionX, positionY = int(BORDER / 2) + 10, 0 + 10
            else:
                running = False
        elif level.get_pixel_value(pilt, (x-BORDER/2,y)) == (0, 255, 0):
            timer_started = True
            if timer_started:
                start_time = pygame.time.get_ticks()

        elif level.get_pixel_value(pilt, (x - BORDER / 2, y)) == (255, 0, 0):
            timer_started = not timer_started

    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time


    #uuendame akent
    #Aja kuvamine
    text = font.render("Current time:", True, font_color)
    text_sec = font.render(str(passed_time / 1000), True, font_color)
    screen.blit(text, (size[0] + int(BORDER / 2), 0))
    screen.blit(text_sec, (size[0] + int(BORDER / 2) + 100, 50))

    pygame.display.update()
    clock.tick(60)
