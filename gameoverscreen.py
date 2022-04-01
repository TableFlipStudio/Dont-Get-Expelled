import pygame
import sys

from save import Button

class GameOverScreen():
    """Ekran do wyświetlania po przegranej"""

    def __init__(self, dogex):
        self.settings = dogex.settings
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect

        self.image = pygame.image.load("images/gameover.bmp")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft

        mmpos = (self.screen_rect.centerx, self.screen_rect.centery + 100)
        self.mainmenubutton = Button(self, mmpos, "Main menu")

        qpos = (mmpos[0], mmpos[1] + self.settings.button_space)
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
                    pygame.mixer.Sound('sounds/interakcja.wav').play()
                    dogex._reset_save()
                    return True

                elif self.quitbutton.rect.collidepoint(mouse_pos):
                    pygame.mixer.Sound('sounds/interakcja.wav').play()
                    sys.exit()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.mainmenubutton.blit_button()
        self.quitbutton.blit_button()
