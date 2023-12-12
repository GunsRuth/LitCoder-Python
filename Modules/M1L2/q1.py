def isValidRow(board, row):
    seenNum = set()
    for coli in range(9):
        if board[row][coli] == '.':
            continue
        if board[row][coli] in seenNum:
            return False
        seenNum.add(board[row][coli])
    return True
    
def isValidCol(board, col):
    seenNum = set()
    for rowi in range(9):
        if board[rowi][col] == '.':
            continue
        if board[rowi][col] in seenNum:
            return False
        seenNum.add(board[rowi][col])
    return True
    
def isValidBox(board, rowo, colo):
    seenNum = set()
    for rowoff in range(3):
        for coloff in range(3):
            temp = board[rowo+rowoff][colo+coloff]
            if temp == '.':
                continue
            if temp in seenNum:
                return False
            seenNum.add(temp)
    return True

def isValid(board, row, col):
    return isValidRow(board, row) and isValidCol(board, col) and isValidBox(board, row-row%3, col-col%3)

def isValidState(board):
    for rowi in range(9):
        for coli in range(9):
            if not isValid(board, rowi, coli):
                return False
    return True

n = int(input())
board = [None for i in range(9)]
for i in range(9):
    board[i] = input().split()
valid = isValidState(board)
print("YES" if valid else "NO")
                                                                                                                            