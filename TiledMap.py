import pygame
from pytmx import load_pygame, TiledImageLayer, TiledTileLayer

class Map():
    def __init__(self, dogex):

        self.settings = dogex.settings
        self.screen  = dogex.screen
        self.character = dogex.character
        
        self.screen_rect = self.screen.get_rect()
        self.tmxdata = load_pygame('mapfolder/test.tmx')

        width = self.tmxdata.width * self.tmxdata.tilewidth
        height = self.tmxdata.height * self.tmxdata.tileheight

        surface = pygame.Surface( ( width, height ) )
        self.rect = surface.get_rect()
        
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def map_can_move_right(self):
        output = (
            self.moving_right 
            and 
            self.character.rect.left > self.rect.left
            and
            self.rect.left < self.screen_rect.left

        )
        return output
    
    def map_can_move_left(self):
        output = (
            self.moving_left 
            and 
            self.character.rect.right < self.rect.right
            and
            self.rect.right > self.screen_rect.right

        )
        return output
    
    def map_can_move_up(self):
        output = (
            self.moving_up 
            and 
            self.character.rect.bottom < self.rect.bottom
            and
            self.rect.bottom > self.screen_rect.bottom

        )
        return output

    def map_can_move_down(self):
        output = (
            self.moving_down 
            and 
            self.character.rect.top > self.rect.top
            and 
            self.rect.top < self.screen_rect.top

        )
        return output
    

    def map_setup(self, tmxdata):

        width = tmxdata.width * tmxdata.tilewidth
        height = tmxdata.height *tmxdata.tileheight

        surface = pygame.Surface( ( width, height ) )

        for layer in tmxdata.visible_layers:
            if isinstance(layer, TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        #image = tmxdata.get_tile_image(x, y, layer)
                        surface.blit(tile, ( x * tmxdata.tilewidth, y * tmxdata.tileheight ))
        return surface

    def update(self):
        if self.map_can_move_right():
            if self.character.can_move_left():
                self.x += self.settings.character_speed / 2
            else:
                self.x += self.settings.character_speed


        if self.map_can_move_left():
            if self.character.can_move_right():
                self.x -= self.settings.character_speed / 2
            else:
                self.x -= self.settings.character_speed


        if self.map_can_move_up():
            if self.character.can_move_down():
                self.y -= self.settings.character_speed / 2
            else:
                self.y -= self.settings.character_speed


        if self.map_can_move_down():
            if self.character.can_move_up():
                self.y += self.settings.character_speed / 2
            else:
                self.y += self.settings.character_speed



        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y