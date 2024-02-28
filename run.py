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

def user_input(place_ship):
    if place_ship == True:
        while True:
                orientation = input("Choose the orientation of your ship (H or V): \n").upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    print('Please enter a valid orientation: H or V')
        while True:
                row = input("Enter the row number in which you want to place your ship (1-8): \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    print("Please enter a valid number: 1 - 8")
        while True:
                column = input("Enter the column in which you want to place your ship (A-H): \n").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
                else:
                    print('Please enter a valid column letter: A - H')
        return row, column, orientation
    else:
        while True:
                row = input("Guess in which row the opponents ship is (1-8): \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    print('Please enter a valid row number: 1 - 8')
        while True:
                column = input("Guess in which column the opponents ship is (A-H) \n").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
                else:
                    print('Please enter a valid column letter: A - H')
        return row, column

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

place_ships(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)

while True:
    if True:
        print('Guess your opponents battleship location')
        print_board(PLAYER_GUESS_BOARD)
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("Congratulations, You Won!")
        break
    if True:
        turn(COMPUTER_GUESS_BOARD)
        break
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("Sorry, You Lost!")
        break
    
