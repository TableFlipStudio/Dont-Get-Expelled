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

        #Pole tesktowe - odpowiedzi gracza
        self.answ_tab_rect = pygame.Rect(self.settings.answ_tab_Xpos,
            self.settings.answ_tab_Ypos, self.settings.tab_width,
            self.settings.tab_height)

        #Pole tekstowe - ogólne
        self.tab_color = self.settings.tab_color
        self.text_color = self.settings.text_color
        self.font = pygame.freetype.SysFont('monospace', 16)

        #Słownik przechowujący wszystkie pliki z dialogami, przypisane do NPC
        self.dialogues = {
            'lines': {
                'test_npc': ['Dialogues/test_dialogue1.txt']
            },
            'answers': {
                'test_npc': ['Dialogues/test_dialogue2.txt']
            }
        }

        #Pusta lista do przechowywania linijek składających się na kwestię
        self.messages = []

    def run_dialogue_sequence(self, id):
        """Uruchomienie serii dialogu NPC-gracz-NPC-gracz itd."""
        repeat = len(self.dialogues['lines'][id])

        for inx in range(repeat):
            self._load_msg_by_id(id, inx)
            self._load_answs_by_id(id, inx)


    def _load_msg_by_id(self, id, inx):
        """Wczytanie kwestii NPC z pliku po podaniu jego ID
        (zwykle jego nazwa)"""
        filename = self.dialogues['lines'][id][inx]
        with open(filename) as file:
            lines = file.readlines()
        yOffset = 0
        for line in lines:
            self._prep_msg(line.strip(), yOffset)
            yOffset += self.font.get_sized_height()

    def _load_answs_by_id(self, id, inx):
        """Wczytanie możliwych odpowiedzi gracza po ID NPC,
        z którym go prowadzi"""
        pass

    def _prep_msg(self, msg, yOffset):
        """Utworzenie obrazu tekstu do wyświetlenia"""
        msg_image, msg_rect = self.font.render(msg)
        msg_rect.x = self.tab_rect.x
        msg_rect.y = self.tab_rect.y + yOffset
        self.messages.append((msg_image, msg_rect))

    def blit_window(self):
        """Wyświetlenie okna dialogowego, pola tekstowego
        i kwestii na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.tab_color, self.tab_rect)
        pygame.draw.rect(self.screen, self.tab_color, self.answ_tab_rect)
        for msg in self.messages:
            self.screen.blit(msg[0], msg[1])
