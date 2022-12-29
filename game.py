from time import sleep
from contestant import Contestant
from human import Human
from ai import Ai


class Game():
    def __init__(self, name: str):
        self.name = name
        self.contestant_one = Human()
        self.contestant_two = Ai('AI')
        self.contestant_three = Human()
        self.winner = ''
        self.current_round = 1
        pass
    
    def run_game(self):
        self.display_welcome()
        self.determine_game_type()
        while self.contestant_one.score < 2 and self.contestant_two.score < 2:
            print(f'Round: {self.current_round}')
            self.choose_gestures()
            self.compare_gestures()
            self.display_round_winner()
        self.display_game_winner()
        pass

    def display_welcome(self):
        print(' ')
        #sleep(1)
        print(f'Welcome to {self.name}.')
        #sleep(1)
        print('Explanation of game rules:')
        #sleep(1)
        print('Rock crushes Scissors')
        #sleep(1)
        print('Scissors cuts Paper')
        #sleep(1)
        print('Paper covers Rock')
        #sleep(1)
        print('Rock crushes Lizard')
        #sleep(1)
        print('Lizard poisons Spock')
        #sleep(1)
        print('Spock smashes Scissors')
        #sleep(1)
        print('Scissors decapitates Lizard')
        #sleep(1)
        print('Lizard eats Paper')
        #sleep(1)
        print('Paper disproves Spock')
        #sleep(1)
        print('Spock vaporizes Rock')
        #sleep(1)
        print(' ')
    
    def determine_game_type(self):
        self.contestant_one.give_name()
        response = input(f'Player 1 {self.contestant_one.name}, what game type would you like? Pick 1 for Single player, pick 2 for multiplayer. ')
        while True:
            if response == '1':
                self.contestant_two = self.contestant_two
                print(f'{self.contestant_one.name} has chosen to play against {self.contestant_two.name}!')
                print(" ")
                break
            elif response == '2':
                self.contestant_two = self.contestant_three
                self.contestant_two.give_name()
                print(f'Player 2: {self.contestant_two.name}') 
                print(' ')        
                break 
            else: 
                print('Wrong input! Please select 1 for single player or 2 for multiplayer.')
                response = input(f'Player 1 {self.contestant_one.name}, what game type would you like? Pick 1 for Single player, pick 2 for multiplayer. ')

    def choose_gestures(self):

            self.contestant_one.choose_gesture()
            self.contestant_one.display_chosen_gesture()
            self.contestant_two.choose_gesture()
            self.contestant_two.display_chosen_gesture()
            
    def compare_gestures(self):
            if self.contestant_one.chosen_gesture == self.contestant_two.chosen_gesture:
                print(f'Round: {self.current_round}')
                self.choose_gestures()
                return self.compare_gestures()
            elif self.contestant_one.chosen_gesture == 'Rock': 
                if self.contestant_two.chosen_gesture == 'Spock' or self.contestant_two.chosen_gesture == 'Paper':
                    self.winner = self.contestant_two
                    self.current_round += 1
                else:
                    self.winner = self.contestant_one
                    self.current_round += 1
            elif self.contestant_one.chosen_gesture == 'Paper':
                if self.contestant_two.chosen_gesture == 'Scissors' or self.contestant_two.chosen_gesture == 'Lizard':
                    self.winner = self.contestant_two
                    self.current_round += 1
                else:
                    self.winner = self.contestant_one
                    self.current_round += 1
            elif self.contestant_one.chosen_gesture == 'Scissors':
                if self.contestant_two.chosen_gesture == 'Rock' or self.contestant_two.chosen_gesture == 'Spock':
                    self.winner = self.contestant_two
                    self.current_round += 1
                else:
                    self.winner = self.contestant_one
                    self.current_round += 1
            elif self.contestant_one.chosen_gesture == 'Lizard':
                if self.contestant_two.chosen_gesture == 'Rock' or self.contestant_two.chosen_gesture == 'Scissors':
                    self.winner = self.contestant_two
                    self.current_round += 1
                else:
                    self.winner = self.contestant_one
                    self.current_round += 1
            elif self.contestant_one.chosen_gesture == 'Spock':
                if self.contestant_two.chosen_gesture == 'Lizard' or self.contestant_two.chosen_gesture == 'Paper':
                    self.winner = self.contestant_two
                    self.current_round += 1
                else:
                    self.winner = self.contestant_one
                    self.current_round += 1
            self.winner.score += 1
            
            
    def display_round_winner(self):
        sleep(1)
        print(f"{self.winner.name} won that round, {self.winner.name}'s score is {self.winner.score}.")

    def display_game_winner(self):
        sleep(1)
        print(f'{self.winner.name} has won the best of 3!')
        sleep(1)
        response = input('Would you like to play the game again? y or n? ')
        if response == 'y':
            self.contestant_one.score = 0
            self.contestant_two.score = 0
            self.contestant_three.score = 0
            self.current_round = 1
            self.contestant_two = Ai('AI')
            self.run_game()
            

        


