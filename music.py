import pygame

class Music():

    def __init__(self, dogex):
        

        self.music = {
            'background': 'sounds/background.wav',
        }

        self.sounds = {
            'item': 'sounds/podnoszenie_przedmiotu.wav',
            'corridor': 'sounds/chodzenie_korytarz.wav',
            'gameover': 'sounds/Wywalenie_z_domu.wav',
            'interakcja': 'sounds/interakcja.wav',
            'game_over_better': 'sounds/game_over_better.wav',
        }
        self.music_playing = None

    def play_music(self, music_name):
    
        pygame.mixer.music.load(self.music[music_name])
        pygame.mixer.music.play(-1)
        #self.music_playing = music_name

    def play_sound(self, sound_name):
        if sound_name == 'game_over_better':
            pygame.mixer.Sound(file=self.sounds[sound_name]).set_volume(2)
        pygame.mixer.Sound(self.sounds[sound_name]).play()
        pygame.mixer.Sound(self.sounds[sound_name]).stop()