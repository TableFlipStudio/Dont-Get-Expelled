Jedną z opcji naprawienia tego błędu jest stworzenie funkcji
_update_content(), która będzie używałą metody _access_Object() (czyli
_access_WallObject() po przerobieniu), żeby dobrać się do każdego obiektu
po kolei i  zmienić jego parametry X i Y

Coś jak

def _update_content(self):
     walls = _access_Object('collision.walls')

     if <warunki ruchu w górę>:
        walls.y -= 1

      etc.        
