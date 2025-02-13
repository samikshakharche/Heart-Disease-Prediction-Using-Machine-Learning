import math

# Grid initialization
grid = []
line = []
for i in range(3):
    for j in range(3):
        line.append(" ")
    grid.append(line)
    line = []

# Grid printing
def print_grid():
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(grid[i][j], "|", end="")
        print("")

# Player turn
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"It's {player2}'s turn")
    else:
        turn_player1 = True
        print(f"It's {player1}'s turn")
    return turn_player1

# Choosing cell
def write_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j = cell % 3
    if turn_player1 == True:
        grid[i][j] = player1_symbol
    else:
        grid[i][j] = player2_symbol
    return grid

# Checking cell
def free_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j = cell % 3
    if grid[i][j] == player1_symbol or grid[i][j] == player2_symbol:
        print("This cell is not free")
        return False
    return True

# Game opening
print("Welcome to the Tic-Tac-Toe!")
print("")
print_grid()
print("")
player1 = input("Please enter name of player 1 : ")
player1_symbol = input("Please enter the symbol of player 1 : ")
player2 = input("Please enter name of player 2 : ")
player2_symbol = input("Please enter the symbol of player 2 : ")
game = True
full_grid = False
turn_player1 = False
winner = ""

# Heuristic function to evaluate board states
def evaluate_board(board, player):
    score = 0
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] == player:
            score += 10
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] == player:
            score += 10
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == player:
            score += 10
        if board[0][2] == board[1][1] == board[2][0] == player:
            score += 10
    return score

# DLS implementation
def dls(board, depth, player, alpha, beta):
    if depth == 0 or check_winner(board) != None:
        return evaluate_board(board, player)
    if player == player1:
        best_value = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    value = dls(board, depth - 1, player2, alpha, beta)
                    board[i][j] = " "
                    best_value = max(best_value, value)
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        break
        return best_value
    else:
        best_value = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    value = dls(board, depth - 1, player1, alpha, beta)
                    board[i][j] = " "
                    best_value = min(best_value, value)
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break
        return best_value

# Win check
def win_check(grid, player1_symbol, player2_symbol):
    full_grid = True
    player1_symbol_count = 0
    player2_symbol_count = 0
    #checking rows
    for i in range(3):
        for j in range(3):
            if grid[i][j] == player1_symbol:
                player1_symbol_count += 1
                player2_symbol_count = 0
                if player1_symbol_count == 3:
                    game = False
                    winner = player1
                    return game, winner
            if grid[i][j] == player2_symbol:
                player2_symbol_count += 1
                player1_symbol_count = 0
                if player2_symbol_count == 3:
                    game = False
                    winner = player2
                    return game, winner
            if grid[i][j] == " ":
                full_grid = False

        player1_symbol_count = 0
        player2_symbol_count = 0
    #checking columns
    player1_symbol_count = 0
    player2_symbol_count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i + k <= 2:
                    if grid[i + k][j] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
                if grid[i][j] == " ":
                    full_grid = False

        player1_symbol_count = 0
        player2_symbol_count = 0
    #checking diagonals
    player1_symbol_count = 0
    player2_symbol_count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if j + k <= 2 and i + k <= 2:
                    if grid[i + k][j + k] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j + k] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
                if grid[i][j] == " ":
                    full_grid = False

            player1_symbol_count = 0
            player2_symbol_count = 0

        player1_symbol_count = 0
        player2_symbol_count = 0

    player1_symbol_count = 0
    player2_symbol_count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if j - k >= 0 and i + k <= 2:
                    if grid[i + k][j - k] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j - k] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
                if grid[i][j] == " ":
                    full_grid = False

        player1_symbol_count = 0
        player2_symbol_count = 0

    #full grid or not
    if full_grid == True:
        game = False
        winner = ""
        return game, winner
    else:
        game = True
        winner = ""
        return