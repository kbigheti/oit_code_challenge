import os

#the variable board contains empty spaces that represents the positions of the board
board = [' ' for x in range(10)]

#inserts the letter X or O in the desired spot
def insertBoard(letter, position):
    board[position] = letter
    
#the funciton prints the board each either the player or the computer makes a move
def displayBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#checks if the spot is free on the board
def freeSpot(position):
    return board[position] == ' '

#this function allows the player to make a move by selecting a specific position on the board (1-9),
#and alos checks if the position is free or not.
def player():
    turn = True
    while turn:
        move = input("\nSelect a specific position to make your move (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freeSpot(move):
                    turn = False
                    insertBoard('X', move)
                else:
                    print("\n---THIS SPOT IS ALREADY TAKEN!---")
            else:
                print("\nPLEASE TYPE A NUMBER BETWEEN 1-9")
        except:
            print("\nRemember, type a number (1-9)!")
            
def comp():
   
    #the possMoves variable checks all the spots and if they are empty or not
    possMoves = [x for x, letter in enumerate(board) if letter == ' ' and x !=0]
    move = 0
    
    #here we create a copy of the board that places the letter 'O' in the spot that is empty
    for letter in ['O', 'X']:
        for i in possMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move
    
    #here the computer checks if the center is open
    if 5 in possMoves:
        move = 5 
        return move
    
    #here the computer checks for open corners
    openCorner = []
    for i in possMoves:
        if i in [1, 3, 7, 9]:
            openCorner.append(i)
    if len(openCorner) > 0:
        move = random(openCorner)
        return move
   
    #here the computer checks for open edges
    openEdges = []
    for i in possMoves:
        if i in [2, 4, 6, 8]:
            openEdges.append(i)
    if len(openEdges) > 0:
        move = random(openEdges)
    
    return move 
        
def random(list):
    import random
    length = len(list)
    rnumber = random.randrange(0,length) 
    return list[rnumber]

#returns true if the board is full and false is not
def boardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#the winner function will check horizontally, vertically, and diagonally if the letters are the same.
def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (
            board[4] == letter and board[5] == letter and board[6] == letter) or (
            board[7] == letter and board[8] == letter and board[9] == letter) or (
                
            board[1] == letter and board[4] == letter and board[7] == letter) or (
            board[2] == letter and board[5] == letter and board[8] == letter) or (
            board[3] == letter and board[6] == letter and board[9] == letter) or (
            
            board[1] == letter and board[5] == letter and board[9] == letter) or (
            board[3] == letter and board[5] == letter and board[7] == letter)

def main():

    os.system('clear')
    
    print("\n\n\n-------WELCOME TO THE MOST SIMPLE TIC TAC TOE YOU WILL EVER PLAY!!!-------\n")
    input("---PRESS ENTER TO CONTINUE...---")

    os.system('clear')
    
    print("In this game you will be the letter 'X' and the CPU will be the letter 'O'.\n")
    input("PRESS ENTER TO START PLAYING...")
            
    displayBoard(board)
        
    while not (boardFull(board)):
        if not(isWinner(board, 'O')):
            player()
            displayBoard(board)
        else:
            print('\n---THE COMPUTER WON!!!---')
            break
            
        if not(isWinner(board, 'X')):
            move = comp()
            if move == 0:
                print("\n---ITS A TIE!---")
            else:
                insertBoard('O', move)
                print("The CPU made a move and placed 'O' in the position", move)
                displayBoard(board)
        else:
            print('\n---YOU WON---!!!')
            break
        
while True:
    again = input('Do you want to play again? (Y/N): ')
    if again.lower() == 'y' or again.lower == 'yes':
        os.system('clear')
        board = [' ' for x in range(10)]
        main()
    else:
        break


