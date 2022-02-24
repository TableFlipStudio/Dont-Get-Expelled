import pygame, time

class MainCharacter():
    """Klasa do zarządzania postacią główną"""

    def __init__(self, dogex):
        """Inicjalizacja postaci głównej i zasobów"""
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_height = self.screen_rect.height
        self.screen_width = self.screen_rect.width

        self.settings = dogex.settings

        self.l = 0

        #Wczytanie obrazu głównej postaci
        self.image = pygame.image.load('images/test_character.bmp') 

        self.facing_h = "stationary"
        self.facing_v = "stationary"
        self.last_x = 0
        self.last_y = 0

        #Wczytanie prostokąta postaci i wycentrowanie go
        self.rect = self.image.get_rect()
        #self.rect.topleft = self.screen_rect.topleft
        #self.rect.center = (809, 715)

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

    def player_facing(self):

        if self.last_x > self.x:
            self.facing_h = "left"
        
        if self.last_x < self.x:
            self.facing_h = "right"
        
        if self.last_y > self.y:
            self.facing_v = "up"

        if self.last_y < self.y:
            self.facing_v = "down"
        
        if self.last_x == self.x and self.last_y == self.y:
            self.facing_v, self.facing_h = "stationary", "stationary"
        
    def animation_list(self):
        moving_list =  [
            pygame.image.load('images/blue_ball.bmp'),
            pygame.image.load('images/blue_ball.bmp'),
            pygame.image.load('images/blue_ball.bmp'),
            pygame.image.load('images/blue_ball.bmp'),
            pygame.image.load('images/blue_ball.bmp'),
            pygame.image.load('images/green_ball.bmp'),
            pygame.image.load('images/green_ball.bmp'),
            pygame.image.load('images/green_ball.bmp'),
            pygame.image.load('images/green_ball.bmp'),
            pygame.image.load('images/green_ball.bmp'),
            pygame.image.load('images/red_ball.bmp'),
            pygame.image.load('images/red_ball.bmp'),
            pygame.image.load('images/red_ball.bmp'),
            pygame.image.load('images/red_ball.bmp'),
            pygame.image.load('images/red_ball.bmp'),
            ]

        stationary_list = [
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character_blue.bmp'),
            pygame.image.load('images/test_character_blue.bmp'),
            pygame.image.load('images/test_character_blue.bmp'),
            pygame.image.load('images/test_character_blue.bmp'),
            pygame.image.load('images/test_character_blue.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            pygame.image.load('images/test_character.bmp'),
            ]
            
        if self.facing_h == "left" or self.facing_h == "right" or self.facing_v == "up" or self.facing_v == "down":
            return moving_list[self.animation_loop()]

        elif self.facing_h == "stationary" or self.facing_v == "stationary":
            return stationary_list[self.animation_loop()]
    
    
    def animation_loop(self):
        if self.l >= 14:
            self.l = 0

        #time.sleep(0.1)
        self.l += 1
        return self.l


    def update(self):
        """Aktualizacja położenia postaci i jej kierunku"""
        self.player_facing()

        self.image = self.animation_list()

        #zapis popszedniej wartości x and y
        self.last_x = self.x
        self.last_y = self.y

        #Aktualizacja wartości współrzędnych postaci a nie jej prostokąta
        if self.can_move_right():
            self.x += self.settings.character_speed

        if self.can_move_left():
            self.x -= self.settings.character_speed

        if self.can_move_up():
            self.y -= self.settings.character_speed

        if self.can_move_down():
            self.y += self.settings.character_speed

        #print(self.facing)

        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Wyświetlenie postaci głównej na ekranie"""
        self.screen.blit(self.image, self.rect)
