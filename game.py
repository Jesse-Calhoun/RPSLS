from time import sleep
from contestant import Contestant
from human import Human
from ai import Ai
class Game():
    def __init__(self, name: str):
        self.name = name
        self.contestant = ''
        self.contesant_power = 0
        pass
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        print()
        print('Welcome to RPSLS')
        print()
        #sleep(1)
        

    def battle_phase(self):
        contestant_one = Human()
        contestant_two = Ai('Joe')
        contestant_one.give_name()
        contestant_one.choose_gesture()
        contestant_two.choose_gesture()
        # print(contestant_two.chosen_gesture)
        # print(contestant_one.name)
        

    def display_winner(self):
        pass

game = Game('RPSLS')
game.display_welcome()
game.battle_phase()