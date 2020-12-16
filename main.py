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
    window = tkinter.Tk()
    window.title("Yatzy")
    window.geometry("500x500")
    window.resizable(0,0)
    
    # parempi looppi!
    players = []
    i = 0
    while i<2:
        nro = i+1
        text = "Player "+ str(nro) +" name?"
        name = tkinter.simpledialog.askstring("Input", text, parent=window)
        player = player_class.Player(name)
        players.append(player)
        i += 1
    
    gui = gui_class.GUI(window, players)
    #turn = Turn(gui)
    game = game_class.Game(gui, players)
    gui.add_game_logic(game)
    game.start()

    """
    pelaaja alustus
    gui alustus
    game alustus
    game start
        turn
        turn = 3 -> seuraava pelaaja
        rounds = 15 -> game end
    pistelasku
    """
    
    window.mainloop()