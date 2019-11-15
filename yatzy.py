from random import randint


class Player:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self):
        self.round = 0
        self.players = []

    def start(self):
        pass

class Scores:
    def __init__(self):
        pass


class Turn:
    def __init__(self):
        self.rolls = 0
        self.hand  = []
        self.current = []


    def roll(self):
        for i in range(0,6-len(self.hand)):
            self.current.append(randint(1,6))
        self.rolls += 1
        print self.current


if __name__ == "__main__":
    #name = raw_input("Player 1: ")
    turn = Turn()
    turn.roll()
