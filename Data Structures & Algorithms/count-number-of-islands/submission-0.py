class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCtr = 0

        def dfs(i, j):

            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] =="0":
                return

            grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for ctr1 in range(len(grid)):
            for ctr2 in range(len(grid[0])):
                if grid[ctr1][ctr2] == "1":
                    islandCtr += 1
                    dfs(ctr1, ctr2)

        return islandCtr