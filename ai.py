from time import sleep
import random
from contestant import Contestant

class Ai(Contestant):
    def __init__(self, name:str):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print()
           
        
    def display_chosen_gesture(self):
        super().display_chosen_gesture()
        
