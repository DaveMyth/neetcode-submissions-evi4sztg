class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(i: int, j:int) -> int:

            if i<0 or j<0 or i>=ROWS or j>=COLS or grid[i][j] == 0:
                return 0

            print(i,j)
            grid[i][j] = 0
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i, j+1)

        for ctr1 in range(ROWS):
            for ctr2 in range(COLS):
                if grid[ctr1][ctr2] == 1:
                    maxArea = max(maxArea, dfs(ctr1, ctr2))

        return maxArea
        