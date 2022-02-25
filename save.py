import pygame

class Save():
    """Klasa przechowująca informacje o zapisie gry"""

    def __init__(self):
        self.character_pos = 0
        self.npc_pos = 0
        self.inventory_content = 0

class SaveMenu():
    """Menu zapisywanie i resetowania"""

    def __init__(self, dogex):
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dogex.settings

        self.rect = pygame.Rect(0, 0, self.screen_rect.width,
            self.screen_rect.height)
        self.color = pygame.Color(128, 141, 146, 50)

        self.savebutton_rect = pygame.Rect((0, 0), self.settings.button_size)
        self.savebutton_rect.center = self.screen_rect.center
        self.savebutton_rect.y -= self.settings.slot_height
        self.button_color =  self.settings.button_color

        self.active = False

    def blit_menu(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.button_color, self.savebutton_rect)
