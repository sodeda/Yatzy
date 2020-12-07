import tkinter
from random import randint


def count(hand, nro):
    return len([x for x in hand if x == nro])


def summa(hand, nro):
    return sum([x for x in hand if x == nro])


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
                nro = 3
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=0)
                self.hand[0] = nro
            if not self.vars[1].get():
                nro = randint(1,6)
                nro = 3
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=1)
                self.hand[1] = nro
            if not self.vars[2].get():
                nro = randint(1,6)
                nro = 1
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=2)
                self.hand[2] = nro
            if not self.vars[3].get():
                nro = randint(1,6)
                nro = 1
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=3)
                self.hand[3] = nro
            if not self.vars[4].get():
                nro = randint(1,6)
                nro = 3
                self.cl1 = tkinter.Label(window, text=nro).grid(row=2,column=4)
                self.hand[4] = nro

            self.rolls += 1

        else:
            self.give_possible_hands()

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


    def give_possible_hands(self):
        # tsekkaa 1-6 osumat
        for n in range (6):
            if count(self.hand, n+1) >= 1:
                if n == 0:
                    print("Ykköset: ", summa(self.hand, n+1))
                if n == 1:
                    print("Kakkoset: ", summa(self.hand, n+1))
                if n == 2:
                    print("Kolmoset: ", summa(self.hand, n+1))
                if n == 3:
                    print("Neloset: ", summa(self.hand, n+1))
                if n == 4:
                    print("Vitoset: ", summa(self.hand, n+1))
                if n == 5:
                    print("Kutoset: ", summa(self.hand, n+1))

        # pari
        max_pts = 0
        for n in range (6):
            if count(self.hand, n+1) >= 2:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            print("Pari: ", max_pts)
            max_pts = 0
            
        # kolmoset
        for n in range (6):
            if count(self.hand, n+1) >= 3:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            print("Kolmoset: ", max_pts)
            max_pts = 0
                       
        # neloset
        for n in range (6):
            if count(self.hand, n+1) >= 4:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            print("Neloset: ", max_pts)
            max_pts = 0
        
        # kaksi paria
        laskin = []
        for x in self.hand:
            laskin.append(count(self.hand, x))    
        for x in laskin:
            if count(laskin, x) == 4 or x == 4:
                pts = 0
                for x in self.hand:
                    if count(self.hand, x) == 2 or count(self.hand, x) == 4:
                        pts = pts + summa(self.hand, x)
                print("Kaksi paria: ", pts/2)
        
        # täyskäsi
        laskin = []
        minus = 0
        for x in self.hand:
            laskin.append(count(self.hand, x))
            if count(self.hand, x) == 3:
                minus = x
        if 3 in laskin and 2 in laskin:
            print("Kaksi paria: ", sum(self.hand) - minus)
            print("Täyskäsi: ", sum(self.hand))
                  
        # pieni suora
        if sorted(self.hand) == [1,2,3,4,5]:
            print("Pieni suora: 15")
        # iso suora
        if sorted(self.hand) == [2,3,4,5,6]:
            print("Iso suora: 20")
            
        # sattuma
        print("Sattuma: ", sum(self.hand))
            
        # yatzy
        for n in range (6):
            if count(self.hand, n+1) == 5:
                print("YATZY: 50")
            
            
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
