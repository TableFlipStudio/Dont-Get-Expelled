import pygame

class StoryEvents():
    """Zarządzanie biegiem fabuły i zdarzeniami z nim związanymi."""

    def __init__(self, dogex):
        self.settings = dogex.settings
        self.map = dogex.map
        self.window = dogex.window
        self.character = dogex.character
        self.dogex = dogex

        # List of quest codenames and index to decide, which quest is active
        self.quests = ['math']

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
                self.window.active = True
                self.window.node = self.window.dialogues[found_npc.id][found_npc.stage]
                self.window.load_dialogue(found_npc)
                self.quests.remove('zyzio')

                for npc in self.dogex.npcs.sprites():
                    if npc.id == 'cud':
                        npc.stage = 0

        if 'concierge' in self.quests:
            concierge = self.map._access_Object('objects.concierge')
            concierge_rect = pygame.Rect(concierge.x, concierge.y,
                concierge.width, concierge.height)

            if self.character.rect.colliderect(concierge_rect):
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
                self.window.active = True
                self.window.node = self.window.dialogues['office']
                self.window.load_dialogue()
                self.quests.remove('office')
