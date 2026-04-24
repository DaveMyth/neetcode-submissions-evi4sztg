class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row: int, col: int) -> None:
            if row<0 or row==ROWS or col<0 or col==COLS or board[row][col] == 'X' or board[row][col] == 'T':
                return
            board[row][col] = 'T'
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for ctr in range(ROWS):
            dfs(ctr,0)
            dfs(ctr,COLS-1)

        for ctr in range(COLS):
            dfs(0,ctr)
            dfs(ROWS-1, ctr)

        # for ctr1 in range(ROWS):
        #     for ctr2 in range(COLS):

        for ctr1 in range(ROWS):
            for ctr2 in range(COLS):
                if board[ctr1][ctr2] == 'O':
                    board[ctr1][ctr2] = 'X'

                if board[ctr1][ctr2] == 'T':
                    board[ctr1][ctr2] = 'O'