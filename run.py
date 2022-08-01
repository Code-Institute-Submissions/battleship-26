import random

LENGTH_OF_SHIPS = [2,3,3,4,5] # Length of ships
PLAYER_BOARD = [[" "] * 8 for i in range(8)] #the player board
COMPUTER_BOARD = [[" "] * 8 for i in range(8)] 
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} #list for letters to numbers

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board: #loop through board
        print("%d|%s|" % (row_number, "|".join(row))) #decimal and string print
        row_number += 1

def place_ships(board):
    pass

def check_ship_fit():
    pass

def ship_overlap():
    pass

def user_input():
    pass

def count_hit_ships():
    pass

def turn(board):
    pass

while True:



