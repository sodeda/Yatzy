# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:46:23 2020

@author: soderdahl
"""

import tkinter
import tkinter.ttk
import time
from random import randint
from PIL import Image, ImageTk


class GUI:
    def __init__(self, window, players):
        self.window = window
        self.throw_button = tkinter.Button(window, text="Throw")
        self.throw_button.grid(row=1,column=1)
        self.next_button = tkinter.Button(window, text="Next turn", command=self.reset_turn, state="disabled")
        self.next_button.grid(row=1,column=0)
        self.players = players
        self.set_players(players)

        self.dices = [tkinter.Label(window, text="").grid(row=2,column=3),
                      tkinter.Label(window, text="").grid(row=2,column=4),
                      tkinter.Label(window, text="").grid(row=2,column=5),
                      tkinter.Label(window, text="").grid(row=2,column=6),
                      tkinter.Label(window, text="").grid(row=2,column=7)]
        
        self.turn = tkinter.StringVar()
        self.hand_names = [tkinter.Label(window, text=self.turn.get()).grid(row=3,column=0),
                           tkinter.Label(window, text="Ykköset: ").grid(row=4,column=0,sticky='w'),
                           tkinter.Label(window, text="Kakkoset: ").grid(row=6,column=0,sticky='w'),
                           tkinter.Label(window, text="Kolmoset: ").grid(row=8,column=0,sticky='w'),
                           tkinter.Label(window, text="Neloset: ").grid(row=10,column=0,sticky='w'),
                           tkinter.Label(window, text="Vitoset: ").grid(row=12,column=0,sticky='w'),
                           tkinter.Label(window, text="Kutoset: ").grid(row=14,column=0,sticky='w'),
                           tkinter.Label(window, text="YHTEENSÄ: ", font=('Helvetica',10,'bold')).grid(row=16,column=0,sticky='w'),
                           tkinter.Label(window, text="BONUS", fg='red', font=('Helvetica',9,'bold')).grid(row=18,column=0,sticky='w'),
                           tkinter.Label(window, text="Pari: ").grid(row=20,column=0,sticky='w'),
                           tkinter.Label(window, text="Kaksi paria: ").grid(row=22,column=0,sticky='w'),
                           tkinter.Label(window, text="Kolme samaa: ").grid(row=24,column=0,sticky='w'),
                           tkinter.Label(window, text="Neljä samaa: ").grid(row=26,column=0,sticky='w'),
                           tkinter.Label(window, text="Pieni suora: ").grid(row=28,column=0,sticky='w'),
                           tkinter.Label(window, text="Iso suora: ").grid(row=30,column=0,sticky='w'),
                           tkinter.Label(window, text="Täyskäsi: ").grid(row=32,column=0,sticky='w'),
                           tkinter.Label(window, text="Sattuma: ").grid(row=34,column=0,sticky='w'),
                           tkinter.Label(window, text="YATZY: ").grid(row=36,column=0,sticky='w'),
                           tkinter.Label(window, text="YHTEENSÄ: ", font=('Helvetica',10,'bold')).grid(row=38,column=0,sticky='w')]
        
        self.vars = [tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),
                     tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),
                     tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar()]
        self.hands = [tkinter.Label(window, textvariable=self.vars[0]).grid(row=4,column=1),
                      tkinter.Label(window, textvariable=self.vars[1]).grid(row=6,column=1),
                      tkinter.Label(window, textvariable=self.vars[2]).grid(row=8,column=1),
                      tkinter.Label(window, textvariable=self.vars[3]).grid(row=10,column=1),
                      tkinter.Label(window, textvariable=self.vars[4]).grid(row=12,column=1),
                      tkinter.Label(window, textvariable=self.vars[5]).grid(row=14,column=1),
                      tkinter.Label(window, textvariable=self.vars[6]).grid(row=20,column=1),
                      tkinter.Label(window, textvariable=self.vars[7]).grid(row=22,column=1),
                      tkinter.Label(window, textvariable=self.vars[8]).grid(row=24,column=1),
                      tkinter.Label(window, textvariable=self.vars[9]).grid(row=26,column=1),
                      tkinter.Label(window, textvariable=self.vars[10]).grid(row=28,column=1),
                      tkinter.Label(window, textvariable=self.vars[11]).grid(row=30,column=1),
                      tkinter.Label(window, textvariable=self.vars[12]).grid(row=32,column=1),
                      tkinter.Label(window, textvariable=self.vars[13]).grid(row=34,column=1),
                      tkinter.Label(window, textvariable=self.vars[14]).grid(row=36,column=1)]
        i = 0
        for button in self.vars:
            self.vars[i].set("")
            i += 1
        
        self.dice_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.hands_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.dbuttons = [tkinter.Checkbutton(window, variable=self.dice_vars[0]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[1]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[2]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[3]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[4])]    
        self.hbuttons = [tkinter.Checkbutton(window, variable=self.hands_vars[0], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[1], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[2], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[3], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[4], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[5], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[6], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[7], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[8], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[9], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[10], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[11], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[12], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[13], state = 'disabled'),
                         tkinter.Checkbutton(window, variable=self.hands_vars[14], state = 'disabled')]
        i = 0
        for button in self.dbuttons:
            button.grid(row=3, column=3+i)
            i += 1
        i = 0
        for button in self.hbuttons:
            if i <= 10:
                button.grid(row=i+4, column=2)
            else:
                button.grid(row=i+8, column=2)
            i += 2
        
        # horizontal lines
        i = 0
        for x in range(17):
            tkinter.ttk.Separator(window, orient='horizontal').grid(column=0, row=5+i, columnspan=30, sticky = 'we')
            i += 2
            
        self.images = []
        image = Image.open("C:/Users/soder/Downloads/Alea_1.png")
        image = image.resize((30,30))
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
        image = Image.open("C:/Users/soder/Downloads/Alea_2.png")
        image = image.resize((30,30))
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
        image = Image.open("C:/Users/soder/Downloads/Alea_3.png")
        image = image.resize((30,30))
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
        image = Image.open("C:/Users/soder/Downloads/Alea_4.png")
        image = image.resize((30,30))
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
        image = Image.open("C:/Users/soder/Downloads/Alea_5.png")
        image = image.resize((30,30))
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
        image = Image.open("C:/Users/soder/Downloads/Alea_6.png")
        image = image.resize((30,30))
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
            

    def set_players(self, players):
        # tähän looppi riippuen kuinka monta pelaajaa
        self.player_vars = [tkinter.StringVar(), tkinter.StringVar()]
        self.point_vars = [tkinter.StringVar(), tkinter.StringVar()]
        self.bonus_vars = [tkinter.StringVar(), tkinter.StringVar()]
        self.point_vars2 = [tkinter.StringVar(), tkinter.StringVar()]
        i = 0
        for player in self.player_vars:
            self.player_vars[i].set("")
            self.point_vars[i].set("")
            self.bonus_vars[i].set("")
            self.point_vars2[i].set("")
            i += 1
        self.players_names = [tkinter.Label(self.window, text=self.player_vars[0].get()).grid(row=2,column=9),
                              tkinter.Label(self.window, text=self.player_vars[1].get()).grid(row=2,column=11)]
        self.point_labels = [tkinter.Label(self.window, text=self.point_vars[0].get(), font=('Helvetica',10,'bold')).grid(row=16,column=9),
                              tkinter.Label(self.window, text=self.point_vars[1].get(), font=('Helvetica',10,'bold')).grid(row=16,column=11)]
        self.bonus = [tkinter.Label(self.window, text=self.bonus_vars[0].get(), fg='red', font=('Helvetica',9,'bold')).grid(row=18,column=9),
                      tkinter.Label(self.window, text=self.bonus_vars[1].get(), fg='red', font=('Helvetica',9,'bold')).grid(row=18,column=11)]
        self.point_labels2 = [tkinter.Label(self.window, text=self.point_vars2[0].get(), font=('Helvetica',10,'bold')).grid(row=38,column=9),
                              tkinter.Label(self.window, text=self.point_vars2[1].get(), font=('Helvetica',10,'bold')).grid(row=38,column=11)]
        
        tkinter.ttk.Separator(self.window, orient='vertical').grid(column=8, row=2, rowspan=40, sticky = 'ns')
        tkinter.ttk.Separator(self.window, orient='vertical').grid(column=10, row=2, rowspan=40, sticky = 'ns')        
        
        i = 0
        for player in self.players_names:
            self.points = [tkinter.Label(self.window, text="").grid(row=4,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=6,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=8,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=10,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=12,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=14,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=16,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=18,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=20,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=22,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=24,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=26,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=28,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=30,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=32,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=34,column=9+i),
                           tkinter.Label(self.window, text="").grid(row=36,column=9+i)]
            i += 2


    def add_game_logic(self, game):
        self.game = game
        self.turn.set(self.game.get_player_num())
        name = self.players[int(self.turn.get())].get_name()
        self.hand_names[0] = tkinter.Label(self.window, text=name).grid(row=3,column=0)


    def update_possible_hand(self, new_hand, nro):
        ind = self.game.get_player_num()
        if self.players[ind].check_hands()[nro] == 0:
            self.vars[nro].set(new_hand)            
        else:
            return
        

    # käytetääks tätä?
    def update_dice(self, nro):
        self.dices[0] = nro
        
        
    def change(self, i, nro):
        label = tkinter.Label(self.window, image = self.images[nro-1])
        label.image = self.images[nro-1]
        label.grid(row=2, column=3+i)

    
    def throw_dice(self, i):
        nro = randint(1,6)
        label = tkinter.Label(self.window, image = self.images[nro-1])
        label.image = self.images[nro-1]
        label.grid(row=2, column=3+i)
        nro = randint(1,6)
        label.after(200, lambda:self.change(i,nro))
        nro = randint(1,6)
        label.after(400, lambda:self.change(i,nro))
        nro = randint(1,6)
        label.after(600, lambda:self.change(i,nro))
        nro = randint(1,6)
        label.after(800, lambda:self.change(i,nro))
        nro = randint(1,6)
        label.after(1000, lambda:self.change(i,nro))
        nro = randint(1,6)
        label.after(1200, lambda:self.change(i,nro))
        self.dices[i] = nro

        return self.dices[i]

        
    def get_hand(self):
        return self.dices
    

    def get_dices(self, nro):
        for box in self.dbuttons:
            box.configure(state="normal")
        return self.dice_vars[nro].get()
    
    
    def get_window(self):
        return self.window
    
    
    def add_score(self):
        i = 0
        j = 0
        ind = self.game.get_player_num()
        for hand in self.hands_vars:
            if hand.get():
                if self.vars[i].get() == "":
                    self.vars[i].set(0)
                if j <= 10:
                    self.points[i] = tkinter.Label(self.window, text=self.vars[i].get()).grid(row=j+4,column=9+ind+ind)
                else:
                    self.points[i] = tkinter.Label(self.window, text=self.vars[i].get()).grid(row=j+8,column=9+ind+ind)
                    
                self.players[ind].add_hand(i)
                self.players[ind].add_score(self.vars[i].get(), i)
 
                self.point_vars[ind].set(self.players[ind].calculate_mid_points())
                self.point_labels[ind] = tkinter.Label(self.window, 
                                                       text=self.point_vars[ind].get(), font=('Helvetica',10,'bold')).grid(row=16,column=9+ind+ind)     
                self.point_vars2[ind].set(self.players[ind].calculate_points())
                self.point_labels2[ind] = tkinter.Label(self.window, 
                                                       text=self.point_vars2[ind].get(), font=('Helvetica',10,'bold')).grid(row=38,column=9+ind+ind)
                
                if self.players[ind].check_bonus():
                    self.bonus_vars[ind].set("50")
                    self.bonus[ind] = tkinter.Label(self.window, 
                                                       text=self.bonus_vars[ind].get(), fg='red', font=('Helvetica',9,'bold')).grid(row=18,column=9+ind+ind)  
                break
            i += 1
            j += 2


    def add_command_to_button(self, turn):
        self.throw_button.configure(command=turn.roll)
        
        
    def add_players(self, players):
        i = 0
        for player in players:
            self.player_vars[i].set(player.get_name())
            self.players_names[i] = tkinter.Label(self.window, text=self.player_vars[i].get()).grid(row=2,column=9+i+i)
            i += 1


    def change_buttons(self, state):
        if state == 0:
            self.throw_button.configure(state="disabled")
            self.next_button.configure(state="normal")
        else:
            self.throw_button.configure(state="normal")
            self.next_button.configure(state="disabled")
            
            
    def adjust_checboxes(self, hands):
        ind = self.game.get_player_num()
        used_hands = self.players[ind].check_hands()
        i = 0
        buttons_active = 0
        for point in hands:
            if point > 0 and used_hands[i] == 0:
                self.hbuttons[i].configure(state="normal")                
                buttons_active += 1
            i += 1
            
        if buttons_active == 0:
            j = 0
            for hand_not_used in used_hands:
                if hand_not_used == 0:
                    self.hbuttons[j].configure(state="normal")                
                j += 1


    def reset_turn(self):   
        self.add_score()
        for box in self.hbuttons:
            box.deselect()
            box.configure(state="disabled")
        for box in self.dbuttons:
            box.deselect()
            box.configure(state="disabled")
        i = 0
        for button in self.vars:
            self.vars[i].set("")
            i += 1
        self.change_buttons(1)
        self.game.next_round()
        self.turn.set(self.game.get_player_num())
        name = self.players[int(self.turn.get())].get_name()
        self.hand_names[0] = tkinter.Label(self.window, text=name).grid(row=3,column=0)
        
        
    def end_game(self):
        #restart game lisää?
        self.reset_turn()
        self.throw_button.configure(state="disabled")
        self.next_button.configure(state="disabled")