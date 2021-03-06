import pygame
from pytmx import load_pygame, TiledImageLayer, TiledTileLayer, TiledObjectGroup

class Map():
    def __init__(self, dogex):

        self.settings = dogex.settings
        self.screen  = dogex.screen

        self.character = dogex.character

        self.screen_rect = self.screen.get_rect()
        self.tmxdata = load_pygame('mapfolder/test.tmx') # Informacje o mapie wczytane z pliku Tiled (.tmx)

        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        surface = pygame.Surface((self.width, self.height))
        self.rect = surface.get_rect()

        self.image = pygame.image.load('images/minimap.png')
        self.image = pygame.transform.scale(self.image, (self.settings.screen_width, self.settings.screen_height))

        self.active = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Położenie mapy przed ostatnim wywołaniem update() Potrzebne to obliczania kierunku
        # kolizji, przesuwania przedmiotów i paru innych rzeczy
        self.last_x = 0
        self.last_y = 0

    def _access_Object(self, path):
        """Uzyskanie dostępu do dowolnego obiektu lub warstwy i zwrócenie go
        Atrybut path musi być ciągiem tesktowym (string) i wskazywać ścieżkę
        dostępu do obiektu, rozdzielając segmenty kropkami np.
        'collision.walls.wall_1'"""
        path = path.split(sep='.')
        target = self._go_through_path(path, self.tmxdata.visible_layers)
        return target

    def _go_through_path(self, path, parent, path_inx=0):  #Path Index
        """Główna podfunkcja metody _access_Object(). Rekurencyjnie
        przeszukuje self.tmxdata szukając warstw i obiektów podanych
        w ścieżce dostępu"""
        for instance in parent:
            if instance.name == path[path_inx]:
                #pathToGo sprawdza, czy argument path wskazuje na obecność
                # dalszych obiektów do znalezienia (czy nal liście path jest
                #coś jeszcze za obiektem wzkazanym przez path_inx)
                pathToGo = len(path) - 1 > path_inx
                if pathToGo: #Jeśli tak, odpal algorytm jeszcze raz i szukaj następnego elementu ścieżki
                    path_inx += 1
                    child = self._go_through_path(path, instance, path_inx)
                    return child
                else: #Jeśli nie, zwróc aktualnie wskazany obiekt, bo to jego szukamy
                    return instance

    def set_spawn(self, instance):
        """Umieszczenie postaci na spawnie (ustawianym w edytorze mapy)"""
        if instance == "player":
            obj = self._access_Object('objects.spawn')
            self.character.rect.center = (self.from_map_to_screen_ratio(obj.x, obj.y))

    def from_map_to_screen_ratio(self, x, y):
        """Przeskalowanie wymiarów: wymiary mapy na wymiary ekranu"""
        new_x = ((self.settings.screen_width * x) / self.width)
        new_y = ((self.settings.screen_height * y) / self.height)-30
        return new_x,new_y

    def from_screen_to_map_ratio(self, x=0, y=0):
        """Przeskalowanie wymiarów: wymiary ekranu na wymiary mapy"""
        new_x = ((self.width * x) / self.settings.screen_width)
        new_y = ((self.height * y) / self.settings.screen_height)

        if x==0:
            return new_y

        elif y==0:
            return new_x

        else:
            return new_x,new_y

    def map_setup(self, tmxdata):
        """Utworzenie obrazu mapy, przez scalenie wszystkich warstw"""
        width = tmxdata.width * tmxdata.tilewidth
        height = tmxdata.height * tmxdata.tileheight

        surface = pygame.Surface( ( width, height ) )

        for layer in tmxdata.visible_layers:
            if isinstance(layer, TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, ( x * tmxdata.tilewidth, y * tmxdata.tileheight ))
        return surface


    def _get_all_contents(self, parameter='all'):
        """Zwraca listę wszystkich dzieci podanej warstwy"""

        if parameter == 'all':
            contents = []
            for layer in self.tmxdata.visible_layers:
                if isinstance(layer, TiledObjectGroup):
                    contents += [obj for obj in layer]

        # Przesuwanie tylko tych obiektów, które nigdy nie zmieniają swojego
        # położenia względem mapy. Był problem z NPC i itemami, których położenie można zmienić - nakładające
        # się dane z plików zapisu oraz pliku mapy powodowały olbrzymie przesunięcia
        # tych obiektów, czyli praktycznie ich usunięcie po wcyztaniu zapisu.
        elif parameter == 'static_only':
            contents = []
            layers = ['collision', 'objects', 'exit-areas']
            for layer in layers:
                layer = self._access_Object(layer)
                contents += [obj for obj in layer]

        else:
            layer = self._access_Object(parameter)
            contents = [obj for obj in layer]

        return contents

    def display_mini_map(self):
        self.screen.blit(self.image, self.screen_rect)
        #pygame.draw.rect(self.screen, ((0,255,0)), self.screen_rect)

    def collision(self):
        """Wykrycie typu kolizj między obiektami na mapie a postacią"""
        contents = self._get_all_contents('collision')

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


    def update(self, parameter):
        """Aktualizacja położenia mapy oraz jej zawartości"""

        mapHorizontalSpeed = ((self.width - self.screen_rect.width) / 2) / (self.screen_rect.width / 2 - (self.character.rect.width / 2)) * -1
        mapVerticalSpeed = ((self.height - self.screen_rect.height) / 2) / (self.screen_rect.height / 2 - (self.character.rect.height / 2)) * -1

        contents = self._get_all_contents(parameter)

        self.last_x = self.x
        self.last_y = self.y

        '''Przesuwanie mapy ze względu na położenie postaci'''
        self.x = self.character.x * mapHorizontalSpeed
        self.y = self.character.y * mapVerticalSpeed

        '''Przesuwanie objektów kolizji w zależności od ostatniego położenia mapy'''
        for obj in contents:
            if self.last_x > self.x:
                obj.x -= (self.last_x - self.x)
            else:
                obj.x += (self.x - self.last_x)

            if self.last_y > self.y:
                obj.y -= (self.last_y - self.y)
            else:
                obj.y += (self.y - self.last_y)

        #Aktualizacja położenia prostokąta na podstawie self.x i self.y
        self.rect.x = self.x
        self.rect.y = self.y
