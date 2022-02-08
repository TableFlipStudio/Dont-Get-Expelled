import pygame
from pytmx import load_pygame, TiledImageLayer, TiledTileLayer, TiledObjectGroup

class Map():
    def __init__(self, dogex):

        self.settings = dogex.settings
        self.screen  = dogex.screen
        self.character = dogex.character

        self.screen_rect = self.screen.get_rect()
        self.tmxdata = load_pygame('mapfolder/mapbetter.tmx')

        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        surface = pygame.Surface( ( self.width, self.height ) )
        self.rect = surface.get_rect()

        #self.spawn_obj = self._access_Object('objects.spawn')
        #self.character.rect.topleft = (self.spawn_obj.x, self.spawn_obj.y)

        self.rect.topleft = self.screen_rect.topleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        print(self._access_Object('collision.w20'))

        #self.mapHorizontalSpeed = self.settings.character_speed * ((self.width - self.screen_rect.width) / 2) / (self.screen_rect.width / 2 - (self.character.rect.width / 2))
        #self.mapVerticalSpeed = self.settings.character_speed * ((self.height - self.screen_rect.height) / 2) / (self.screen_rect.height / 2 - (self.character.rect.height / 2))


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

        self.width = tmxdata.width * tmxdata.tilewidth
        height = tmxdata.height * tmxdata.tileheight

        surface = pygame.Surface( ( self.width, self.height ) )

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
        
            #FIXME the loop only uses the first item; even after deleting the 'collision.w1'
            # object, it still displays on the map as the only object.  

        contents = [
            self._access_Object('collision.w1'),
            self._access_Object('collision.w2'),
            self._access_Object('collision.w3'),
            self._access_Object('collision.w4'),
            self._access_Object('collision.w5'),
            self._access_Object('collision.w6'),
            self._access_Object('collision.w7'),
            self._access_Object('collision.w8'),
            self._access_Object('collision.w9'),
            self._access_Object('collision.w10'),
            self._access_Object('collision.w11')
        ]
        return contents

    def collision(self):
        """Wykrycie kolizji między obiektami na mapie a postacią"""
        contents = self._get_all_contents()

        for obj in contents:
            if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.character.rect):
                self.character.image = pygame.image.load('images/test_character_blue.bmp')
            else:
                self.character.image = pygame.image.load('images/test_character.bmp')


    def update(self):
        """Aktualizacja położenia mapy oraz jej zawartości"""
        contents = self._get_all_contents()

        self.mapHorizontalSpeed = self.settings.character_speed * ((self.width - self.screen_rect.width) / 2) / (self.screen_rect.width / 2 - (self.character.rect.width / 2))
        self.mapVerticalSpeed = self.settings.character_speed * ((self.height - self.screen_rect.height) / 2) / (self.screen_rect.height / 2 - (self.character.rect.height / 2))


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
