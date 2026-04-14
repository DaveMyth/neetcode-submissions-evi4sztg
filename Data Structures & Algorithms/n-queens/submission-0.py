class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for ctr in range(n)] for ctr2 in range(n)]

        col = set()
        posDiag = set() #r+c
        negDiag = set() #r-c

        def backtracker(r):

            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue

                board[r][c] = 'Q'
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtracker(r+1)
                board[r][c] = '.'
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        
        backtracker(0)
        return res