# PRZETESTOWAĆ:
# wczytywanie zapisu (nie wczytują się przedmioty)
# zapisywanie



import sys
import pygame
import json

from settings import Settings
from character import MainCharacter
from inventory import Inventory, Slot
from dialogues import DialogueWindow
from item import Item
from TiledMap import Map
from npc import NPC
from save import SaveMenu, Button

class DoGeX():
    """Ogólna klasa zarządzająca grą i jej zasobami"""

    def __init__(self):
        """Inicjalizacja gry i zasobów"""
        pygame.init()
        self.settings = Settings()

        self.clock = pygame.time.Clock()

        #Wczytanie ekranu i nadanie tytułu
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Don't Get Expelled! The Batory Game")

        #Wczytanie zasobów z pliku
        self.character = MainCharacter(self)
        self.character.facing = "stationary"
        self.inventory = Inventory(self)
        self.map = Map(self)
        self.map_image = self.map.map_setup(self.map.tmxdata)
        self.window = DialogueWindow(self)
        self.menu = SaveMenu(self)

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
        self.resetbutton = None
        self.snquitbutton = None
        self.quitbutton = None

        # Utworzenie przycisków menu zapisu
        self._create_smenu_buttons()

        #Testowe rozmieszczenie przedmiotów i NPC
        self.items.add(Item(self, 'red_ball', (100, 100)))
        self.items.add(Item(self, 'blue_ball', (1000, 400)))
        self.items.add(Item(self, 'green_ball', (500, 650)))

        self.npcs.add(NPC(self,'test_npc'))

        self._load_save()

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

        reset_pos = (snquit_pos[0], snquit_pos[1] + self.settings.button_space)
        self.resetbutton = Button(self, reset_pos, "Reset all data")

        quit_pos = (reset_pos[0], reset_pos[1] + self.settings.button_space)
        self.quitbutton = Button(self, quit_pos, "Quit without saving")

    def _load_save(self):
        """Wczytanie zapisu i odpowiednie ustawienie parametrów gry"""
        with open("jsondata/character_pos.json") as file:
            chpos = json.load(file)

        with open("jsondata/map_pos.json") as file:
            mpos = json.load(file)

        with open("jsondata/inventory.json") as file:
            inv_content = json.load(file)

        with open("jsondata/items.json") as file:
            items = json.load(file)

        self.character.rect.topleft = chpos
        self.map.rect.topleft = mpos
        for slot in self.slots.sprites():
            try:
                itemid = inv_content.pop()
            except IndexError:
                slot.content = None
            else:
                slot.content = Item(self, itemid, (0, 0))

        self.items.empty() # Tworzymy tę grupę od nowa
        for itemdata in items:
            item = Item(self, itemdata[0], itemdata[1])
            self.items.add(item)

    def _list_to_group(self, myList):
        """Utworzenie grupy sprite'ów na podstawie listy ich ID,
        wczytanej przez moduł JSON"""
        group = pygame.sprite.Group()
        for spriteid in myList:
            pass

    def _write_save(self):
        """Zapisanie postępu w grze"""
        chpos = self.character.rect.topleft
        mpos = self.map.rect.topleft
        invcnt = []
        items = self._group_to_list(self.items)

        for slot in self.slots.sprites():
            if slot.content is not None:
                invcnt.append(slot.content.id)

        with open("jsondata/character_pos.json", 'w') as file:
            json.dump(chpos, file)

        with open("jsondata/map_pos.json", 'w') as file:
            json.dump(mpos, file)

        with open("jsondata/inventory.json", 'w') as file:
            json.dump(invcnt, file)

        with open("jsondata/items.json", 'w') as file:
            json.dump(items, file)

    def _group_to_list(self, group):
        """Utworzenie listy ID i pozycji obiektów na podstawie grupy pygame.
        Potrzebne do zapisywania, ponieważ moduł JSON nie obsługuje
        niewbudowanych struktur danych"""
        myList = [] # nazwa dziwna bo 'list' jest zajęte przez built-in func.
        for sprite in group.sprites():
            spritedata = (sprite.id, sprite.rect.topleft)
            myList.append(spritedata)
        return myList

    def _reset_save(self):
        """Zresetowanie postępu w grze"""
        chpos = (0, 0)
        mpos = (0, 0)
        invcnt = []
        items = [
            Item(self, 'red_ball', (100, 100)),
            Item(self, 'blue_ball', (1000, 400)),
            Item(self, 'green_ball', (500, 650))
            ]
        items = [(item.id, item.rect.topleft) for item in items]

        with open("jsondata/character_pos.json", 'w') as file:
            json.dump(chpos, file)

        with open("jsondata/map_pos.json", 'w') as file:
            json.dump(mpos, file)

        with open("jsondata/inventory.json", 'w') as file:
            json.dump(invcnt, file)

        with open("jsondata/items.json", 'w') as file:
            json.dump(items, file)

    def interface_active(self, exclude=None):
        """Zwraca True, jeśli którykolwiek z interfejsów
        (ekranów wyświetlanych zamiast głównego widoku gry i blokujących
        bieg gry), za wyjątkiem wskazanego przez argument exclude,
        jest aktywny"""

        if exclude is None:
            detected = (
                self.inventory.active or
                self.window.active or
                self.menu.active
                )
        elif exclude == "inventory":
            detected = (
                self.window.active or
                self.menu.active
                )
        elif exclude == "window":
            detected = (
                self.inventory.active or
                self.menu.active
                )
        elif exclude == "menu":
            detected = (
                self.inventory.active or
                self.window.active
                )
        return detected

    def run_game(self):
        """Uruchomienie pętli głównej gry"""

        while True:
            self._check_events()
            #self.map.collision()

            if not self.interface_active():
                self.character.update()
                self.map.update()
                self._update_npcs()

            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Reakcja na zdarzenia wywołane przez klawiaturę i mysz"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if (self.inventory.grabbed_item is None and
                self.inventory.active):
                    self.inventory.grab_item(self, mouse_pos)

                elif self.menu.active:
                    if self.savebutton.rect.collidepoint(mouse_pos):
                        self._write_save()
                    elif self.resetbutton.rect.collidepoint(mouse_pos):
                        self._reset_save()
                    elif self.snquitbutton.rect.collidepoint(mouse_pos):
                        self._write_save()
                        sys.exit()
                    elif self.quitbutton.rect.collidepoint(mouse_pos):
                        sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP and self.inventory.active:
                mouse_pos = pygame.mouse.get_pos()
                self.inventory.release_item(self, mouse_pos)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza"""

        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True
            self.map.moving_left = True
            self.character.facing = "right"

        if event.key == pygame.K_LEFT:
            self.character.moving_left = True
            self.map.moving_right = True
            self.character.facing = "left"

        if event.key == pygame.K_UP:
            if self.window.active:
                self._change_selection(-1)
            else:
                self.character.moving_up = True
                self.map.moving_down = True

        if event.key == pygame.K_DOWN:
            if self.window.active:
                self._change_selection(1)
            else:
                self.character.moving_down = True
                self.map.moving_up = True

        if event.key == pygame.K_i:
            if not self.interface_active("inventory"):
                self.inventory.active = not self.inventory.active

        if event.key == pygame.K_RETURN:
            self._choose_answer()

        if event.key == pygame.K_q:
            if not self.interface_active("menu"):
                self.menu.active = not self.menu.active

        if event.key == pygame.K_e:
            npc_collide = self._find_npc_collision()
            if not self.interface_active():
                if npc_collide is None:
                    self._pickup_item()
                else:
                    #Jeśli E kliknięto przy NPC, wejdź z nim w dialog
                    self.window.active = True
                    self.window.node = self.window.dialogues[npc_collide.id]
                    self.window.load_dialogue(npc_collide.id)

        if event.key == pygame.K_LSHIFT:
            self.settings.character_speed *= 2

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

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
            npcid = self._find_npc_collision().id
            self.window.node = self.window.node.children[msgid]
            self.window.load_dialogue(npcid)

    def _check_keyup_events(self, event):
        """Reakcja na puszczenie klawisza"""

        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
            self.map.moving_left = False
            self.character.facing = "stationary"

        if event.key == pygame.K_LEFT:
            self.character.moving_left = False
            self.map.moving_right = False
            self.character.facing = "stationary"

        if event.key == pygame.K_UP:
            self.character.moving_up = False
            self.map.moving_down = False
            self.character.facing = "stationary"

        if event.key == pygame.K_DOWN:
            self.character.moving_down = False
            self.map.moving_up = False
            self.character.facing = "stationary"

        if event.key == pygame.K_LSHIFT:
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
        for tree in self.window.dialogues.values():
            self._rewriteNodeAndGO(tree, available_chars)

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
            if pygame.Rect.colliderect(self.character.rect, item):
                for slot in self.slots.sprites():
                    #Umieść przedmiot tylko raz
                    if slot.content is None:
                        slot.content = item
                        break

                self.items.remove(item)

    def _check_npc_vertical_edges(self):
        """Zmiana kierunku poruszania się NPC, jeśli dotarł blisko
        krawędzi ekranu"""
        for npc in self.npcs.sprites():
            if npc.check_vertical_edges():
                npc.yDirection *= -1

    def _update_npcs(self):
        """Uaktualnienie pozycji wszystkich NPC"""
        self._check_npc_vertical_edges()
        self.npcs.update()

    def _update_screen(self):
        """Aktualizacja zawartości ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.map_image, (self.map.x, self.map.y))
        #pygame.draw.rect(self.screen, self.map.debug_color, self.map.debug_rect) #TOBEDELETED
        self.character.blitme()

        #Wyświetlamy przedmioty i postacie tylko, gdy ekwipunek jest nieaktywny
        if not self.inventory.active:
            self.character.blitme()

            for npc in self.npcs.sprites():
                npc.blit_npc()

            for item in self.items.sprites():
                item.blit_item()

        #Wyświetlamy ekwipunek tylko, jeśli jest on aktywny (naciśnięto I)
        if self.inventory.active and not self.window.active:
            self.inventory.display_inventory()
            for slot in self.slots.sprites():
                slot.draw_slot()
                slot.blit_content()

            #Wyświetlenie slotu do upuszczania przemiotów
            self.drop_slot.draw_slot()

            #Wyświetlenie przedmiotu pochwyconego myszą
            self.inventory.display_grabbed_item()

        #Ekwipunek i okno dialogowe nie mogą występować jednocześnie
        if not self.inventory.active and self.window.active:
            self.window.blit_window()

        # Menu zapisu
        if self.menu.active:
            self.menu.blit_menu()
            self.savebutton.blit_button()
            self.resetbutton.blit_button()
            self.snquitbutton.blit_button()
            self.quitbutton.blit_button()

        #Wyświetlenie zmodyfikowanego ekranu
        pygame.display.flip()




if __name__ == '__main__':
    dogex = DoGeX()
    dogex.run_game()
