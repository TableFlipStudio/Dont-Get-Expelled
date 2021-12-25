import pygame
from pygame.sprite import Sprite

class NPC(Sprite):
    """Klasa do zarządzania postaciami niekierowanymi przez gracza
    (Non-Person Character)"""

    def __init__(self, dogex):
        """Inicjalizacja NPC"""
        super().__init__()
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dogex.settings

        self.image = pygame.image.load('images/test_npc.bmp')
        self.rect = self.image.get_rect()

        #Postać testowa zaczyna po lewej stronie mapy
        self.rect.midleft = self.screen_rect.midleft
        self.rect.x += 50

        #Położenie NPc przechowywane jest w zmiennej zmiennoprzecinkwej
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Przesuwanie postaci dookoła mapy"""
        self.y += self.settings.npc_speed * self.settings.npc_yDirection

        self.rect.y = self.y

    def blit_npc(self):
        """Wyświetlene NPC na ekranie"""
        self.screen.blit(self.image, self.rect)
