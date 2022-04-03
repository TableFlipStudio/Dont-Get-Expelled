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

        #var for animation loop
        self.l = 0

        #Wczytanie obrazu głównej postaci
        self.image = pygame.image.load('animation/down/fwrd0.png')
        self.down_list =  [
            pygame.image.load('animation/down/fwrd0.png'),
            pygame.image.load('animation/down/fwrd1.png'),
            pygame.image.load('animation/down/fwrd2.png'),
            pygame.image.load('animation/down/fwrd3.png'),
            pygame.image.load('animation/down/fwrd4.png'),
            pygame.image.load('animation/down/fwrd5.png'),
            pygame.image.load('animation/down/fwrd6.png'),
            pygame.image.load('animation/down/fwrd7.png'),
            pygame.image.load('animation/down/fwrd8.png'),
            pygame.image.load('animation/down/fwrd9.png'),
            pygame.image.load('animation/down/fwrd10.png'),
            pygame.image.load('animation/down/fwrd0.png'),
            pygame.image.load('animation/down/fwrd1.png'),
            pygame.image.load('animation/down/fwrd2.png'),
            pygame.image.load('animation/down/fwrd3.png'),
            pygame.image.load('animation/down/fwrd4.png'),
            pygame.image.load('animation/down/fwrd5.png'),
            pygame.image.load('animation/down/fwrd6.png'),
            pygame.image.load('animation/down/fwrd7.png'),
            pygame.image.load('animation/down/fwrd8.png'),
            pygame.image.load('animation/down/fwrd9.png'),
            pygame.image.load('animation/down/fwrd10.png'),
            pygame.image.load('animation/down/fwrd0.png'),
            pygame.image.load('animation/down/fwrd1.png'),
            pygame.image.load('animation/down/fwrd2.png'),
            pygame.image.load('animation/down/fwrd3.png'),
            pygame.image.load('animation/down/fwrd4.png'),
            pygame.image.load('animation/down/fwrd5.png'),
            pygame.image.load('animation/down/fwrd6.png'),
            pygame.image.load('animation/down/fwrd7.png'),
            pygame.image.load('animation/down/fwrd8.png'),
            pygame.image.load('animation/down/fwrd9.png'),
            pygame.image.load('animation/down/fwrd10.png'),
            ]

        self.left_list = [
            pygame.image.load('animation/left/East0.png'),
            pygame.image.load('animation/left/East1.png'),
            pygame.image.load('animation/left/East2.png'),
            pygame.image.load('animation/left/East3.png'),
            pygame.image.load('animation/left/East4.png'),
            pygame.image.load('animation/left/East5.png'),
            pygame.image.load('animation/left/East6.png'),
            pygame.image.load('animation/left/East7.png'),
            pygame.image.load('animation/left/East8.png'),
            pygame.image.load('animation/left/East9.png'),
            pygame.image.load('animation/left/East10.png'),
            pygame.image.load('animation/left/East0.png'),
            pygame.image.load('animation/left/East1.png'),
            pygame.image.load('animation/left/East2.png'),
            pygame.image.load('animation/left/East3.png'),
            pygame.image.load('animation/left/East4.png'),
            pygame.image.load('animation/left/East5.png'),
            pygame.image.load('animation/left/East6.png'),
            pygame.image.load('animation/left/East7.png'),
            pygame.image.load('animation/left/East8.png'),
            pygame.image.load('animation/left/East9.png'),
            pygame.image.load('animation/left/East10.png'),
            pygame.image.load('animation/left/East0.png'),
            pygame.image.load('animation/left/East1.png'),
            pygame.image.load('animation/left/East2.png'),
            pygame.image.load('animation/left/East3.png'),
            pygame.image.load('animation/left/East4.png'),
            pygame.image.load('animation/left/East5.png'),
            pygame.image.load('animation/left/East6.png'),
            pygame.image.load('animation/left/East7.png'),
            pygame.image.load('animation/left/East8.png'),
            pygame.image.load('animation/left/East9.png'),
            pygame.image.load('animation/left/East10.png'),
            ]

        self.right_list = [

            pygame.image.load('animation/right/West0.png'),
            pygame.image.load('animation/right/West1.png'),
            pygame.image.load('animation/right/West2.png'),
            pygame.image.load('animation/right/West3.png'),
            pygame.image.load('animation/right/West4.png'),
            pygame.image.load('animation/right/West5.png'),
            pygame.image.load('animation/right/West6.png'),
            pygame.image.load('animation/right/West7.png'),
            pygame.image.load('animation/right/West8.png'),
            pygame.image.load('animation/right/West9.png'),
            pygame.image.load('animation/right/West10.png'),
            pygame.image.load('animation/right/West0.png'),
            pygame.image.load('animation/right/West1.png'),
            pygame.image.load('animation/right/West2.png'),
            pygame.image.load('animation/right/West3.png'),
            pygame.image.load('animation/right/West4.png'),
            pygame.image.load('animation/right/West5.png'),
            pygame.image.load('animation/right/West6.png'),
            pygame.image.load('animation/right/West7.png'),
            pygame.image.load('animation/right/West8.png'),
            pygame.image.load('animation/right/West9.png'),
            pygame.image.load('animation/right/West10.png'),
            pygame.image.load('animation/right/West0.png'),
            pygame.image.load('animation/right/West1.png'),
            pygame.image.load('animation/right/West2.png'),
            pygame.image.load('animation/right/West3.png'),
            pygame.image.load('animation/right/West4.png'),
            pygame.image.load('animation/right/West5.png'),
            pygame.image.load('animation/right/West6.png'),
            pygame.image.load('animation/right/West7.png'),
            pygame.image.load('animation/right/West8.png'),
            pygame.image.load('animation/right/West9.png'),
            pygame.image.load('animation/right/West10.png'),
            ]

        self.up_list = [
            pygame.image.load('animation/up/BCWRD0.png'),
            pygame.image.load('animation/up/BCWRD1.png'),
            pygame.image.load('animation/up/BCWRD2.png'),
            pygame.image.load('animation/up/BCWRD3.png'),
            pygame.image.load('animation/up/BCWRD4.png'),
            pygame.image.load('animation/up/BCWRD5.png'),
            pygame.image.load('animation/up/BCWRD6.png'),
            pygame.image.load('animation/up/BCWRD7.png'),
            pygame.image.load('animation/up/BCWRD8.png'),
            pygame.image.load('animation/up/BCWRD9.png'),
            pygame.image.load('animation/up/BCWRD10.png'),
            pygame.image.load('animation/up/BCWRD0.png'),
            pygame.image.load('animation/up/BCWRD1.png'),
            pygame.image.load('animation/up/BCWRD2.png'),
            pygame.image.load('animation/up/BCWRD3.png'),
            pygame.image.load('animation/up/BCWRD4.png'),
            pygame.image.load('animation/up/BCWRD5.png'),
            pygame.image.load('animation/up/BCWRD6.png'),
            pygame.image.load('animation/up/BCWRD7.png'),
            pygame.image.load('animation/up/BCWRD8.png'),
            pygame.image.load('animation/up/BCWRD9.png'),
            pygame.image.load('animation/up/BCWRD10.png'),
            pygame.image.load('animation/up/BCWRD0.png'),
            pygame.image.load('animation/up/BCWRD1.png'),
            pygame.image.load('animation/up/BCWRD2.png'),
            pygame.image.load('animation/up/BCWRD3.png'),
            pygame.image.load('animation/up/BCWRD4.png'),
            pygame.image.load('animation/up/BCWRD5.png'),
            pygame.image.load('animation/up/BCWRD6.png'),
            pygame.image.load('animation/up/BCWRD7.png'),
            pygame.image.load('animation/up/BCWRD8.png'),
            pygame.image.load('animation/up/BCWRD9.png'),
            pygame.image.load('animation/up/BCWRD10.png'),
            ]

        self.stationary_image = pygame.image.load('animation/down/fwrd0.png')

        #Wczytanie prostokąta postaci i wycentrowanie go
        self.rect = self.image.get_rect()
        #self.rect.center = self.screen_rect.center

        #Położenie postaci przechowywane jest w zmienniej zmiennoprzecinkwej
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Opcje wskazujące na poruszanie się
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.moving = False


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

    def animation_list(self):
    
        if self.moving_up and self.moving_down:
            return self.stationary_image

        if self.moving_right and self.moving_left:
            return self.stationary_image

        if self.moving_down:
            return self.down_list[self.animation_loop(9)]

        elif self.moving_up:
            return self.up_list[self.animation_loop(9)]

        elif self.moving_right:
            return self.right_list[self.animation_loop(9)]

        elif self.moving_left:
            return self.left_list[self.animation_loop(9)]

        
        else:
            return self.stationary_image

    def animation_loop(self, len):

        if self.l >= len:
            self.l = 0

        self.l += 1
        return self.l

    def update(self):
        """Aktualizacja położenia postaci i jej kierunku"""

        self.image = self.animation_list()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Aktualizacja wartości współrzędnych postaci a nie jej prostokąta
        if self.can_move_right():
            self.x += self.settings.character_speed

        if self.can_move_left():
            self.x -= self.settings.character_speed

        if self.can_move_up():
            self.y -= self.settings.character_speed

        if self.can_move_down():
            self.y += self.settings.character_speed

        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y

        
            

    def blitme(self):
        """Wyświetlenie postaci głównej na ekranie"""
        self.screen.blit(self.image, self.rect)
