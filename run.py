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
    # loop through the length of the ships
    for ship_length in LENGTH_OF_SHIPS:
        #loop through until the ship fits and no overlap
        while True:
            if board == COMPUTER_BOARD: #if computer randomly place pieces that fit on board
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ships
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[row][i] = "X"
                        break        

def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True           
    

def ship_overlap(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[row][i]  == "X":
                return True           
    

def user_input():
    pass

def count_hit_ships():
    pass

def turn(board):
    pass

while True:



