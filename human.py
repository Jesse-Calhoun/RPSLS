from time import sleep

class Human:
    def __init__(self):
        self.chosen_gesture = 5
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

        pass

# human = Human()
# human.give_name()
