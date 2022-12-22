from time import sleep
import random
from contestant import Contestant

class Ai(Contestant):
    def __init__(self, name:str):
        super().__init__()
        self.name = name
        self.score = 0

    def choose_gesture(self):
        gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = str(random.randint(0, 4))
        print()
        # sleep(1)
        self.chosen_gesture = gestures[int(self.chosen_gesture)]
        print(f'{self.name} has chosen {self.chosen_gesture}')
        print()
        
# ai = Ai("Jesse", 5)
# ai.choose_geture()