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
        self.active = False

        #Początkowo żaden przedmiot nie znajduje się przy kursorze
        self.grabbed_item = None

    def display_inventory(self):
        """Wyświetlenie ekwipunku na ekranie"""
        self.screen.blit(self.image, self.rect)

    def grab_item(self, dogex, mouse_pos):
        """Wyciągnięcie przedmiotu ze slotu w ekwipunku"""
        for slot in dogex.slots.sprites():
            if slot.rect.collidepoint(mouse_pos):
                self.grabbed_item = slot.content
                slot.content = None

    def display_grabbed_item(self):
        """Wyświetlenie przedmiotu podniesionego przy użyciu myszy"""
        if self.grabbed_item is not None:
            mouse_pos = pygame.mouse.get_pos()
            self.grabbed_item.rect.center = mouse_pos
            self.screen.blit(self.grabbed_item.image, self.grabbed_item.rect)




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
        self.rect.left = inventory.rect.centerx - 550
        self.rect.y = inventory.rect.centery - 200

        #Slot początowo jest pusty
        self.content = None

    def draw_slot(self):
        """Wyświetlenie slotów na ekwipunku"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def blit_content(self):
        """Wyświetlenie przedmiotów w slotach"""
        if self.content is not None:
            self.content.rect.center = self.rect.center
            self.screen.blit(self.content.image, self.content.rect)
