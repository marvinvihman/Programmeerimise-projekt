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

pygame.init()

if FULLSCREEN == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    disp_h = 1080
    disp_w = 1920
else:
    screen = pygame.display.set_mode((disp_w, disp_h))

pygame.display.set_caption("MUTENESS")

playerImage = pygame.image.load("ball.png")

def Player(pos):
    screen.blit(playerImage, pos)

Player(startPos)
moveRight = 0
moveLeft = 0
moveUp = 0
moveDown = 0

running = True
while running:
    screen.fill(bgColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moveRight = 1
            if event.key == pygame.K_a:
                moveLeft = -1
            if event.key == pygame.K_s:
                moveDown = 1
            if event.key == pygame.K_w:
                moveUp = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moveRight = 0
            if event.key == pygame.K_a:
                moveLeft = 0
            if event.key == pygame.K_s:
                moveDown = 0
            if event.key == pygame.K_w:
                moveUp = 0

    positionX += moveRight + moveLeft
    positionY += moveUp + moveDown




    if positionX <= 0:
        positionX = 0

    elif positionX >= disp_w - 128:
        positionX = disp_w - 128

    if positionY <= 0:
        positionY = 0
    elif positionY >= disp_h -128:
        positionY = disp_h - 128


    Player((positionX, positionY))



    pygame.display.update()



