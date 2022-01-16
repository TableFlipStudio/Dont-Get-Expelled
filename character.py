import pygame

class MainCharacter():
    """Klasa do zarządzania postacią główną"""

    def __init__(self, dogex):
        """Inicjalizacja postaci głównej i zasobów"""
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_height = self.screen_rect.height
        self.screen_width = self.screen_rect.width

        self.settings = dogex.settings

        #Wczytanie obrazu głównej postaci
        self.image = pygame.image.load('images/test_character.bmp')

        self.facing = "up"

        #Wczytanie prostokąta postaci i wycentrowanie go
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft

        #Położenie postaci przechowywane jest w zmienniej zmiennoprzecinkwej
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Opcje wskazujące na poruszanie się
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def can_move_right(self):
        output = (
            self.moving_right
            and
            self.rect.right < self.screen_width

        )
        return output

    def can_move_left(self):
        output = (
            self.moving_left
            and
            self.rect.left > 0
        )
        return output

    def can_move_up(self):
        output = (
            self.moving_up
            and
            self.rect.top > 0
        )
        return output

    def can_move_down(self):
        output = (
            self.moving_down
            and
            self.rect.bottom < self.screen_height
        )
        return output

    def update(self):
        """Aktualizacja położenia postaci"""

        #Aktualizacja wartości współrzędnych postaci a nie jej prostokąta
        if self.can_move_right():
            self.x += self.settings.character_speed
            self.facing = "right"

        if self.can_move_left():
            self.x -= self.settings.character_speed
            self.facing = "left"

        if self.can_move_up():
            self.y -= self.settings.character_speed
            self.facing = "up"

        if self.can_move_down():
            self.y += self.settings.character_speed
            self.facing = "down"



        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y

        print("x: ", self.rect.x, "\ny: ", self.rect.y)

    def blitme(self):
        """Wyświetlenie postaci głównej na ekranie"""
        self.screen.blit(self.image, self.rect)
