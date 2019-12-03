########################   user vs user #################################



def print_board(grid):
    print('Current board:')
    for row in grid:
        for piece in row:
            print(piece, end=' ')
        print()
    print()


# Gets the next (row,column) move from the current player
def get_move(grid, player):
    print(player, 'turn:')
    row = int(input('Enter row（0-2）: '))
    col = int(input('Enter column （0-2）: '))

    # This should really check to see that the position is empty
    # and that the row,col is a valid position (not too big or too small)
    grid[row][col] = player


# Returns whether player got 3 in a row
def winner(grid, player):
    # on a row
    # row 0 (top row)
    if grid[0][0] == grid[0][1] == grid[0][2] == player:
        return True

    # row 1 (middle row)
    if grid[1][0] == grid[1][1] == grid[1][2] == player:
        return True

    # row 2 (bottom row)
    if grid[2][0] == grid[2][1] == grid[2][2] == player:
        return True

    # on a column
    # column 0 (left column)
    if grid[0][0] == grid[1][0] == grid[2][0] == player:
        return True

    # column 1 (middle column)
    if grid[0][1] == grid[1][1] == grid[2][1] == player:
        return True

    # column 2 (right column)
    if grid[0][2] == grid[1][2] == grid[2][2] == player:
        return True

    # on a diagonal \
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True

    # on a diagonal /
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    return False


# Returns whether the board is full
def full(grid):
    for row in grid:
        for piece in row:
            if piece == '_':
                return False
    return True


########Main program goes below here###########
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

turn = 'X'

print_board(board)

# while the board is not full
while not full(board):
    # get the next move
    get_move(board, turn)

    # print the board
    print_board(board)

    # check for a winner
    if winner(board, turn):
        print(turn, 'wins!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

