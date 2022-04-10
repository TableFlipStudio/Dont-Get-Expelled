import sys
import pygame
import json
from time import sleep



from settings import Settings
from character import MainCharacter
from inventory import Inventory, Slot
from dialogues import DialogueWindow
from expelling import Expelling
from item import Item
from TiledMap import Map
from npc import NPC
from save import SaveMenu, Button
from mainmenu import MainMenu
from gameoverscreen import GameOverScreen
from story import StoryEvents
from intro import IntroScreen
from music import Music


class DoGeX():
    """Ogólna klasa zarządzająca grą i jej zasobami"""

    def __init__(self):
        """Inicjalizacja gry i zasobów"""
        pygame.init()
        self.settings = Settings()

        self.clock = pygame.time.Clock()

        pygame.mixer.music.load('sounds/background.wav')
        pygame.mixer.music.set_volume(0.2)

        #Wczytanie ekranu i nadanie tytułu
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Don't Get Expelled! The Batory Game")

        #Wczytanie zasobów z pliku
        self.character = MainCharacter(self)
        self.sounds = Music(self)
        self.map = Map(self)
        self.map_image = self.map.map_setup(self.map.tmxdata)
        self.inventory = Inventory(self)
        self.expelling = Expelling(self)
        self.window = DialogueWindow(self)
        self.menu = SaveMenu(self)
        self.m_menu = MainMenu(self)
        self.story = StoryEvents(self)

        self.window_options = IntroScreen(self)# ta klasa występuje też pod nazwą intro_screen tylko dla głównej pętli gry (na dole)

        self.slots = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()

        #Przed wywołaniem _create_slots() nie ma jeszcze slotu do upuszczania
        #Atrybut wyłącznie dla przejrzystości kodu
        self.drop_slot = None

        #Utworzenie slotów
        self._create_slots()

        # Te przyciski jeszcze nie istnieją, atrybuty dla przejrzystości
        self.savebutton = None
        self.snquitbutton = None
        self.quitbutton = None

        # Utworzenie przycisków menu zapisu
        self._create_smenu_buttons()

        # Utworzenie przedmiotów i NPC
        self.items.add(Item(self, 'energy_drink'))
        self.items.add(Item(self, 'kartka', True))
        self.items.add(Item(self, 'trampki', True))
        self.items.add(Item(self, 'zubr', True, 1))

        self.npcs.add(NPC(self,'kuba', -1))
        self.npcs.add(NPC(self,'kasia', -1))
        self.npcs.add(NPC(self,'marek', -1))
        self.npcs.add(NPC(self, 'cud', -1))
        self.npcs.add(NPC(self, 'zyzio'))
        self.npcs.add(NPC(self, 'andrzej', -1))
        self.npcs.add(NPC(self, 'deezlegz'))

        self.map.set_spawn("player")

        self.game_won = False

    def run_game(self):
        """Uruchomienie pętli głównej gry"""
        i = 0

        self.sounds.play_music('bg', 0.3)


        #self.sounds.play_music('background')

        while True:
            self._check_events()
            self.expelling.check_fault_committed()
            self.map.collision()

            if not self.interface_active():
                pygame.mixer.music.unpause()
                self.character.update()
                self.sounds.check_walking_sound()
                if self.m_menu._check_save_exists() and i < 1:
                    self.map.update('static_only')
                    i += 1
                self.map.update('all')
                self._update_npcs()
                self._update_items()
            else:
                self.sounds.check_walking_sound('stop')
            self._update_screen()
            self.clock.tick(self.settings.fps)

            # Zatrzymaj grę, jeśli wyrzucono gracza ze szkoły
            if self.expelling.check_expelled() or self.game_won:
                pygame.mixer.music.pause()
                self.sounds.check_walking_sound('stop')
                break

        return self.game_won

    def _create_slots(self):
        """Utworzenie wszystkich slotów ekwipunku"""
        for row_number in range(2): #Dwa rzędy slotów
            for slot_number in range(8): #Po 8 slotów każdy
                slot = Slot(self.inventory)
                slot_width  = slot.rect.width
                slot_height = slot.rect.height

                slot.x = (slot.rect.x + slot_width +
                    1.5 * slot_width * slot_number)
                slot.rect.x = slot.x
                slot.rect.y += slot_height + 2 * slot_height * row_number
                self.slots.add(slot)
            #Po utworzeniu wszystkich slotów utwórz dodatkowy slot do upuszczania
            else:
                slot = Slot(self.inventory)
                slot.rect.centerx = self.screen.get_rect().centerx
                slot.rect.y += slot_height + 2 * slot_height * 2
                self.drop_slot = slot

    def _create_smenu_buttons(self):
        """Utworzenie przycisków menu zapisu"""
        save_pos = (self.screen_rect.centerx,
            self.screen_rect.centery - self.settings.slot_height)
        self.savebutton = Button(self, save_pos, "Save")

        snquit_pos = (save_pos[0], save_pos[1] + self.settings.button_space)
        self.snquitbutton = Button(self, snquit_pos, "Save and quit")

        quit_pos = (snquit_pos[0], snquit_pos[1] + self.settings.button_space)
        self.quitbutton = Button(self, quit_pos, "Quit without saving")

    def _load_save(self):
        """Wczytanie zapisu i odpowiednie ustawienie parametrów gry"""
        with open("jsondata/character_pos.json") as file:
            chpos = json.load(file)

        with open("jsondata/inventory.json") as file:
            inv_content = json.load(file)

        with open("jsondata/items.json") as file:
            items = json.load(file)

        with open("jsondata/faults.json") as file:
            faultcntr = json.load(file)

        with open("jsondata/stages.json") as file:
            stages = json.load(file)

        with open("jsondata/quest.json") as file:
            quest = json.load(file)

        with open("jsondata/npcs.json") as file:
            npcs = json.load(file)

        self.character.rect.topleft = chpos
        self._set_loaded_inv_content(inv_content)
        self._place_loaded_items(items)
        self._place_loaded_NPCs(npcs)
        self.expelling.fault_counter = faultcntr
        self.story.quests = quest

        for npc in self.npcs.sprites():
            npc.stage = stages[npc.id]

    def _set_loaded_inv_content(self, inv_content):
        """Załadowanie do ekwipunku przedmiotów wczytanych z inventory.json"""
        for slot in self.slots.sprites():
            try:
                itemid = inv_content.pop()
            # Jeśli lista jest już pusta, slot też ma być pusty
            except IndexError:
                slot.content = None
            else:
                slot.content = Item(self, itemid)

    def _place_loaded_items(self, items):
        """Umieszczenie przedmiotów wczytanych z items.json z powrotem
        w self.items (a więc na mapie)"""
        self.items.empty() # Tworzymy tę grupę od nowa
        for itemdata in items:
            item = Item(self, itemdata[0])
            (item.obj.x, item.obj.y) = (itemdata[1][0] + 30, itemdata[1][1] + 30)
            item.rect.center = (itemdata[1])
            item.shown = itemdata[2]
            item.faultValue = itemdata[3]
            self.items.add(item)

    def _place_loaded_NPCs(self, npcs):
        """Umieszczenie przedmiotów wczytanych z npcs.json z powrotem
        w self.npcs (a więc na mapie)"""
        self.npcs.empty() # Tworzymy tę grupę od nowa
        for NPCdata in npcs:
            npc = NPC(self, NPCdata[0])
            (npc.obj.x, npc.obj.y) = (NPCdata[1][0] + 30, NPCdata[1][1] + 30)
            npc.rect.center = (NPCdata[1])
            self.npcs.add(npc)

    def _list_to_group(self, myList):
        """Utworzenie grupy sprite'ów na podstawie listy ich ID,
        wczytanej przez moduł JSON"""
        group = pygame.sprite.Group()
        for spriteid in myList:
            pass

    def _write_save(self):
        """Zapisanie postępu w grze"""
        chpos = self.character.rect.topleft
        invcnt = []
        items = self._group_to_list(self.items, True)
        npcs = self._group_to_list(self.npcs)
        quest = self.story.quests

        for slot in self.slots.sprites():
            if slot.content is not None:
                invcnt.append(slot.content.id)

        faultcntr = self.expelling.fault_counter
        stages = {}



        for npc in self.npcs.sprites():
            stages[npc.id] = npc.stage

        with open("jsondata/character_pos.json", 'w') as file:
            json.dump(chpos, file)

        with open("jsondata/inventory.json", 'w') as file:
            json.dump(invcnt, file)

        with open("jsondata/items.json", 'w') as file:
            json.dump(items, file)

        with open("jsondata/faults.json", 'w') as file:
            json.dump(faultcntr, file)

        with open("jsondata/stages.json", 'w') as file:
            json.dump(stages, file)

        with open("jsondata/npcs.json", 'w') as file:
            json.dump(npcs, file)

        with open('jsondata/quest.json', 'w') as file:
            json.dump(quest, file)

    def _group_to_list(self, group, isItem=False):
        """Utworzenie listy ID i pozycji obiektów na podstawie grupy pygame.
        Potrzebne do zapisywania, ponieważ moduł JSON nie obsługuje
        niewbudowanych struktur danych. isItem określa, czy podana grupa
        to przedmioty (ze względu na dodatkowe parametry)"""
        myList = [] # nazwa dziwna bo 'list' jest zajęte przez built-in func.
        for sprite in group.sprites():
            spritedata = (sprite.id, sprite.rect.topleft, sprite.shown, sprite.faultValue) if isItem else (sprite.id, sprite.rect.topleft)
            myList.append(spritedata)
        return myList

    def _reset_save(self):
        """Zresetowanie postępu w grze"""
        chpos = (0, 0)
        invcnt = []
        items = [
            Item(self, 'kartka', True),
            Item(self, 'trampki', True),
            Item(self, 'zubr', True, 1),
            Item(self, 'energy_drink')
            ]
        npcs = [
            NPC(self, 'kasia', -1),
            NPC(self, 'kuba', -1),
            NPC(self, 'marek', -1),
            NPC(self, 'zyzio'),
            NPC(self, 'cud', -1),
            NPC(self, 'andrzej', -1),
            NPC(self, 'deezlegz')
            ]
        items = [(item.id, item.rect.topleft) for item in items]
        npcs = [(npc.id, npc.rect.center) for npc in npcs]
        faultcntr = self.settings.faults_to_be_expelled
        stages = {}
        quest = ['math']


        with open("jsondata/character_pos.json", 'w') as file:
            json.dump(chpos, file)

        with open("jsondata/inventory.json", 'w') as file:
            json.dump(invcnt, file)

        with open("jsondata/items.json", 'w') as file:
            json.dump(items, file)

        with open("jsondata/faults.json", 'w') as file:
            json.dump(faultcntr, file)

        with open("jsondata/stages.json", 'w') as file:
            json.dump(stages, file)

        with open("jsondata/npcs.json", 'w') as file:
            json.dump(npcs, file)

        with open('jsondata/quest.json', 'w') as file:
            json.dump(quest, file)

    def interface_active(self, exclude=None):
        """Zwraca True, jeśli którykolwiek z interfejsów
        (ekranów wyświetlanych zamiast głównego widoku gry i blokujących
        bieg gry), za wyjątkiem wskazanego przez argument exclude,
        jest aktywny"""

        if exclude is None:
            detected = (
                self.inventory.active or
                self.window.active or
                self.menu.active or
                self.map.active
                )
        elif exclude == "inventory":
            detected = (
                self.window.active or
                self.menu.active or
                self.map.active
                )
        elif exclude == "window":
            detected = (
                self.inventory.active or
                self.menu.active or
                self.map.active
                )
        elif exclude == "menu":
            detected = (
                self.inventory.active or
                self.window.active or
                self.map.active
                )
        elif exclude == "map":
            detected = (
                self.inventory.active or
                self.window.active or
                self.menu.active
                )
        return detected

    def _check_events(self):
        """Reakcja na zdarzenia wywołane przez klawiaturę i mysz"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            self.check_moving_keys()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                if (self.inventory.grabbed_item is None and
                self.inventory.active):
                    self.inventory.grab_item(self, mouse_pos)

                elif self.menu.active:
                    if self.savebutton.rect.collidepoint(mouse_pos):
                        self.sounds.play_sound('interakcja')
                        self._write_save()
                        self.menu.active = False
                    elif self.snquitbutton.rect.collidepoint(mouse_pos):
                        self._write_save()
                        self.sounds.play_sound('interakcja')
                        sys.exit()
                    elif self.quitbutton.rect.collidepoint(mouse_pos):
                        self.sounds.play_sound('interakcja')
                        sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP and self.inventory.active:
                mouse_pos = pygame.mouse.get_pos()
                self.inventory.release_item(self, mouse_pos)

        self.story._check_story_events()

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza"""

        if event.key == pygame.K_UP:
            if self.window.active:
                self._change_selection(-1)

        if event.key == pygame.K_DOWN:
            if self.window.active:
                self._change_selection(1)

        if event.key == pygame.K_i:
            if not self.interface_active("inventory"):
                self.inventory.active = not self.inventory.active

        if event.key == pygame.K_m:
            if not self.interface_active("map"):
                self.map.active = not self.map.active

        if event.key == pygame.K_RETURN:
            self._choose_answer()

        if event.key == pygame.K_ESCAPE:
            if not self.interface_active("menu"):
                self.menu.active = not self.menu.active

        if event.key == pygame.K_e:
            found_npc = self._find_npc_collision()
            if not self.interface_active():
                if found_npc is None:
                    self._pickup_item()
                else:
                    # Jesli ten NPC nie ma dialogów, nie wczytuj
                    try:
                        max_stage = len(self.window.dialogues[found_npc.id]) - 1
                    except KeyError:
                        pass
                    else:
                        if found_npc.stage <= max_stage and found_npc.stage >= 0:
                            #Jeśli E kliknięto przy NPC, wejdź z nim w dialog
                            self.window.active = True
                            self.window.node = self.window.dialogues[found_npc.id][found_npc.stage]
                            self.window.load_dialogue(found_npc)

        if event.key == pygame.K_LSHIFT:
            self.sounds.corridor.stop()
            self.sounds.corridor = pygame.mixer.Sound('sounds/chodzenie_korytarz_x2.wav')
            self.sounds.corridor.set_volume(0)
            self.sounds.corridor.play(-1)
            self.settings.character_speed *= 2

        elif event.key == pygame.K_q:
            sys.exit()

    def check_moving_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.character.moving_up = True
            self.map.moving_down = True

        if keys[pygame.K_DOWN]:
            self.character.moving_down = True
            self.map.moving_up = True

        if keys[pygame.K_RIGHT]:
            self.character.moving_right = True
            self.map.moving_left = True

        if keys[pygame.K_LEFT]:
            self.character.moving_left = True
            self.map.moving_right = True

    def _change_selection(self, UpOrDown: "-1 or 1 (int)"):
        """Zmnienia zaznaczenie odpowiedzi gracza w oknie dialogowym
        (przesuwa strzałkę)"""
        self.window.selectedID += 1 * UpOrDown
        id = self.window.selectedID
        id_limit = self.window.msgs[-1]['id']
        if id < 0 or id > id_limit:
            self.window.selectedID -= 1 * UpOrDown
        self.window._update_pointer()

    def _choose_answer(self):
        """Zatwierdzenia wskazanej odpowiedzi i wczytanie ciągu dalszego
        dialogu"""
        if self.window.active:
            msgid = str(self.window.selectedID)
            npc = self._find_npc_collision()
            try:
                self.window.node = self.window.node.children[msgid]
            except KeyError:
                pass
            else:
                self.window.load_dialogue(npc)

    def _check_keyup_events(self, event):
        """Reakcja na puszczenie klawisza"""

        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
            self.map.moving_left = False

        if event.key == pygame.K_LEFT:
            self.character.moving_left = False
            self.map.moving_right = False

        if event.key == pygame.K_UP:
            self.character.moving_up = False
            self.map.moving_down = False

        if event.key == pygame.K_DOWN:
            self.character.moving_down = False
            self.map.moving_up = False

        if event.key == pygame.K_LSHIFT:
            self.sounds.corridor.stop()
            self.sounds.corridor = pygame.mixer.Sound('sounds/chodzenie_korytarz.wav')
            self.sounds.corridor.set_volume(0)
            self.sounds.corridor.play(-1)
            self.settings.character_speed /= 2

    def rewrite_dialogue_files(self):
        """Funkcja zczytuje zawartość wszystkich plików a następnie odtwarza
        ją tak, aby wszystkie linijki mieściły się w polu tekstowym. Funkcja
        powinna być wywoływana tylko przy rozpoczęciu nowej gry, zmianie treści
        plików z dialogami lub zmianie ustawień wyświetlania (szerokośc ekranu,
        szerokośc pola tekstowego)"""
        exammple_char = self.window.font.render('x')[0]
        char_width = exammple_char.get_width()
        available_chars = self.settings.tab_width // char_width
        for trees in self.window.dialogues.values():
            if isinstance(trees, list): # Math questions is a tree, not a list of trees
                for tree in trees:
                    self._rewriteNodeAndGO(tree, available_chars)
            else:
                self._rewriteNodeAndGO(trees, available_chars)

    def _rewriteNodeAndGO(self, node, available_chars):
        """Rekurencyjnie odtwrzarza wszystkie pliki drzewa dialogowego"""
        if node.data == "QUIT":
            return

        self._rewrite_lines(available_chars, node.data)
        self._rewrite_answers() #This virtually does not exist yet

        for child in node.children.values():
            self._rewriteNodeAndGO(child, available_chars)

    def _rewrite_lines(self, available_chars, filename):
        """Odtworzenie pliku z kwestiami NPC"""
        lines, answs = self._read_file(filename)
        words = self._form_wordlist(lines)
        output = self._form_output(words, available_chars)
        self._write_output(output, answs, filename)

    def _rewrite_answers(self):
        """Odtworzenie plików z odpowidziami gracza"""
        pass

    def _read_file(self, filename):
        """Zczytanie zawartości pliku dialogowego"""
        with open(filename) as file:
            lines = file.readlines()
            answs = [] # Lista do przechowywanie odpowiedzi na czas przepisywania kwestii
            worklines = lines[:] # Kopia listy bo nie należy usuwać elementów
            # listy podczas iteracji przez nią.

            # Usuń wszystko co jest odpowiedzią
            for line in worklines:
                if line[0] == ">":
                    answs.append(line)
                    lines.remove(line)
        return lines, answs

    def _form_wordlist(self, lines):
        """Reorganizacja listy z linijkami tak, aby uformować listę wszystkich
        słów w pliku"""
        lines_with_words = [word.strip().split(' ') for word in lines]
        words = []
        for word in lines_with_words: #Scal podlisty w jedną listę
            words += word
        return words

    def _form_output(self, words, available_chars):
        """Uformowanie nowych linijek tak, aby mieściły się w polu tekstowym
        okna dialogowego."""
        currentLine = ''
        output = ''
        for word in words:
            all_len = len(currentLine) + len(f'{word} ') + 5
            if all_len <= available_chars:
                currentLine += f'{word} '
            else:
                output += f'{currentLine}\n'
                currentLine = f'{word} '
        output += f'{currentLine}'
        return output

    def _write_output(self, output, answs, filename):
        """Zapisanie zreorganizowanej linii dialogowej w pliku wyjściowym,
        nadpisując wartość pierwotną"""
        with open(filename, 'w') as file:
            file.write(output)

            # Dodaj odpowiedzi usunięte na początku
            file.write(f'\n')
            for answ in answs:
                file.write(answ)

    def _find_npc_collision(self):
        """Sprawdza, czy postać głowna koliduje z którymś NPC,
        jeśli tak, zwraca go"""
        for npc in self.npcs.sprites():
            if self.character.rect.colliderect(npc):
                return npc
        else:
            return None

    def _pickup_item(self):
        """Sprawdzenie, czy postać stoi koło przedmiotu
        i ewentualne podniesienie"""

        for item in self.items.copy():

            if pygame.Rect.colliderect(self.character.rect, item) and item.shown:
                pygame.mixer.Sound('sounds/podnoszenie_przedmiotu.wav').play()

            if pygame.Rect.colliderect(self.character.rect, item) and item.shown:
                for slot in self.slots.sprites():
                    #Umieść przedmiot tylko raz
                    if slot.content is None:
                        if item.faultValue > 0:
                            self.expelling.faults.append(item.faultValue)
                        slot.content = item
                        break

                item.shown = False

    def _update_npcs(self):
        """Uaktualnienie pozycji wszystkich NPC"""
        for npc in self.npcs.sprites():
            npc.rect.center = ((npc.obj.x), (npc.obj.y))

    def _update_items(self):
        """Uaktualnienie pozycji wszystkich przedmiotów"""
        for item in self.items.sprites():
            item.rect.center = ((item.obj.x), (item.obj.y))


    def _update_screen(self):
        """Aktualizacja zawartości ekranu"""

        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.map_image, (self.map.x, self.map.y))
        #pygame.draw.rect(self.screen, ((0,255,0)), self.map.rect) #TOBEDELETED
        self.character.blitme()
        self.expelling.blitmsg()
        self.story.blitmsg()

        #Wyświetlamy przedmioty i postacie tylko, gdy ekwipunek jest nieaktywny
        if not self.inventory.active:

            for npc in self.npcs.sprites():
                npc.blit_npc()

            for item in self.items.sprites():
                if item.shown:
                    item.blit_item()

            self.character.blitme()

        if self.map.active and not self.interface_active('map'):
            self.map.display_mini_map()

        #Wyświetlamy ekwipunek tylko, jeśli jest on aktywny (naciśnięto I)
        if self.inventory.active and not self.interface_active('inventory'):
            self.inventory.display_inventory()
            for slot in self.slots.sprites():
                slot.draw_slot()
                slot.blit_content()

            #Wyświetlenie slotu do upuszczania przemiotów
            self.drop_slot.draw_slot()

            #Wyświetlenie przedmiotu pochwyconego myszą
            self.inventory.display_grabbed_item()

        #Ekwipunek i okno dialogowe nie mogą występować jednocześnie
        if self.window.active and not self.interface_active('window'):
            self.window.blit_window()

        # Menu zapisu
        if self.menu.active:
            self.menu.blit_menu()
            self.savebutton.blit_button()
            self.snquitbutton.blit_button()
            self.quitbutton.blit_button()


        #Wyświetlenie zmodyfikowanego ekranu
        pygame.display.flip()


def _run_main_menu(dogex):
    """Uruchomienie menu głównego - wykrywanie zdarzeń itd."""
    #commented ponieważ przyciski są działające a fade in zajmuje się obrazem

    dogex.sounds.play_music('bg',0.3)

    intro_screen.fadein(menu.static_img, 0.2, 50)
    menu.blitme()
    pygame.display.flip()
    while True:
        # Jeśli kliknięto Load game albo New game, przerwij działanie menu
        # i uruchom grę
        run_detected = menu.check_events(dogex)
        if run_detected:
            pygame.mixer.music.stop()
            intro_screen.fadeout(0.3)
            break

def intro(dogex):
    """Wyświetlenie ekranu powitalnego"""
    intro_screen.black_screen()
    pygame.display.flip()

    pygame.time.wait(1000)
    intro_screen.intro_fadein(0.3)
    intro_screen.blitme()
    pygame.display.flip()

    pygame.time.wait(1000)
    intro_screen.fadeout(0.3)

def _run_game_over(dogex, game_won):
    """Uruchomienie ekranu końca gry - tak jak _run_main_menu()"""
    gmovr = GameOverScreen(dogex, game_won)
    intro_screen.black_screen()
    pygame.display.flip()
    pygame.time.wait(250)
    if not game_won:
        dogex.sounds.play_sound('game_over_better')
    else:
        dogex.sounds.play_sound('yaaaay')
    pygame.time.wait(1700)
    intro_screen.fadein(gmovr.static_img, 0.3, 100)
    gmovr.blitme()
    pygame.display.flip()

    while True:
        # Patrz: _run_main_menu()
        relaunch = gmovr.check_events(dogex)
        if relaunch:
            break

if __name__ == '__main__':
    while True:
        dogex = DoGeX()
        intro_screen = IntroScreen(dogex)
        intro(dogex)
        menu = MainMenu(dogex)

        _run_main_menu(dogex)
        game_won = dogex.run_game()
        _run_game_over(dogex, game_won) # This can be a win too
