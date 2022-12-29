from time import sleep
from contestant import Contestant
import random


class Human(Contestant):
    def __init__(self):
        super().__init__()
        self.name = ''

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
        self.chosen_gesture = input(f'{self.name} what is your chosen gesture? ')
        while True:
            if self.chosen_gesture == '0':
                self.chosen_gesture = self.gestures[int(self.chosen_gesture)]
                break
            elif self.chosen_gesture == '1':
                self.chosen_gesture = self.gestures[int(self.chosen_gesture)]
                break
            elif self.chosen_gesture == '2':
                self.chosen_gesture = self.gestures[int(self.chosen_gesture)]
                break
            elif self.chosen_gesture == '3':
                self.chosen_gesture = self.gestures[int(self.chosen_gesture)]
                break
            elif self.chosen_gesture == '4':
                self.chosen_gesture = self.gestures[int(self.chosen_gesture)]
                break
            else:
                print("Wrong input! Please use 0, 1, 2, 3, or 4 to select a gesture.")
                self.chosen_gesture = (input('Please pick new gesture. '))
            

    def display_chosen_gesture(self):
        super().display_chosen_gesture()
        