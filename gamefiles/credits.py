import pygame
import sys

class Credits:
    """Napisy końcowe"""

    def __init__(self, gmovrs): # Game Over Screen
        self.settings = gmovrs.settings
        self.screen = gmovrs.screen
        self.screen_rect = self.screen.get_rect()
        self.sounds = gmovrs.sounds

        self.image = pygame.image.load('images/credits.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midbottom

        self.y = float(self.rect.y)

    def launch_credits(self):
        """Uruchomienie napisów końcowych"""
        self.screen.fill((0, 0, 0))
        self.sounds.play_music('bg', 0.3)

        while True:
            # Takie trochę _check_events()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
            self.blitme()
            pygame.display.flip()

            if self.rect.bottom < 0:
                pygame.mixer.music.pause()
                break

    def update(self):
        """Przesunięcie napisów w górę"""
        self.y -= self.settings.credits_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
