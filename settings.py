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

        self.collision_tollerance = 32

        #Ustawienia dotyczące slotów w ekwipunku
        self.slot_width = 80
        self.slot_height = 80
        self.slot_color = (115, 115, 115)

        #Ustawienia dotyczące NPC
        self.npc_speed = 1
        self.npc_bounce_at = 20
        self.npc_images = {
            'test_npc': 'test_npc'
        }

        #Ustawienia dotyczące okna dialogowego
        self.window_color = (128, 141, 146)
        self.tab_width = self.screen_width // 2
        self.tab_height = self.screen_height // 4
        self.tab_color = (255, 255, 255)
        self.text_color = (0, 0, 0)

        self.tab_Xpos = self.screen_width // 4
        self.tab_Ypos = self.screen_height // 4
        self.answ_tab_Xpos = self.tab_Xpos
        self.answ_tab_Ypos = self.screen_height * 0.6

        # Ustawienia dotyczące przycisków zapisu i resetu
        self.button_size = (self.screen_width / 4, self.slot_height)
        self.button_color = (0, 255, 0)
        self.button_space = 1.5 * self.slot_height # Pusta przestrzeń między przyciskami
