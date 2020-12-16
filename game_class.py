# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:46:34 2020

@author: soderdahl
"""


import tkinter
from random import randint


def count(hand, nro):
    return len([x for x in hand if x == nro])


def summa(hand, nro):
    return sum([x for x in hand if x == nro])


class Game:
    def __init__(self, gui, players):
        self.round = 0
        self.players = players
        self.turn_ind = 0
        self.gui = gui
        # self.button = ""


    def start(self):
        turn = Turn(self.gui)
        self.gui.add_command_to_button(turn)
        self.gui.add_players(self.players)
        
        
    def next_round(self):
        self.round += 1
        if self.round == 15:
            self.end()
        if turn_ind == sizeof(self.players):
            turn_ind = 0
        else:
            turn_ind += 1
        
        
    def end(self):
        for player in self.players:
            player.calculate_points()
            
            
    def get_player_num(self):
        return self.turn_ind
        

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
                nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=3)
                self.gui.update_dice(nro)
            if not self.gui.get_dices(1):
                nro = randint(1,6)
               # nro = 2
                self.hand[1] = nro
                nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=4)
            if not self.gui.get_dices(2):
                nro = randint(1,6)
                #nro = 1
                self.hand[2] = nro
                nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=5)
            if not self.gui.get_dices(3):
                nro = randint(1,6)
                #nro = 4
                self.hand[3] = nro
                nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=6)                
            if not self.gui.get_dices(4):
                nro = randint(1,6)
                #nro = 5
                self.hand[4] = nro
                nro = tkinter.Label(self.gui.get_window(), text=nro).grid(row=2,column=7)


            self.rolls += 1

        else:
            self.give_possible_hands()
            self.gui.adjust_checboxes(self.hands)
            self.gui.change_buttons(0)
            # self.gui.reset_turn()
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
        #print(self.hand)
        for i in self.hands:
            print (i)
        #pass