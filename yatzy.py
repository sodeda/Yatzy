import tkinter
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
        self.hand  = [0, 0, 0, 0, 0]
        self.current = []
        self.vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.cl1 = tkinter.Label(window, text="").grid(row=2,column=0)
        self.cl2 = tkinter.Label(window, text="").grid(row=2,column=1)
        self.cl3 = tkinter.Label(window, text="").grid(row=2,column=2)
        self.cl4 = tkinter.Label(window, text="").grid(row=2,column=3)
        self.cl5 = tkinter.Label(window, text="").grid(row=2,column=4)
        self.cbuttons = [tkinter.Checkbutton(window, variable=self.vars[0]).grid(row=3,column=0),
        tkinter.Checkbutton(window, variable=self.vars[1]).grid(row=3,column=1),
        tkinter.Checkbutton(window, variable=self.vars[2]).grid(row=3,column=2),
        tkinter.Checkbutton(window, variable=self.vars[3]).grid(row=3,column=3),
        tkinter.Checkbutton(window, variable=self.vars[4]).grid(row=3,column=4)]

    def roll(self):
        if self.rolls < 3:
            if not self.vars[0].get():
                nro = randint(1,6)
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=0)
                self.hand[0] = nro
            if not self.vars[1].get():
                nro = randint(1,6)
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=1)
                self.hand[1] = nro
            if not self.vars[2].get():
                nro = randint(1,6)
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=2)
                self.hand[2] = nro
            if not self.vars[3].get():
                nro = randint(1,6)
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=3)
                self.hand[3] = nro
            if not self.vars[4].get():
                nro = randint(1,6)
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=4)
                self.hand[4] = nro

            self.rolls += 1

        else:
            

        #self.cl1 = tkinter.Label(window, text=self.current[0]).grid(row=2,column=0)
        #self.cl2 = tkinter.Label(window, text=self.current[1]).grid(row=2,column=1)
        #self.cl3 = tkinter.Label(window, text=self.current[2]).grid(row=2,column=2)
        #self.cl4 = tkinter.Label(window, text=self.current[3]).grid(row=2,column=3)
        #self.cl5 = tkinter.Label(window, text=self.current[4]).grid(row=2,column=4)

        #cl1.pack(padx=5, side=tkinter.LEFT)
        #cl2.pack(padx=5, side=tkinter.LEFT)
        #cl3.pack(padx=5, side=tkinter.LEFT)
        #cl4.pack(padx=5, side=tkinter.LEFT)
        #cl5.pack(padx=5, side=tkinter.LEFT)

    def test(self):
        #print(self.vars[0].get())
        print(self.hand)
        pass


def test():
    turn.roll()
    turn.test()


if __name__ == "__main__":
    #name = raw_input("Player 1: ")
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("200x200")
    window.resizable(0,0)
    turn = Turn()
    throw_button = tkinter.Button(window, text="Throw", command=test)
    throw_button.grid(row=1,column=2)
    #throw_button.pack()
    window.mainloop()
