import pygame
from pygame.sprite import Sprite

class NPC(Sprite):
    """Klasa do zarządzania postaciami niekierowanymi przez gracza
    (Non-Person Character)"""

    def __init__(self, dogex, id):
        """Inicjalizacja NPC"""
        super().__init__()
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dogex.settings
        self.character = dogex.character
        self.map = dogex.map

        # Identyfikator NPC - używany np. do wczytywania dialogów
        self.id = id

        # Etap 'relacji' z NPC - przed questem, w trakcie, po queście itd.
        self.stage = 0

        image = {
            'kasia': 'images/npc/npc-nerd.png',#'images/npc/kasia.bmp',
            'kuba': 'images/npc/npc-smoker1.png',#'images/npc/kuba.bmp',
            'marek': 'images/npc/npc-smoker2.png',
        }
        self.image = pygame.image.load(image[id])
        self.rect = self.image.get_rect()

    def blit_npc(self):
        """Wyświetlene NPC na ekranie"""
        self.screen.blit(self.image, self.rect)
