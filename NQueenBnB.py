#NQueen using Branch, Bound

n = int(input("Enter the number of Queens: "))

board = [[0]*n for _ in range(n)]

def isSafe_BnB(board, row, col, column, slash, backslash):
    if column[col] or slash[row+col] or backslash[row-col+len(board)-1]:
        return False
    return True


def setArrays(row, col, column, slash, backslash):
    column[col] = 1
    slash[row+col] = 1
    backslash[row-col+len(column)-1] = 1


def branchAndBound(board, row, col_arr, slash, backslash):
    # for printing the solution
    if row == len(board):
        for i in board:
            for j in i:
                print(j, end= " ")
            print()

        return True
    
    for col in range(len(board[0])):
        if isSafe_BnB(board, row, col, col_arr, slash, backslash):
            setArrays(row, col, col_arr, slash, backslash)
            board[row][col] = 1
            if not branchAndBound(board, row+1, col_arr, slash, backslash):
                col_arr[col] = 0
                board[row][col] = 0
                slash[row+col] = 0
                backslash[row-col+len(col_arr)-1] = 0


col_arr = [0 for i in range(len(board))]
slash = [0 for i in range(2*len(board)-1)]
backslash = [0 for i in range(2*len(board)-1)]
branchAndBound(board, 0, col_arr, slash, backslash)
