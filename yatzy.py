import tkinter
from random import randint


def count(hand, nro):
    return len([x for x in hand if x == nro])


def summa(hand, nro):
    return sum([x for x in hand if x == nro])


class Player:
    def __init__(self, name):
        self.name = name


class GUI:
    def __init__(self):
        self.throw_button = tkinter.Button(window, text="Throw", command=test)
        self.throw_button.grid(row=1,column=2)

        self.dices = [tkinter.Label(window, text="").grid(row=2,column=1),
                      tkinter.Label(window, text="").grid(row=2,column=2),
                      tkinter.Label(window, text="").grid(row=2,column=3),
                      tkinter.Label(window, text="").grid(row=2,column=4),
                      tkinter.Label(window, text="").grid(row=2,column=5)]
        
        self.hands = [tkinter.Label(window, text="Ykköset: ").grid(row=4,column=0),
                      tkinter.Label(window, text="Kakkoset: ").grid(row=5,column=0),
                      tkinter.Label(window, text="Kolmoset: ").grid(row=6,column=0),
                      tkinter.Label(window, text="Neloset: ").grid(row=7,column=0),
                      tkinter.Label(window, text="Vitoset: ").grid(row=8,column=0),
                      tkinter.Label(window, text="Kutoset: ").grid(row=9,column=0),
                      tkinter.Label(window, text="Pari: ").grid(row=10,column=0),
                      tkinter.Label(window, text="Kaksi paria: ").grid(row=11,column=0),
                      tkinter.Label(window, text="Kolme samaa: ").grid(row=12,column=0),
                      tkinter.Label(window, text="Neljä samaa: ").grid(row=13,column=0),
                      tkinter.Label(window, text="Pieni suora: ").grid(row=14,column=0),
                      tkinter.Label(window, text="Iso suora: ").grid(row=15,column=0),
                      tkinter.Label(window, text="Täyskäsi: ").grid(row=16,column=0),
                      tkinter.Label(window, text="Sattuma: ").grid(row=17,column=0),
                      tkinter.Label(window, text="YATZY: ").grid(row=18,column=0)]
        self.point1 = tkinter.Label(window, text="").grid(row=4,column=7)
        self.point2 = tkinter.Label(window, text="").grid(row=5,column=7)
        self.point3 = tkinter.Label(window, text="").grid(row=6,column=7)
        self.point4 = tkinter.Label(window, text="").grid(row=7,column=7)
        self.point5 = tkinter.Label(window, text="").grid(row=8,column=7)
        self.point6 = tkinter.Label(window, text="").grid(row=9,column=7)
        self.point7 = tkinter.Label(window, text="").grid(row=10,column=7)
        self.point8 = tkinter.Label(window, text="").grid(row=11,column=7)
        self.point9 = tkinter.Label(window, text="").grid(row=12,column=7)
        self.point10 = tkinter.Label(window, text="").grid(row=13,column=7)
        self.point11 = tkinter.Label(window, text="").grid(row=14,column=7)
        self.point12 = tkinter.Label(window, text="").grid(row=15,column=7)
        self.point13 = tkinter.Label(window, text="").grid(row=16,column=7)
        self.point14 = tkinter.Label(window, text="").grid(row=17,column=7)
        self.point15 = tkinter.Label(window, text="").grid(row=18,column=7)
        
        self.dice_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.hands_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.dbuttons = [tkinter.Checkbutton(window, variable=self.dice_vars[0]).grid(row=3,column=1),
                         tkinter.Checkbutton(window, variable=self.dice_vars[1]).grid(row=3,column=2),
                         tkinter.Checkbutton(window, variable=self.dice_vars[2]).grid(row=3,column=3),
                         tkinter.Checkbutton(window, variable=self.dice_vars[3]).grid(row=3,column=4),
                         tkinter.Checkbutton(window, variable=self.dice_vars[4]).grid(row=3,column=5)]    
        
        self.hbuttons = [tkinter.Checkbutton(window, variable=self.hands_vars[0]).grid(row=4,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[1]).grid(row=5,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[2]).grid(row=6,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[3]).grid(row=7,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[4]).grid(row=8,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[5]).grid(row=9,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[6]).grid(row=10,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[7]).grid(row=11,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[8]).grid(row=12,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[9]).grid(row=13,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[10]).grid(row=14,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[11]).grid(row=15,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[12]).grid(row=16,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[13]).grid(row=17,column=1),
                         tkinter.Checkbutton(window, variable=self.hands_vars[14]).grid(row=18,column=1)]


    def update_possible_hand(self, new_hand, nro):
        self.hands[nro] = new_hand
        

    def update_dice(self, nro):
        self.dices[0] = nro

        
    def get_dices(self, nro):
        return self.dice_vars[nro].get()
        
        
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
    def __init__(self, gui):
        self.rolls = 0
        self.hand  = [0, 0, 0, 0, 0]
        self.gui = gui
        
        # self.current = []
        # self.vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        # self.cl1 = tkinter.Label(window, text="").grid(row=2,column=0)
        # self.cl2 = tkinter.Label(window, text="").grid(row=2,column=1)
        # self.cl3 = tkinter.Label(window, text="").grid(row=2,column=2)
        # self.cl4 = tkinter.Label(window, text="").grid(row=2,column=3)
        # self.cl5 = tkinter.Label(window, text="").grid(row=2,column=4)
        # self.cbuttons = [tkinter.Checkbutton(window, variable=self.vars[0]).grid(row=3,column=0),
        # tkinter.Checkbutton(window, variable=self.vars[1]).grid(row=3,column=1),
        # tkinter.Checkbutton(window, variable=self.vars[2]).grid(row=3,column=2),
        # tkinter.Checkbutton(window, variable=self.vars[3]).grid(row=3,column=3),
        # tkinter.Checkbutton(window, variable=self.vars[4]).grid(row=3,column=4)]


    def roll(self):
        if self.rolls < 3:
            if not self.gui.get_dices(0):
                nro = randint(1,6)
                nro = 3
                self.hand[0] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=1)
                self.gui.update_dice(nro)
            if not self.gui.get_dices(1):
                nro = randint(1,6)
                nro = 2
                self.hand[1] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=2)
            if not self.gui.get_dices(2):
                nro = randint(1,6)
                nro = 1
                self.hand[2] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=3)
            if not self.gui.get_dices(3):
                nro = randint(1,6)
                nro = 4
                self.hand[3] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=4)                
            if not self.gui.get_dices(4):
                nro = randint(1,6)
                nro = 5
                self.hand[4] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=5)


            self.rolls += 1

        else:
            self.give_possible_hands()


    def give_possible_hands(self):
        # tsekkaa 1-6 osumat
        for n in range (6):
            if count(self.hand, n+1) >= 1:
                if n == 0:
                    t = ("Ykköset: ", summa(self.hand, n+1))
                    label = tkinter.Label(window, text=t).grid(row=4,column=0)
                    self.gui.update_possible_hand(label, 0)
                if n == 1:
                    t = ("Kakkoset: ", summa(self.hand, n+1))
                    label = tkinter.Label(window, text=t).grid(row=5,column=0)
                    self.gui.update_possible_hand(label, 1)                    
                if n == 2:
                    t = ("Kolmoset: ", summa(self.hand, n+1))
                    label = tkinter.Label(window, text=t).grid(row=6,column=0)
                    self.gui.update_possible_hand(label, 2)                    
                if n == 3:
                    t = ("Neloset: ", summa(self.hand, n+1))
                    label = tkinter.Label(window, text=t).grid(row=7,column=0)
                    self.gui.update_possible_hand(label, 3)                    
                if n == 4:
                    t = ("Vitoset: ", summa(self.hand, n+1))
                    label = tkinter.Label(window, text=t).grid(row=8,column=0)
                    self.gui.update_possible_hand(label, 4)                    
                if n == 5:
                    t = ("Kutoset: ", summa(self.hand, n+1))
                    label = tkinter.Label(window, text=t).grid(row=9,column=0)
                    self.gui.update_possible_hand(label, 5)                    

        # pari
        max_pts = 0
        for n in range (6):
            if count(self.hand, n+1) >= 2:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            t = ("Pari: ", max_pts)
            label = tkinter.Label(window, text=t).grid(row=10,column=0)
            self.gui.update_possible_hand(label, 6)            
            max_pts = 0
            
        # kolmoset
        for n in range (6):
            if count(self.hand, n+1) >= 3:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            t = ("Kolmoset: ", max_pts)
            label = tkinter.Label(window, text=t).grid(row=12,column=0)
            self.gui.update_possible_hand(label, 8)
            max_pts = 0
                       
        # neloset
        for n in range (6):
            if count(self.hand, n+1) >= 4:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            t = ("Neloset: ", max_pts)
            label = tkinter.Label(window, text=t).grid(row=13,column=0)
            self.gui.update_possible_hand(label, 9)            
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
                t = ("Kaksi paria: ", pts/2)
                label = tkinter.Label(window, text=t).grid(row=11,column=0)
                self.gui.update_possible_hand(label, 7)                
        
        # täyskäsi
        laskin = []
        minus = 0
        for x in self.hand:
            laskin.append(count(self.hand, x))
            if count(self.hand, x) == 3:
                minus = x
        if 3 in laskin and 2 in laskin:
            t = ("Kaksi paria: ", sum(self.hand) - minus)
            label = tkinter.Label(window, text=t).grid(row=11,column=0)
            self.gui.update_possible_hand(label, 7)            
            t = ("Täyskäsi: ", sum(self.hand))
            label = tkinter.Label(window, text=t).grid(row=16,column=0)
            self.gui.update_possible_hand(label, 12)            
                  
        # pieni suora
        if sorted(self.hand) == [1,2,3,4,5]:
            t = ("Pieni suora: 15")
            label = tkinter.Label(window, text=t).grid(row=14,column=0)
            self.gui.update_possible_hand(label, 10)            
        # iso suora
        if sorted(self.hand) == [2,3,4,5,6]:
            t = ("Iso suora: 20")
            label = tkinter.Label(window, text=t).grid(row=15,column=0)
            self.gui.update_possible_hand(label, 11)            
            
        # sattuma
        t = ("Sattuma: ", sum(self.hand))
        label = tkinter.Label(window, text=t).grid(row=17,column=0)
        self.gui.update_possible_hand(label, 13)        
            
        # yatzy
        for n in range (6):
            if count(self.hand, n+1) == 5:
                t = ("YATZY: 50")
                label = tkinter.Label(window, text=t).grid(row=18,column=0)
                self.gui.update_possible_hand(label, 14)                
            
            
    def test(self):
        #print(self.vars[0].get())
        print(self.hand)
        pass


def test():
    turn.roll()
    turn.test()
    #pass

if __name__ == "__main__":
    #name = raw_input("Player 1: ")
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("300x500")
    window.resizable(0,0)
    gui = GUI()
    turn = Turn(gui)
    #throw_button = tkinter.Button(window, text="Throw", command=test)
    #throw_button.grid(row=1,column=2)
    #throw_button.pack()
    window.mainloop()
