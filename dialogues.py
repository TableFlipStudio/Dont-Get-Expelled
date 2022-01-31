import pygame
import pygame.freetype

class DialogueWindow():
    """Klasa odpowiadająca za okno dialogowe"""
    def __init__(self, dogex):
        """Inicjalizacja okna dialogowego"""
        self.screen = dogex.screen
        self.settings  = dogex.settings

        self.rect = pygame.Rect(0, 0, self.settings.screen_width,
            self.settings.screen_height)
        self.color = self.settings.window_color

        #Na początku okno dialogowe jest zamknięte
        self.active = False

        #Pole tekstwowe - kwestie NPC
        self.tab_rect = pygame.Rect(self.settings.tab_Xpos,
            self.settings.tab_Ypos, self.settings.tab_width,
            self.settings.tab_height)
        self.tab_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.freetype.SysFont(None, 16)

        self._prep_msg('Some text')

    def _prep_msg(self, msg):
        """Utworzenie obrazu tekstu do wyświetlenia"""
        msg_pos = (self.tab_rect.x, self.tab_rect.y)
        self.msg_image, self.msg_rect = self.font.render(msg)
        self.msg_rect.x = self.tab_rect.x
        self.msg_rect.y = self.tab_rect.y

    def blit_window(self):
        """Wyświetlenie okna dialogowego, pola tekstowego
        i kwestii na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.tab_color, self.tab_rect)
        self.screen.blit(self.msg_image, self.msg_rect)

class DialogueLoader():
    """Klasa przechowująca pliki .txt z dialogami i zarządzająca nimi."""
    def __init__(self):
        """Inicjalizacja bazy danych"""
        self.dialogues = {
            'test_npc': 'Dialogues/test_dialogue1.txt'
        }
