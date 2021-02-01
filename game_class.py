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
        self.round = 0 # keeps track how many turns have been played
        self.players = players
        self.turn_ind = 0 # whos turn
        self.gui = gui
        self.scores = scores_class.Scores(self.players)

    
    # initializes game
    def start(self):
        turn = turn_class.Turn(self.gui)
        self.gui.add_command_to_button(turn)
        self.gui.add_players(self.players)
        
        
    def next_round(self):
        self.round += 1
        
        # ends game if certain number of turns have been played
        if self.round == 15*len(self.players):
            self.end()
            
        # changes turn to next player
        if self.turn_ind == len(self.players)-1:
            self.turn_ind = 0
        else:
            self.turn_ind += 1
    

    def calculate_scores(self, ind):
        # calculate players scores and checks bonus
        mid = self.scores.calculate_mid_points(ind)
        full = self.scores.calculate_points(ind)
        bonus = self.scores.check_bonus(ind)
        
        return [mid, full, bonus]


    # adds score to given player and hand
    def add_score(self, points, hand, player):
        self.scores.add_score(points, hand, player)
    
        
    def end(self):
        self.gui.end_game()
        
        # calculate all players points
        points = []
        for player in self.players:
            points.append(player.calculate_points())
            
        # checks winners points
        win_pts = max(points)
        
        # finds which player won
        win_ind = [i for i, pts in enumerate(points) if pts == win_pts]
        win_ind = win_ind[0]
        win_player = self.players[win_ind].get_name()
        
        # pop up window
        text = "Voittaja on " + str(win_player) + ", " + str(win_pts) + " pisteellä."
        tkinter.messagebox.showinfo("Winner", text)
        
            
    def get_player_num(self):
        return self.turn_ind      