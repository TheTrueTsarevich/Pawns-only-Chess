# Board game project
# Abhiyan
# Game name: Pawns-only chess
# 9/11/2022

board = [["O1", "O2", "O3", "O4"],
        ["  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  "],
        ["X1", "X2", "X3", "X4"]]
    
def display_board(board):
    """This displays the board."""

    # To display the board
    for i in range(4):
        print(board[i])


##def findz(boardz, letter):
##    myList = []
##    for i in range(len(boardz)):
##        for t in range(len(boardz)):
##            if str(boardz[i][t]) == letter:
##                myList.append(t)
##                myList.append(i)
##                # print(myList)
##
##    return myList




def play(board, x, y, letter):
    """This plays the selected piece with input on the board."""
    print("Playing at " + str(x) + ","+ str(y))
    a = x
    b = y
    
    # This is a mini-function inside the play function to find the current location
    for i in range(4):
        for t in range(4):

            if board[i][t] == letter:
                n = i
                m = t
                

    # All of the available plays for the side X
    if letter == "X1" or letter == "X2" or letter == "X3" or letter == "X4":
        
        # If the piece is on the left edge of the board
        if m == 0:

            # If the coordinates match the case for a frontal move, move the piece
            if b == n-1 and a == m:
                if board[b][a] == "  ":
                    board[b][a] = letter
                    board[n][m] = "  "                

            # If the coordinates match the case for a right-diagonal attack, move the piece   
            elif b == n-1 and a == m+1:
                if board[b][a] == "O1" or board[b][a] == "O2" or board[b][a] == "O3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the move does match either of these cases when the piece is on the edge of the board, it is invalid
            else:
                print("That was not a valid move, you lost your turn.")

        # If the piece is on the right edge of the board
        elif m == 3:

            # If the coordinates match the case for a frontal move, move the piece
            if b == n-1 and a == m:
                if board[b][a] == "  ":
                    board[b][a] = letter
                    board[n][m] = "  "
                    
            # If the coordinates match a left-diagonal attack, move the piece
            if b == n-1 and a == m-1:
                if board[b][a] == "O1" or board[b][a] == "O2" or board[b][a] == "O3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the move does not match either of these cases when the piece is the on the edge of the board, it is invalid
            else:
                print("That was not a valid move, you lost your turn.")

        # For the piece in any other x position
        else:

            # If the coordinates match the case for a frontal move, move the piece
            if b == n-1 and a == m:
                if board[b][a] == "  ":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the coordinates match a left-diagonal attack, move the piece
            elif b == n-1 and a == m+1:           
                if board[b][a] == "O1" or board[b][a] == "O2" or board[b][a] == "O3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the coordinates match a right-diagonal attack, move the piece
            elif b == n-1 and a == m-1:
                if board[b][a] == "O1" or board[b][a] == "O2" or board[b][a] == "O3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the move does not match either of these cases when the piece is the on the edge of the board, it is invalid
            else:
                print("That was not a valid move, you lost your turn.")
                

            
                
                
    # All of the available plays for the side O
    if letter == "O1" or letter == "O2" or letter == "O3" or letter == "O4":

        # If the piece is on the left edge of the board
        if m == 0:

            # If the coordinates match the case for a frontal move, move the piece
            if b == n+1 and a == m:
                if board[b][a] == "  ":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the coordinates match a right-diagonal attack, move the piece    
            elif b == n+1 and a == m+1:
                if board[b][a] == "X1" or board[b][a] == "X2" or board[b][a] == "X3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the move does not match either of these cases when the piece is the on the edge of the board, it is invalid
            else:
                print("That was not a valid move, you lost your turn.")

        # If the peice is on the right edge of the board
        elif m == 3:

            # If the coordinates match the case for a frontal move, move the piece
            if b == n+1 and a == m:
                if board[b][a] == "  ":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the coordinates match the case for a left-diagonal attack 
            elif b == n+1 and a == m-1:
                if board[b][a] == "X1" or board[b][a] == "X2" or board[b][a] == "X3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the move does not match either of these cases when the piece is the on the edge of the board, it is invalid
            else:
                print("That was not a valid move, you lost your turn.")

        # For the piece in any other x position
        else:

            # If the coordinates match the case for a frontal move, move the piece
            if b == n+1 and a == m:
                if board[b][a] == "  ":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the coordinates match a right-diagonal attack, move the piece
            elif b == n+1 and a == m+1:
                if board[b][a] == "X1" or board[b][a] == "X2" or board[b][a] == "X3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the coordinates match a left-diagonal attack, move the piece
            elif b == n+1 and a == m-1:
                if board[b][a] == "X1" or board[b][a] == "X2" or board[b][a] == "X3" or board[b][a] == "O4":
                    board[b][a] = letter
                    board[n][m] = "  "

            # If the move does not match either of these cases when the piece is the on the edge of the board, it is invalid
            else:
                print("That was not a valid move, you lost your turn.")
                          
                          
def game_won(board):
    """This function checks whether there is a win on either side."""

    # These are all the conditions in which either side can win
    
    if board[0][0] == "X1" or board[0][1] == "X1" or board[0][2] == "X1" or board[0][3] == "X1":
        return "X"
    elif board[0][0] == "X2" or board[0][1] == "X2" or board[0][2] == "X2" or board[0][3] == "X2":
        return "X"
    elif board[0][0] == "X3" or board[0][1] == "X3" or board[0][2] == "X3" or board[0][3] == "X3":
        return "X"
    elif board[0][0] == "X4" or board[0][1] == "X4" or board[0][2] == "X4" or board[0][3] == "X4":
        return "X"
    elif board[3][0] == "O1" or board[3][1] == "O1" or board[3][2] == "O1" or board[3][3] == "O1":
        return "O"
    elif board[3][0] == "O2" or board[3][1] == "O2" or board[3][2] == "O2" or board[3][3] == "O2":
        return "O"
    elif board[3][0] == "O3" or board[3][1] == "O3" or board[3][2] == "O3" or board[3][3] == "O3":
        return "O"
    elif board[3][0] == "O4" or board[3][1] == "O4" or board[3][2] == "O4" or board[3][3] == "O4":
        return "O"
    else:
        return False


import time

# These are the rules, read if you want to know what you are doing

print("This is pawn-only chess.")
time.sleep(1)
print("The rules are as follows:")
time.sleep(1)
print("You can only go forward one space.")
time.sleep(2)
print("You cannot move into a space that is occupied by another piece.")
time.sleep(2)
print("To eat an opponent's piece, it must be one step diagonal to your piece.")
time.sleep(2)
print("To win, you must have at least one piece on the opponent's base line.")
time.sleep(3)

display_board(board)
print("The game shall begin...")
time.sleep(2)

# While nobody is winning, the while loop with continue
while game_won(board) == False:
    print("It is X's turn.")
    print("Which piece would you like to move?")

    # Which piece is moved
    letter = input()

    print("Which Y-coordinate do you want to move your piece")

    # The Y-coordinate of where the user wants to move 
    y = int(input())
    print("What column is it in?")

    # The X-coordinate of where the user wants to move
    x = int(input())

    # Initiates play function (already explained), and then displays the board
    play(board, x, y, letter)
    display_board(board)
      

    # Checks if X has won the game after their move, and if so, break loop and declare winner
    if game_won(board) == "X":
        print(str(game_won(board)) + " has won the game")
        break

    # If no win on X side, move on to O side
    else:
        print("It is O's turn.")
        print("Which piece would you like to move?")

        # Which piece is moved
        letter = input()

        print("Which Y-coordinate do you want to move your piece to?")

        # The Y-coordinate of where the user wants to move
        y = int(input())
        print("What column is it in?")

        # The X-coordinate of where the user wants to move
        x = int(input())

        # Initiates play function (already explained), and then displays the board
        play(board, x, y, letter)
        display_board(board)

        # Checks if O has won the game after their move, and if so, break loop and declare winner
        if game_won(board) == "O":
            print(str(game_won(board)) + " has won the game")
            break
    






