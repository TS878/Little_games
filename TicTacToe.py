# TicTacToe

###Imports###
import random

###Functions###
def draw_board(board):
    # This function prints out the board that it was passed.
    
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter():
    # Lets the player type which letter they want to be.
    
    # Returns a list with the player's letter as the first item an the 
    ## computer's as the secound
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want your letter to be X or O?:\n').upper()
            
    if letter == 'X':
        return ['X','O']
    elif letter == 'O':
        return ['O','X']

def who_goes_first():
    # Randomly choose which player goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makes_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    # Given a board and a player's letter, this function returns true if 
    ## the player has won.
    # We use bo instead of "board" and "le" instead of letter so we don't
    ## have to type as much.
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Top row across
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Middle row across
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Bottom row across
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Left row donwn
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Middle row down
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Right row down
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diahonal

def get_board_copy(board):
    # Makes a copy of the board list and return it.
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def is_space_free(board, move):
    # Rrue if the passed move is free on the passed board.
    return board[move] == ' '

def get_player_move(board):
    # Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not\
    is_space_free(board, int(move)):
        move = input('What is your next move?:\n')
        return int(move)
        
def choose_random_move_from_list(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
            
        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None

def get_computer_move(board,computer_letter):
    # Given a board and the computer's letter, determine where to move and 
    ## return that move.
    
    if computer_letter == 'X':
        player_letter == 'O'
    else:
        player_letter == 'X'
        
        # First, check if we can win in the next move
        for i in range(1,10):
            board_copy = get_board_copy(board)
            if is_space_free(board_copy, i):
                makes_move(board_copy, computer_letter, i)
                if is_winner(board_copy, computer_letter):
                    return i
        # Check if player could win their next move and block them.
        for i in range(1,10):
            board_copy = get_board_copy(board)
            if is_space_free(board_copy, i):
                makes_move(board_copy,player_letter, i)
                if is_winner(board_copy, player_letter):
                    return i
        # Try to take one of the conners, if they are free
        move = choose_random_move_from_list(board,[1,3,7,9])
        if move != None:
            return move
        
        # Try to take the middle, if it is free.
        if is_space_free(board, 5):
            return 5
        
        # Move on one of the sides, if it is free.
        return choose_random_move_from_list(board, [2,4,6,8])

def is_board_full(board):
    # Return True if every space is taken. otherwise return False.
    for i in range(1,10):
        if is_space_free(board, i):
            return False
    return True

###Main Program###
print('Welcome to Tic-Tac-Toe')

while True:
    # Reset the board.
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The %s will go first' % turn)
    game_is_playing = True
    
    while game_is_playing == True:
        if turn == 'player':
            # Player's turn
            draw_board(the_board)
            move = get_player_move(the_board)
            makes_move(the_board, player_letter, move)
            
            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn.
            move = get_computer_move(the_board, computer_letter)
            makes_move(the_board, computer_letter,move)
            
            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player'
    print('Do you want to play again? (yes of no)')
    if not input().lower().startswith('y'):
        break
