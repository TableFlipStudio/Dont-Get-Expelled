import pygame
from pygame.sprite import Sprite

class Inventory():
    """Klasa zarządzająca ekwipunkiem"""

    def __init__(self, dogex):
        """Inicjalizacja ekwipunku"""
        self.screen = dogex.screen
        self.settings = dogex.settings
        self.image = pygame.image.load('images/inventory_tab.bmp')
        self.rect = self.image.get_rect()

        #Okno ekwipunku na początku jest zamknięte
        self.inventory_active = False

    def display_inventory(self):
        """Wyświetlenie ekwipunku na ekranie"""
        self.screen.blit(self.image, self.rect)

class Slot(Sprite):
    """Klasa zarządzająca slotami w ekwipunku"""

    def __init__(self, inventory):
        """Inicjalizacja slotów"""
        super().__init__()

        #Wczytanie zasobów
        self.screen = inventory.screen
        self.settings = inventory.settings

        #Utworzenie slotu i umieszczenie go na ekwipunku
        self.rect = pygame.Rect(0, 0, 80, 80)
        self.color = (115, 115, 115)
        self.rect.left = inventory.rect.centerx - 300
        self.rect.y = inventory.rect.centery - 100

    def draw_slot(self):
        """Wyświetlenie slotów na ekwipunku"""
        pygame.draw.rect(self.screen, self.color, self.rect)
