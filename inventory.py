import pygame
from pygame.sprite import Sprite

class Inventory(Sprite):
    """Klasa zarządzająca ekwipunkiem"""

    def __init__(self, dogex):
        """Inicjalizacja ekwipunku"""
        super().__init__()
        self.screen = dogex.screen
        self.settings = dogex.settings
        self.image = pygame.image.load('images/inventory_tab.bmp')
        self.rect = self.image.get_rect()

        #Utworzenie slotu i umieszczenie go na ekwipunku
        self.slot_rect = pygame.Rect(0, 0, 80, 80)
        self.slot_color = (115, 115, 115)
        self.slot_rect.center = self.rect.center

        #Okno ekwipunku na początku jest zamknięte
        self.inventory_active = False

    def display_inventory(self):
        """Wyświetlenie ekwipunku na ekranie"""
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.slot_color, self.slot_rect)
