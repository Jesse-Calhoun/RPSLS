from time import sleep
from contestant import Contestant
from human import Human
from ai import Ai
class Game():
    def __init__(self, name: str):
        self.name = name
        self.contestant = ''
        self.contesant_power = 0
        self.winner = ''
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
        if contestant_one.chosen_gesture == contestant_two.chosen_gesture:
            return self.battle_phase()
        elif contestant_one.chosen_gesture == 'Rock': 
            if contestant_two.chosen_gesture == 'Spock' or contestant_two.chosen_gesture == 'Paper':
                self.winner = contestant_two.name
                return self.winner
        elif contestant_one.chosen_gesture == 'Paper':
            if contestant_two.chosen_gesture == 'Scissors' or contestant_two.chosen_gesture == 'Lizard':
                self.winner = contestant_two.name
                return self.winner
        elif contestant_one.chosen_gesture == 'Scissors':
            if contestant_two.chosen_gesture == 'Rock' or contestant_two.chosen_gesture == 'Spock':
                self.winner = contestant_two.name
                return self.winner
            else:
                self.winner = contestant_one.name
                return self.winner

        elif contestant_one.chosen_gesture == 'Lizard':
            if contestant_two.chosen_gesture == 'Rock' or contestant_two.chosen_gesture == 'Scissors':
                self.winner = contestant_two.name
                return self.winner
        elif contestant_one.chosen_gesture == 'Spock':
            if contestant_two.chosen_gesture == 'Lizard' or contestant_two.chosen_gesture == 'Paper':
                self.winner = contestant_two.name
                return self.winner
        else:
            self.winner = contestant_one.name
            return self.winner
        #not getting winner to print.
        print(self.winner)
        
        

        # print(contestant_two.chosen_gesture)
        # print(contestant_one.name)
        # winner = 
        

    def display_winner(self):
        pass

game = Game('RPSLS')
game.display_welcome()
game.battle_phase()