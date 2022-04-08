import pygame
import pygame.font

class StoryEvents():
    """Zarządzanie biegiem fabuły i zdarzeniami z nim związanymi."""

    def __init__(self, dogex):
        self.screen = dogex.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dogex.settings

        self.map = dogex.map
        self.window = dogex.window
        self.character = dogex.character
        self.dogex = dogex
        self.sounds = dogex.sounds

        # List of quest codenames and index to decide, which quest is active
        self.quests = ['math']

        self.hints = {
            'math': "Go to the math lesson in room 114",
            'cud': "Get the book list from the Library",
            'andrzej': "Bring an energy drink to the Girl In Black",
            'concierge': "Ask for book list in the concierge",
            'office': "Ask for book list in the school's office",
            'exit': "Exit the school",
            'trainers': "Find the Sporty Girl's trainers"
        }

        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (255, 255, 255)

        self._update_msg()

    def _set_hint(self):
        """Uformowanie wskazówki na podstawie aktualnych questów"""
        hint = 'Quests: '
        for i, quest in list(enumerate(self.quests)):
            last_quest = not (len(self.quests) > i + 1) # Checks if this is the last quest from the list

            try:
                hint += self.hints[quest]
            except KeyError:
                pass
            else:
                hint += '' if last_quest else ', '

        return hint

    def _update_msg(self):
        """Utworzenie obrazka licznika na podstawie self.fault_counter."""
        hint = self._set_hint()

        self.image = self.font.render(hint, True,
            self.text_color, None)
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen_rect.bottomleft

    def _check_story_events(self):
        """Zdarzenia związane z biegiem fabuły"""
        if 'math' in self.quests:
            math_trigger_area = self.map._access_Object('objects.mathtrigger')
            mta_rect = pygame.Rect(math_trigger_area.x, math_trigger_area.y,
                math_trigger_area.width, math_trigger_area.height)

            if self.character.rect.colliderect(mta_rect):
                self.window.active = True
                self.window.node = self.window.dialogues['matma']
                self.window.load_dialogue()
                self.quests.remove('math')
                self.quests.append('zyzio')

        if 'zyzio' in self.quests:
            encounter = self.map._access_Object('objects.zyzioencounter')
            zyzio_obj = self.map._access_Object('npc.zyzio')
            zyzio_obj.x, zyzio_obj.y = encounter.x, encounter.y

            found_npc = self.dogex._find_npc_collision()
            if found_npc and found_npc.id == 'zyzio':
                self.sounds.check_walking_sound('stop')
                self.window.active = True
                self.window.node = self.window.dialogues[found_npc.id][found_npc.stage]
                self.window.load_dialogue(found_npc)
                self.quests.remove('zyzio')
                self.quests.append('cud')

        if 'cud' in self.quests:
            for npc in self.dogex.npcs.sprites():
                if npc.id == 'cud' and npc.stage < 0:
                    npc.stage = 0

        if 'andrzej' in self.quests:
            for npc in self.dogex.npcs.sprites():
                if npc.id == 'andrzej' and npc.stage < 0:
                    npc.stage = 0


        if 'concierge' in self.quests:
            concierge = self.map._access_Object('objects.concierge')
            concierge_rect = pygame.Rect(concierge.x, concierge.y,
                concierge.width, concierge.height)

            if self.character.rect.colliderect(concierge_rect):
                self.sounds.check_walking_sound('stop')
                self.window.active = True
                self.window.node = self.window.dialogues['concierge']
                self.window.load_dialogue()
                self.quests.remove('concierge')
                self.quests.append('office')

        if 'office' in self.quests:
            office = self.map._access_Object('objects.office')
            office_rect = pygame.Rect(office.x, office.y,
                office.width, office.height)

            if self.character.rect.colliderect(office_rect):
                self.sounds.check_walking_sound('stop')
                self.window.active = True
                self.window.node = self.window.dialogues['office']
                self.window.load_dialogue()
                self.quests.remove('office')
                self.quests.append('exit')

        if 'exit' in self.quests:
            exits = self.map._get_all_contents('exit-areas')
            for exit in exits:
                exit_rect = pygame.Rect(exit.x, exit.y,
                    exit.width, exit.height)

                if self.character.rect.colliderect(exit_rect):
                    self.sounds.check_walking_sound('stop')
                    #print('collision!')
                    self.dogex.game_won = True

        self._update_msg()

    def blitmsg(self):
        self.screen.blit(self.image, self.rect)
