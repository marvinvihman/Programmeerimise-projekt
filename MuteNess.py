#################################################
#program by Karl Martin Kadaja and Marvin Vihman#
#################################################
import ctypes
import pygame
from pygame.locals import *
import math

user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

WIDTH = int(width/2)
HEIGHT = int(height/2)

forward = 0
rotation = 0
a = 0
b = 0

RAW_MAP = """001111111111
101000000001
101011111101
100011111101
111111111101"""

rectangle = pygame.Surface([40,20])
rectangle.fill((255,255,0))


def draw_map(screen, raw_map):

    map = raw_map.split("\n")
    size = int((WIDTH-1) / len(map[0]))

    for i in range(len(map)):

        for j in range(len(map[i])):

            if map[i][j] == "0":
                color = (0, 0, 0)
            elif map[i][j] == "1":
                color = (0, 0, 255)

            pygame.draw.rect(screen, color,(j*size,i*size, size, size))

def square(screen, a, b, rectangle, forward, rotation):

    #global rectangle, a, b
    a = a + rotation #a and b testing variables
    b = b + forward
    rectangle = pygame.transform.rotate(rectangle, a)
    #pygame.draw.rect(rectangle, (255,255,0),(100,100,100,100))
    #rect = pygame.draw.rect(screen, (255,0,0),(forward, forward,10,10))
    #rotatedRect = pygame.transform.rotate(rect, rotation)
    screen.blit(rectangle, (int((b+20)*math.cos(math.radians(forward))), int((b+20)*math.cos(math.radians(90-forward)))))
    return a, b

def update(dt, forward, rotation):

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                forward = 1
            if event.key == pygame.K_s:
                forward = -1
            if event.key == pygame.K_a:
                rotation = -1
            if event.key == pygame.K_d:
                rotation = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                forward = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                rotation = 0
    return forward, rotation

def draw(screen, a, b, rectangle, forward, rotation):

    screen.fill((255, 0, 0))

    draw_map(screen, RAW_MAP)

    a, b = square(screen, a, b, rectangle, forward, rotation)

    pygame.display.flip()
    return a, b

def run(forward, rotation, a, b, rectangle):
    pygame.init()

    FPS = 60
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    dt = 1/FPS

    forward = 0
    rotation = 0

    while True:

        forward, rotation = update(dt, forward, rotation)
        a, b = draw(screen, a, b, rectangle, forward, rotation)

        dt = clock.tick(FPS)

run(forward, rotation, a, b, rectangle)