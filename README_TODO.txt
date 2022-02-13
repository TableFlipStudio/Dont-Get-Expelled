Parę rad dotyczących kodu, bo nie chcę ci grzebać w twojej działce:

1. Metoda _collision_type() jest absolutnie zbędna. Zamiast

def collision():
    if _collision_type() == "top":
        <code>
    if _collision_type() == "bottom":
        <code>

wystarczy

def collision():
    if _collision_top():
        <code>
    if _collision_bottom():
        <code>

a samo _collision_type() posłać w otchłań.

2. Metoda _get_all_contents() jest absolutnie koszmarna a będzie jeszcze
gorsza jak się pojawi więcej obiektów. Zamiast 3 tysięcy wywołań _access_Object()
powinno wystarczyć tyle

def _get_all_contents():
    layer = _access_Object('collision')
    contents = [obj for obj in layer]

Nwm, czy znasz listy składane, jak coś to masz to w podręczniku w rozdziale 4
na stronie 103. Wartością zwrotną będzie lista wszystkich obiektów w grupie
collision.

3. Ten problem z tym że raz da się wejść w ścianę a drugi nie na oko
wyglada jak stary dobry numer z błędem przesuwania prostokątów.
Wysoce zalecane jest zrobienie kolorowych prostokątów testowych, które
będą śledziły nasze hitboxy ścian (tak jak to było na mapie testowej,
dzięki czemu znaleźliśmy ten błąd)
