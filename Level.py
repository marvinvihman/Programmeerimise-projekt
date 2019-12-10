from PIL import Image
import pygame
from pygame.locals import *

class Level:
    "Leveli .png fail läheb muutujaks"
    def __init__(self, piltFail):
        self.piltFail = piltFail

    "PIL Image'iga avab pildi, et andmed saada kätte"
    def open_pic(self):
        return Image.open(self.piltFail, "r") #Originaal pilt

    "Pildi downscalimiseks" \
    "Avab leveli ning teeb etteantud suuruseks" \
    "tagastab uue leveli"
    def resize_level(self, new_size):
        self.new_size = new_size # Uus (width, height)
        piltFail = self.open_pic().copy() # Avab leveli, Image.open(level)
        level = piltFail.resize(new_size, Image.LANCZOS) # Tagastab uue leveli uute mõõtmetega
        return level

    "Funktsioon tagastab, mis ette antud positsioonil värvi data on"
    def get_pixel_value(self, level, pos):
        self.level = level # Image.open(level)
        self.pos = pos # (x, y) kujul positsioon, kust soovid data't saada
        pix_value = level.getpixel(pos) # Tagastab (r,g,b)
        return pix_value


""" ns proov
level = Level("Leveli näide.png")
current_pos = (25,25)
print(level.get_pixel_value(level.open_pic(), current_pos))
"""

"""
level = Level("Level1.png")
pilt = level.open_pic() #default size (1440, 1080)

mode = pilt.mode
size = pilt.size
data = pilt.tobytes()

lisa = 500
x = size[0] + lisa
y = size[1]

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((0,0), FULLSCREEN)
pygame.display.set_caption('Basic Pygame program')

# Background
this = pygame.image.fromstring(data, size, mode)
background = this

# Event loop
while 1:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    screen.blit(background, (int(lisa/2), 0))
    pygame.display.flip()

"""