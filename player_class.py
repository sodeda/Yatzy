# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:46:12 2020

@author: soderdahl
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.used_hands = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        
    def get_name(self):
        return self.name
    
    
    def add_hand(self, hand):
        self.used_hands[hand] = 1
        
        
    def check_hands(self):
        return self.used_hands
    
    
    def add_score(self, point, hand):
        self.points[hand] = point
        
        
    def calculate_points(self):
        points = 0
        i = 0
        for point in self.points:
            points = points + int(point)
            if i == 6:
                if points > 63:
                    points = points + 50
        print(points)