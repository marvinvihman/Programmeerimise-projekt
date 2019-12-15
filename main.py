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

pygame.init()

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#Aja muutujad
clock = pygame.time.Clock()
font = pygame.font.Font(None, 54)
font_color = pygame.Color('red')

passed_time = 0
timer_started = False



if FULLSCREEN == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    disp_h = 1080
    disp_w = 1920
else:
    screen = pygame.display.set_mode((disp_w, disp_h))

pygame.display.set_caption("MUTENESS")

playerImage = pygame.image.load("ball.png")

playerImage = pygame.transform.scale(playerImage, (playerSize, playerSize))

def Player(pos):
    screen.blit(playerImage, pos)

Player(startPos)
moveRight = 0
moveLeft = 0
moveUp = 0
moveDown = 0

PI = math.pi

level = Level("Level1.png")
pilt = level.open_pic() #default size (1440, 1080)

mode = pilt.mode
size = pilt.size
data = pilt.tobytes()

x = size[0] + BORDER
y = size[1]

background = pygame.image.fromstring(data, size, mode)

running = True
while running:
    screen.fill(bgColor)

    screen.blit(background, (int(BORDER / 2), 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                moveRight = 0
            if event.key == pygame.K_x:
                moveLeft = 0
            if event.key == pygame.K_c:
                moveDown = 0
            if event.key == pygame.K_v:
                moveUp = 0

    checkDiagonal = max(1, abs(moveRight + moveLeft) + abs(moveDown + moveUp))

    positionX += (moveRight + moveLeft) / math.sqrt(checkDiagonal) * SPEED
    positionY += (moveUp + moveDown) / math.sqrt(checkDiagonal) * SPEED


    if positionX <= 0:
        positionX = 0

    elif positionX >= disp_w - 128:
        positionX = disp_w - 128

    if positionY <= 0:
        positionY = 0
    elif positionY >= disp_h -128:
        positionY = disp_h - 128




    Player((int(positionX), int(positionY)))
    screen.blit(myfont.render(str(level.get_pixel_value(pilt, (positionX-BORDER/2, positionY))), False, (0, 0, 0)), (10, 10))

    for i in range(1,playerSize+1):
        x = int(playerSize/2*math.sin(math.degrees(360/i))+positionX+playerSize/2)
        y = int(playerSize/2*math.cos(math.degrees(360/i))+positionY+playerSize/2)
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

        pygame.draw.line(screen, (randint(0,255), randint(0,255), randint(0,255)), (x, y), (x, y), 10)

    #Aja kuvamine
    text = font.render("Current time:", True, font_color)
    text_sec = font.render(str(passed_time / 1000), True, font_color)
    screen.blit(text, (size[0] + int(BORDER / 2), 0))
    screen.blit(text_sec, (size[0] + int(BORDER / 2) + 100, 50))

    pygame.display.update()
    clock.tick(60)
