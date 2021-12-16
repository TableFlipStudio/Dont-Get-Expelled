import sys
import pygame

from settings import Settings
from character import MainCharacter
from inventory import Inventory, Slot
from item import Item

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
        self.slots = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        #Utworzenie slotów
        self._create_slots()

        #Testowe rozmieszczenie przedmiotów
        self.items.add(Item(self, 'red_ball', 100, 100))
        self.items.add(Item(self, 'blue_ball', 1000, 400))
        self.items.add(Item(self, 'green_ball', 500, 650))

    def run_game(self):
        """Uruchomienie pętli głównej gry"""

        while True:
            self._check_events()

            if not self.inventory.active:
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
            self.inventory.active = not self.inventory.active

        if event.key == pygame.K_SPACE:
            self._pickup_item()

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

    def _create_slots(self):
        """Utworzenie wszystkich slotów ekwipunku"""

        for row_number in range(2): #Dwa rzędy slotów
            for slot_number in range(8): #Po 8 slotów każdy
                slot = Slot(self.inventory)
                slot_width  = slot.rect.width
                slot_height = slot.rect.height

                slot.x = (slot.rect.x + slot_width +
                    1.5 * slot_width * slot_number)
                slot.rect.x = slot.x
                slot.rect.y += slot_height + 2 * slot_height * row_number
                self.slots.add(slot)

    def _pickup_item(self):
        """Sprawdzenie, czy postać stoi koło przedmiotu
        i ewentualne podniesienie"""

        for item in self.items.copy():
            if pygame.Rect.colliderect(self.character.rect, item):
                self.items.remove(item)


    def _update_screen(self):
        """Aktualizacja zawartości ekranu"""

        self.screen.fill(self.settings.bg_color)
        self.character.blitme()

        #Wyświetlamy ekwipunek tylko, jeśli jest on aktywny (naciśnięto I)
        if self.inventory.active:
            self.inventory.display_inventory()
            for slot in self.slots.sprites():
                slot.draw_slot()

        #Wyświetlamy przedmioty tylko, gdy ekwipunek jest nieaktywny
        if not self.inventory.active:
            for item in self.items.sprites():
                item.blit_item()

        #Wyświetlenie zmodyfikowanego ekranu
        pygame.display.flip()


if __name__ == '__main__':
    dogex = DoGeX()
    dogex.run_game()
