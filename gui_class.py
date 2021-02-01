# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:46:23 2020

@author: soderdahl
"""


import tkinter
import tkinter.ttk
from random import randint
from PIL import Image, ImageTk


class GUI:
    def __init__(self, window, players):
        self.window = window
        
        # add buttons
        self.throw_button = tkinter.Button(window, text="Throw")
        self.throw_button.grid(row=1,column=1)
        self.next_button = tkinter.Button(window, text="Next turn", command=self.reset_turn, state="disabled")
        self.next_button.grid(row=1,column=0)
        
        # sets players
        self.players = players
        self.set_players(players)

        # labels for dices
        self.dices = [tkinter.Label(window, text="", width=5, height=2).grid(row=2,column=3),
                      tkinter.Label(window, text="", width=5, height=2).grid(row=2,column=4),
                      tkinter.Label(window, text="", width=5, height=2).grid(row=2,column=5),
                      tkinter.Label(window, text="", width=5, height=2).grid(row=2,column=6),
                      tkinter.Label(window, text="", width=5, height=2).grid(row=2,column=7)]
        
        # dice images
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
        
        # tkinter variables for labels
        self.turn = tkinter.StringVar() # indicates whos turn
        # text for hands
        self.vars = [tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),
                     tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),
                     tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar()]
        # for checkboxes
        self.dice_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        self.hands_vars = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),
                           tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        
        # labels for all hands and points (first element is turn indicator)
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
        
        # text for hands
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
        
        # checkboxes
        self.dbuttons = [tkinter.Checkbutton(window, variable=self.dice_vars[0]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[1]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[2]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[3]),
                         tkinter.Checkbutton(window, variable=self.dice_vars[4])]    
        self.hbuttons = [tkinter.Checkbutton(window, variable=self.hands_vars[0], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[1], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[2], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[3], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[4], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[5], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[6], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[7], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[8], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[9], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[10], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[11], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[12], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[13], state = 'disabled', command=self.activate_next_turn_button),
                         tkinter.Checkbutton(window, variable=self.hands_vars[14], state = 'disabled', command=self.activate_next_turn_button)]
        
        # set all hands ""
        i = 0
        for var in self.vars:
            self.vars[i].set("")
            i += 1
            
        # set checkboxes to grid
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
            
            
    def add_command_to_button(self, turn):
        self.throw_button.configure(command=turn.roll)
        
        
    # adds game loic to gui
    def add_game_logic(self, game):
        self.game = game
        
        # turn text
        self.turn.set(self.game.get_player_num())
        name = self.players[int(self.turn.get())].get_name()
        self.hand_names[0] = tkinter.Label(self.window, text=name).grid(row=3,column=0)


    # adds players to guis variables  
    def add_players(self, players):
        i = 0
        for player in players:
            self.player_vars[i].set(player.get_name())
            self.players_names[i] = tkinter.Label(self.window, text=self.player_vars[i].get()).grid(row=2,column=9+i+i)
            i += 1
            
            
    def add_score(self):
        i = 0
        j = 0
        ind = self.game.get_player_num()
        
        # finds what hand to add
        for hand in self.hands_vars:
            if hand.get():
                
                # zero points/missed points/crossed over
                if self.vars[i].get() == "":
                    self.vars[i].set(0)
                    
                # before bonus points/upper points
                if j <= 10:
                    self.points[i] = tkinter.Label(self.window, text=self.vars[i].get()).grid(row=j+4,column=9+ind+ind)
                
                # under bonus points
                else:
                    self.points[i] = tkinter.Label(self.window, text=self.vars[i].get()).grid(row=j+8,column=9+ind+ind)
                
                # marks added hand to player and adds points to scoretable
                self.players[ind].add_hand(i)
                self.game.add_score(self.vars[i].get(), i, ind)
 
                # calculate mid points, all points and checks bonus
                points = self.game.calculate_scores(ind)
    
                # adds points to gui
                self.point_vars[ind].set(points[0])
                self.point_labels[ind] = tkinter.Label(self.window, 
                                                       text=self.point_vars[ind].get(), font=('Helvetica',10,'bold')).grid(row=16,column=9+ind+ind)     
                self.point_vars2[ind].set(points[1])
                self.point_labels2[ind] = tkinter.Label(self.window, 
                                                       text=self.point_vars2[ind].get(), font=('Helvetica',10,'bold')).grid(row=38,column=9+ind+ind)
                
                # adds bonus to gui
                if points[2]:
                    self.bonus_vars[ind].set("50")
                    self.bonus[ind] = tkinter.Label(self.window, 
                                                       text=self.bonus_vars[ind].get(), fg='red', font=('Helvetica',9,'bold')).grid(row=18,column=9+ind+ind)  
                break
            
            i += 1
            j += 2
            
    
    # activates only available hands      
    def adjust_checboxes(self, hands):
        ind = self.game.get_player_num()
        used_hands = self.players[ind].check_hands()
        i = 0
        buttons_active = 0
        for point in hands:
            
            # checks if it is not used before
            if point > 0 and used_hands[i] == 0:
                self.hbuttons[i].configure(state="normal")                
                buttons_active += 1
            i += 1
            
        # if none found how all not used hands for crossover
        if buttons_active == 0:
            j = 0
            for hand_not_used in used_hands:
                if hand_not_used == 0:
                    self.hbuttons[j].configure(state="normal")                
                j += 1  
                
                
    # changes which is active
    def change_buttons(self, state):
        if state == 0:
            self.throw_button.configure(state="disabled")
        else:
            self.throw_button.configure(state="normal")
            self.next_button.configure(state="disabled")
            
    
    # activates next_button only if exactly one checbox is selected         
    def activate_next_turn_button(self):
        if self.next_button['state'] == "disabled":
            i = 0
            for checker in self.hands_vars:
                if checker.get() == 1:
                    i += 1
            if i == 1:
                self.next_button.configure(state="normal")
        else:
            self.next_button.configure(state="disabled")
            
            
    # checks what checkboxes/dices are selected
    def get_dices(self, nro):
        for box in self.dbuttons:
            box.configure(state="normal")
        return self.dice_vars[nro].get()

     
    def get_hand(self):
        return self.dices
    
    
    def get_window(self):
        return self.window
    
    
    def set_players(self, players):
        self.player_vars = []
        self.point_vars = []
        self.bonus_vars = []
        self.point_vars2 = []
        self.players_names = []
        self.point_labels = []
        self.bonus = []
        self.point_labels2 = []
        
        i = 0
        j = 0 # for vertical lines
        for player in players:
            
            # tkinter variables for all players
            self.player_vars.append(tkinter.StringVar())
            self.point_vars.append(tkinter.StringVar())
            self.bonus_vars.append(tkinter.StringVar())
            self.point_vars2.append(tkinter.StringVar())
            
            # all set to ""
            self.player_vars[i].set("")
            self.point_vars[i].set("")
            self.bonus_vars[i].set("")
            self.point_vars2[i].set("")

            # sets and initializes player name and different points
            self.players_names.append(tkinter.Label(self.window, text=self.player_vars[i].get()).grid(row=2,column=9+j))
            self.point_labels.append(tkinter.Label(self.window, text=self.point_vars[i].get(), font=('Helvetica',10,'bold')).grid(row=16,column=9+j))
            self.bonus.append(tkinter.Label(self.window, text=self.bonus_vars[i].get(), fg='red', font=('Helvetica',9,'bold')).grid(row=18,column=9+j))
            self.point_labels2.append(tkinter.Label(self.window, text=self.point_vars2[i].get(), font=('Helvetica',10,'bold')).grid(row=38,column=9+j))
            self.points = [tkinter.Label(self.window, text="").grid(row=4,column=9+i),
                   tkinter.Label(self.window, text="").grid(row=6,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=8,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=10,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=12,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=14,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=16,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=18,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=20,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=22,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=24,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=26,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=28,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=30,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=32,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=34,column=9+j),
                   tkinter.Label(self.window, text="").grid(row=36,column=9+j)]
            
            # vertical lines between players
            tkinter.ttk.Separator(self.window, orient='vertical').grid(column=8+j, row=2, rowspan=40, sticky = 'ns')
                
            i += 1
            j += 2
        
    
    # helper function for throwing dices
    def change(self, i, nro):
        label = tkinter.Label(self.window, image = self.images[nro-1])
        label.image = self.images[nro-1]
        label.grid(row=2, column=3+i)

    
    # "animates" throwing
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
    
    
    # updates possible hand that are given to gui
    def update_possible_hand(self, new_hand, points):
        ind = self.game.get_player_num()
        if self.players[ind].check_hands()[points] == 0:
            self.vars[points].set(new_hand)            
        else:
            return


    # resets gui for new turn
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