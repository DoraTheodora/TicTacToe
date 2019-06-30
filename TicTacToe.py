from IPython.display import clear_output
################################################################
def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
################################################################
def player_input():
    '''
    Output is a tuple: player 1 marker, player 2 marker
    '''
    gotIt = True
    marker = input("Player1 your marker X or O: ").upper()
    if (marker == 'X' or marker == 'O'):
        gotIt == True
    else:
        gotIt = False
        
    while gotIt == False:
        marker = input("Insert your marker X or O: ")
        if (marker == 'X' or marker == 'O'):
            gotIt = True
            break
   
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
################################################################
def place_marker(board, marker, position):
    board[position] = marker
################################################################
def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker))
################################################################
import random
def choose_first():
    flip = random.randint(0,1)
    if(flip == 0):
        return "Player1"
    else:
        return "Player2"
################################################################
def space_check(board, position):
    return board[position] == ' '
################################################################
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
################################################################
def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input("Choose position: "))
	return position
################################################################
def replay():
    answer = input("Play again!? ")
    if answer == "Yes": 
        return True
###################################################################
###################################################################
###################################################################
while True:
    the_board = [' ']*10
    display_board(the_board)
    player1Marker, player2Marker = player_input()
    
    turn = choose_first()
    print(turn  +  " will go first.")
    
    playing = True
    while playing:
        if turn == "Player 1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1Marker, position)
            
            if win_check(the_board, player1Marker):
                display_board(the_board)
                print("Player 1 HAS WON!")
                playing = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    playing = False
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2Marker, position)
            
            if win_check(the_board, player2Marker):
                display_board(the_board)
                print("Player 2 HAS WON!")
                playing = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    playing = False
                else:
                    turn = "Player 1"
        
    if not replay():
        break