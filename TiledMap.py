import pygame
from pytmx import load_pygame, TiledImageLayer, TiledTileLayer, TiledObjectGroup

class Map():
    def __init__(self, dogex):

        self.settings = dogex.settings
        self.screen  = dogex.screen
        
        self.character = dogex.character    

        self.screen_rect = self.screen.get_rect()
        self.tmxdata = load_pygame('mapfolder/testmap.tmx')

        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        surface = pygame.Surface( ( self.width, self.height ) )
        self.rect = surface.get_rect()

        self.rect.topleft = self.screen_rect.topleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.mapHorizontalSpeed = self.settings.character_speed * ((self.width - self.screen_rect.width) / 2) / (self.screen_rect.width / 2 - (self.character.rect.width / 2))
        self.mapVerticalSpeed = self.settings.character_speed * ((self.height - self.screen_rect.height) / 2) / (self.screen_rect.height / 2 - (self.character.rect.height / 2))

    def _access_Object(self, path):
        """Uzyskanie dostępu do dowolnego obiektu lub warstwy i zwrócenie go
        Atrybut path musi być ciągiem tesktowym (string) i wskazywać ścieżkę
        dostępu do obiektu, rozdzielając segmenty kropkami np.
        'collision.walls.wall_1'"""
        path = path.split(sep='.')
        target = self._go_through_path(path, self.tmxdata.visible_layers)
        return target

    def _go_through_path(self, path, instance, path_inx=0):  #Path Index
        """Główna podfunkcja metody _access_Object(). Rekurencyjnie
        przeszukuje self.tmxdata szukając warstw i obiektów podanych
        w ścieżce dostępu"""
        for subinstance in instance:
            if subinstance.name == path[path_inx]:
                #pathToGo sprawdza, czy argument path wskazuje na obecność
                # dalszych obiektów do znalezienia (czy nal liście path jest
                #coś jeszcze za obiektem wzkazanym przez path_inx)
                pathToGo = len(path) - 1 > path_inx
                if pathToGo: #Jeśli tak, odpal algorytm jeszcze raz i szukaj następnego elementu ścieżki
                    path_inx += 1
                    child = self._go_through_path(path, subinstance, path_inx)
                    return child
                else: #Jeśli nie, zwróc aktualnie wskazany obiekt, bo to jego szukamy
                    return subinstance

    def map_can_move_right(self):
        output = (
            self.moving_right
            and
            self.rect.left < self.screen_rect.left

        )
        return output

    def map_can_move_left(self):
        output = (
            self.moving_left
            and
            self.rect.right > self.screen_rect.right

        )
        return output

    def map_can_move_up(self):
        output = (
            self.moving_up
            and
            self.rect.bottom > self.screen_rect.bottom

        )
        return output

    def map_can_move_down(self):
        output = (
            self.moving_down
            and
            self.rect.top < self.screen_rect.top

        )
        return output

    def map_setup(self, tmxdata):

        width = tmxdata.width * tmxdata.tilewidth
        height = tmxdata.height * tmxdata.tileheight

        surface = pygame.Surface( ( width, height ) )

        for layer in tmxdata.visible_layers:
            if isinstance(layer, TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        #image = tmxdata.get_tile_image(x, y, layer)
                        surface.blit(tile, ( x * tmxdata.tilewidth, y * tmxdata.tileheight ))
        return surface

    def _get_all_contents(self):
        """Zwraca listę wszystkich obiektów na mapie, pomocnicza do update()"""
        layer = self._access_Object('collision')
        contents = [obj for obj in layer]
        return contents

    def collision(self):
        """Wykrycie typu kolizj między obiektami na mapie a postacią"""
        contents = self._get_all_contents()
        

        for obj in contents:
            self.coll_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)

            if (self.coll_rect).colliderect(self.character.rect):
                
                if abs(self.character.rect.top - self.coll_rect.bottom) < self.settings.collision_tollerance and self.character.moving_up:
                    self.character.moving_up = False
                    self.moving_down = False
                
                if abs(self.character.rect.bottom - self.coll_rect.top) < self.settings.collision_tollerance and self.character.moving_down:
                    self.character.moving_down = False
                    self.moving_up = False
                
                if abs(self.character.rect.left - self.coll_rect.right) < self.settings.collision_tollerance and self.character.moving_left:
                    self.character.moving_left = False
                    self.moving_right = False

                if abs(self.character.rect.right - self.coll_rect.left) < self.settings.collision_tollerance and self.character.moving_right:
                    self.character.moving_right = False
                    self.moving_left = False
            

    def update(self):
        """Aktualizacja położenia mapy oraz jej zawartości"""

        self.mapHorizontalSpeed = self.settings.character_speed * ((self.width - self.screen_rect.width) / 2) / (self.screen_rect.width / 2 - (self.character.rect.width / 2))
        self.mapVerticalSpeed = self.settings.character_speed * ((self.height - self.screen_rect.height) / 2) / (self.screen_rect.height / 2 - (self.character.rect.height / 2))

        contents = self._get_all_contents()

        if self.map_can_move_right():
            self.x += self.mapHorizontalSpeed
            for object in contents:
                object.x += self.mapHorizontalSpeed

        if self.map_can_move_left():
            self.x -= self.mapHorizontalSpeed
            for object in contents:
                object.x -= self.mapHorizontalSpeed

        if self.map_can_move_up():
            self.y -= self.mapVerticalSpeed
            for object in contents:
                object.y -= self.mapVerticalSpeed

        if self.map_can_move_down():
            self.y += self.mapVerticalSpeed
            for object in contents:
                object.y += self.mapVerticalSpeed

        
        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y
