from time import sleep
class Game():
    def __init__(self, name: str):
        self.name = name
        self.contestant = 'Joe'
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
        sleep(1)
        

    def battle_phase(self):
        
        pass

    def display_winner(self):
        pass

game = Game('RPSLS')
game.display_welcome()