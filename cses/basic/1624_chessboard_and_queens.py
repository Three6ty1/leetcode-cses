board = []
for i in range(8):
    curr = []
    for i in list(input()):
        curr.append(i)
    
    board.append(curr)

def solve(row, occupied_col, occupied_primary, occupied_secondary):
    if row == 8:
        return 1
    
    sum = 0

    for col in range(8):
        if board[row][col] == "*" or occupied_col[col] or occupied_primary[row + col] or occupied_secondary[row - col + 8]:
            continue
        
        occupied_col[col] = True
        occupied_primary[row + col] = True
        occupied_secondary[row - col + 8] = True
        sum += solve(row + 1, occupied_col, occupied_primary, occupied_secondary)
        occupied_col[col] = False
        occupied_primary[row + col] = False
        occupied_secondary[row - col + 8] = False

    return sum

occupied_col = [False] * 8
occupied_primary = [False] * 20
occupied_secondary = [False] * 20

print(solve(0, occupied_col, occupied_primary, occupied_secondary))
