from time import sleep
from contestant import Contestant
from human import Human
from ai import Ai
class Game():
    def __init__(self, name: str):
        self.name = name
        self.contestant_one = Human()
        self.contestant_two = Ai('Joe')
        self.contestant_three = Human()
        self.winner = ''
        pass
    
    def run_game(self):
        self.display_welcome()
        self.determine_game_type()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        print()
        print(f'Welcome to {self.name}')
        print()
        #sleep(1)
    
    def determine_game_type(self):
        self.contestant_one.give_name()
        response = input(f'{self.contestant_one.name}, what game type would you like? Pick 1 for Single player, pick 2 for multiplayer. ')
        if response == '1':
            self.contestant_two = self.contestant_two
            self.contestant_two.give_name()
        else:
            self.contestant_two = self.contestant_three
            self.contestant_two.give_name()
            

    def battle_phase(self):
        # self.contestant_one = Human()
        # self.contestant_two = Ai('Joe')
        #self.contestant_one.give_name()
        round_count = 1
        print(self.contestant_one.name)
        print(self.contestant_two.name)
        while self.contestant_one.score < 2 and self.contestant_two.score < 2:
            print(f'Round: {round_count}')
            self.contestant_one.choose_gesture()
            self.contestant_two.choose_gesture()
            if self.contestant_one.chosen_gesture == self.contestant_two.chosen_gesture:
                return self.battle_phase()
            elif self.contestant_one.chosen_gesture == 'Rock': 
                if self.contestant_two.chosen_gesture == 'Spock' or self.contestant_two.chosen_gesture == 'Paper':
                    self.winner = self.contestant_two
            elif self.contestant_one.chosen_gesture == 'Paper':
                if self.contestant_two.chosen_gesture == 'Scissors' or self.contestant_two.chosen_gesture == 'Lizard':
                    self.winner = self.contestant_two
            elif self.contestant_one.chosen_gesture == 'Scissors':
                if self.contestant_two.chosen_gesture == 'Rock' or self.contestant_two.chosen_gesture == 'Spock':
                    self.winner = self.contestant_two
                else:
                    self.winner = self.contestant_one
            elif self.contestant_one.chosen_gesture == 'Lizard':
                if self.contestant_two.chosen_gesture == 'Rock' or self.contestant_two.chosen_gesture == 'Scissors':
                    self.winner = self.contestant_two
            elif self.contestant_one.chosen_gesture == 'Spock':
                if self.contestant_two.chosen_gesture == 'Lizard' or self.contestant_two.chosen_gesture == 'Paper':
                    self.winner = self.contestant_two
            else:
                self.winner = self.contestant_one
            self.winner.score += 1
            round_count += 1
            print(f"{self.winner.name} won that round, {self.winner.name}'s score is {self.winner.score}.")

    def display_winner(self):
        print(f'{self.winner.name} has won the best of 3!')
        

# game = Game('RPSLS')
# game.run_game()
