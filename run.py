import random

LENGTH_OF_SHIPS = [2,3,3,4,5]
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3,'E':4, 'F':5, 'G':6, 'H':7,}

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    for ship_length in LENGTH_OF_SHIPS:
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break

            else:
                place_ship = True
                print('Place your ship. It has a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        print_board(PLAYER_BOARD)
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

def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

def user_input():
    if place_ship == True:
        while True:
            try:
                orientation = input("Choose the orientation of your ship (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Please enter a valid orientation: H or V')
        while True:
            try:
                row = input("Enter the row number in which you want to place your ship (1-8): ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print("Please enter a valid number: 1 - 8")
        while True:
            try:
                column = input("Enter the column in which you want to place your ship (A-H): ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Please enter a valid column letter: A - H')
        return row, column, orientation