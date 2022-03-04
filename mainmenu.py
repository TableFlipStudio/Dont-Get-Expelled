import pygame
import sys

from save import Button

class MainMenu():
    """Menu główne, wczytywane przed uruchomieniem run_game()"""

    def __init__(self, dogex):
        self.settings = dogex.settings
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect

        self.image = pygame.image.load("images/mainmenu.bmp")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)
