# Tic Tac Toe Game

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    return (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    )

# Function to make a move
def make_move(player, position):
    board[position] = player

# Function to play the game
def play_game():
    print('Welcome to Tic Tac Toe!')
    print_board()
    player = 'X'
    while True:
        position = int(input('Player ' + player + ', enter your move (0-8): '))
        if board[position] == ' ':
            make_move(player, position)
            print_board()
            if check_winner(player):
                print('Player ' + player + ' wins!')
                break
            if is_board_full():
                print('It\'s a tie!')
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

# Start the game
play_game()
