# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:38:23 2021

@author: soderdahl
"""


def count(hand, nro):
    return len([x for x in hand if x == nro])


def summa(hand, nro):
    return sum([x for x in hand if x == nro])


class Turn:
    def __init__(self, gui):
        self.rolls = 0
        self.hand  = [0, 0, 0, 0, 0]
        self.hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gui = gui

    def roll(self):
        if not self.gui.get_dices(0):
            nro = self.gui.throw_dice(0)
            self.hand[0] = nro
            #nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=3)
            #self.gui.update_dice(nro)
        if not self.gui.get_dices(1):
            nro = self.gui.throw_dice(1)
            self.hand[1] = nro
            #nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=4)
        if not self.gui.get_dices(2):
            nro = self.gui.throw_dice(2)
            self.hand[2] = nro
            #nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=5)
        if not self.gui.get_dices(3):
            nro = self.gui.throw_dice(3)
            self.hand[3] = nro
            #nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=6)                
        if not self.gui.get_dices(4):
            nro = self.gui.throw_dice(4)
            self.hand[4] = nro
            #nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=7)

        self.rolls += 1

        if self.rolls == 3:
            self.hand = self.gui.get_hand()
            #print(self.hand)
            self.give_possible_hands()
            self.gui.adjust_checboxes(self.hands)
            self.gui.change_buttons(0)
            self.rolls = 0 # poista tää kun monta pelaajaa?
            self.hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



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
                pts = 2*(n+1)
                if max_pts < pts:
                    max_pts = pts
        if max_pts > 0:
            self.hands[6] = max_pts
            self.gui.update_possible_hand(self.hands[6], 6)            
            max_pts = 0
            
        # kolmoset
        for n in range (6):
            if count(self.hand, n+1) >= 3:
                if max_pts < 3*(n+1):
                    max_pts = 3*(n+1)
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
                    if count(self.hand, x) == 2:
                        pts = pts + summa(self.hand, x)
                        self.hands[7] = int(pts/2)
                    elif count(self.hand, x) == 4:
                        pts = pts + summa(self.hand, x)
                        self.hands[7] = int(pts/4)                        
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