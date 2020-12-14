import tkinter
from random import randint


def count(hand, nro):
    return len([x for x in hand if x == nro])


def summa(hand, nro):
    return sum([x for x in hand if x == nro])


class Player:
    def __init__(self, name):
        self.name = name
        self.points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        
    def add_point(self, hand):
        self.points[hand] = 1
        
        
    def check_points(self, hand):
        return self.points[hand]


class GUI:
    def __init__(self, player):
        self.throw_button = tkinter.Button(window, text="Throw")
        self.throw_button.grid(row=1,column=1)
        self.next_button = tkinter.Button(window, text="Next turn", command=self.reset_turn, state="disabled")
        self.next_button.grid(row=1,column=0)
        self.player = player

        self.dices = [tkinter.Label(window, text="").grid(row=2,column=3),
                      tkinter.Label(window, text="").grid(row=2,column=4),
                      tkinter.Label(window, text="").grid(row=2,column=5),
                      tkinter.Label(window, text="").grid(row=2,column=6),
                      tkinter.Label(window, text="").grid(row=2,column=7)]
        
        self.hand_names = [tkinter.Label(window, text="Ykköset: ").grid(row=4,column=0),
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
        
        self.vars = [tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),
                     tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),
                     tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar()]
        self.hands = [tkinter.Label(window, textvariable=self.vars[0]).grid(row=4,column=1),
                      tkinter.Label(window, textvariable=self.vars[1]).grid(row=5,column=1),
                      tkinter.Label(window, textvariable=self.vars[2]).grid(row=6,column=1),
                      tkinter.Label(window, textvariable=self.vars[3]).grid(row=7,column=1),
                      tkinter.Label(window, textvariable=self.vars[4]).grid(row=8,column=1),
                      tkinter.Label(window, textvariable=self.vars[5]).grid(row=9,column=1),
                      tkinter.Label(window, textvariable=self.vars[6]).grid(row=10,column=1),
                      tkinter.Label(window, textvariable=self.vars[7]).grid(row=11,column=1),
                      tkinter.Label(window, textvariable=self.vars[8]).grid(row=12,column=1),
                      tkinter.Label(window, textvariable=self.vars[9]).grid(row=13,column=1),
                      tkinter.Label(window, textvariable=self.vars[10]).grid(row=14,column=1),
                      tkinter.Label(window, textvariable=self.vars[11]).grid(row=15,column=1),
                      tkinter.Label(window, textvariable=self.vars[12]).grid(row=16,column=1),
                      tkinter.Label(window, textvariable=self.vars[13]).grid(row=17,column=1),
                      tkinter.Label(window, textvariable=self.vars[14]).grid(row=18,column=1)]
        i = 0
        for button in self.vars:
            self.vars[i].set("")
            i += 1
        
        self.points = [tkinter.Label(window, text="").grid(row=4,column=7),
                       tkinter.Label(window, text="").grid(row=5,column=7),
                       tkinter.Label(window, text="").grid(row=6,column=7),
                       tkinter.Label(window, text="").grid(row=7,column=7),
                       tkinter.Label(window, text="").grid(row=8,column=7),
                       tkinter.Label(window, text="").grid(row=9,column=7),
                       tkinter.Label(window, text="").grid(row=10,column=7),
                       tkinter.Label(window, text="").grid(row=11,column=7),
                       tkinter.Label(window, text="").grid(row=12,column=7),
                       tkinter.Label(window, text="").grid(row=13,column=7),
                       tkinter.Label(window, text="").grid(row=14,column=7),
                       tkinter.Label(window, text="").grid(row=15,column=7),
                       tkinter.Label(window, text="").grid(row=16,column=7),
                       tkinter.Label(window, text="").grid(row=17,column=7),
                       tkinter.Label(window, text="").grid(row=18,column=7)]
        
        self.dice_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.hands_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.dbuttons = [tkinter.Checkbutton(window, variable=self.dice_vars[0]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[1]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[2]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[3]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[4])]    
        self.hbuttons = [tkinter.Checkbutton(window, variable=self.hands_vars[0]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[1]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[2]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[3]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[4]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[5]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[6]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[7]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[8]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[9]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[10]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[11]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[12]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[13]),
                         tkinter.Checkbutton(window, variable=self.hands_vars[14])]
        i = 0
        for button in self.dbuttons:
            button.grid(row=3, column=3+i)
            i += 1
        i = 0
        for button in self.hbuttons:
            button.grid(row=i+4, column=2)
            i += 1

    def update_possible_hand(self, new_hand, nro):
        if self.player.check_points(nro) == 0:
            self.vars[nro].set(new_hand)
            self.player.add_point(nro)
        else:
            return
        

    def update_dice(self, nro):
        self.dices[0] = nro

        
    def get_dices(self, nro):
        return self.dice_vars[nro].get()
    
    
    def add_score(self):
        i = 0
        for hand in self.hands_vars:
            if hand.get():
                self.points[i] = tkinter.Label(window, text=self.vars[i].get()).grid(row=i+4,column=8)
                break
            i += 1


    def add_command_to_button(self, turn):
        self.throw_button.configure(command=turn.roll)


    def change_buttons(self, state):
        if state == 0:
            self.throw_button.configure(state="disabled")
            self.next_button.configure(state="normal")
        else:
            self.throw_button.configure(state="normal")
            self.next_button.configure(state="disabled")


    def reset_turn(self):   
        self.add_score()
        for box in self.hbuttons:
            box.deselect()
        for box in self.dbuttons:
            box.deselect()
        i = 0
        for button in self.vars:
            self.vars[i].set("")
            i += 1
        self.change_buttons(1)


        
        
class Game:
    def __init__(self, gui):
        self.round = 0
        self.players = []
        self.gui = gui
        # self.button = ""

    def start(self):
        turn = Turn(self.gui)
        self.gui.add_command_to_button(turn)
        # self.button = tkinter.Button(window, text="Throw", command=turn.roll)
        # self.button.grid(row=1,column=2)
        #self.gui.reset_turn()
        # self.round += 1
        # while self.round < 15:
        #     turn = Turn(self.gui)
        #     self.round += 1
        

class Scores:
    def __init__(self):
        pass


class Turn:
    def __init__(self, gui):
        self.rolls = 0
        self.hand  = [0, 0, 0, 0, 0]
        self.hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gui = gui

    def roll(self):
        if self.rolls < 2:
            if not self.gui.get_dices(0):
                nro = randint(1,6)
                #nro = 3
                self.hand[0] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=3)
                self.gui.update_dice(nro)
            if not self.gui.get_dices(1):
                nro = randint(1,6)
               # nro = 2
                self.hand[1] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=4)
            if not self.gui.get_dices(2):
                nro = randint(1,6)
                #nro = 1
                self.hand[2] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=5)
            if not self.gui.get_dices(3):
                nro = randint(1,6)
                #nro = 4
                self.hand[3] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=6)                
            if not self.gui.get_dices(4):
                nro = randint(1,6)
                #nro = 5
                self.hand[4] = nro
                nro = tkinter.Label(window, text=nro).grid(row=2,column=7)


            self.rolls += 1

        else:
            self.give_possible_hands()
            self.gui.change_buttons(0)
            # self.gui.reset_turn()
            self.rolls = 0 # poista tää kun monta pelaajaa?
            # self.hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



    def give_possible_hands(self):  
        # tsekkaa 1-6 osumat
        for n in range (6):
            if count(self.hand, n+1) >= 1:
                if n == 0:
                    self.hands[n] = summa(self.hand, n+1)
                    self.gui.update_possible_hand(self.hands[n], 0)
                if n == 1:
                    self.hands[n] = summa(self.hand, n+1)                  
                    self.gui.update_possible_hand(self.hands[n], 1)                    
                if n == 2:
                    self.hands[n] = summa(self.hand, n+1)
                    self.gui.update_possible_hand(self.hands[n], 2)                    
                if n == 3:
                    self.hands[n] = summa(self.hand, n+1)
                    self.gui.update_possible_hand(self.hands[n], 3)                    
                if n == 4:
                    self.hands[n] = summa(self.hand, n+1)
                    self.gui.update_possible_hand(self.hands[n], 4)                    
                if n == 5:
                    self.hands[n] = summa(self.hand, n+1)
                    self.gui.update_possible_hand(self.hands[n], 5)                    

        # pari
        max_pts = 0
        for n in range (6):
            if count(self.hand, n+1) >= 2:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            self.hands[6] = max_pts
            self.gui.update_possible_hand(self.hands[6], 6)            
            max_pts = 0
            
        # kolmoset
        for n in range (6):
            if count(self.hand, n+1) >= 3:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            self.hands[8] = max_pts
            self.gui.update_possible_hand(self.hands[8], 8)
            max_pts = 0
                       
        # neloset
        for n in range (6):
            if count(self.hand, n+1) >= 4:
                if max_pts < summa(self.hand, n+1):
                    max_pts = summa(self.hand, n+1)
        if max_pts > 0:
            self.hands[9] = max_pts
            self.gui.update_possible_hand(self.hands[9], 9)            
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
                self.hands[7] = pts/2
                self.gui.update_possible_hand(self.hands[7], 7)                
        
        # täyskäsi
        laskin = []
        minus = 0
        for x in self.hand:
            laskin.append(count(self.hand, x))
            if count(self.hand, x) == 3:
                minus = x
        if 3 in laskin and 2 in laskin:
            self.hands[7] = sum(self.hand)-minus
            self.gui.update_possible_hand(self.hands[7], 7)            
            self.hands[12] = sum(self.hand)
            self.gui.update_possible_hand(self.hands[12], 12)            
                  
        # pieni suora
        if sorted(self.hand) == [1,2,3,4,5]:
            self.hands[10] = 15
            self.gui.update_possible_hand(self.hands[10], 10)            
        # iso suora
        if sorted(self.hand) == [2,3,4,5,6]:
            self.hands[11] = 20
            self.gui.update_possible_hand(self.hands[11], 11)            
            
        # sattuma
        self.hands[13] = sum(self.hand)
        self.gui.update_possible_hand(self.hands[13], 13)        
            
        # yatzy
        for n in range (6):
            if count(self.hand, n+1) == 5:
                self.hands[14] = 50
                self.gui.update_possible_hand(self.hands[14], 14)          
            
            
    def test(self):
        #print(self.vars[0].get())
        print(self.hand)
        #pass


# def test():
#     turn.roll()
#     turn.test()
    #pass

if __name__ == "__main__":
    #name = raw_input("Player 1: ")
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("500x500")
    window.resizable(0,0)
    player = Player("daniel")
    gui = GUI(player)
    #turn = Turn(gui)
    # throw_button = tkinter.Button(window, text="Throw", command=turn.roll)
    # throw_button.grid(row=1,column=2)
    game = Game(gui)
    game.start()
    window.mainloop()
