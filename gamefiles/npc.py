import pygame
from pygame.sprite import Sprite

class NPC(Sprite):
    """Klasa do zarządzania postaciami niekierowanymi przez gracza
    (Non-Person Character)"""

    def __init__(self, dogex, id, stage=0, shown=True):
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
        self.stage = stage

        # Obecność na mapie
        self.shown = shown

        image = {
            'kasia': 'images/npc/npc-nerd.png',
            'kuba': 'images/npc/npc-smoker1.png',
            'marek': 'images/npc/npc-smoker2.png',
            'cud': 'images/npc/lbos.png',
            'zyzio': 'images/npc/zyzio.png',
            'andrzej': 'images/npc/kolega.png',
            'deezlegz': 'images/npc/trampkowiara.png',
            'kanciapa': 'images/npc/kanciapa.png',
        }
        self.image = pygame.image.load(image[id])
        self.rect = self.image.get_rect()

        self.obj = self.map._access_Object('npc.'+id)

    def blit_npc(self):
        """Wyświetlene NPC na ekranie"""
        self.screen.blit(self.image, self.rect)
