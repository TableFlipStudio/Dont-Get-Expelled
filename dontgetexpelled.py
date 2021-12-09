import sys
import pygame

from settings import Settings
from character import MainCharacter
from inventory import Inventory

class DoGeX():
    """Ogólna klasa zarządzająca grą i jej zasobami"""

    def __init__(self):
        """Inicjalizacja gry i zasobów"""
        pygame.init()
        self.settings = Settings()

        #Wczytanie ekranu i nadanie tytułu
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("Don't Get Expelled! The Batory Game")

        #Wczytanie zasobów z pliku
        self.character = MainCharacter(self)
        self.inventory = Inventory(self)

    def run_game(self):
        """Uruchomienie pętli głównej gry"""

        while True:
            self._check_events()

            if not self.inventory.inventory_active:
                self.character.update()

            self._update_screen()

    def _check_events(self):
        """Reakcja na zdarzenia wywołane przez klawiaturę i mysz"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza"""

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.character.moving_right = True

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.character.moving_left = True

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.character.moving_up = True

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.character.moving_down = True

        if event.key == pygame.K_i:
            self.inventory.inventory_active = not self.inventory.inventory_active

        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reakcja na puszczenie klawisza"""

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.character.moving_right = False

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.character.moving_left = False

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.character.moving_up = False

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.character.moving_down = False

    def _update_screen(self):
        """Aktualizacja zawartości ekranu"""

        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        if self.inventory.inventory_active:
            self.inventory.display_inventory()

        #Wyświetlenie zmodyfikowanego ekranu
        pygame.display.flip()


if __name__ == '__main__':
    dogex = DoGeX()
    dogex.run_game()
