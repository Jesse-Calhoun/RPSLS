from time import sleep

class Contestant:
    def __init__(self) -> None:
        self.chosen_gesture = 5 
        self.score = 0
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        pass

    def choose_gesture(self):
        pass
    
    def display_chosen_gesture(self):
        sleep(1)
        print()
        print(f'{self.name} chose {self.chosen_gesture}')
        pass