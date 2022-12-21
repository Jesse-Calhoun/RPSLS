from time import sleep
import random

class Ai:
    def __init__(self, name:str):
        self.choosen_gesture = 5
        self.name = name
        self.score = 0

    def choose_geture(self):
        gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.choosen_gesture = str(random.randint(0, 4))
        print()
        sleep(1)
        print(f'{self.name} has chosen {gestures[int(self.choosen_gesture)]}')
        print()
        
# ai = Ai("Jesse", 5)
# ai.choose_geture()