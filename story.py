import pygame

class StoryEvents():
    """Zarządzanie biegiem fabuły i zdarzeniami z nim związanymi."""

    def __init__(self, dogex):
        self.settings = dogex.settings
        self.map = dogex.map
        self.window = dogex.window
        self.character = dogex.character

        # List of quest codenames and index to decide, which quest is active
        self.quests = ['math', None]
        self.inx = 0

    def _check_story_events(self):
        """Zdarzenia związane z biegiem fabuły"""
        if self.quests[self.inx] == 'math':
            math_trigger_area = self.map._access_Object('objects.mathtrigger')
            mta_rect = pygame.Rect(math_trigger_area.x, math_trigger_area.y,
                math_trigger_area.width, math_trigger_area.height)

            if self.character.rect.colliderect(mta_rect):
                self.window.active = True
                self.window.node = self.window.dialogues['matma']
                self.window.load_dialogue()
                self.inx += 1
