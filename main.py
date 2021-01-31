# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:41:00 2020

@author: soderdahl
"""

import tkinter
import player_class
import gui_class
import game_class


if __name__ == "__main__":
    # game window settings
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("500x600")
    window.resizable(0,0)
    window.lift()
    window.attributes("-topmost", True)
    
    # asks how many player will be playing
    nro_players = tkinter.simpledialog.askinteger("Players", "How many players?", parent=window)
    
    # asks player names and makes list of players (Player class)
    players = []
    i = 0
    while i<nro_players:
        nro = i+1
        text = "Player "+ str(nro) +" name?"
        name = tkinter.simpledialog.askstring("Player name", text, parent=window)
        player = player_class.Player(name)
        players.append(player)
        i += 1

    # initializes gui and game-logic with given players
    gui = gui_class.GUI(window, players)
    game = game_class.Game(gui, players)
    gui.add_game_logic(game)
    
    game.start()
    
    window.mainloop()