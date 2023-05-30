# NQueen Solution using Backtracking

def solve_n_queens():
    n = int(input("Enter the number of queens: "))

    def is_safe(board, row, col):
        #check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        #check if there is a queen in the uppler-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        #check if there is a queen in the uppler-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True


    def backtrack(board, row):
        if row == n:
            #All queens have been placed successfully
            return True
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1

                #Recursively place the queens in the next row
                if backtrack(board, row+1):
                    return True

                board[row][col] = 0
        return False

    #create an empty chessboard
    board = [[0]*n for _ in range(n)]

    #start the backtracking algorithm from the first row
    if backtrack(board, 0):
        return board

    #No solution found
    return None


#solve n-queens problem
solution = solve_n_queens()

if solution:
    print("Solution: ")
    for row in solution:
        print(row)
else:
    print("No solution found.")