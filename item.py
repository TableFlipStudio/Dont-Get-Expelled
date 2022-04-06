import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    """Klasa zarządzająca przedmiotami w grze"""

    def __init__(self, dogex, item_type):
        """Inicjalizacja przedmiotu"""
        super().__init__()
        self.screen = dogex.screen
        self.map = dogex.map

        #Rózne obrazy dla róznych egzemplarzy
        images = {
            'zubr': 'images/items/zubr.png',
            'trampki': 'images/items/trampki.png',
            'kartka': 'images/items/kartka.png',
            'energy_drink': 'images/items/energy-drink.png',
        }

        self.image = pygame.image.load(images[item_type])
        self.rect =  self.image.get_rect()

        self.obj = self.map._access_Object('items.'+item_type)

        #Położenie zależy od atrybutu xyPos (krotka)
        self.id = item_type

        self.shown = False

    def blit_item(self):
        """Wyświetlenie przedmiotu na ekranie"""
        self.screen.blit(self.image, self.rect)
