class Settings():
    """Klasa przechowująca ustawienia gry"""

    def __init__(self):
        #Ustawienia dotyczące ekranu
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (0, 0, 0)

        #Ustawienia dotyczące postaci głównej
        self.character_speed = 1
        self.fps = 60

        #Ustawienia dotyczące slotów w ekwipunku
        self.slot_width = 80
        self.slot_height = 80
        self.slot_color = (115, 115, 115)

        #Ustawienia dotyczące NPC
        self.npc_speed = 1
        self.npc_bounce_at = 20
