class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        atl, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(row: int, col:int, prevHeight: int, visitedSet: set) -> None:

                if (row,col) in visitedSet or row<0 or row==ROWS or col<0 or col==COLS or heights[row][col] < prevHeight:
                    return

                visitedSet.add((row,col))
                dfs(row-1, col, heights[row][col], visitedSet)
                dfs(row+1, col, heights[row][col], visitedSet)
                dfs(row, col-1, heights[row][col], visitedSet)
                dfs(row, col+1, heights[row][col], visitedSet)

        for ctr in range(ROWS):
            dfs(ctr,0, heights[ctr][0], pac)
            dfs(ctr,COLS-1, heights[ctr][COLS-1], atl)

        for ctr in range(COLS):
            dfs(0,ctr, heights[0][ctr], pac)
            dfs(ROWS-1,ctr, heights[ROWS-1][ctr], atl)

        for rec in pac:
            if rec in atl:
                res.append(rec)

        return res

        
