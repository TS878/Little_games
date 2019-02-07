# Sonar Treasure Hunt
###Imports###
import random
import sys
import math
###Functions###
def get_new_board():
    # Create a 60x15 board data structure.
    board = []
    for x in range(60): # The main list is a list of 60 lists.
        board.append([])
        for y in range(15):
            # Each list in the main list has 15 single-character strings.
            # Use different characters for the ocean to make it more readable.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def draw_board(board):
    # Draw the board data structure.
    tens_digits_line = ' '
    # Initial space for the numbers down the left side of the board.
    for i in range(1,6):
        tens_digits_line += (' ' * 9) + str(i)
        
    # Print the numbers acrros the top of the board.
    print(tens_digits_line)
    print(' ' +('0123456789'*6))
    print()
    
    # Print each of the 15 rows.
    for row in range(15):
        # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''
        
        # Create the string for this row on the board
        board_row = ''
        for column in range(60):
            board_row += board[column][row]
        print('%s%s%s%s' % (extra_space,row,board_row,row))
        
    # Print the numbers across the bottom of the board.
    print()
    print(' ' + ('0123456789' * 6))
    print(tens_digits_line)

def get_random_chest(num_chest):
    # Create a list of chest data structures (two-item list of x,y coordinates)
    chests = []
    while len(chests) < num_chest:
        new_chest = [random.randint(0,59), random.randint(0,14)]
        if new_chest not in chests: 
            chests.append(new_chest)
    return chests
def is_on_board(x, y):
    # Return True if the coordinates are on the board; otherwise, return False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14
    
def make_move(board, chest, x, y):
    # Change the board data structure with a sonar device character.
    # Remove treasure chests from the chests list as they are found.
    # Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    smallest_distance = 100
    for cx, cy in chest:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
    
        if distance < smallest_distance:
            smallest_distance = distance
    smallest_distance = round(smallest_distance)
    
    if smallest_distance == 0:
        # xc is directly on a treasure chest!
        chest.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return 'Treasure detected at a distance of %s.'% smallest_distance
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything.'
def enter_player_move(previous_moves):
    # Let the player enter their move. Return a two-item list of coordinates.
    print('Where do you want to drop the next sonar device?(0-59 0-14)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and \
is_on_board(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previous_moves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]
        print('''Enter a number from 0 to 59, a space, then a number from 0 \
to 14.''')

def show_instructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. your current \
mission is to use sonar devices to find three sunken treasure chest at the \
bottom of the ocean. But you only have cheap sonar that finds the distance \
not direction. Enter the coordinates to drop 
a sonar device. The ocean map will be marked with how far away the nearest \
chest is, or an X if it is beyond the sonar device's range. For example, the \
C marks are where chests are. The sonar device shows a 3 because the closest \
chest is 3 spaces away.
        1         2         3
          012345678901234567890123456789012

         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
         2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
         3 ````````~~~`````~~~`~`````~`~``~` 3
         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

           012345678901234567890123456789012
         1         2         3
(In the real game, the chests are not visible in the ocean.)

 Press enter to continue...''')
    input()
    print('''Where you drop a soar device directly on a chest you retrieve it \
 and the other sonar devices update to show how far away the next nearest \
 chest is. The chest are beyond the range of the sonar device on the left, so \
 it shows an X.
 1         2         3
           012345678901234567890123456789012
           
         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
         2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
         3 ````````~~~`````~~~`~`````~`~``~` 3
         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

           012345678901234567890123456789012
                     1         2         3

The treasure chest don't move around. Sonar devices can detect treasure up to \
a distance of 9 spaces. Try to collect all 3 chest before running out of \
sonar devices. Good luck!

Press enter to continue...''')
    input()


###Main Program###
print('S O N A R !')
print()
print('Would you like to veiw the instructions ? (yes/no)')
if input().lower().startswith('y'):
    show_instructions()

while True:
    # Game setup
    sonar_devices = 20
    the_board = get_new_board()
    the_chest = get_random_chest(3)
    draw_board(the_board)
    previous_moves = [ ]
    
    while sonar_devices > 0:
        # Show sonar device and chest statuses
        print('You have %s sonar device(s) left.' % sonar_devices, end = ' ')
        print('%s treasure chest(s) remaining.' % len(the_chest))
        x, y = enter_player_move(previous_moves)
        previous_moves.append([x, y])
        
        move_results = make_move(the_board, the_chest, x, y)
        if move_results == False:
            continue
        else:
            if move_results == 'You have found a sunken treasure chest!':
                for x,y in previous_moves:
                    make_move(the_board, the_chest, x, y)
            draw_board(the_board)
            print(move_results)
        if len(the_chest) == 0:
            print('You have found all the sunken treasure chests!', end = ' ')
            print('Congratulations and good game!')
            break
        sonar_devices -= 1
    if sonar_devices == 0:
        print("We've run out of sonar devices! Now we have to turn" ,end=' ')
        print("the ship around and head")
        print("for home with treasure chest still out there! Game over")
        print('    The remaining chests were here:')		
        for x, y in the_chest:		
            print('    %s, %s' % (x, y))
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        sys.exit()
