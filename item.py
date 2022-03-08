import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    """Klasa zarządzająca przedmiotami w grze"""

    def __init__(self, dogex, item_type, pos):
        """Inicjalizacja przedmiotu"""
        super().__init__()
        self.screen = dogex.screen

        #Rózne obrazy dla róznych egzemplarzy
        images = {
            'green_ball': 'images/green_ball.bmp',
            'red_ball': 'images/red_ball.bmp',
            'blue_ball': 'images/blue_ball.bmp'
        }

        self.image = pygame.image.load(images[item_type])
        self.rect =  self.image.get_rect()

        #Położenie zależy od atrybutu xyPos (krotka)
        self.rect.x, self.rect.y = pos

        self.id = item_type

    def blit_item(self):
        """Wyświetlenie przedmiotu na ekranie"""
        self.screen.blit(self.image, self.rect)
