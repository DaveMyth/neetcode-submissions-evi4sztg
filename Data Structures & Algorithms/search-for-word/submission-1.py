class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for ctr in range(len(board[0]))] for ctr2 in range(len(board))]

        def helper(currStr: str, i: int, j: int):

            if currStr == word:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if visited[i][j]:
                return False

            visited[i][j] = True
            above = helper(currStr + board[i][j], i-1, j)
            below = helper(currStr + board[i][j], i+1, j) 
            left = helper(currStr + board[i][j], i, j-1)
            right = helper(currStr + board[i][j], i, j+1)
            visited[i][j] = False

            return above or below or left or right

        for ctr1 in range(len(board)):
            for ctr2 in range(len(board[0])):
                if helper("", ctr1, ctr2):
                    return True
        return False