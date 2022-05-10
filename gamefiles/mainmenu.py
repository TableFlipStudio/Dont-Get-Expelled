import pygame
import sys
import requests

from save import Button

class MainMenu():
    """Menu główne, wczytywane przed uruchomieniem run_game()"""

    def __init__(self, dogex):
        self.settings = dogex.settings
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect
        self.sounds = dogex.sounds

        self.image = pygame.image.load("images/mainmenu.bmp")
        self.static_img = pygame.image.load("images/static_img/mMenu.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft
        
        #info about the game version
        self.version = pygame.font.SysFont('comicsansms', 30)
        self.version_text = self.version.render('You don\'t have the lastest version', True, (139,0,0), None)
        self.version_rect = self.version_text.get_rect()
        self.version_rect.center = (self.screen_rect.centerx+ self.screen_rect.width/4, self.screen_rect.centery - self.screen_rect.height/6)
        
        #getting the latest version number from github
        
        v = ''   #cloud version 
        r = requests.get(
            'https://raw.githubusercontent.com/TableFlipStudio/Dont-Get-Expelled/main/gamefiles/version.txt', stream=True)  # pobieranie wersji

        for chunk in r.iter_content(chunk_size=None):
            chunk = chunk.decode('utf-8')   # chunk is a byte string
        for i in chunk:
            if i.isdigit(): # if i is a digit
                v += i      # add it to v
                
        with open('version.txt', 'r') as file:
            lv = file.readline() # lv - local version 
        
        if v != lv:
            self.lastest = False
        else:
            self.lastest = True
            

        # Przyciski manu głównego
        ngpos = (self.settings.screen_width / 5,
            self.settings.screen_height / 2.5)
        self.newgamebutton = Button(self, ngpos, "New game")

        lgpos = (ngpos[0], ngpos[1] + self.settings.button_space)
        self.loadgamebutton = Button(self, lgpos, "Load game")

        qpos = (lgpos[0], lgpos[1] + self.settings.button_space)
        self.quitbutton = Button(self, qpos, "Quit")

    def check_events(self, dogex):
        """Metoda identyczna jak _check_events() klasy DoGeX(), służy
        jednak ona do detekcji zdarzeń na etapie menu głównego, czyli przed
        uruchomieniem gry jako takiej."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.newgamebutton.rect.collidepoint(mouse_pos):
                    self.sounds.play_sound('interakcja')
                    dogex._reset_save()
                    return True

                elif (
                    self.loadgamebutton.rect.collidepoint(mouse_pos)
                    and self._check_save_exists() # Przycisk jest zablokowany jeśli zapis nie istnieje
                ):
                    self.sounds.play_sound('interakcja')
                    dogex._load_save()
                    return True

                elif self.quitbutton.rect.collidepoint(mouse_pos):
                    self.sounds.play_sound('interakcja')
                    sys.exit()

    def _check_save_exists(self):
        with open('jsondata/character_pos.json') as file:
            test = file.read()
        if '[0, 0]' not in test: # Takie koordynaty na w zasadzie mogą wystąpić tylko po uruchomieniu nowej gry.
            return True # Jeśli użytkonik akurat zapisze grę w tym miejscu to jego problem
        else:
            return False
        
    

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.newgamebutton.blit_button()
        self.loadgamebutton.blit_button()
        self.quitbutton.blit_button()
        if not self.lastest:
            self.screen.blit(self.version_text, self.version_rect)
