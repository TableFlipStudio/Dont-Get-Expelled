#POSSIBLYTODO: Currently the way how msgs work is a parody of OOP (atributes etc.)
# We may want to actually make it OOP - make a Message() class, and so on.
# This would probably make things a lit simpler but
# currently I'm quite unmotivated to do it, so, Igor, tell me what do you think
# about it

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

        #Strzałka wzkazująca wybraną odpowiedź
        self.pointer_image = pygame.image.load('images/answer_pointer.bmp')
        self.pointer_rect = self.pointer_image.get_rect()
        self.selectedID = 0 # Decyduje, która odpowiedź ma być wskazana przez strzałkę

        #Słownik przechowujący wszystkie pliki z dialogami, przypisane do NPC
        self.dialogues = {
            'test_npc': self.build_dialogue_tree()
        }

        #Pusta lista do przechowywania wszystkich tekstów do wyświetlenia
        self.msgs = []

    def build_dialogue_tree(self):
        """Utworzenie drzewa dialogowego"""
        dp = "Dialogues/" # Directory Prefix
        root = DialogueTreeNode('root', dp+"test_dialogue1.txt")

        after0 = DialogueTreeNode('after0', dp+"test_dialogue2.txt")
        after1 = DialogueTreeNode('after1', "QUIT")

        root.add_child(after0, 0)
        root.add_child(after1, 1)

        return root

    def load_dialogue(self, id, inx = 0):
        """Wczytanie całego dialogu, razem z odpowiedziami i interfejsem"""
        self.msgs = [] # Wyczyszczenie ewentualnych poprzednich wiadomości
        self._load_msg_by_id(id, inx)
        self._load_answs_by_id(id, inx)
        self._update_pointer()

    def _load_msg_by_id(self, id, inx):
        """Wczytanie kwestii NPC z pliku po podaniu jego ID
        (zwykle jego nazwa)"""
        filename = self.dialogues[id].data
        with open(filename) as file:
            lines = file.readlines()

        yPos = self.tab_rect.y
        for line in lines:
            if line[0] == ">":
                return # Początek części z odpowiedziami, zatrzymaj wczytywanie kwestii
            self._prep_msg(line.strip(), yPos)
            yPos += self.font.get_sized_height()

    def _load_answs_by_id(self, id, inx):
        # WARNING: Function crashes on multi-line answers. To be fixed later
        """Wczytanie możliwych odpowiedzi gracza po ID NPC,
        z którym go prowadzi"""
        filename  = self.dialogues[id].data
        lines = self._prepare_anwsers(filename)

        enumerated_lines = list(enumerate(lines)) #Potrzebne jako ID do odnoszenia
        yPos = self.answ_tab_rect.y               #się do danej odpowiedzi
        for msgid, line in enumerated_lines:
            #Pusta linijka oddzielająca poszczególne odpowiedzi
            if line[0] == ">":
                yPos += self.font.get_sized_height()

            self._prep_msg(line.strip(), yPos, msgid)
            yPos += self.font.get_sized_height()

    def _prepare_anwsers(self, filename):
        """Wczytanie pliku dialogowego i usunięcie (lokalne) całej zawartości
        nie będącej listą odpowiedzi"""
        with open(filename) as file:
            lines = file.readlines()
            worklines = lines[:] # Kopia listy bo nie należy usuwać elementów
            # listy podczas iteracji przez nią.

            # Usuń wszystko co nie jest odpowiedzią
            for line in worklines:
                if line[0] != ">":
                    lines.remove(line)
        return lines

    def _update_pointer(self):
        """Umieszczenie strzałki wskazującej przy aktualnie wybranej
        odpowiedzi"""
        for msg in self.msgs:
            if msg['id'] == self.selectedID:
                self.pointer_rect.midright = msg['rect'].midleft

    def _prep_msg(self, msg, yPos, id=None):
        """Utworzenie obrazu tekstu do wyświetlenia"""
        image, rect = self.font.render(msg)
        rect.x = self.tab_rect.x
        rect.y = yPos
        self.msgs.append({'image': image, 'rect': rect, 'id': id})

    def blit_window(self):
        """Wyświetlenie okna dialogowego, pola tekstowego
        i kwestii na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.tab_color, self.tab_rect)
        pygame.draw.rect(self.screen, self.tab_color, self.answ_tab_rect)
        self.screen.blit(self.pointer_image, self.pointer_rect)
        for msg in self.msgs:
            self.screen.blit(msg['image'], msg['rect'])



# Based on https://www.youtube.com/watch?v=4r_XR9fUPhQ
class DialogueTreeNode():
    """Drzewo przechowujące pliki z dialogami wraz z informacją
    o kolejności, jaki dialog po jakiej odpowiedzi itd."""

    def __init__(self, name, data):
        """Inicjalizacja węzła"""
        self.name = name
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child, index: 0 - 3):
        """Dodanie potomka do drzewa. index to indeks odpowiedzi, po której
        powinien nastąpić ten dialog"""
        child.parent = self
        self.children.append((index, child))
