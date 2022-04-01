import pygame

class Music():

    def __init__(self, dogex):
        

        self.music = {
            'background': 'sounds/background.wav',
        }

        self.sounds = {
            'item': 'sounds/podnoszenie_przedmiotu.wav',
            'corridor': 'sounds/chodzenie_korytarz.wav',
            'gameover': 'sounds/gameover.wav',
            'interaction': 'sounds/interakcja.wav',
        }
        self.music_playing = None

    def play_music(self, music_name):
        if self.music_playing == music_name:
            return
        else:
            pygame.mixer.music.load(self.music[music_name])
            pygame.mixer.music.play(-1)
            self.music_playing = music_name

    def play_sound(self, sound_name):
        pygame.mixer.Sound(self.sounds[sound_name]).play()