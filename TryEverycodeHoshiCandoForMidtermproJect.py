import datetime
import time

def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    print('   1   2   3   4   5   6   7 ')
    print(' ' + '-' * 29)
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print(' ' + '-' * 29)
    print('   1   2   3   4   5   6   7 ')

def is_valid_move(board, column):
    return column >= 0 and column < 7 and board[0][column] == ' '

def drop_disc(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            break

def check_winner(board, player):     
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + i][col + 3 - i] == player for i in range(4)):
                return True
    
    return False

def if_board_full(board):
    return all(board[0][col] != ' ' for col in range(7))

def record_results(result, elapsed_time, player1, player2):
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('connect_four_results.txt', 'a') as file:
        file.write(f"{formatted_date} | {player1} vs {player2} | {result} | Time: {elapsed_time:.2f} seconds\n")

def main():
    player1 = input("Enter Player X's name: ")
    player2 = input("Enter Player O's name: ")
    
    board = create_board()
    current_player = 'X'
    
    start_time = time.time()
    print('  Welcome to Connect Four!  ')

    while True:      
        print_board(board)
        move = input(f'Player {current_player}, choose a column (1-7) (Type "quit" to exit): ')

        if move.lower() == 'quit':
            end_time = time.time()
            print('See you next time!')
            break

        try:
            column = int(move) - 1
            
        except ValueError:
            print("Invalid input. Please enter a valid column number.")
            continue

        if is_valid_move(board, column):
            drop_disc(board, column, current_player)
            if check_winner(board, current_player):
                print_board(board)
                winner = player1 if current_player == 'X' else player2
                print(f"Congratulations, {winner} wins!")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Total time spent: {elapsed_time:.2f} seconds")
                record_results(f"{winner} wins", elapsed_time, player1, player2)
                break
            elif if_board_full(board):
                print_board(board)
                print("It's a tie!")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Total time spent: {elapsed_time:.2f} seconds")
                record_results("Tie", elapsed_time, player1, player2)
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('!Invalid move! Please choose a valid column.')

if __name__ == '__main__':
    main()
