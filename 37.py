def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]

    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"

                if backtrack(row + 1):
                    return True

                board[row][col] = "."

        return False

    if backtrack(0):
        for row in board:
            print(" ".join(row))
    else:
        print("No solution exists")


n = 4
solve_n_queens(n)