import pygame

class Music():

    def __init__(self, dogex):
        self.character = dogex.character

        self.corridor = pygame.mixer.Sound('sounds/chodzenie_korytarz.wav')
        self.corridor.set_volume(0)
        self.corridor.play(-1)
    

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
        self.sound_playing = None
        self.walkind_sound = False

    def play_music(self, music_name, volume=0.2):
        """puszcza muzykę

        Args:
            music_name (str): nazwa muzyki
        """
    
        pygame.mixer.music.load(self.music[music_name])
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        #self.music_playing = music_name

    def play_sound(self, sound_name, volume=0.2):
        """puszcza dzwięk

        Args:
            sound_name (str): nazwa dzwieku
        """
        if sound_name == 'game_over_better':
            pygame.mixer.Sound(file=self.sounds[sound_name]).set_volume(2)
        
        pygame.mixer.Sound(file=self.sounds[sound_name]).set_volume(volume)
            
        pygame.mixer.Sound(self.sounds[sound_name]).play()
        pygame.mixer.Sound(self.sounds[sound_name]).stop()

    def check_sounds(self, sound_name, state='play'):
        """sprawdza czy dany dzwiek jest włączony i włącza go

        Args:
            sound_name (str): nazwa dzwieku
            state (str, optional): czy ma dżwięk zatrzymać sprawdza. Defaults to 'play'. #polska jenzyk trudna być
        """
        sound = pygame.mixer.Sound(self.sounds[sound_name])
        
        if self.sound_playing == None:
            sound.play(-1)
            self.sound_playing = sound_name
        
        elif state == 'stop':
            sound.stop()
            self.sound_playing = None

        elif self.sound_playing == sound_name:
            sound.stop()
            self.sound_playing = None
            
    def check_walking_sound(self):
        """sprawdza czy dzwiek chodzenia jest włączony i włącza go"""
        
        if self.character.can_move_down() or self.character.can_move_up() or self.character.can_move_left() or self.character.can_move_right():
            self.corridor.set_volume(1)
        elif not (self.character.can_move_down() and self.character.can_move_up() and self.character.can_move_left() and self.character.can_move_right()):
            self.corridor.set_volume(0)
            
        
        
        
        
        
        
        
        
        
        
            
        