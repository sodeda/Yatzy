# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:46:34 2020

@author: soderdahl
"""


import tkinter
import turn_class
import scores_class


class Game:
    def __init__(self, gui, players):
        self.round = 0
        self.players = players
        self.turn_ind = 0
        self.gui = gui
        self.scores = scores_class.Scores(self.players)


    def start(self):
        turn = turn_class.Turn(self.gui)
        self.gui.add_command_to_button(turn)
        self.gui.add_players(self.players)
        
        
    def next_round(self):
        self.round += 1
        if self.round == 15*len(self.players):
            self.end()
        if self.turn_ind == len(self.players)-1:
            self.turn_ind = 0
        else:
            self.turn_ind += 1
    

    def calculate_scores(self, ind):
        mid = self.scores.calculate_mid_points(ind)
        full = self.scores.calculate_points(ind)
        bonus = self.scores.check_bonus(ind)
        
        return [mid, full, bonus]


    def add_score(self, points, ind1, ind2):
        self.scores.add_score(points, ind1, ind2)
    
    
    
    
        
    def end(self):
        self.gui.end_game()
        points = []
        for player in self.players:
            points.append(player.calculate_points())
        win_pts = max(points)
        win_ind = [i for i, pts in enumerate(points) if pts == win_pts]
        win_ind = win_ind[0]
        win_player = self.players[win_ind].get_name()
        text = "Voittaja on " + str(win_player) + ", " + str(win_pts) + " pisteellä."
        tkinter.messagebox.showinfo("Winner", text)
        
            
    def get_player_num(self):
        return self.turn_ind      