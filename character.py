import pygame

class MainCharacter():
    """Klasa do zarządzania postacią główną"""

    def __init__(self, dogex):
        """Inicjalizacja postaci głównej i zasobów"""
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dogex.settings

        #Wczytanie obrazu głównej postaci
        self.image = pygame.image.load('images/test_character.bmp')

        #Wczytanie prostokąta postaci i wycentrowanie go
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        #Położenie postaci przechowywane jest w zmienniej zmiennoprzecinkwej
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Opcje wskazujące na poruszanie się
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Aktualizacja położenia postaci"""

        #Aktualizacja wartości współrzędnych postaci a nie jej prostokąta
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.x += self.settings.character_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.character_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.character_speed

        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.y += self.settings.character_speed

        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Wyświetlenie postaci głównej na ekranie"""
        self.screen.blit(self.image, self.rect)
