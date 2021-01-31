# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:38:43 2021

@author: soderdahl
"""


class Scores:
    def __init__(self, players):
        self.players = players
        
        #player_points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.all_points = []
        for player in players:
            self.all_points.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    
    
    def add_score(self, point, hand, ind):
        self.all_points[ind][hand] = point
        print(self.all_points)
        
        
    def check_bonus(self,ind):
        bonus = self.all_points[ind][0:6]
        bonus_pts = 0
        for pts in bonus:
            bonus_pts += int(pts)
        if bonus_pts >= 63:
            return True
        else:
            return False
        
        
    def calculate_mid_points(self, ind):
        points = 0
        for point in self.all_points[ind][0:6]:
            points = points + float(point)

        return int(points)
    
    
    def calculate_points(self, ind):
        points = 0
        for point in self.all_points[ind]:
            points = points + float(point)
        if self.check_bonus(ind):
            points += 50

        return int(points)