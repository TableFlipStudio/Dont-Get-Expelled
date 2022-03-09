import pygame
import pygame.font

class Expelling():
    """Klasa nadzoruje mechanikę wyrzucania ze szkoły"""

    def __init__(self, dogex):
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect
        self.settings = dogex.settings

        self.font = pygame.font.SysFont(None, 32)
        self.text_color = (255, 255, 255)

        self.fault_counter = self.settings.faults_to_be_expelled

        self.cntr_msg = f'Faults to be expelled: {self.fault_counter}'
        self.image = self.font.render(self.cntr_msg, True,
            self.text_color, None)
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen_rect.bottomright

    def blitmsg(self):
        self.screen.blit(self.image, self.rect)
