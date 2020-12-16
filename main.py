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
    #name = raw_input("Player 1: ")
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("500x500")
    window.resizable(0,0)
    
    # parempi looppi!
    players = []
    i = 0
    while i<2:
        name = tkinter.simpledialog.askstring("Input", "Player 1 name?", parent=window)
        player = player_class.Player(name)
        players.append(player)
        i += 1
    
    #player = Player("daniel")
    gui = gui_class.GUI(window, player)
    #turn = Turn(gui)
    # throw_button = tkinter.Button(window, text="Throw", command=turn.roll)
    # throw_button.grid(row=1,column=2)
    game = game_class.Game(gui, players)
    game.start()
    window.mainloop()