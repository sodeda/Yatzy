from random import randint
import tkinter


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
        hand_label = tkinter.Label(window, text=self.current)
        c1 = tkinter.Checkbutton(window)
        c2 = tkinter.Checkbutton(window)
        c3 = tkinter.Checkbutton(window)
        c4 = tkinter.Checkbutton(window)
        c5 = tkinter.Checkbutton(window)
        c1.grid(row=3,column=0)
        c2.grid(row=3,column=1)
        c3.grid(row=3,column=2)
        c4.grid(row=3,column=3)
        c5.grid(row=3,column=4)
        hand_label.grid(row=2,column=2)
        #c1.pack(), c2.pack(), c3.pack(), c4.pack()#, c5.pack()


def test():
    turn =Turn()
    turn.roll()


if __name__ == "__main__":
    #name = raw_input("Player 1: ")
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("200x200")
    window.resizable(0,0)
    #turn = Turn()
    throw_button = tkinter.Button(window, text="Throw", command=test)
    throw_button.grid(row=1,column=2)
    window.mainloop()
