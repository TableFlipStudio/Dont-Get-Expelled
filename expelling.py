import pygame

class Expelling():
    """Klasa nadzoruje mechanikę wyrzucania ze szkoły"""

    def __init__(self, dogex):
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect
        self.settings = dogex.settings

        self.font = pygame.font.SysFont(None, 32)
        self.text_color = (255, 255, 255)

        # Licznik przewinień - jak dużo niedobrych rzeczy można zrobić zanim
        # zostanie się wyrzuconym ze szkoły
        self.fault_counter = self.settings.faults_to_be_expelled

        # Lista przewinień - każde popełnione przewinienie jest dodawane
        # do tej listy (wartość numeryczna oznaczająca powagę przewinienia),
        # zaś lista jest opróżniana przez check_fault_committed
        self.faults = []

        self._update_msg()

    def _update_msg(self):
        """Utworzenie obrazka licznika na podstawie self.fault_counter."""
        self.cntr_msg = f'Faults to be expelled: {self.fault_counter}'
        self.image = self.font.render(self.cntr_msg, True,
            self.text_color, None)
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen_rect.bottomright

    def check_fault_committed(self):
        """Sprawdza, czy zostało popełnione jakieś przewinienie, jeśli tak,
        uaktualnia licznik"""
        for fault in self.faults[:]:
            self.fault_counter -= fault
            self.faults.remove(fault)
        self._update_msg()

    def check_expelled(self):
        """Sprawdza, czy, licznik dopuszczalnych przewinień się wyczerpał,
        jeśli tak, zwraca True aby zatrzymać grę"""
        if self.fault_counter <= 0:
            return True

    def blitmsg(self):
        self.screen.blit(self.image, self.rect)
