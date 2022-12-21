from time import sleep
from contestant import Contestant
import random


class Human(Contestant):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.score = 0
        pass

    def give_name(self):
        print()
        sleep(1)
        self.name = input('What is your name? ')
        print()
        sleep(1)
        return self.name

    def choose_gesture(self):
        print()
        sleep(1)
        print('''
        Choose 0 for Rock
        Choose 1 for Paper
        Choose 2 for Scissors
        Choose 3 for Lizard
        Choose 4 for Spock 
        ''')
        gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        list = range(0, len(gestures)-1)
        
        while True: #  if is failing us!!
            self.chosen_gesture = int(input('What is your chosen gesture? '))
            if  self.chosen_gesture != list:
                print("Wrong input!")
                continue
        

    

human = Human()
human.give_name()
human.choose_gesture()
