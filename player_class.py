# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:46:12 2020

@author: soderdahl
"""


class Player:
    def __init__(self, name):
        self.name = name
        
        # used_hands tells what hands player has already used so it can't be used again
        self.used_hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # tracking players points
        self.points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        
    def get_name(self):
        return self.name
    
    
    # marks given hand used
    def add_hand(self, hand):
        self.used_hands[hand] = 1
        
        
    def check_hands(self):
        return self.used_hands