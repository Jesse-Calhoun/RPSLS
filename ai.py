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
        self.chosen_gesture = random.choice(gestures)
        print()
        sleep(1)
        print(f'{self.name} has chosen {self.chosen_gesture}')
        print()
        
