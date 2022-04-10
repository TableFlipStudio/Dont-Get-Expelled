import pygame
import sys

from save import Button

class GameOverScreen():
    """Ekran do wyświetlania po przegranej"""

    def __init__(self, dogex, game_won):
        self.settings = dogex.settings
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect
        self.sounds = dogex.sounds
        self.game_won = game_won

        self.image = pygame.image.load('images/game_over_better.bmp') if not game_won else pygame.image.load("images/gamewon.bmp")
        self.static_img = pygame.image.load('images/game_over_better.bmp') if not game_won else pygame.image.load("images/gamewon.bmp")
        self.image = pygame.transform.scale(self.image, (self.settings.screen_width, self.settings.screen_height))
        self.static_img = pygame.transform.scale(self.static_img, (self.settings.screen_width, self.settings.screen_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft

        mmpos = (self.screen_rect.centerx, self.screen_rect.centery + 100)
        self.mainmenubutton = Button(self, mmpos, "Main menu")

        if game_won:
            cpos = (mmpos[0], mmpos[1] + self.settings.button_space)
            self.creditbutton = Button(self, cpos, "Credits")

        qpos = (cpos[0], cpos[1] + self.settings.button_space) if game_won else (mmpos[0], mmpos[1] + self.settings.button_space)
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

                if self.mainmenubutton.rect.collidepoint(mouse_pos):

                    self.sounds.play_sound('interakcja')
                    return True

                elif self.quitbutton.rect.collidepoint(mouse_pos):
                    self.sounds.play_sound('interakcja')
                    sys.exit()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.mainmenubutton.blit_button()
        self.quitbutton.blit_button()
        if self.game_won:
            self.creditbutton.blit_button()
