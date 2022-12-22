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
        while contestant_one.score < 2 and contestant_two.score < 2:
            contestant_one.choose_gesture()
            contestant_two.choose_gesture()
            if contestant_one.chosen_gesture == contestant_two.chosen_gesture:
                return self.battle_phase()
            elif contestant_one.chosen_gesture == 'Rock': 
                if contestant_two.chosen_gesture == 'Spock' or contestant_two.chosen_gesture == 'Paper':
                    self.winner = contestant_two
            elif contestant_one.chosen_gesture == 'Paper':
                if contestant_two.chosen_gesture == 'Scissors' or contestant_two.chosen_gesture == 'Lizard':
                    self.winner = contestant_two
            elif contestant_one.chosen_gesture == 'Scissors':
                if contestant_two.chosen_gesture == 'Rock' or contestant_two.chosen_gesture == 'Spock':
                    self.winner = contestant_two
                else:
                    self.winner = contestant_one
            elif contestant_one.chosen_gesture == 'Lizard':
                if contestant_two.chosen_gesture == 'Rock' or contestant_two.chosen_gesture == 'Scissors':
                    self.winner = contestant_two
            elif contestant_one.chosen_gesture == 'Spock':
                if contestant_two.chosen_gesture == 'Lizard' or contestant_two.chosen_gesture == 'Paper':
                    self.winner = contestant_two
            else:
                self.winner = contestant_one
            self.winner.score += 1
            print(f"{self.winner.name} won that round, {self.winner.name}'s score is {self.winner.score}.")

    def display_winner(self):
        print(f'{self.winner.name} has won the best of 3!')
        

# game = Game('RPSLS')
# game.run_game()
