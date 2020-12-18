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
        
        
    def check_bonus(self):
        bonus = self.points[0:6]
        bonus_pts = 0
        for pts in bonus:
            bonus_pts += int(pts)
        if bonus_pts >= 63:
            return True
        else:
            return False
        
        
    def calculate_mid_points(self):
        points = 0
        for point in self.points[0:6]:
            points = points + float(point)

        return int(points)
    
    
    def calculate_points(self):
        points = 0
        for point in self.points:
            points = points + float(point)
        if self.check_bonus():
            points += 50

        return int(points)