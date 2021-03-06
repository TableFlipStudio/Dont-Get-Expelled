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
        self.map = dogex.map
        self.character = dogex.character

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

    def release_item(self, dogex, mouse_pos):
        """Upuszczenie przedmiotu z powrotem do slotu lub wyrzucenie
        z ekwipunku"""
        pygame.mixer.Sound('sounds/podnoszenie_przedmiotu.wav').play()

        # Te trzy funkcje się wzajemnie wykluczają, jednak jeśli którakolwiek z nich
        # wykona swoje zadanie, pozostałe będą operowały na wartościach None
        # więc de facto nic nie będą robiły
        self._lay_item(dogex, mouse_pos)
        self._put_item_in_slot(dogex, mouse_pos)
        self._put_item_back(dogex)

    def _lay_item(self, dogex, mouse_pos):
        """Umieszczenie na mapie przedmiotu, gdy został on umieszczony
        w slocie upuszczającym"""
        if dogex.drop_slot.rect.collidepoint(mouse_pos):
            pygame.mixer.Sound('sounds/podnoszenie_przedmiotu.wav').play()
            item = self.grabbed_item

            # Nie umieszczaj przedmiotu jeśli kolidowałby z przedmiotem już leżącym
            if self._check_item_collides(dogex, item):
                return
            if item: # Wykonaj tylko, jesli jest pochwyony jakiś przedmiot
                item.rect.midleft = dogex.character.rect.center
                ((item.obj.x), (item.obj.y)) = item.rect.center
                item.shown = True
                self.grabbed_item = None

    def _check_item_collides(self, dogex, item):
        """Sprawdzenie, czy przedmiot umieszczany na mapie koliduje z jakimś
        innym przedmiotem"""
        for map_item in dogex.items.sprites():
            if item: # Wykonaj tylko, jesli jest pochwyony jakiś przedmiot
                if item.rect.colliderect(map_item) and map_item.shown:
                    return True

    def _put_item_in_slot(self, dogex, mouse_pos):
        """Umieszczenie pochwyconego myszą przedmiotu w slocie,
        jeśli jest on pusty"""
        for slot in dogex.slots.sprites():
            if slot.rect.collidepoint(mouse_pos) and slot.content is None:
                slot.content = self.grabbed_item
                self.grabbed_item = None

    def _put_item_back(self, dogex):
        """Umieszczenie przedmiotu w pierwszym wolnym slocie,
        gdy nie upuszczono do żadnego slotu, lub slot, do którego go upuszczono
        był zajęty"""
        for slot in dogex.slots.sprites():
            if slot.content is None:
                slot.content = self.grabbed_item
                self.grabbed_item = None
                break # Umieść przedmiot tylko raz

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
        self.rect = pygame.Rect(0, 0, self.settings.slot_width,
            self.settings.slot_height)
        self.color = self.settings.slot_color
        self.rect.x = inventory.rect.centerx - 550
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
