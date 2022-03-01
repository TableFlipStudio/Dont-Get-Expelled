import pygame
import pygame.font

class SaveMenu():
    """Menu zapisywania i resetowania"""

    def __init__(self, dogex):
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dogex.settings

        self.rect = pygame.Rect(0, 0, self.screen_rect.width,
            self.screen_rect.height)
        self.color = pygame.Color(128, 141, 146, 50)

        self.active = False

    def blit_menu(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Button():
    """Przyciski do interakcji z menu"""

    def __init__(self, save, centerpos, msg):
        self.screen = save.screen
        self.screen_rect = save.screen_rect
        self.settings = save.settings

        self.rect = pygame.Rect((0, 0), self.settings.button_size)
        self.rect.center = centerpos
        self.rect.y -= self.settings.slot_height
        self.color =  self.settings.button_color
        self.font = pygame.font.SysFont(None, 44)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Przygotowanie treści przycisku"""
        self.msg_image = self.font.render(msg, True, (255, 255, 255))
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def blit_button(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
