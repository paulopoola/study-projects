#!/usr/bin/env python
# coding: utf-8

# In[2]:


# TIC TAC TOE GAME 
from IPython.display import clear_output

def display_board(board):
    
    #this is a "clear screen/output command below works only on jupyter otherwise use 'print('\n'*100)'"
    clear_output()
    print('\n')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    
def player_input():
    choice = ''
    
    # asks the player to make a choice
    
    while choice != 'X' and choice != 'O':
        choice = input('Player1, choose between X and O : ').upper()
        
  
    #player2 is has to be can't have same choice as player1
    if choice == 'X':
        return('X', 'O')
    
    else:
        return('O', 'X')
    
def place_choice(board, choice, position):
    board[position] = choice
    
    
def win_check(board, choice):
    #Checking to see if theres any three consecutive 'X' or 'O' choices across the diagonal, horizonal and vertical.
    return (board[7] == board[8] == board[9] == choice or  # across the top row
    board[4] == board[5] == board[6] == choice  or         # across the middle row
    board[1] == board[2] == board[3] == choice  or         # across the bottom row
    board[7] == board[5] == board[3] == choice  or         # across the diagonal from left top to right bottom or vice versa
    board[1] == board[5] == board[9] == choice  or         # across the diagonal from left bottom to top right or vice versa
    board[7] == board[4] == board[1] == choice  or         # across the first column 
    board[8] == board[5] == board[2] == choice  or         # across the middle column
    board[9] == board[6] == board[3] == choice  )          #across the 3rd column
     

import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'
    
    
    
def space_check(board, position):
    
    return board[position] == ' '




def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    # if i returns true for space_check therefore board isnt full.
    return True



def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to TIC TAC TOE !')

while True:
    
    # Set the game up here ( turn, who goes first, choice X or O)
    the_board = [' '] * 10
    player1_choice, player2_choice = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to Play?, Y OR N').lower()
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
# Player 1 Turn
    while game_on:
        if turn == 'Player1':
            #show the board
            display_board(the_board)
            #choose the position
            position = player_choice(the_board)
            #place marker on the position choosen
            place_choice(the_board, player1_choice, position)
            #check if they won
            if win_check(the_board, player1_choice):
                display_board(the_board)
                print('PLAYER 1 WINS!!!')
                game_on = False
            #check for a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME TIED')
                    game_on = False
                else: 
                    turn = 'Player2'
                
            
            
        else:
            #show the board
            display_board(the_board)
            #choose the position
            position = player_choice(the_board)
            #place marker on the position choosen
            place_choice(the_board, player2_choice, position)
            #check if they won
            if win_check(the_board, player2_choice):
                display_board(the_board)
                print('PLAYER 2 WINS!!!')
                game_on = False
            #check for a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME TIED')
                    game_on = False
                else: 
                    turn = 'Player1'
    if not replay():
        break


# #### 

# In[ ]:


7

win_check(test_board,'o')


# In[ ]:




