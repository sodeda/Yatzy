# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:38:23 2021

@author: soderdahl
"""

# helper functions
def count(hand, nro):
    return len([x for x in hand if x == nro])


def summa(hand, nro):
    return sum([x for x in hand if x == nro])


class Turn:
    def __init__(self, gui):
        self.rolls = 0
        self.hand  = [0, 0, 0, 0, 0] # dices
        self.hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gui = gui


    def roll(self):
        # throws dices that are not selected
        if not self.gui.get_dices(0):
            nro = self.gui.throw_dice(0)
            self.hand[0] = nro
        if not self.gui.get_dices(1):
            nro = self.gui.throw_dice(1)
            self.hand[1] = nro
        if not self.gui.get_dices(2):
            nro = self.gui.throw_dice(2)
            self.hand[2] = nro
        if not self.gui.get_dices(3):
            nro = self.gui.throw_dice(3)
            self.hand[3] = nro               
        if not self.gui.get_dices(4):
            nro = self.gui.throw_dice(4)
            self.hand[4] = nro

        self.rolls += 1

        # after 3 rolls shows possible hands, adjusts checkboxes and changes which buttons are active
        if self.rolls == 3:
            self.hand = self.gui.get_hand()
            self.give_possible_hands()
            self.gui.adjust_checboxes(self.hands)
            self.gui.change_buttons(0)
            self.rolls = 0
            self.hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



    def give_possible_hands(self):       
        max_par = 0
        max_triple = 0
        max_quad = 0
        
        for n in range (6):
            
            # checks possible upper points
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
            
            # checks best pair
            if count(self.hand, n+1) >= 2:
                pts = 2*(n+1)
                if max_par < pts:
                    max_par = pts
            
            # checks best 3 of a kind
            if count(self.hand, n+1) >= 3:
                if max_par < 3*(n+1):
                    max_triple = 3*(n+1)
                   
            # checks best 4 of a kind
            if count(self.hand, n+1) >= 4:
                if max_triple < summa(self.hand, n+1):
                    max_quad = summa(self.hand, n+1)
                    
            # yatzy
            if count(self.hand, n+1) == 5:
                self.hands[14] = 50
                self.gui.update_possible_hand(self.hands[14], 14)  
        
        # updates pair, 3 and 4 of a kinds
        if max_par > 0:
            self.hands[6] = max_par
            self.gui.update_possible_hand(self.hands[6], 6)            
            #max_pts = 0

        if max_triple > 0:
            self.hands[8] = max_triple
            self.gui.update_possible_hand(self.hands[8], 8)
            #max_pts = 0

        if max_quad > 0:
            self.hands[9] = max_quad
            self.gui.update_possible_hand(self.hands[9], 9)            
            #max_pts = 0
        
        # two pairs
        laskin = []
        for x in self.hand:
            laskin.append(count(self.hand, x))    
        for x in laskin:
            
            # find if there is two pairs or 4 of a kind
            if count(laskin, x) == 4 or x == 4:
                pts = 0
                for x in self.hand:
               
                    # calculate points depending on type of two pair
                    if count(self.hand, x) == 2:
                        pts = pts + summa(self.hand, x)
                        self.hands[7] = int(pts/2)
                    elif count(self.hand, x) == 4:
                        pts = pts + summa(self.hand, x)
                        self.hands[7] = int(pts/4)     
                        
                self.gui.update_possible_hand(self.hands[7], 7)                
        
        # full house
        laskin = []
        minus = 0
        for x in self.hand:
            laskin.append(count(self.hand, x))
            if count(self.hand, x) == 3:
                minus = x
        if 3 in laskin and 2 in laskin:
            # adds also two pairs, because two pair handle doesn't recognize if there is three of other pair
            self.hands[7] = sum(self.hand)-minus
            self.gui.update_possible_hand(self.hands[7], 7)  
            
            # adds full house
            self.hands[12] = sum(self.hand)
            self.gui.update_possible_hand(self.hands[12], 12)            
                  
        # small straight
        if sorted(self.hand) == [1,2,3,4,5]:
            self.hands[10] = 15
            self.gui.update_possible_hand(self.hands[10], 10)            
        # large straight
        if sorted(self.hand) == [2,3,4,5,6]:
            self.hands[11] = 20
            self.gui.update_possible_hand(self.hands[11], 11)            
            
        # chance
        self.hands[13] = sum(self.hand)
        self.gui.update_possible_hand(self.hands[13], 13)             