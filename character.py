from pygame.locals import *
from gameSprite import GameSprite
import pygame


class Character(object):
    def __init__(self, scene):
        self.image = 'Asset/player.png'
        self.scene = scene
        self.width = 40
        self.height = 40
        self.direction_x = 0
        self.direction_y = 0
        self.rect = Rect(0, 0, self.width, self.height)
        self.sprite = GameSprite(self.image, self.rect)
        self.sprite_surface = self.sprite.getImage()  # get the player sprite surface
        self.bwidth, self.bheight = 660, 660
        self.pos = mt.Vector2(self.bwidth / 2, self.bheight / 2)  # initialize the position of the player sprite
        self.draw_pos = mt.Vector2(self.pos.x, self.pos.y)

        pygame.display.set_icon(
            self.sprite_surface)  # use the same player surface object as the icon for the game window

    def setX(self, _x):
        # set new x position and detect the boundary on the game scene
        self.direction_x = _x

    def setY(self, _y):
        # set new y position and detect the boundary on the game scene
        self.direction_y = _y

    def __init__(self, x, y, rect, window):
        self.x = x
        self.y = y
        self.rect = rect
        self.window = window


    def draw(self):
        self.window.blit(self.rect(self.x, self.y))

    def update(self):


    def move(self, speedx, speedy):
        self.x += speedx
        self.y += speedy