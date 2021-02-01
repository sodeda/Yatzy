# Yatzy

Player class:
- gives track of players name and used hands

self.name
self.used_hands


GUI class:
- everything related to GUI

self.window
self.throw_button
self.next_button
self.players
self.dices
self.turn
self.game
self.hand_names
self.dbuttons - checkboxes for dices
self.hbuttons - checkboxes for hands

def __init__(self, window, players) - initializer
def add_command_to_button(self, turn) - links throw button and turn classes roll function
def add_game_logic(self, game) - initializer
def add_players(self, players) - initializer
def add_score(self) - adds score to right player and hand in gui
def adjust_checboxes(self, hands) - adjust available checkboxes normal and others disabled
def change_buttons(self, state) - changes next turn and throw buttons state
def activate_next_turn_button(self) - activates if exactly one checkbox is selected
def get_dices(self, nro) - gives checkboxes
def get_hand(self) - gives dices
def get_window(self) - gives gui window
def set_players(self, players) - initializer
def throw_dice(self, i) - "animates" and throws dices
def update_possible_hand(self, new_hand, points) - shows points in gui for player to choose
def reset_turn(self) - add_scores and resets turn for next player
def end_game(self) - calculates points to gui and shows winner in pop up


Game class:
- games logic

self.round - played rounds/turns
self.players
self.turn_ind - indicates which players turn
self.gui
self.scores - scores class object

def __init__(self, gui, players) - initializer
def add_score(self, points, hand, player) - add players score to scores class
def calculate_scores(self, ind) - calculates players points
def end(self) - ends game and calculates points and winner
def get_player_num(self) - shows whos turn
def next_round(self) - chances turn indicator and checks if all rounds have been played
def start(self) - initializer


Turn class:
- throwing and checking possible hands

self.rolls - how many rolls done in turn
self.hand - dices
self.hands - points from every possible hand, others are 0
self.gui

def __init__(self, gui) - initializer
def roll(self) - roll dices and checks if turn is over
def give_possible_hands(self) - calculates possible hands from thrown dices


Scores class:
- handles all players points

self.players
self.all_points

def __init__(self, players) - initializer
def add_score(self, point, hand, player) - add scores to given players given hand
def check_bonus(self,ind) - checks players bonus reward
def calculate_mid_points(self, ind) - calculate players upper points
def calculate_points(self, ind) - calculates players points
