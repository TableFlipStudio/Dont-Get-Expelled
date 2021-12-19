import pygame as py
from settings import *


class Map():
    def __init__(self, dogex):

        self.settings = dogex.settings
        self.screen  = dogex.screen

        self.image = py.image.load('images/map.jpg')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height




    def blitMap(self):
        self.screen.blit(self.image, self.rect)



class Camera():
    def __init__(self):
        print()