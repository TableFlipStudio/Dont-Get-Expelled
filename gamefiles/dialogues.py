# POSSIBLY TODO: Currently the way how msgs work is a parody of OOP (atributes etc.)
# We may want to actually make it OOP - make a Message() class, and so on.
# This would probably make things a lit simpler but
# currently I'm quite unmotivated to do it, so, Igor, tell me what do you think
# about it


import pygame
import pygame.freetype

from item import Item

class DialogueWindow():
    """Klasa odpowiadająca za okno dialogowe"""
    def __init__(self, dogex):
        """Inicjalizacja okna dialogowego"""
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings  = dogex.settings
        self.expelling = dogex.expelling
        self.dogex = dogex # Egzemplarz klasy głównej do odnoszenia się do mniej standardowych atrybutów
        self.sounds = dogex.sounds

        self.rect = pygame.Rect(0, 0, self.settings.screen_width,
            self.settings.screen_height)
        self.color = self.settings.window_color

        #Na początku okno dialogowe jest zamknięte
        self.active = False

        #Pole tekstwowe - kwestie NPC
        self.tab_rect = pygame.Rect(0, self.settings.tab_Ypos,
            self.settings.tab_width, self.settings.tab_height)
        self.tab_rect.centerx = self.screen_rect.centerx

        #Pole tesktowe - odpowiedzi gracza
        self.answ_tab_rect = pygame.Rect(0, self.settings.answ_tab_Ypos,
            self.settings.tab_width, self.settings.tab_height)
        self.answ_tab_rect.centerx = self.screen_rect.centerx

        #Pole tekstowe - ogólne
        self.tab_color = self.settings.tab_color
        self.text_color = self.settings.text_color
        self.font = pygame.freetype.SysFont('monospace', 15)

        #Strzałka wzkazująca wybraną odpowiedź
        self.pointer_image = pygame.image.load('images/answer_pointer.bmp')
        self.pointer_rect = self.pointer_image.get_rect()
        self.selectedID = 0 # Decyduje, która odpowiedź ma być wskazana przez strzałkę

        #Słownik przechowujący wszystkie pliki z dialogami, przypisane do NPC
        self.dialogues = {
            'cud': [
                self.build_dialogue_tree("cudstage0"),
                self.build_dialogue_tree("cudstage1")
            ],
            'zyzio': [
                self.build_dialogue_tree("zyziostage0")
            ],
            'andrzej': [
                self.build_dialogue_tree('andrzejstage0')
            ],
            'deezlegz': [
                self.build_dialogue_tree('deezlegzstage0'),
                self.build_dialogue_tree('deezlegzstage1')
            ],
            'matma': self.build_maths_tree(),
            'concierge': self.build_concierge_tree(),
            'office': self.build_office_tree()

        }

        #Pusta lista do przechowywania wszystkich tekstów do wyświetlenia
        self.msgs = []

        # Węzeł drzewa dialogowego, na którym aktualnie się znajdujemy i operujemy,
        # czyli po prostu aktualnie wyświetlany dialog
        # Deklaracja atrybutu jest absulutnie zbędna i jest tu tylko dla
        # przejrzystości kodu
        self.node = None

    def build_dialogue_tree(self, mode):
        """Utworzenie drzewa dialogowego. Wartość QUIT przypisawana jest
        węzłowi następującemu po odpowiedzi, która kończy dialog"""
        if mode == "cudstage0":
            dp = "Dialogues/cud/stage0/" # Directory Prefix
            root = DialogueTreeNode(dp+"root.txt")

            i_need_library = DialogueTreeNode(dp+'i_need_library.txt')
            beated_up = DialogueTreeNode(dp+'beated_up.txt')

            after_beated_up = DialogueTreeNode("QUIT", faultValue=2137)
            favour = DialogueTreeNode(dp+'favour.txt')

            accepted = DialogueTreeNode(dp+"accepted.txt")
            threatened = DialogueTreeNode(dp+"threatened.txt")
            after_threatened = DialogueTreeNode("QUIT", faultValue=3, stageUp=2, changeQuest=('both', ('concierge', 'cud')))

            after_accepted = DialogueTreeNode("QUIT", stageUp=1, changeQuest=('add', 'andrzej'))

            accepted.add_child(after_accepted, '0')
            threatened.add_child(after_threatened, '0')

            favour.add_child(accepted, '0')
            favour.add_child(threatened, '1')

            i_need_library.add_child(favour, '0')
            beated_up.add_child(after_beated_up, '0')

            root.add_child(i_need_library, "0")
            root.add_child(beated_up, "1")

        elif mode == "cudstage1":
            dp = "Dialogues/cud/stage1/"
            root = DialogueTreeNode(dp+"root.txt")

            energy_not_found = DialogueTreeNode("QUIT")
            energy_found = DialogueTreeNode(dp+'got_nrg_drink.txt', targetItem='energy_drink')
            liar = DialogueTreeNode(dp+'dont_lie.txt', faultValue=1)

            after_liar = DialogueTreeNode("QUIT")
            after_found = DialogueTreeNode("QUIT", stageUp=1, giveItem='energy_drink', changeQuest=('both', ('concierge', 'cud')))

            energy_found.add_child(after_found, "0")
            liar.add_child(after_liar, "0")

            root.add_child(energy_found, "0")
            root.add_child(energy_not_found, "1")
            root.add_child(liar, "ITEMNOTFOUND")

        elif mode == "zyziostage0":
            dp = "Dialogues/zyzio/stage0/" # Directory Prefix
            root = DialogueTreeNode(dp+"root.txt")

            library = DialogueTreeNode(dp+"library.txt")
            after_library = DialogueTreeNode("QUIT", stageUp=1)

            library.add_child(after_library, "0")

            root.add_child(library, "0")

        elif mode == 'andrzejstage0':
            dp = 'Dialogues/andrzej/stage0/'
            root = DialogueTreeNode(dp+'root.txt')
            yes = DialogueTreeNode(dp+'yes.txt')
            oh_right = DialogueTreeNode(dp+'oh_right.txt', stageUp=1, getItem='energy_drink', changeQuest=('remove', 'andrzej'))
            end = DialogueTreeNode("QUIT")

            oh_right.add_child(end, '0')
            yes.add_child(oh_right, '0')
            root.add_child(yes, '0')

        elif mode == 'deezlegzstage0':
            dp = 'Dialogues/deezlegz/stage0/'

            root = DialogueTreeNode(dp+'root.txt')
            get_lost = DialogueTreeNode("QUIT")
            wassup = DialogueTreeNode(dp+'where_trainers.txt')
            end = DialogueTreeNode("QUIT", stageUp=1, changeQuest=('add', 'trainers'))

            wassup.add_child(end, '0')
            root.add_child(wassup, '0')
            root.add_child(get_lost, '1')

        elif mode == 'deezlegzstage1':
            dp = 'Dialogues/deezlegz/stage1/'

            root = DialogueTreeNode(dp+'root.txt')

            liar = DialogueTreeNode(dp+'dont_lie.txt', faultValue=1)
            after_liar = DialogueTreeNode('QUIT')
            not_found = DialogueTreeNode("QUIT")

            trainers = DialogueTreeNode(dp+'got_trainers.txt', targetItem='trampki', changeQuest=('remove', 'trainers'))
            end = DialogueTreeNode("QUIT", giveItem='trampki', faultValue=-2, stageUp=1)

            trainers.add_child(end, '0')
            liar.add_child(after_liar, '0')

            root.add_child(trainers, '0')
            root.add_child(not_found, '1')
            root.add_child(liar, 'ITEMNOTFOUND')

        return root

    def build_maths_tree(self):
        """Drzewo dialogowe do pytań matematycznych na początku gr - FABUŁA"""
        dp = "Dialogues/maths/"

        root = DialogueTreeNode(dp+"root.txt")

        # X is the faulty option
        addition = DialogueTreeNode(dp+'addition.txt')
        square_func = DialogueTreeNode(dp+'square_func.txt')
        square_funcX = DialogueTreeNode(dp+'square_func.txt', faultValue=1)
        bytkow = DialogueTreeNode(dp+'bytkow.txt')
        bytkowX = DialogueTreeNode(dp+'bytkow.txt', faultValue=1)
        end = DialogueTreeNode("QUIT")
        endX = DialogueTreeNode("QUIT", faultValue=1)

        bytkow.add_child(end, "0")
        bytkow.add_child(endX, "1")

        bytkowX.add_child(end, "0")
        bytkowX.add_child(endX, "1")

        square_func.add_child(bytkowX, "0")
        square_func.add_child(bytkow, "1")

        square_funcX.add_child(bytkowX, "0")
        square_funcX.add_child(bytkow, "1")

        addition.add_child(square_func, "0")
        addition.add_child(square_funcX, "1")

        root.add_child(addition, '0')

        return root

    def build_concierge_tree(self):
        """Drzewo dialogowe do wydarzeń na portierni - FABUŁA"""
        dp = 'Dialogues/concierge/'

        root = DialogueTreeNode(dp+'root.txt')
        no_list = DialogueTreeNode(dp+'no_list_here.txt')
        end = DialogueTreeNode("QUIT")

        no_list.add_child(end, '0')
        root.add_child(no_list, '0')

        return root

    def build_office_tree(self):
        """Drzewo dialogowe do wydarzeń w sekretariacie - FABUŁA"""
        dp = 'Dialogues/office/'

        root = DialogueTreeNode(dp+'root.txt')
        no_list = DialogueTreeNode(dp+'no_list_here.txt')
        end = DialogueTreeNode("QUIT")

        no_list.add_child(end, '0')
        root.add_child(no_list, '0')

        return root

    def _check_node_events(self, npc):
        """Sprawdzenie instrukcji specjalnych dotyczących węzła: zwiększnie
        stage'a, popełnione przewinienie, przekazywanie przedmiotów itd."""

        if self.node.targetItem:
            if not self._check_item_in_inventory(self.node.targetItem):
                self.node = self.node.parent.children['ITEMNOTFOUND']

        # How bad is this answer?
        if self.node.faultValue != 0:
            self.expelling.faults.append(self.node.faultValue)

        if npc: # uruchom tylko, jesli to dialog z NPC (Obsługa dialogów bez przypisanych NPC)
            if self.node.stageUp > 0:
                npc.stage += self.node.stageUp

        for slot in self.dogex.slots.sprites():
            if slot.content:
                if self.node.giveItem == slot.content.id:
                    slot.content = None
                    break

        if self.node.getItem:
            for slot in self.dogex.slots.sprites():
                if slot.content is None:
                    slot.content = Item(self.dogex, self.node.getItem)
                    break

        if self.node.changeQuest:
            mode, quest = self.node.changeQuest
            if mode == 'add':
                self.dogex.story.quests.append(quest)
            elif mode == 'remove':
                self.dogex.story.quests.remove(quest)
            elif mode == 'both':
                self.dogex.story.quests.append(quest[0])
                self.dogex.story.quests.remove(quest[1])

    def load_dialogue(self, npc=None):
        """Wczytanie całego dialogu, razem z odpowiedziami i interfejsem.
        Domyślny NPC to None, żeby móc obsługiwać dialogi bez NPC takie jak pytania
        matematycznr czy rozmową z panią na portierni"""
        self.msgs = [] # Wyczyszczenie ewentualnych poprzednich wiadomości

        self._check_node_events(npc)

        if self.node.data == "QUIT": # See: build_dialogue_tree()
            self.active = False
        else:
            self._load_msg_from_node()
            self._load_answs_from_node()
            self._update_pointer()

    def _load_msg_from_node(self):
        """Wczytanie kwestii NPC z pliku na podstawie self.node"""
        filename = self.node.data
        with open(filename) as file:
            lines = file.readlines()

        yPos = self.tab_rect.y
        for line in lines:
            if line[0] == ">":
                return # Początek części z odpowiedziami, zatrzymaj wczytywanie kwestii
            self._prep_msg(line.strip(), yPos)
            yPos += self.font.get_sized_height()

    def _load_answs_from_node(self):
        # WARNING: Function crashes on multi-line answers. Don't make multi-line answers.
        """Wczytanie możliwych odpowiedzi gracza na postawie self.node"""
        filename  = self.node.data
        lines = self._prepare_anwsers(filename)

        enumerated_lines = list(enumerate(lines)) #Potrzebne jako ID do odnoszenia
        yPos = self.answ_tab_rect.y               #się do danej odpowiedzi
        for msgid, line in enumerated_lines:
            # Pusta linijka oddzielająca poszczególne odpowiedzi
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
                self.sounds.play_sound('dialogi', 0.1)
                self.pointer_rect.midright = msg['rect'].midleft

    def _prep_msg(self, msg, yPos, id=None):
        """Utworzenie obrazu tekstu do wyświetlenia"""
        image, rect = self.font.render(msg)
        rect.x = self.tab_rect.x
        rect.y = yPos
        self.msgs.append({'image': image, 'rect': rect, 'id': id})

    def _check_item_in_inventory(self, itemID):
        """Zwraca True, jeśli podany przedmiot znajduje się w ekwipunku"""
        for slot in self.dogex.slots.sprites():
            if slot.content:
                if slot.content.id == itemID:
                    return True

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

    def __init__(self, data, faultValue=0, stageUp=0, targetItem=None,
        giveItem=None, getItem=None, changeQuest=None):
        """Inicjalizacja węzła"""
        self.data = data
        self.children = {}
        self.parent = None

        # Does this dialogue change something between you an NPC? e.g. quest accepted.
        self.stageUp = stageUp

        # The bigger the fault value, the more severe the fault is
        # and makes you closer to being expelled
        self.faultValue = faultValue

        # When loading this dialogue, the game will check whether you have
        # the item in inventory and basing on that will load different dialogues
        self.targetItem = targetItem

        # Item (ID) to be removed from invetory after loading this node
        self.giveItem = giveItem

        # Item (ID) to be placed in inventory after loading this node
        self.getItem = getItem

        # Tuple (mode, quest), where mode is either 'add' or 'remove'
        # and quest is well, the quest OR
        # ('both', (questToAdd, questToRemove))
        self.changeQuest = changeQuest

    def add_child(self, child, index: str()):
        """Dodanie potomka do drzewa. index to indeks odpowiedzi, po której
        powinien nastąpić ten dialog (od 0 do 3)"""
        child.parent = self
        self.children[index] = child
