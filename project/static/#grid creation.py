#grid creation
grid = []
line = []
for i in range (3):
    for j in range (3):
        line.append(" ")
    grid.append(line)
    line = []
 
#grid printing
def print_grid():
    for i in range(3):
        print("|", end ="")
        for j in range(3):
            print (grid[i][j], "|", end ="")
        print("")
         
#player turn
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"It's {player2}'s turn")
    else:
        turn_player1 = True
        print(f"It's {player1}'s turn")        
    return turn_player1
 
#choosing cell
def write_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3   
    if turn_player1 == True:
        grid[i][j] = player1_symbol
    else:
        grid[i][j] = player2_symbol
    return grid
 
#checking cell
def free_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3
    if grid[i][j] == player1_symbol or grid[i][j] == player2_symbol:
        print("This cell is not free")
        return False
    return True
 
#game opening
print("Welcome to the Tic-Tac-Toe !")
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
 
#win check
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
    for i in range (3):
        for j in range (3):
            for k in range (3):
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
    for i in range (3):
        for j in range (3):
            for k in range (3):
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
    for i in range (3):
        for j in range (3):
            for k in range (3):
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
        return game, winner
 
#game
while game == True:
    turn_player1 = player_turn(turn_player1)
    free_box = False
    while free_box == False:
        cell = int(input("Please enter a number for your case (1 to 9 from left to right and from top to bottom) : "))
        free_box = free_cell(cell)
    grid = write_cell(cell)
    print_grid()
    game, winner = win_check(grid, player1_symbol, player2_symbol)
     
#end of game
if winner == player1:
    print(f"Winner is {player1} !")
elif winner == player2:
    print(f"Winner is {player2} !")
else:
    print(f"Grid is full : equality for {player1} and {player2} !")