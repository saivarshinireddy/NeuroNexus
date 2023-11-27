def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for i in range(3):
        if all(row[i] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    # If none of the above conditions are met, the player has not won
    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def make_move(board, move, player):
    i, j = move
    if board[i][j] == ' ':
        board[i][j] = player
        return True
    return False

def get_best_move(board, depth):
    best_score = float('-inf')
    best_move = None

    for move in available_moves(board):
        i, j = move
        board[i][j] = 'X'
        score = minimax(board, depth, False)
        board[i][j] = ' '

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return -1
    elif is_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    scores = []

    for move in available_moves(board):
        i, j = move
        board[i][j] = 'X' if is_maximizing else 'O'
        score = minimax(board, depth - 1, not is_maximizing)
        board[i][j] = ' '
        scores.append(score)

    return max(scores) if is_maximizing else min(scores)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        player_move = tuple(map(int, input("Enter your move (row and column, space-separated): ").split()))
        if make_move(board, player_move, 'O'):
            print_board(board)
            if is_winner(board, 'O'):
                print("You win!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            # Computer's move
            print("Computer's move:")
            computer_move = get_best_move(board, depth=3)  # Adjust the depth as needed
            make_move(board, computer_move, 'X')
            print_board(board)

            if is_winner(board, 'X'):
                print("Computer wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

if __name__ == '__main__':
    play_game()
